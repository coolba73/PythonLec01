import pprint
import json
import pandas as pd
import numpy as np
import codecs

# source = json.loads(codecs.open('D:\FinInsightServices\PythonLec01\CalStd\data.dat','r','utf-8').read())

source = json.loads(open('D:\FinInsightServices\PythonLec01\CalStd\data2.dat','r').read())

df = pd.DataFrame( source['InputData']);

TargetColumn = source["TargetColumn"]

df = df[TargetColumn]

stdval = np.std(df, ddof=1)

reary = []
reval = {}
re = {}

reval[TargetColumn + "_Std"] = stdval

reary.append(reval)

re['result'] = reary


print( json.dumps(re))

