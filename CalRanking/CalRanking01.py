import json
import pprint
import pandas as pd
import pprint

source = json.loads(open('D:\FinInsightServices\PythonLec01\CalRanking\data.dat','r').read())

key = source["InputData"].keys()

targetColumn = source["TargetColumn"]

# df = pd.DataFrame(sourd["InputData"])

re = {}

for k in source["InputData"].keys():
    df = pd.DataFrame( source["InputData"][k]["result"])
    df[targetColumn + "_Ranking"] = df[targetColumn].rank(ascending=False)


re["result"] = json.loads( df.to_json(orient='records'))


print(json.dumps(re))

