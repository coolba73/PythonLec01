import pandas


prices = pandas.DataFrame([1035.23, 1032.47, 1011.78, 1010.59, 1016.03, 1007.95, 
              1022.75, 1021.52, 1026.11, 1027.04, 1030.58, 1030.42,
              1036.24, 1015.00, 1015.20])

# print(prices)

# print(prices[1:] )


price2 = { 'p1' : prices[:-1].values.tolist() , 'p2' : prices[1:].values.tolist() }

df = pandas.DataFrame(data = price2)

print(df)

