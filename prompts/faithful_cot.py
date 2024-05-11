table_instruction = ("Q: The table below is presented in a linear format. "
    "Columns are separated by tabs, and rows are separated by newlines. "
    "Subsections are partitioned by double newlines.")


def few_shot_faitful_cot(tables: list[str],
                         questions: list[dict[str, dict[str, str|int]]],
                         split: str, question_id: int) -> str:
    prompt = table_instruction + "\n\n\n"
    prompt += tables[questions["train"][0]["table_id"]] + "\n"
    prompt += questions["train"][0]["question"] + "\n\n\n"
    prompt += ("# To answer this question, write a Python program to answer the following subquestions:\n"
               "# 1. What year did Davis's death occur? (independent, support: [\"Died	October 6, 1989 | (1989-10-06) | (aged 81) | Neuilly-sur-Seine, France\"])\n"
               "death_year = 1989\n"
               "# 2. What year did she marry Harmon Oscar Nelson? (independent, support: [\"Spouse(s)	Harmon Oscar Nelson | ( | married |  1932; | divorced |  1938) | Arthur Farnsworth | ( | married |  1940; died 1943) | William Grant Sherry | ( | married |  1945; | divorced |  1950) | Gary Merrill | ( | married |  1950; | divorced |  1960)\"])\n"
               "marriage_year = 1932\n"
               "# 3. How many years elapsed between Davis's marriage to Harmon Oscar Nelson and her death? (depends on 1 and 2, support: [])\n"
               "years_elapsed = death_year - marriage_year\n"
               "# 4. Final Answer: How many years prior to Davis's death did she marry Harmon Oscar Nelson? (depends on 3, support: [])\n"
               "answer = years_elapsed\n\n\n\n")

    prompt += table_instruction + "\n\n\n"
    prompt += tables[questions["train"][30]["table_id"]] + "\n"
    prompt += questions["train"][30]["question"] + "\n\n\n"
    prompt += ("# To answer this question, write a Python program to answer the following subquestions:\n"
               "# 1. What years did Johnny Weissmuller get married? (independent, support: [\"Spouse(s)	Bobbe Arnst | ( | married |  1931; | divorced |  1933) | Lupe Vélez | ( | married |  1933; | divorced |  1939) | Beryl Scott | ( | married |  1939; | divorced |  1948) | Allene Gates | ( | married |  1948; | divorced |  1962) | Maria Gertrude Baumann | ( | married |  1963)\"])\n"
               "marriage_years = {1939, 1948, 1963}\n"
               "# 2. Which of Johnny's marriage years came first? (depends on 1, support: [])\n"
               "first_marriage_year = min(marriage_years)\n"
               "# 3. Final Answer: When did Johnny Weissmuller first get married? (depends on 2, support: [])\n"
               "answer = first_marriage_year\n\n\n\n")

    prompt += table_instruction + "\n\n\n"
    prompt += tables[questions["train"][70]["table_id"]] + "\n"
    prompt += questions["train"][70]["question"] + "\n\n\n"
    prompt += ("# To answer this question, write a Python program to answer the following subquestions:\n"
               "# 1. What year did Triple H's wrestling career begin? (independent, support: [\"Years active	1992-2022 (wrestling) | 2010-present (business) | 1998-2017 (acting)\"])\n"
               "wresting_begin_year = 1992\n"
               "# 2. What year did Triple H's wrestling career end? (independent, support: [\"Years active	1992-2022 (wrestling) | 2010-present (business) | 1998-2017 (acting)\"])\n"
               "wresting_end_year = 2022\n"
               "# 3. How many years did Triple H's wrestling career last? (depends on 1 and 2, support: [])\n"
               "wrestling_years = wresting_end_year - wrestling_begin_year\n"
               "# 4. What year did Triple H's acting career begin? (independent, support: [\"Years active	1992-2022 (wrestling) | 2010-present (business) | 1998-2017 (acting)\"])\n"
               "acting_begin_year = 1998\n"
               "# 5. What year did Triple H's acting career end? (independent, support: [\"Years active	1992-2022 (wrestling) | 2010-present (business) | 1998-2017 (acting)\"])\n"
               "acting_end_year = 2017\n"
               "# 6. How many years did Triple H's acting career last? (depends on 4 and 5, support: [])\n"
               "acting_years = acting_end_year - acting_begin_year\n"
               "# 7. How many more years was Triple H's wrestling career than his acting career? (depends on 3 and 6, support: [])\n"
               "difference_years = wrestling_years - acting_years\n"
               "# 8. Final Answer: How much longer was Triple H's wrestling career over his acting career? (depends on 7, support: [])\n"
               "answer = difference_years\n\n\n\n")

    prompt += table_instruction + "\n\n\n"
    prompt += tables[questions[split][question_id]["table_id"]] + "\n"
    prompt += questions[split][question_id]["question"] + "\n\n\n"
    prompt += ("# To answer this question, write a Python program to answer the following subquestions:\n"
               "# 1. ")

    return prompt


def zero_shot_faitful_cot(tables: list[str],
                         questions: list[dict[str, dict[str, str|int]]],
                         split: str, question_id: int) -> str:
    prompt = table_instruction + "\n\n\n"
    prompt += tables[questions[split][question_id]["table_id"]] + "\n"
    prompt += questions[split][question_id]["question"] + "\n\n\n"
    prompt += ("# To answer this question, write a Python program to answer the following subquestions:\n"
               "# 1. ")

    return prompt
