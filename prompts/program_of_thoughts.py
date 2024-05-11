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
               "death_year = 1989\n"
               "marriage_year = 1932\n"
               "years_elapsed = death_year - marriage_year\n"
               "answer = years_elapsed\n\n\n\n")

    prompt += table_instruction + "\n\n\n"
    prompt += tables[questions["train"][30]["table_id"]] + "\n"
    prompt += questions["train"][30]["question"] + "\n\n\n"
    prompt += ("# To answer this question, write a Python program to answer the following subquestions:\n"
               "marriage_years = {1939, 1948, 1963}\n"
               "first_marriage_year = min(marriage_years)\n"
               "answer = first_marriage_year\n\n\n\n")

    prompt += table_instruction + "\n\n\n"
    prompt += tables[questions["train"][70]["table_id"]] + "\n"
    prompt += questions["train"][70]["question"] + "\n\n\n"
    prompt += ("# To answer this question, write a Python program to answer the following subquestions:\n"
               "wresting_begin_year = 1992\n"
               "wresting_end_year = 2022\n"
               "wrestling_years = wresting_end_year - wrestling_begin_year\n"
               "acting_begin_year = 1998\n"
               "acting_end_year = 2017\n"
               "acting_years = acting_end_year - acting_begin_year\n"
               "difference_years = wrestling_years - acting_years\n"
               "answer = difference_years\n\n\n\n")

    prompt += table_instruction + "\n\n\n"
    prompt += tables[questions[split][question_id]["table_id"]] + "\n"
    prompt += questions[split][question_id]["question"] + "\n\n\n"
    prompt += "# To answer this question, write a Python program to answer the following subquestions:\n"

    return prompt


def zero_shot_faitful_cot(tables: list[str],
                         questions: list[dict[str, dict[str, str|int]]],
                         split: str, question_id: int) -> str:
    prompt = table_instruction + "\n\n\n"
    prompt += tables[questions[split][question_id]["table_id"]] + "\n"
    prompt += questions[split][question_id]["question"] + "\n\n\n"
    prompt += "# To answer this question, write a Python program to answer the following subquestions:\n"

    return prompt
