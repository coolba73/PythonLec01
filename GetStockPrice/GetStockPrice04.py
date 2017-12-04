import datetime
import requests
from io import StringIO
from pandas.io.common import urlencode
import pandas as pd

BASE = 'http://finance.google.com/finance/historical'


def get_params(symbol, start, end):
    params = {
        'q': symbol,
        'startdate': start.strftime('%Y/%m/%d'),
        'enddate': end.strftime('%Y/%m/%d'),
        'output': "csv"
    }
    return params


def build_url(symbol, start, end):
    params = get_params(symbol, start, end)
    return BASE + '?' + urlencode(params)


# today = '{0:%Y-%m-%d}'.format(datetime.datetime.now())

# start = '{0:%Y-%m-%d}'.format(datetime.datetime( int(today.split('-')[0]) - 1 ,int(today.split('-')[1]) ,int(today.split('-')[2]) ))
# end = today

today = '{0:%Y-%m-%d}'.format(datetime.datetime.now())
start = datetime.datetime( int(today.split('-')[0]) - 1 ,int(today.split('-')[1]) ,int(today.split('-')[2]) )
end = datetime.datetime.now()

# start = datetime.datetime(2010, 1, 1)
# end = datetime.datetime.today()

# sym = 'SPY'
sym = 'KRX:035420'
url = build_url(sym, start, end)

data = requests.get(url).text
data = pd.read_csv(StringIO(data), index_col='Date', parse_dates=True)

print(data.head())
