import json
import pandas as pd

data = open('D:\FinInsightServices\PythonLec01\CalMinus\CalMinus01.dat','r').read()

source = json.loads(data)

dfList = []

totalre = {}

colName = source["TargetColumn"]

for k in source["InputData"].keys():
    indata = json.loads(source["InputData"][k])

    if (len(indata["result"]) == 1):
        df_powval = pd.DataFrame(indata["result"])
    else:
        df_tarval = pd.DataFrame(indata["result"])
        dfList.insert(1,df_tarval)

powval = df_powval[df_powval.columns[0]][0]

for df in dfList:
    df[ colName + "_Cal"] = df[colName] - powval
    df["multiply_value"] = powval

totalre["result"] = json.loads( df.to_json(orient='records'))

print(totalre)









