# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 12:28:24 2017

@author: Sadhna Kathuria
"""

## generate random numbers

import numpy as np
#random number between 1  and 100
print np.random.randint(1,100)

#random number between 0 and 1
print np.random.random()

#function for generating multiple random numbers

def randint_range(n,a,b):
    x=[]
    for i in range(n):
        x.append(np.random.randint(a,b))
    return x


print randint_range(10,1,45)

# generate random numbers in the range 0 to 100 that are multiples of 4
import random
for i in range(3):
    print random.randrange(0,100,4) ## note that the first number will always be zero /10/100
    

#shuffle a list
a=range(20)
np.random.shuffle(a)
print a


#choose a random value from a list
import pandas as pd

path = 'C:/Users/Sadhna Kathuria/Documents/Shreeya_Programming/Predictive/Chapter 2'
filename1 = 'Customer Churn Model.txt'
fullpath = path + '/' + filename1
data = pd.read_csv(fullpath)

column_names = data.columns.values.tolist()

print np.random.choice(column_names)

#generate the same random numbers using seed
p=[]
np.random.seed(1)
for i in range(5):
    p.append(np.random.randint(1,10))

print p
    

q=[]
for i in range(5):
     q.append(np.random.randint(1,10))

print q

r=[]
np.random.seed(1)
for i in range(5):
     r.append(np.random.randint(1,10))

print r