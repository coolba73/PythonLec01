import json
import pandas as pd
import numpy as np

data = open('Callbeta.dat','r').read()

source = json.loads(data)

df_kospi = pd.DataFrame(source["KOSPI200"])
df1 = pd.DataFrame(source["005930"])
df2 = pd.DataFrame(source["066570"])

var_kospi = np.var(df_kospi["LogYield"]) 

cov1 = np.cov(df_kospi["LogYield"] , df1["LogYield"] )[0][1] 
cov2 = np.cov(df_kospi["LogYield"] , df2["LogYield"] )[0][1] 

beta_1 = cov1 / var_kospi 
beta_2 = cov2 / var_kospi 

print(beta_1)
print(beta_2)
