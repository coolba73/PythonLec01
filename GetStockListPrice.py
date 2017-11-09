import json
from pandas_datareader import data
from collections import OrderedDict

# items = OrderedDict()

# items["item"] = ["0001","0002"]

# jobj = json.dumps(items)

# print(jobj)

# for i in jobj["item"]:
#     print(i)


itemCode = "005930"

df = data.DataReader("KRX:" + itemCode,"google" )

df.index = df.index.strftime('%Y-%m-%d')


# df = df.drop('Open',1)
# df = df.drop('High',1)
# df = df.drop('Low',1)
# df = df.drop('Volume',1)
# print(df)
# print(df.to_dict()['Close'])

# print(df.to_json())

re = OrderedDict()
re[itemCode] = df.to_dict()["Close"]

print(re)



