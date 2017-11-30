import json
import pprint
import pandas as pd

source = json.loads(open('D:\FinInsightServices\PythonLec01\CalInvestRate02\data.dat','r').read())

# pprint.pprint(source)

df_array = []

for k in source["InputData"].keys():
    df_array.append(pd.DataFrame(source["InputData"][k]["result"]))

icnt = 0

for idf in df_array:
    icnt += 1
    if ( icnt > 1):
        df = pd.merge(idf, preDf, how='inner', left_on = "ItemCode", right_on="ItemCode")

    preDf = idf    

rho = 0.5

df["Zi"] = (1 / ((1-rho)*df["sigma"]))* ( df["ExcessReturn"] - df["cutrate"] )

sumZi = df["Zi"].sum()

df["InvestRate"] = df["Zi"] / sumZi * 100

df = df[["ItemCode","InvestRate"]]


re = {}
re['result'] = json.loads( df.to_json(orient='records'))
print( json.dumps(re))






    
