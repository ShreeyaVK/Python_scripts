# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 15:11:04 2017

@author: Sadhna Kathuria
"""

import pandas as pd
import pylab
import matplotlib.pyplot as plt

path = 'C:/Users/Sadhna Kathuria/Documents/Shreeya_Programming/Predictive/Chapter 2'
filename1 = 'Customer Churn Model.txt'
fullpath = path + '/' + filename1
data = pd.read_csv(fullpath)
"""
#plot

data.plot(kind='scatter', x='Day Mins', y='Day Charge')
pylab.savefig('C:\Users\Sadhna Kathuria\Documents\Shreeya_Programming\Python\Predictive analytics\scatterplot.png')

data.plot(kind ='scatter', x = 'Night Calls', y= 'Night Charge')


## subplots

figure, axs = plt.subplots(2,2,sharey=True,sharex=False)
data.plot(kind='scatter',x='Day Mins',y='Day Charge', ax=axs[0][0])
data.plot(kind='scatter',x='Night Mins',y='Night Charge', ax=axs[0][1])
data.plot(kind='scatter',x='Day Calls', y='Day Charge', ax=axs[1][0])
data.plot(kind='scatter',x='Night Calls',y='Night Charge',ax=axs[1][1])
figure.savefig('C:\Users\Sadhna Kathuria\Documents\Shreeya_Programming\Python\Predictive analytics\subplot.png')


## histograms

plt.hist(data['Day Calls'], bins = [0, 25,50,75,100,125,150,175])
plt.xlabel('Day Calls value')
plt.ylabel('Frequency')
plt.title('Frequency Distribution of day calls')

"""

## boxplots
plt.boxplot(data['Day Calls'])
plt.ylabel('Day Calls')
plt.title('Box Plot of day calls')