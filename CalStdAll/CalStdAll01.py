import json
import numpy as np
import pandas as pd

source = json.loads(open('D:\FinInsightServices\PythonLec01\CalStdAll\data.dat','r').read())

targetColumn = source["TargetColumn"]

itemList = []
itemStd = {}

for k in source["InputData"]:
    src = source["InputData"]
    for k2 in src[k]:
        if k2 == 'KOSPI200':
            continue
        itemsrc = src[k][k2]
        df = pd.DataFrame(itemsrc)
        stdval = np.std(df, ddof=1)
        itemStd = {}
        itemStd["ItemCode"] = k2
        itemStd["sigma"] = stdval[targetColumn]
        itemList.append(itemStd)

re = {}

re["resutl"] = itemList

print( json.dumps(re) )
