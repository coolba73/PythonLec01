import json
import pandas as pd
import pprint
import re
import numpy as np

source = json.loads(open('D:\FinInsightServices\PythonLec01\CalCutRateA\data.dat','r').read())

#초과수익률
target_source = source["propCutRateAColumnInfo"]["Over_TargetSource"]
target_table = source["propCutRateAColumnInfo"]["Over_TargetTable"]
over_column = source["propCutRateAColumnInfo"]["Over_TargetColumn"]
df_over = pd.DataFrame(source["InputData"][target_source][target_table])
# print(df_over)

#베타
target_source = source["propCutRateAColumnInfo"]["Beta_TargetSource"]
target_table = source["propCutRateAColumnInfo"]["Beta_TargetTable"]
beta_column = source["propCutRateAColumnInfo"]["Beta_TargetColumn"]
df_beta = pd.DataFrame(source["InputData"][target_source][target_table])
# print(df_beta)

#자산의위험
target_source = source["propCutRateAColumnInfo"]["Sigma_TargetSource"]
target_table = source["propCutRateAColumnInfo"]["Sigma_TargetTable"]
risk_column = source["propCutRateAColumnInfo"]["Sigma_TargetColumn"]
df_risk = pd.DataFrame(source["InputData"][target_source][target_table])
# print(df_risk)

rank_column = source["propCutRateAColumnInfo"]["Rank_TargetColumn"]

df = pd.merge(df_over[["ItemCode", over_column, rank_column]], df_beta[["ItemCode",beta_column]], how='inner' ,left_on=["ItemCode"], right_on=["ItemCode"])
df = pd.merge(df , df_risk[["ItemCode",risk_column]], how='inner', left_on=["ItemCode"], right_on=["ItemCode"])
df = df[["ItemCode", rank_column, over_column, beta_column, risk_column]]
df["key"] = 1
df = pd.merge(df, df, how='inner', left_on=["key"], right_on=["key"])
df = df.loc[df[rank_column + "_x"] >= df[rank_column + "_y"]]
df['Value_A'] = df[over_column + "_y"] * (df[beta_column+"_y"]**2) / df[risk_column + "_y"]
df = df.groupby(["ItemCode_x", rank_column + "_x"], as_index=False).agg({"Value_A":np.sum})
df.rename(columns = lambda x: x.replace('_x','').replace('_y',''), inplace = True)
df = df.sort_values(rank_column,ascending=True)

re = {}
re['result'] = json.loads( df.to_json(orient='records'))
print( json.dumps(re))






















