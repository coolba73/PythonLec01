import os
import json
import platform
from pandas_datareader import data
from collections import OrderedDict

source = json.loads(open('D:\FinInsightServices\PythonLec01\GetStockPrice\data.dat','r').read())

startDate = "2017-01-01"
re = {}

for itemcode in source:
    
    if (itemcode == 'KOSPI200'):
        item = "^KS11"
    else:
        item = itemcode + ".KS"

    df = data.get_data_yahoo(item,startDate)

    if (len(df) == 0):
        item = itemcode + ".KQ"
        df = data.get_data_yahoo(item,startDate)

    df.index = df.index.strftime('%Y-%m-%d')
    re[itemcode] = json.loads(df.reset_index().to_json(orient='records'))


print( json.dumps(re))

