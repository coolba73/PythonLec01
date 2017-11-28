import os
import json
import pandas as pd


source = json.loads( open("D:\FinInsightServices\PythonLec01\CalProc\data.dat","r").read())

dfList = []
totalre = {}

colName = source["TargetColumn"]
calType = source["CalType"]
resultColumnName = ''

if ("ResultColumnName" in source):
    resultColumnName = source["ResultColumnName"]
else:
    resultColumnName = "Result_" + colName + "_" + calType

if resultColumnName == '':
    resultColumnName = "Result_" + colName + "_" + calType

for k in source["InputData"].keys():
    indata = json.loads(source["InputData"][k])

    if (len(indata["result"]) == 1):
        df_powval = pd.DataFrame(indata["result"])
    else:
        df_tarval = pd.DataFrame(indata["result"])
        dfList.insert(1,df_tarval)

srcval = df_powval[df_powval.columns[0]][0]

for df in dfList:
    
    if (calType == "Minus"):
        df[ resultColumnName ] = df[colName] - srcval

    if (calType == "Multiply"):
        df[ resultColumnName ] = df[colName] * srcval

    df["cal_factor"] = srcval

# print(df)

totalre["result"] = json.loads( df.to_json(orient='records'))

print(json.dumps(totalre))
