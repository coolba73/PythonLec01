import json
import pandas as pd


source = json.loads(open('D:\FinInsightServices\PythonLec01\CalRowByRow\data.dat','r').read())

# print(source["InputData"])

NumeratorColumn = source["NumeratorColumn"]
DenominatorColumn = source["DenominatorColumn"]
ResultColumnName = source["ResultColumnName"]
CalType  = source["CalType"]

df_list = []

re = {}


for k in source['InputData'].keys():
    # print(source['InputData'][k]['result'])
    df = pd.DataFrame(source['InputData'][k]['result'])

if (ResultColumnName == ''):
    ResultColumnName = "CalResult"

if (CalType == "division"):
    df[ResultColumnName] = df[NumeratorColumn] / df[DenominatorColumn]


re["result"] = json.loads( df.to_json(orient='records'))

print( json.dumps(re))
    