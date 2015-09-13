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

# Function to generate test data
def CreateDataSet(Number=1):
    Output = []

    for i in range(Number):

        # Create a weekly (mondays) date range
        rng = pd.date_range(start='1/1/2009', end='12/31/2012', freq='W-MON')

        # Create random data
        data = np.randint(low=25, high=1000, size=len(rng))

        # Status pool
        status = [1, 2, 3]

        # Make a random list of statuses
        random_status = [status[np.randint(low=0, high=len(status))] for i in range(len(rng))]

        # State pool
        states = ['GA', 'FL', 'fl', 'NY', 'NJ', 'TX']

        # Make a random list of states
        random_states = [states[np.randint(low=0, high=len(states))] for i in range(len(rng))]

        Output.extend(zip(random_states, random_status, data, rng))

    return Output


# Create dataset
dataset = CreateDataSet(4)
df = pd.DataFrame(data=dataset, columns=['State', 'Status', 'Customer Count', 'Status Date'])
df.info()

print df.head()

df.to_excel('Lesson3.xlsx', index=False)
print 'Done'

#reading xlsx file
location = r'Lesson3.xlsx'

# parse a specific sheet
df = pd.read_excel(location, 0, index_col='Status Date')
print df.dtypes

print df.index
