import pandas as pd 

d1 = {'key':['a','b','c'], 'col1':[1,2,3,], 'col2':[10,20,30]}
d2 = {'key':['a','c','b'], 'cola':[4,5,6,], 'colb':[40,50,60]}

df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)

print(df1)
print(df2)


result = pd.merge(df1,df2, on='key')

print(result)

