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

#read data
#reading xlsx file
location = r'Lesson3.xlsx'

# parse a specific sheet
df = pd.read_excel(location, 0, index_col='Status Date')
print df.dtypes

print df.index

print df.head()
