def clear(tables: list[str], questions: list[dict[str, dict[str, str|int]]],
          split: str, question_id: int) -> str:
    prompt = \
"""Given an entity-centric table and corresponding question, follow the steps below exactly to answer the question:

Step 1. Comprehend Information: Apply domain knowledge to understand how to approach and answer the question.

Step 2. Locate Relevant Rows: Identify and extract any rows from the table that could be relevant to the question. Explain why these rows are selected. Also output the relevant rows verbatim.

Step 3. Examine the Question and Create Sub-Questions: Determine whether the original question can be solved by a simple table lookup. If not, break down the original question into between 2 and 4 smaller, more manageable sub-questions. Assume each sub-problem can be solved using the provided evidence. Explain how one could approach solving each sub-problem.

Step 4. Answer Sub-Questions: Answer each sub-question using evidence from the table. Explain the step-by-step reasoning process that leads to each answer. Include any calculations or logical deduction to arrive at each conclusion, no matter how simple.

Step 5. Resolve Information to Form the Final Answer: Using the answers to each sub-question, answer the original question. Explain the step-by-step reasoning process that leads to this final answer. Include any calculations or logical deduction to arrive at each conclusion, no matter how simple. Clearly state the final answer using "Final Answer:", providing the answer as concisely as possible without unnecessary information.


Each table-question pair is presented as a table (identified by "Table:") followed by a question (identified by "Q:"). Tables are presented in a linear format, with columns separated by tabs, rows separated by newlines, and subsections separated by double newlines. If necessary, assume the current date is December, 2022.

Here are three examples that follow these instructions. Answer the provided question in a similar format:

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


A:

Step 1. Comprehend Information
Domain Knowledge:
- The question asks "how long", so the answer should be a length of time
- To determine the time between two years, take the absolute value of the difference between the two years.

Step 2. Locate Relevant Rows
- "Title	Bette Davis": This indicates that the information in the table is about Bette Davis.
- "Years active	1929-1989": This provides the start and end year of Bette Davis's career.
- "Bette Davis	['BETTEDavis (cropped).jpg | Publicity photo, 1935']": This provides the year the photo was taken.

Step 3. Examine the Question and Create Sub-Questions
OQ) How long after Davis's career began did she take the photo? The table doesn't provide this information. To determine the time between these two events, we need to know the following:
    SQ1) When did Davis's career begin?
    SQ2) When did Davis take the photo? Davis took the photo in 1935

SQ1) When did Davis's career begin? The table gives the range years spanning Davis's career. We can determine the begin year of her career by looking at the start year of this range.

SQ2) When did Davis take the photo? The table provides the year the photo was taken.

Step 4. Answer Sub-Questions
SQ1) Davis's career lasted from 1929 to 1989. Therefore, her career began in 1929.
SQ2) The photo was taken in 1935.

Step 5. Resolve Information to Form the Final Answer
OQ) How long after Davis's career began did she take the photo?
Davis's career began in 1929 (SQ1), and she took the photo in 1935 (SQ2). To get the number of years between these two events, take the absolute value of the difference between the two years. The absolute value of (1929-1935) is 6.
Therefore, the photo was taken 6 years after Davis's career began.
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


A:

Step 1. Comprehend Information
Domain Knowledge:
- The question asks "what year", so the answer should be a year

Step 2. Locate Relevant Rows
- "Title	"2 Hearts 1 Love"": This indicates that the information in the table is about 2 Hearts 1 Love.
- "Released	8 September 2013": This provides the release date of 2 Hearts 1 Love.

Step 3. Examine the Question and Create Sub-Questions
OQ) What year was 2 Hearts 1 Love released? The table provides the year 2 Hearts 1 Love was released

Step 4. Answer Sub-Questions
N/A

Step 5. Resolve Information to Form the Final Answer
OQ) What year was 2 Hearts 1 Love released?
2 Hearts 1 Love was released in on 8 September 2013, which is in the year 2013.
Therefore, 2 Hearts 1 Love was released in the year 2013.
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


A:

Step 1. Comprehend Information
Domain Knowledge:
- The question asks "when", so the answer should be a date or time.
- To determine the last team someone was associated with, identify the one that occurred most recently.
- Given an event spanning a range of years, the start is the first number in that range.

Step 2. Locate Relevant Rows
- "Title	Dwight Bernard": This indicates that the information in the table is about Dwight Bernard.
- "Teams	['New York Mets (1978-1979) | Milwaukee Brewers (1981-1982)']": This provides a list of all teams Dwight Bernard played with and the years he played with each.

Step 3. Examine the Question and Create Sub-Questions
OQ) When did Dwight Bernard start playing with the last team he was associated with? The table doesn't provide this information. To determine this, we need to know the following:
    SQ1) What was the last team Dwight Bernard was associated with?
    SQ2) When did Dwight Bernard start playing for this team?

SQ1) What was the last team Dwight Bernard was associated with? The table doesn't provide this information. However, the table provides a list of all teams Bernard was associated with and the years he was associated with each team. We can determine the last team Dwight Bernard was associated with by comparing the last year he was associated with each of his teams.

SQ2) When did Dwight Bernard start playing for this team? The table provides the range of years Bernard was associated with each of his teams. We can determine the year he started playing for that team by looking at the start year in the range.

Step 4. Answer Sub-Questions
SQ1) The only teams Dwight Bernard has played with are the New York Mets and Milwaukee Brewers. Bernard played for the Mets from 1978 to 1979 and the Brewers from 1981 to 1982. He was associated with the Brewers in 1982, which is more recent than the Mets in 1979; therefore, the last team he was associated with is the Brewers.
SQ2) He played with the Brewers from 1981 to 1982, so he started playing for the Brewers in 1981.

Step 5. Resolve Information to Form the Final Answer
OQ) When did Dwight Bernard start playing with the last team he was associated with?
The last team Dwight Bernard was associated with was the Brewers (SQ1), which he started playing for in 1981 (SQ2).
Therefore, Dwight Bernard started playing with the last team he was associated with in 1981.
Final Answer: 1981

========================

Table:

"""

    prompt += tables[questions[split][question_id]["table_id"]] + "\n"
    prompt += "Q: " + questions[split][question_id]["question"] + "\n\n\n"
    prompt += "A:"

    return prompt
