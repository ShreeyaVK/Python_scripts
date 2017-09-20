# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 19:20:22 2017

@author: Sadhna Kathuria
"""

import pandas as pd

path = 'C:/Users/Sadhna Kathuria/Documents/Shreeya_Programming/Predictive/Chapter 2'
filename = 'Tab Customer Churn Model.txt'
fullpath = path + '/' + filename
data = pd.read_csv(fullpath)