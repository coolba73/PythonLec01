import json
from pandas_datareader import data
from collections import OrderedDict

items = OrderedDict()
re = OrderedDict()

items["item"] = ["005930","066570"]

for item in items["item"]:

    df = data.DataReader("KRX:" + item,"google" )
    df.index = df.index.strftime('%Y-%m-%d')
    re[item] = df.to_dict()["Close"]

# print(re)

print(json.dumps(re))



