import json
import pandas as pd
import pprint
import re
import numpy as np

source = json.loads(open('D:\FinInsightServices\PythonLec01\CalCutRateTotal\data.dat','r').read())


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
marketrisk_column = source["propCutRateAColumnInfo"]["MarketRisk_TargetColumn"]

df = pd.merge(df_over[["ItemCode", over_column, rank_column,]], df_beta[["ItemCode",beta_column]], how='inner' ,left_on=["ItemCode"], right_on=["ItemCode"])
df = pd.merge(df , df_risk[["ItemCode",risk_column,marketrisk_column]], how='inner', left_on=["ItemCode"], right_on=["ItemCode"])

df = df[["ItemCode", rank_column, over_column, beta_column, risk_column, marketrisk_column]]

df["key"] = 1
df = pd.merge(df, df, how='inner', left_on=["key"], right_on=["key"])


df = df.loc[df[rank_column + "_x"] >= df[rank_column + "_y"]]
df['Value_A'] = df[over_column + "_y"] * (df[beta_column+"_y"]**2) / df[risk_column + "_y"]
df['Value_B'] = (df[beta_column+"_y"]**2) / df[risk_column + "_y"]

df = df.groupby(["ItemCode_x", rank_column + "_x"], as_index=False).agg({"Value_A":np.sum , 
                                                                         "Value_B":np.sum, 
                                                                         marketrisk_column + "_y" : np.min, 
                                                                         beta_column + "_x" : np.min, 
                                                                         risk_column + "_x" : np.min, 
                                                                         over_column + "_x" : np.min 
                                                                         }
                                                                         )

df.rename(columns = lambda x: x.replace('_x','').replace('_y',''), inplace = True)

df['CutRate'] = ((df[marketrisk_column] ** 2 ) * df["Value_A"]) / ( 1 + ( (df[marketrisk_column]**2) * df["Value_B"] ) )

df = df.sort_values(rank_column,ascending=True)

df['Zi'] = df[beta_column]/df[risk_column]*(df[over_column] - df["CutRate"])

totZi = np.sum(df['Zi'])

df["InvestRate"] = df["Zi"] / totZi

df["InvestRate"] = df["InvestRate"] * 100
df = df[["ItemCode", "InvestRate"]]

print(df.to_string())
print(np.sum(df["InvestRate"]))

re = {}
re['result'] = json.loads( df.to_json(orient='records'))

# print( json.dumps(re) )

