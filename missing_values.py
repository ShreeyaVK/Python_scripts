# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 14:00:25 2017

@author: Sadhna Kathuria
"""

import pandas as pd

path = 'C:/Users/Sadhna Kathuria/Documents/Shreeya_Programming/Predictive/Chapter 2'
filename1 = 'titanic3.csv'
fullpath = path + '/' + filename1
data = pd.read_csv(fullpath)


print pd.isnull(data['body'])

pd.isnull(data['body'].values.ravel().sum())

#how to clean data?

# Deletion:drop all rows where all cells have nan; use 'any' for atleast one cell

newdata = data.dropna(axis=0, how='all')

# Imputation

data_missing = data.fillna('missing')
data_0 = data.fillna(0)
age_mean = data['age'].fillna(data['age'].mean())
age_ffil = data['age'].fillna(method = 'ffill')
age_backfill = data['age'].fillna(method = 'backfill')

