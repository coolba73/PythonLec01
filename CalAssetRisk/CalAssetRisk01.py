import json
import pprint
import pandas as pd

source = json.loads(open('D:\FinInsightServices\PythonLec01\CalAssetRisk\data.dat','r').read())

for k in source["InputData"].keys():
    
    if(len(source["InputData"][k]["result"]) == 1):
      for k2 in source["InputData"][k]["result"][0].keys():
        marketRisk = source["InputData"][k]["result"][0][k2]
    else:
        df = pd.DataFrame(source["InputData"][k]["result"])    

resultColumn = source["ResultColumnName"]
targetColumn = source["TargetColumn"]

if (resultColumn == ""):
    resultColumn = "AssetRisk"

df["MarketRisk"] = marketRisk
df[resultColumn] =  (df[targetColumn]**2) * (marketRisk**2)

re = {}
re['result'] = json.loads( df.to_json(orient='records'))


pprint.pprint( json.dumps(re) )


# pprint.pprint(source)