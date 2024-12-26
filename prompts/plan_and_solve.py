def plan_and_solve(tables: list[str], questions: list[dict[str, dict[str, str|int]]],
                   split: str, question_id: int) -> str:
    prompt = \
"""Each table-question pair is presented as a table (identified by "Table:") followed by a question (identified by "Q:"). Tables are presented in a linear format, with columns separated by tabs, rows separated by newlines, and subsections separated by double newlines. If necessary, assume the current date is December, 2022.

Here are three examples. Answer the provided question in a similar format:

========================

Table:

Title	Bette Davis
Died	October 6, 1989 | (1989-10-06) | (aged 81) | Neuilly-sur-Seine, France
Resting place	Forest Lawn Memorial Park
Occupation	Actress
Years active	1929-1989
Political party	Democratic
Spouse(s)	Harmon Oscar Nelson | ( | married |  1932; | divorced |  1938) | Arthur Farnsworth | ( | married |  1940; died 1943) | William Grant Sherry | ( | married |  1945; | divorced |  1950) | Gary Merrill | ( | married |  1950; | divorced |  1960)
Children	3, including B. D. Hyman
Bette Davis	['BETTEDavis (cropped).jpg | Publicity photo, 1935']


Q: How long after Davis's career began did she take the photo?


A: Let's first understand the problem, extract relevant variables and their corresponding numerals, and devise a plan. Then, let's carry out the plan, calculate intermediate results (pay attention to calculation and common sense), solve the problem step by step, and show the answer. We will clearly state the final answer using "Final Answer:", providing the answer as concisely as possible without unnecessary information.

Variables:
Year Davis's career started: 1929
Year of photo: 1935

Plan:
We can use the given information to calculate the difference in time.

Calculation:
The difference in time is 1935-1929=6 years

Answer:
The photo was taken 6 years after Davis's career began.
Final Answer: 6 years

========================

Table:

Title	"2 Hearts 1 Love"
"2 Hearts 1 Love"	['2 Hearts 1 Love.jpeg']

Single by 911

from the album | Illuminate... (The Hits and More)
Released	8 September 2013
Recorded	2013 | Central Sounds Studio, | Glasgow, Scotland
Genre	Pop
Songwriter(s)	911
Producer(s)	John McLaughlin

911 singles chronology
911 singles chronology	['"Wonderland" | (1999) | " | 2 Hearts 1 Love | " | (2013) | "I Wish It Could Be Christmas Everyday" | (2013)']


Q: What year was 2 Hearts 1 Love released?


A: Let's first understand the problem, extract relevant variables and their corresponding numerals, and devise a plan. Then, let's carry out the plan, calculate intermediate results (pay attention to calculation and common sense), solve the problem step by step, and show the answer. We will clearly state the final answer using "Final Answer:", providing the answer as concisely as possible without unnecessary information.

Variables:
Release date: 8 September 2013

Plan:
We can find the release year from the provided release date.

Calculation:
8 September 2013 is in the year 2013.

Answer:
2 Hearts 1 Love was released in the year 2013.
Final Answer: 2013

========================

Table:

Title	Dwight Bernard
Dwight Bernard	['Dwight Bernard.jpg']

Pitcher

Born | ( | 1952-05-31 | ) | May 31, 1952 | (age 70) | Mount Vernon, Illinois

Batted | Right | Threw | Right

MLB debut
MLB debut	['June 29, 1978, for the New York Mets']

Last MLB appearance
Last MLB appearance	['October 2, 1982, for the Milwaukee Brewers']

MLB statistics
Win-loss record	4-8
Earned run average	4.14
Strikeouts	92

Teams
Teams	['New York Mets (1978-1979) | Milwaukee Brewers (1981-1982)']


Q: When did Dwight Bernard start playing with the last team he was associated with?


A: Let's first understand the problem, extract relevant variables and their corresponding numerals, and devise a plan. Then, let's carry out the plan, calculate intermediate results (pay attention to calculation and common sense), solve the problem step by step, and show the answer. We will clearly state the final answer using "Final Answer:", providing the answer as concisely as possible without unnecessary information.

Variables:
Years played with New York Mets: 1978-1979
Years played with Milwaukee Brewers: 1981-1982

Plan:
We can find the last team Dwight Bernard played with, and then find the year he started playing with that team from the information provided.

Calculation:
The only teams Dwight Bernard has played with are the New York Mets and Milwaukee Brewers. Bernard played for the Mets from 1978 to 1979 and the Brewers from 1981 to 1982. He was associated with the Brewers in 1982, which is more recent than the Mets in 1979; therefore, the last team he was associated with is the Brewers.
He played with the Brewers from 1981 to 1982, so he started playing for the Brewers in 1981.

Answer:
Dwight Bernard started playing with the last team he was associated with in 1981.
Final Answer: 1981

========================

Table:

"""

    prompt += tables[questions[split][question_id]["table_id"]] + "\n"
    prompt += "Q: " + questions[split][question_id]["question"] + "\n\n\n"
    prompt += "A:"

    return prompt
