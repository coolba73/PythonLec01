import json
import pandas as pd
import numpy as np
from collections import OrderedDict

f = open("dataLogYield.dat",'r')
data = f.read()
# print(data)

source = json.loads(data)

#===================================================================================
def calLogYield(adf):
    # adf = adf.sort(['index'])
    
    dfSrc = adf[["index","Close"]]
    dfSrc.columns = ["Date","Close"] 

    dfSrc = dfSrc.sort_values(['Date'], ascending = False)
    dfSrc = pd.concat( [dfSrc, dfSrc.shift(-1)], axis=1)
    dfSrc.columns = ["Date","Close","PreDate","PreClose"]
    dfSrc = dfSrc[['Date','Close','PreClose']]
    dfSrc = dfSrc.dropna()
    dfSrc["LogYield"] = np.log( dfSrc["Close"] / dfSrc["PreClose"] )
    
    re = dfSrc.to_json(orient='records')

    return re

    # return dfSrc.to_json()

#===================================================================================

total = OrderedDict();

for k in source.keys():

    # print(k)
    source2 = json.loads(source[k]);
    # print(source2.keys())


    for k2 in source2.keys():
        # re = calLogYield( pd.DataFrame(source2[k2]))
        total[k2] = json.loads( calLogYield( pd.DataFrame(source2[k2])) )
        # print (re)


print( json.dumps( total) )  


