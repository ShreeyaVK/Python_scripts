# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 18:45:58 2017

@author: Sadhna Kathuria
"""

#number of cols

import pandas as pd

path = 'C:/Users/Sadhna Kathuria/Documents/Shreeya_Programming/Predictive/Chapter 2'
#filename1 = 'titanic3.csv'
filename2 = 'Customer Churn Model.txt'
file_cols = 'Customer Churn Columns.csv'
#filename3 = 'titanic3.xls'
#fullpath = os.path.join(path, filename)
fullpath = path + '/' + filename2


data = open(fullpath,'r')
cols = data.next().strip().split(',')
no_cols =len(cols)

#number of rows

counter =0
main_dict = {}
for col in cols:
    main_dict[col] = []


for line in data:
    values = line.strip().split(',')
    for i in range(no_cols):
        main_dict[cols[i]].append(values[i])
        
    counter += 1
    
print "The dataset contains %s number of rows and %s number of columns" %(counter, no_cols)
        

# convert the dictionary to data frame

df= pd.DataFrame(main_dict)
df.to_csv(path+'/'+ 'new Customer Churn Model.csv')
df.to_excel(path + '/' + 'new Customer Churn Model.xls')