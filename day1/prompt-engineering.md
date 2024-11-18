# Self attention
>>> What is a card? Give me a brief summary in two sentences.
A card is a flat, rectangular object made of various materials, such as 
paper, plastic, or cardboard, that contains information, designs, or 
messages. Cards can be used for playing games, expressing greetings, 
providing identification, or serving as a means of payment, and they are 
an integral part of many aspects of our daily lives.

>>> What is a credit card? Give me a brief summary in two sentences.
A credit card is a type of loan that allows you to borrow money from the 
bank or financial institution that issued it, with the promise to pay back 
the borrowed amount plus interest and fees, typically within a set period. 
Credit cards are widely accepted as a form of payment at merchants and 
online retailers, providing a convenient way to make purchases and earn 
rewards, but they require responsible use to avoid debt and financial 
difficulties.

>>> What is a christmas card? Give me a brief summary in two sentences.
A Christmas card is a greeting card sent during the holiday season, 
typically featuring festive designs, images, or messages conveying wishes 
of joy, cheer, and celebration. Christmas cards are often used to express 
goodwill, share holiday memories, and connect with loved ones during the 
winter holidays, serving as a thoughtful way to spread seasonal cheer.

# 5-shot 1: 번역

>>>"""
Please translate the given word in German.

Q: Cat
A: Katze

Q: Butterfly
A: Schmetterling

Q: Map
A: Karte

Q: Friend
A: Freund

Q: Sky
A: Himmel

Q: Dog
"""
A: Hund

# 5-shot 2: 분류

>>> """
Please classify the given comment whether it is positive(P) or negative(N).

Comment: I loved the end of its story!
Answer: P

Comment: I think they needed more money to film it.
Answer: N

Comment: You MUST watch this film. It will be the best romance movie in your life.
Answer: P

Comment: Why they don't describe the story of the Emma in detail? She was not the heroine, but she was the most attractive person in the movie. I cried when she died to protect her son.
Answer: P

Comment: I'd rather go out and hang out than watch this in my previous time. Absolutely waste of time...
Answer: N

Comment: The storyline was dull and uninspiring.
Answer:
"""
N (Negative)

# SQL
>>>"""
Convert the following natural language requests into SQL queries:
1. "Find all employees whos salary is bigger than 50000": SELECT * FROM employees WHERE salary > 50000;
2. "Find products that out of stock": SELECT * FROM products WHERE stock = 0;
3. "Find students who scored less than 90 in math.": SELECT name FROM students WHERE math_score > 90;
4. "Find all monthly orders": SELECT * FROM orders WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);
5. "Find number of cities of the customers.": SELECT city, COUNT(*) FROM customers GROUP BY city;

Request: "Find the average salary of employees in the marketing department."
"""
Here is the SQL query for the given request:

```sql
SELECT AVG(salary) 
FROM employees 
WHERE department = 'Marketing';
```

This query calculates the average salary of all employees who belong to 
the marketing department.

# Chain of Thought 1
>>>"""
Solve the following problem step-by-step: 23 + 47
"""
A simple arithmetic problem!

Here's the step-by-step solution:

**Step 1: Add 20 + 30 = 50**

**Step 2: Add 3 (of 23) + 7 (of 47) = 10**

**Step 3: Combine the results of Step 1 and Step 2 = 50 + 10 = 60**

Answer: **60**

# Chain of Thought 2
>>>"""
Solve the following problem step-by-step: 123 - 58
"""
A simple arithmetic problem!

Here's the step-by-step solution:

**Step 1: Subtract 50 (of 58) from 123 = 123 - 50 = 73**

**Step 2: Subtract 8 (remaining of 58) from 73 = 73 - 8 = **65**

Answer: **65**

# Chain of Thought 3
>>>"""
Solve the following problem step-by-step.

Q: 23 + 47
A: 
**Step 1: Add 20 + 30 = 50**
**Step 2: Add 3 (of 23) + 7 (of 47) = 10**
**Step 3: Combine the results of Step 1 and Step 2 = 50 + 10 = 60**

Answer: **60**

Q: 123 - 58
A: 
**Step 1: Subtract 50 (of 58) from 123 = 123 - 50 = 73**
**Step 2: Subtract 8 (remaining of 58) from 73 = 73 - 8 = **65**

Answer: **65**

Q: 345 + 678 - 123
A: 
"""
Another step-by-step problem!

Here's the solution:

**Step 1: Add 345 and 678 = 345 + 678 = 1023**

**Step 2: Subtract 123 from 1023 = 1023 - 123 = **900**

Answer: **900**

# Intermediate - 1
>>>"""
Solve the following logic puzzle step-by-step:
Three friends, Alice, Bob, and Carol, have different favorite colors: red, blue, and green. We know that:
1. Alice does not like red.
2. Bob does not like blue.
3. Carol likes green.

Determine the favorite color of each friend.
"""
Let's solve this logic puzzle step-by-step!

**Step 1:** From statement 3, we know that Carol likes green. So, we can assign Carol's favorite color to be green.

**Current state:**
Carol: Green

**Step 2:** From statement 1, we know that Alice does not like red. This means Alice must like either blue or green (since she 
doesn't like red).

**Step 3:** Now we know that Alice is not a fan of red and Carol likes green. This means Bob's favorite color must be red (since he 
doesn't like blue and we've already eliminated green for Alice and Carol).

**Current state:**
Carol: Green
Bob: Red

**Step 4:** Finally, we can determine Alice's favorite color. Since she doesn't like red, and Bob likes red, Alice's favorite color 
must be blue.

**Final solution:**
Alice: Blue
Bob: Red
Carol: Green

There you have it!

# Intermediate - 2
>>>"""
Solve the following logic puzzle step-by-step:
Four people (A, B, C, D) are sitting in a row. We know that:
1. A is not next to B.
2. B is next to C.
3. C is not next to D.

Determine the possible seating arrangements.
"""
Let's solve this logic puzzle step-by-step!

**Step 1:** From statement 1, we know that A is not next to B. This means there are three possible positions for A: at one end of 
the row (either left or right), or in the middle.

**Step 2:** From statement 2, we know that B is next to C. This means B and C must sit together, leaving two people remaining (A 
and D).

**Step 3:** Since A is not next to B, and B is sitting with C, A must be at one of the ends of the row.

**Possible arrangements:**

* A is on the left end: ...A...BCD
* A is on the right end: ...CDAB...

**Step 4:** From statement 3, we know that C is not next to D. This means if C is sitting with B (as stated in step 2), then D must 
be on one of the ends.

**Revised possible arrangements:**

* A is on the left end and D is on the right end: ...A...BCD
* A is on the left end and D is in the middle: ...ABCD...
* A is on the right end and D is on the left end: CDAB...
* A is on the right end and D is in the middle: ABCD...

**Final solution:** There are four possible seating arrangements:

1. ...A...BCD
2. ...ABCD...
3. CDAB...
4. ABCD...

Note that these arrangements are mutually exclusive, meaning only one of them can be true.

