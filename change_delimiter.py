# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 19:03:55 2017

@author: Sadhna Kathuria
"""

import pandas as pd
#change the delimter of a dataset

path = 'C:/Users/Sadhna Kathuria/Documents/Shreeya_Programming/Predictive/Chapter 2'
#filename1 = 'titanic3.csv'
filename2 = 'Customer Churn Model.txt'
filename_tab = 'Tab Customer Churn Model.txt'
#filename3 = 'titanic3.xls'
#fullpath = os.path.join(path, filename)
infile = path + '/' + filename2

outfile = path +'/' + filename_tab

with open(infile) as infile1:
    with open(outfile, 'w') as outfile1:
        
        for line in infile1:
            fields = line.split(',')
            outfile1.write('/t'.join(fields))
            
            
data = pd.read_csv(outfile1)
print data

        