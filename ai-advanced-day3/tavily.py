from tavily import TavilyClient
tavily = TavilyClient(api_key='')

response = tavily.search(query="Where does Messi play right now?", max_results=3)
context = [{"url": obj["url"], "content": obj["content"]} for obj in response['results']]

# response
# {'query': 'Where does Messi play right now?',
#  'follow_up_questions': None,
#  'answer': None,
#  'images': [],
#  'results': [{'title': 'When will Lionel Messi play for Inter Miami? Club schedule, July date ...',
#    'url': 'https://www.sportingnews.com/us/soccer/news/when-lionel-messi-play-inter-miami-schedule-mls-debut/ps55sqx1xdcjzpt0wqb7grmr',
#    'content': "Messi is now set to play for David Beckham's club 16 years after Beckham signed for the LA Galaxy and changed the face of the league. It's expected that Messi's arrival will leave a similar impact",
#    'score': 0.95846003,
#    'raw_content': None},
#   {'title': "When is Lionel Messi's next Inter Miami game? Schedule, live stream ...",
#    'url': 'https://www.cbssports.com/soccer/news/when-is-lionel-messis-next-inter-miami-game-schedule-live-stream-how-to-watch-start-times-tv-channel/',
#    'content': "Schedule, live stream, how to watch, start times, TV channel\nMessi is expected to captain Tata Martino's side moving forward, and here's when he should play\nNow that Lionel Messi has gotten off to a winning start at Inter Miami after his stunning late goal in a 2-1 win for Inter over Cruz Azul in the Leagues Cup, attention has turned to when the Argentina FIFA 2022 World Cup winner might make his full debut. Inter Miami vs. Atlanta United\nIf Inter Miami move on, here are dates to keep in mind:\nMajor League Soccer debut\nThat is when Messi is expected to make his big MLS debut against Charlotte in Fort Lauderdale with Christian Lattanzio's side one of the teams that Messi and Martino will be eyeing as they plot a rise through the positions. Martino needs to get Miami in the habit of winning if they are to target MLS Cup success during Messi's time on the field with the club and victory at this level plus qualification for continental action through the Leagues Cup might represent the best case scenario for Inter in terms of what can be salvaged from the remainder of this campaign. Ranking Michael Bradley's biggest moments\nMLS playoffs: Schedule, bracket, matchups and more\nMessi breaks CONMEBOL WCQ goalscoring record\nU-23 USMNT roster drops as Olympics prep begins\nOlsen praises Houston resiliency in U.S. Open Cup win\nInter Miami's cup final defeat a learning experience\nWinning streaks lead to big changes in rankings\n FC Cincinnati vs. Inter Miami\nFirst MLS match away from home\nSecond only to Messi's actual MLS debut will be his first road game in the U.S. with New York Red Bulls the opponents as Miami travel to New Jersey.",
#    'score': 0.8393393,
#    'raw_content': None},
#   {'title': "Inter Miami schedule: When is Lionel Messi's next MLS game?",
#    'url': 'https://www.nbcsports.com/soccer/news/inter-miami-schedule-when-is-lionel-messis-next-mls-game',
#    'content': "What are Lionel Messi's stats in MLS with Inter Miami? Messi has now played less than a season's worth of games in an Inter Miami shirt when you add his appearances across all competitions. His numbers are, in true Messi form, stunning to the eye. Messi has appeared in 35 games for Miami, scoring 30 times with 17 assists. That's pretty good.",
#    'score': 0.7893961,
#    'raw_content': None}],
#  'response_time': 2.28}

# You can easily get search result context based on any max tokens straight into your RAG.
# The response is a string of the context within the max_token limit.

response_context = tavily.get_search_context(query="Where does Messi play right now?", search_depth="advanced", max_tokens=500)

# response_context
# '"[\\"{\\\\\\"url\\\\\\": \\\\\\"https://www.usatoday.com/story/sports/mls/2024/05/31/is-messi-playing-inter-miami-next-game-vs-st-louis-how-to-watch/73920451007/\\\\\\", \\\\\\"content\\\\\\": \\\\\\"Here\'s the latest. Lionel Messi is expected to play in his final MLS match Saturday before joining Argentina for Copa Am\\\\\\\\u00e9rica next week. Inter Miami hosts St. Louis City on Saturday at 7:30 p.m\\\\\\"}\\", \\"{\\\\\\"url\\\\\\": \\\\\\"https://www.sportingnews.com/us/soccer/news/lionel-messi-playing-inter-miami-vs-cruz-azul-debut-usa/qqzd67t1fwjphrgdbkd89tqz\\\\\\", \\\\\\"content\\\\\\": \\\\\\"Is Lionel Messi playing for Inter Miami vs Cruz Azul? The build up to this game has been filled with questions over Messi\'s involvement with Martino looking to balance the huge glare on his new No.10.\\\\\\"}\\"]"'

# You can also get a simple answer to a question including relevant sources all with a simple function call:
# You can use it for baseline
response_qna = tavily.qna_search(query="Where does Messi play right now?")

# response_qna
# 'Lionel Messi currently plays for Inter Miami in Major League Soccer (MLS). He has played 35 games for Miami, scoring 30 goals and providing 17 assists. Messi is expected to continue captaining the team moving forward and is set to make his full MLS debut against Charlotte in Fort Lauderdale.'