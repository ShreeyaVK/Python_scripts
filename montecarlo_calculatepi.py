# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:31:20 2017

@author: Sadhna Kathuria
"""

## calculate pi using monte carlo simulation


import numpy as np
import matplotlib.pyplot as plt

nums = 1000
iter = 100
#def pi_run(nums,iter):
pi_avg =0
pi_val_list =[]
    
for i in range(iter):
    value = 0
    x=np.random.uniform(0,1,nums).tolist()
    y=np.random.uniform(0,1,nums).tolist()
    for j in range(nums):
        z=np.sqrt(x[j]*x[j] + y[j]*y[j])
        if z<1:
            value = value + 1
    pi_val = (float(value) * 4)/nums
    pi_val_list.append(pi_val)
                
pi_avg = sum(pi_val_list)/iter
ind = range(1,iter+1)
    
fig = plt.plot(ind,pi_val_list)
 #return(pi_avg,fig)
        
                
                
        