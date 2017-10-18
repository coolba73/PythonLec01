

from pandas_datareader import data
import datetime
import numpy as np

df = data.DataReader("KRX:005930","google")
kospi200 = data.DataReader("KRS:KOSPI200","google")



# print(type(df))
# print(df.tail())
# print(kospi200.tail())






