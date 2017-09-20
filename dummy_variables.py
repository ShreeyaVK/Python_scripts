# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 14:42:41 2017

@author: Sadhna Kathuria
"""

# create dummy variables for catagorical variables with two categories like sex can be either male or female

import pandas as pd

path = 'C:/Users/Sadhna Kathuria/Documents/Shreeya_Programming/Predictive/Chapter 2'
filename1 = 'titanic3.csv'
fullpath = path + '/' + filename1
data = pd.read_csv(fullpath)

dummy_sex = pd.get_dummies(data['sex'],prefix = 'sex')

column_names = data.columns.values.tolist()

column_names.remove('sex')

newdata = data[column_names].join(dummy_sex)