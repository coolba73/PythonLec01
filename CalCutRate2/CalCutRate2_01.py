import json
import pprint
import pandas as pd
import numpy as np

source = json.loads(open('D:\FinInsightServices\PythonLec01\CalCutRate2\data.dat','r').read())

for k in source["InputData"].keys():
    df = pd.DataFrame(source["InputData"][k]["result"])

df["key"] = 1
df = df[["key","ItemCode","ExcessReturn" ,"ExcessReturn_Ranking"]]
df = df.rename(columns = {"ExcessReturn" :"ER" ,"ExcessReturn_Ranking":"Rank"})

df = pd.merge(df,df, how='inner', left_on = "key", right_on="key")
del df["key"]

# 랭킹 1위부터 자신까지의 표준편차 대비 초과수익률의 누적을 계산한다.
df = df.loc[df["Rank_x"] >= df["Rank_y"]]
df = df.groupby(["ItemCode_x","Rank_x"], as_index=False).agg({"ER_y":np.sum})
df.rename(columns = lambda x: x.replace('_x','').replace('_y',''), inplace = True)


# 상관계수(ρ)를 0.5라고 하고 절사율을 계산한다.

rho = 0.5

df["cutrate"] = rho / (1-rho+(df["Rank"]*rho)) * df["ER"]

print(df)

