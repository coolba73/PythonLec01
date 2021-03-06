import json
import pandas as pd
import numpy as np
from collections import OrderedDict

data = open("D:\FinInsightServices\PythonLec01\CalBeta\data\CalBeta02.dat",'r').read()

source = json.loads(data)

for k in source.keys():
    source2 = json.loads(source[k])

source = source2

df_kospi = pd.DataFrame(source["KOSPI200"])

var_kospi = np.var(df_kospi["LogYield"])

re = []
totalre = {}
for k in source.keys():
    if (k != 'KOSPI200'):
        df = pd.DataFrame(source[k])
        cov = np.cov(df_kospi["LogYield"] , df["LogYield"] )[0][1] 
        beta = cov / var_kospi
        item = {}
        item["ItemCode"] = k
        item["Beta"] = beta
        re.append(item)

totalre["result"] = re
print( json.dumps( totalre))
