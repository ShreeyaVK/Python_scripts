# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 16:23:20 2017

@author: Sadhna Kathuria
"""

import pandas as pd
#import pylab
#import matplotlib.pyplot as plt

path = 'C:/Users/Sadhna Kathuria/Documents/Shreeya_Programming/Predictive/Chapter 2'
filename1 = 'Customer Churn Model.txt'
fullpath = path + '/' + filename1
data = pd.read_csv(fullpath)

"""
## select particular columns
wanted_columns = ['State','Account Length','Area Code']
subdata = data[wanted_columns]
"""

##for larger datasets
wanted_columns = ['State','Account Length','Area Code']
column_list=data.columns.values.tolist()
sublist=[x for x in column_list if x not in wanted_columns]
subdata = data[sublist]


## subsetting using index numbers

subdata2=data.iloc[1:10,1:20]

### creating new columns

data['Total Mins'] = data['Day Mins'] + data['Eve Mins'] + data['Night Mins']
print data.shape