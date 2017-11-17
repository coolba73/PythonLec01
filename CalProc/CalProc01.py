import os
import json
import pandas as pd

source = json.loads(open(os.environ['req']).read())
response = open(os.environ['res'], 'w')

# source = json.loads( open("D:\FinInsightServices\PythonLec01\CalProc\CalProc01.dat","r").read())

dfList = []
totalre = {}

colName = source["TargetColumn"]
calType = source["CalType"]

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
        df[ colName  +"_CalResult"] = df[colName] - srcval

    if (calType == "Multiply"):
        df[ colName + "_CalResult"] = df[colName] * srcval

    df["cal_factor"] = srcval

# print(df)

totalre["result"] = json.loads( df.to_json(orient='records'))

# print(json.dumps(totalre))

response.write(json.dumps(totalre))
response.close()