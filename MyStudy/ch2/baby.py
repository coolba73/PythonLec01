
#_________________________________________________________________________________________________________________________________________________________________________
#%%

import pandas as pd
import numpy as np

years = range(1880,2011)
columns = ['name','sex','births']
pieces = []

for year in years:
    path = 'D:\Test\PythonForDataAnalysisBook\pydata-book-2nd-edition\pydata-book-2nd-edition\datasets\\babynames\yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)


#_________________________________________________________________________________________________________________________________________________________________________
#%%

total_births = names.pivot_table('births',index ='year', columns='sex', aggfunc=sum)
total_births

#%%
def add_prop(group):
    births = group.births
    group['prop'] = births / births.sum()
    return group

names = names.groupby(['year','sex']).apply(add_prop)

names

# print(np.allclose(names.groupby(['year','sex']).prop.sum(),1))

#_________________________________________________________________________________________________________________________________________________________________________
#%%

def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]

grouped = names.groupby(['year','sex'])

top1000 = grouped.apply(get_top1000)
top1000.index = np.arange(len(top1000))


boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']


boys
girls



    



