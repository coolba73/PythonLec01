import json
import pandas as pd
import pprint

source = json.loads(open('D:\FinInsightServices\PythonLec01\CalListToList\data.dat','r').read())

# pprint.pprint(source)

d_datasource = source["CalculationInfo"]["DenominatorSource"]
d_datatable = source["CalculationInfo"]["DenominatorTable"]
d_column = source["CalculationInfo"]["DenominatorColumn"]

n_datasource = source["CalculationInfo"]["NumeratorSource"]
n_datatable = source["CalculationInfo"]["NumeratorTable"]
n_column = source["CalculationInfo"]["NumeratorColumn"]

keyColumn = source["CalKeyColumn"]
CalType = source["CalType"]
ResultColumnName = source["ResultColumnName"]

d_df = pd.DataFrame(source["InputData"][d_datasource][d_datatable])
n_df = pd.DataFrame(source["InputData"][n_datasource][n_datatable])

# print(d_df.to_string())
# print(n_df.to_string())

df_m = pd.merge(d_df, n_df, on=keyColumn )

if (CalType == "Division"):
    df_m[ResultColumnName] = df_m[n_column] / df_m[d_column]


# print(df_m.to_string())

re = {}
re['result'] = json.loads( df_m.to_json(orient='records'))
print( json.dumps(re))



