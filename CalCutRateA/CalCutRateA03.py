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

df_1 = pd.merge(df_over[["ItemCode", over_column, rank_column]], df_beta[["ItemCode",beta_column]], how='inner' ,left_on=["ItemCode"], right_on=["ItemCode"])

df_2 = pd.merge(df_1 , df_risk[["ItemCode",risk_column]], how='inner', left_on=["ItemCode"], right_on=["ItemCode"])

df_2 = df_2[["ItemCode", rank_column, over_column, beta_column, risk_column]]

df_2 =  df_2.sort_values(rank_column,ascending=1)

df_2["key"] = 1


df_3 = pd.merge(df_2, df_2, how='inner', left_on=["key"], right_on=["key"])

df_4 = df_3.loc[df_3[rank_column + "_x"] >= df_3[rank_column + "_y"]]



# df_4 = df_4.sort_values([rank_column + "_x", rank_column+ "_y"], ascending=[1,1])

df_4['Value_A'] = df_4[over_column + "_y"] * (df_4[beta_column+"_y"]**2) / df_4[risk_column + "_y"]

# print(df_4.to_string())

# df_4.assign( Value_A = lambda x: x[over_column + "_y"] * (x[beta_column+"_y"]**2) / x[risk_column + "_y"])

# df_4.loc['Value_A'] = df_4.loc[:,over_column + "_y"] * (df_4.loc[:,beta_column+"_y"]**2) / df_4.loc[:,risk_column + "_y"]

# df_4.loc[:,'Value_A'] = df_4.apply(lambda row: row[over_column + "_y"] * (row[beta_column+"_y"]**2) / row[risk_column + "_y"] , axis=1)

# df_5 = df_4.groupby(["ItemCode_x", rank_column + "_x"]).agg({"Value_A":np.sum})

df_5 = df_4.groupby(["ItemCode_x", rank_column + "_x"], as_index=False).agg({"Value_A":np.sum})

df_5.rename(columns = lambda x: x.replace('_x','').replace('_y',''), inplace = True)

df_5 = df_5.sort_values(rank_column,ascending=True)

# print(df_5)


re = {}
re['result'] = json.loads( df_5.to_json(orient='records'))
print( json.dumps(re))






















