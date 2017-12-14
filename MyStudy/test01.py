#_________________________________________________________________________________________________________________________________________________________________________
#%%

import pandas as pd
from pandas_datareader import data

all_data = {}

for ticker in {'AAPL','IBM','MSFT','GOOG'}:
    all_data[ticker] = data.DataReader(ticker, 'google', '2015-01-01','2016-01-01')

    
