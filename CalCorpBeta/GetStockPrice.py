
import datetime
import requests
from io import StringIO
from pandas.io.common import urlencode
import pandas as pd
import json

#_________________________________________________________________________________________________________________________________________________________________________
BASE = 'http://finance.google.com/finance/historical'

def get_params(symbol, start, end):
    params = {
        'q': symbol,
        'startdate': start.strftime('%Y/%m/%d'),
        'enddate': end.strftime('%Y/%m/%d'),
        'output': "csv"
    }
    return params

#_________________________________________________________________________________________________________________________________________________________________________
def build_url(symbol, start, end):
    params = get_params(symbol, start, end)
    return BASE + '?' + urlencode(params)

#_________________________________________________________________________________________________________________________________________________________________________
def GetStockPrice(itemCode):
    today = '{0:%Y-%m-%d}'.format(datetime.datetime.now())
    start = datetime.datetime( int(today.split('-')[0]) - 1 ,int(today.split('-')[1]) ,int(today.split('-')[2]) )
    end = datetime.datetime.now()
    sym = "KRX:" + itemCode
    url = build_url(sym, start, end)
    data = requests.get(url).text
    data = pd.read_csv(StringIO(data), index_col='Date', parse_dates=True)
    data = data.reset_index()
    data["Date"] = data["Date"].dt.strftime('%Y-%m-%d')
    return data
#_________________________________________________________________________________________________________________________________________________________________________


re = GetStockPrice("KOSPI200")

print(re)




