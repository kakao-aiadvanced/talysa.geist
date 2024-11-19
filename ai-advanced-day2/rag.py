import getpass
import os

os.environ['USER_AGENT'] = "myagent"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

import bs4
from langchain import hub
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Contents
urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

# Load, chunk and index the contents of the blog.
loader = WebBaseLoader(
    web_paths=(urls),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=1000,
    chunk_overlap=200
)

# Splits
splits = text_splitter.split_documents(docs)

# Vector store
from langchain_openai import OpenAIEmbeddings

# vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

vectorstore = Chroma.from_documents(
    documents=splits, 
    embedding=OpenAIEmbeddings(
        model="text-embedding-3-small"
    )
)

# Retrieve and generate using the relevant snippets of the blog.
retriever = vectorstore.as_retriever(
    search_type="similarity", search_kwargs={"k": 6}
)

# prompt
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

# prompt 빌려쓰기
prompt = hub.pull("rlm/rag-prompt")

parser = JsonOutputParser()

# 쿼리
query="agent memory"

# 쿼리에 대한 데이터 가져옴
retrieved_documents = retriever.invoke(query)

# 가져온 데이터가 질문과 관계 있는지 확인
def validation(query):
    validation_prompt = PromptTemplate(
        template="Are the retrieved documents are relevent to the user query? Answer the relevance with yes or no.\n{format_instructions}\n{query}\nrelevance:",
        input_variables=["query", "retrieved_documents"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    chain = validation_prompt | llm | parser

    return chain.invoke({"query": query,"retrieved_documents": retrieved_documents})

# 답변 서식
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# 출처는 이렇게 접근할 수 있는데, 어떻게 붙이는지 모르겠다.
# docs[0].metadata['source']

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

if (validation(query)['relevance']=="yes"):
    for chunk in rag_chain.stream(query):
        print(chunk, end="", flush=True)

