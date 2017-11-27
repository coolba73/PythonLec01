import json
import pandas as pd
import pprint
import re


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
beta_column = source["propCutRateAColumnInfo"]["Over_TargetColumn"]
df_beta = pd.DataFrame(source["InputData"][target_source][target_table])
# print(df_beta)

#자산의위험
target_source = source["propCutRateAColumnInfo"]["Sigma_TargetSource"]
target_table = source["propCutRateAColumnInfo"]["Sigma_TargetTable"]
risk_column = source["propCutRateAColumnInfo"]["Over_TargetColumn"]
df_risk = pd.DataFrame(source["InputData"][target_source][target_table])
# print(df_risk)

rank_column = source["propCutRateAColumnInfo"]["Rank_TargetColumn"]


df_1 = pd.merge(df_over[["ItemCode", over_column, rank_column]], df_beta[["ItemCode",beta_column]], how='inner' ,left_on=["ItemCode"], right_on=["ItemCode"])


# chkcol = [ col for col in df_1.columns if ('_x' in col) or ('_y' in col)  ]


df_1.rename(columns = lambda x: x.replace('_x','').replace('_y',''), inplace = True)

print(df_1)

# print(chkcol)

# df_1 = df_1[["ItemCode",rank_column + "_x" ,over_column + "_x" ,beta_column + "_x"]]

# print(df_1)

# df_2 = pd.merge(df_1, df_risk[[risk_column]], how='inner', left_on=["ItemCode"], right_on=["ItemCode"] )













