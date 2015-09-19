import pandas as pd
pd.core.format.header_style = None  # <--- This line fixes it.
import numpy.random as np
import matplotlib.pyplot as plt
import sys

#matplotlib inline

print 'Python Version: ' + sys.version
print 'Pandas Version: ' + pd.__version__

#set seed
np.seed(111)

#reading xlsx file
location = r'Lesson3.xlsx'

# parse a specific sheet
df = pd.read_excel(location, 0, index_col='Status Date')

print df['State'].unique()

# Clean State Column, convert to upper case
df['State'] = df.State.apply(lambda x: x.upper())

print df['State'].unique()

# only grab where Status==1
mask = df['Status'] == 1
df = df[mask]

#convert NJ to NY
mask = df.State == 'NJ'
df['State'][mask] = 'NY'
print df['State'].unique()

df['Customer Count'].plot(figsize=(15,5))

sortdf = df[df['State']=='NY'].sort(axis=0)
print sortdf.head(10)

#group by state and status date
Daily = df.reset_index().groupby(['State', 'Status Date']).sum()
print Daily.head()

del Daily['Status']
print Daily.head()

#print Daily.index()

print Daily.index.levels[0]

print Daily.index.levels[1]

Daily.loc['FL'].plot()
Daily.loc['GA'].plot()
Daily.loc['NY'].plot()
Daily.loc['TX'].plot()

Daily.loc['FL']['2012':].plot()
Daily.loc['GA']['2012':].plot()
Daily.loc['NY']['2012':].plot()
Daily.loc['TX']['2012':].plot();
