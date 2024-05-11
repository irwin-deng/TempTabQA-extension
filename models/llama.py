import openai
from openai import OpenAI
import pandas as pd
from tqdm import tqdm
import glob
import json
import time

DF_PATH=''
RESULT_PATH = ''
openai_client = OpenAI(
    api_key = "",
    base_url = ""
)


def llama2_result(prompt):
    try:
        response = openai_client.chat.completions.create(
            model = "meta-llama/Llama-2-70b-chat-hf",
            messages = [{"role": "user", "content": prompt}]
        )
    except Exception as e:
        print(e)
        exit()

    print(response.usage)
    try:
        response_str = response.choices[0].message.content
        assert response_str is not None
    except Exception:
        response_str = ""

    return response_str


id_to_json = {}

for filename in glob.glob("../data/maindata/tables/json/*"):
    f = open(filename,'r')
    data = json.load(f)
    id_to_json[int(filename.split("/")[-1].split(".")[0])] = data

df=pd.read_csv('./data/maindata/qapairs/dev-set/dev-set.csv')

table_string = {}
tables=id_to_json.keys()
for tab in tqdm(tables):
    table_s = ""
    table=id_to_json[tab]
    for key in table.keys():
        if type(table[key]) == type(dict()):
            table_s = table_s + key + "\n"
            for sub_key in table[key].keys():
                if sub_key == key:
                    table_s = table_s + str(table[key][sub_key]) + "\n"
                else:
                    table_s = table_s + sub_key +"\t" + table[key][sub_key] + "\n"
            table_s = table_s + "\n"
        else:
            table_s = table_s + key +"\n" + table[key] + "\n\n"

    table_string[tab] = table_s

df_eval_original=pd.read_csv(RESULT_PATH)

df_eval = pd.DataFrame()
actual_answers=[]
all_qs=[]
all_tabs=[]
all_output = []
count = 0
start = len(df_eval_original)

df=pd.read_csv(DF_PATH)

for i in tqdm(range(len(df))):
    t=df['table_id'][i]
    q=df['question'][i]
    ans=df['answer'][i]
    count += 1
    all_qs.append(q)
    all_tabs.append(t)
    actual_answers.append(ans)

    context = table_string[t]
    input_text = prepare_example(context,q)

    jum = 0
    while True:
        try:
            if jum == 3:
                result = "res"
            else:
                result = llama2_result(input_text)
          # time.sleep()
            break
        except:
            jum += 1
            print("....halt....")
            time.sleep(20)

    all_output.append(result)
    # print(input_text)
    print(ans,result)

    if count%5 == 0:
        df_eval['actual_answer']=actual_answers
        df_eval['question']=all_qs
        df_eval['table']=all_tabs
        df_eval['predicted_answer']=all_output
        df_eval_original = pd.concat([df_eval_original, df_eval], ignore_index=True, sort=False)
        df_eval_original.to_csv(RESULT_PATH,index=False)
        df_eval_original=pd.read_csv(RESULT_PATH)

        all_tabs = []
        all_output = []
        all_qs = []
        actual_answers = []
        df_eval = pd.DataFrame()

df_eval['actual_answer']=actual_answers
df_eval['question']=all_qs
df_eval['table']=all_tabs
df_eval['predicted_answer']=all_output
df_eval_original = pd.concat([df_eval_original, df_eval], ignore_index=True, sort=False)
df_eval_original.to_csv(RESULT_PATH,index=False)
