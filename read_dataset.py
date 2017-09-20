# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 17:04:15 2017

@author: Sadhna Kathuria
"""

import pandas as pd

path = 'C:/Users/Sadhna Kathuria/Documents/Shreeya_Programming/Predictive/Chapter 2'
#filename1 = 'titanic3.csv'
filename2 = 'Customer Churn Model.txt'
file_cols = 'Customer Churn Columns.csv'
#filename3 = 'titanic3.csv'
#fullpath = os.path.join(path, filename)
fullpath = path + '/' + filename2
fullpath_cols = path + '/' + file_cols
data = pd.read_csv(fullpath)


data_columns = pd.read_csv(fullpath_cols)
data_columns_list = data_columns['Column_Names'].tolist()

# change the column names. 
data_new = pd.read_csv(fullpath, header = 0, names = data_columns_list)
print data_new.columns.values


