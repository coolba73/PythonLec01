import json
import pprint
import pandas as pd
import numpy as np
import itertools


source = json.loads(open('D:\FinInsightServices\PythonLec01\CalCrossRisk\data.dat','r').read())


for k in source["InputData"].keys():
    
    if(len(source["InputData"][k]["result"]) == 1):
      for k2 in source["InputData"][k]["result"][0].keys():
        marketRisk = source["InputData"][k]["result"][0][k2]
    else:
        df = pd.DataFrame(source["InputData"][k]["result"])    


df["key"] = 1

df2 = pd.merge(df,df, on='key')

CodePair = list(itertools.combinations(df["ItemCode"],2))

df3 = pd.DataFrame(CodePair)
df3.columns = ["ItemCode_x","ItemCode_y"]

df4 = pd.merge(df2,df3, how='inner', left_on=['ItemCode_x','ItemCode_y'], right_on=['ItemCode_x','ItemCode_y'])

print(df4)







