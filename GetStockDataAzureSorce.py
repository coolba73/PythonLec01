#https://funcinsalways.scm.azurewebsites.net/DebugConsole

import os
import json
import platform
from pandas_datareader import data

postreqdata = json.loads(open(os.environ['req']).read())
response = open(os.environ['res'], 'w')

itemCode = postreqdata['itemcode']

df = data.DataReader("KRX:" + itemCode,"google" )

df.index = df.index.strftime('%Y-%m-%d')

df = df.drop('Open',1)
df = df.drop('High',1)
df = df.drop('Low',1)
df = df.drop('Volume',1)

response.write(df.to_json())
response.close()