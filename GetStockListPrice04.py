import json
from pandas_datareader import data
from collections import OrderedDict

items = OrderedDict()

re = {}

items["item"] = ["005930","066570"]

for item in items["item"]:
    df = data.DataReader("KRX:" + item,"google" )
    df.index = df.index.strftime('%Y-%m-%d')
    re[item] = json.loads(df.reset_index().to_json(orient='records'))

print(json.dumps(re))




