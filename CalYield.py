import pandas as pd
import numpy as np

prices = pd.DataFrame([1035.23, 1032.47, 1011.78, 1010.59, 1016.03, 1007.95, 
              1022.75, 1021.52, 1026.11, 1027.04, 1030.58, 1030.42,
              1036.24, 1015.00, 1015.20])

# print(prices)

df1 = pd.concat( [  prices,  prices.shift(-1) , prices / prices.shift(-1)  ], axis=1);

df1.columns = ['p','p1','p2']

# df1['plog'] = math.log(df1.p2)

df1 =  df1.dropna()

df1["logp"] =  np.log(df1['p2'])

print(df1)






# df1 = pandas.concat([prices.shift(-1)] , axis=1)
# df2 = pandas.concat([ prices / prices.shift(-1)] , axis=1)


# df = pandas.DataFrame([{'p1' : prices.values.tolist()}] )



# df2 = pandas.DataFrame( df1 , columns=['p1','p2','p3']).reset_index()

# print(df1)




# print( math.log( prices / prices.shift(-1)) )

# print(prices[1:] )


# price2 = { 'p1' : prices[:-1].values.tolist() , 'p2' : prices[1:].values.tolist() }

# df = pandas.DataFrame(data = price2)

# cal = df.p1 / df.p2

# df = pandas.DataFrame({'p1':prices[:-1].values , 'p2' : prices[1:].values })

# df['sum'] = df['p1'] + df['p2']

# print(df)


# frame = pandas.DataFrame({'a': [1, 2, 3], 'b': [3, 5, 4]})

# frame['c'] = frame['a'] + frame['b']

# print(frame)
