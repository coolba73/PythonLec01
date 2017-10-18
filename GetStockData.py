


itemCode = "005930"

from pandas_datareader import data

df = data.DataReader("KRX:" + itemCode,"google" )

# print(df.head())

# print(df.columns)
# print(df.index)

# print(df.index.strftime('%Y-%m-%d'))

df.index = df.index.strftime('%Y-%m-%d')


df = df.drop('Open',1)
df = df.drop('High',1)
df = df.drop('Low',1)
df = df.drop('Volume',1)


print(df.to_json())

