
import datetime
import requests
from io import StringIO
from pandas.io.common import urlencode
import pandas as pd
import json

# ==========================================================================================================================================================================
BASE = 'http://finance.google.com/finance/historical'
source = json.loads( open('D:\FinInsightServices\PythonLec01\GetStockPrice\data.dat','r').read())

# ==========================================================================================================================================================================
def get_params(symbol, start, end):
    params = {
        'q': symbol,
        'startdate': start.strftime('%Y/%m/%d'),
        'enddate': end.strftime('%Y/%m/%d'),
        'output': "csv"
    }
    return params

# ==========================================================================================================================================================================
def build_url(symbol, start, end):
    params = get_params(symbol, start, end)
    return BASE + '?' + urlencode(params)
# ==========================================================================================================================================================================


today = '{0:%Y-%m-%d}'.format(datetime.datetime.now())
start = datetime.datetime( int(today.split('-')[0]) - 1 ,int(today.split('-')[1]) ,int(today.split('-')[2]) )
end = datetime.datetime.now()



sym = 'KRX:035420'
url = build_url(sym, start, end)
re = []
itemprice = {}

data = requests.get(url).text
data = pd.read_csv(StringIO(data), index_col='Date', parse_dates=True)
itemprice["1111"] = data.to_json()

print(itemprice)







print(source)