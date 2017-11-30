import os
import json
import platform
from pandas_datareader import data
from collections import OrderedDict
import pandas_datareader.data as wb


df = data.DataReader("KRX:KOSPI","google",'2017-01-01' )

# df = wb.DataReader('KRX:KOSPI', 'google')

# df = data.get_data_google("KRX:KOSPI")

# df = data.get_data_yahoo("^KS11")
# df = data.get_data_yahoo("035420.KS","2017-01-01")

# print(len(df))

print(df)


# revdata = open(os.environ['req']).read()

# source = json.loads(open('D:\FinInsightServices\PythonLec01\GetStockPrice\data.dat','r').read())

# postreqdata = json.loads(revdata)

# response = open(os.environ['res'], 'w')

# print( 'req data : ' + revdata)

# re = {}

# print(source)

# for itemcode in source:
#     df = data.DataReader("KRX:" + itemcode,"google" )
#     df.index = df.index.strftime('%Y-%m-%d')
#     re[itemcode] = json.loads(df.reset_index().to_json(orient='records'))

# print(df)

# response.write(json.dumps(re) )
# response.close()