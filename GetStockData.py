from pandas_datareader import data

itemCode = "005930"
df = data.DataReader("KRX:" + itemCode,"google" )

df.index = df.index.strftime('%Y-%m-%d')

df = df.drop('Open',1)
df = df.drop('High',1)
df = df.drop('Low',1)
df = df.drop('Volume',1)

print(df.to_json())

