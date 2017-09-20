# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 13:57:49 2017

@author: Sadhna Kathuria
"""

import numpy as np
import matplotlib.pyplot as plt

#standard normal distribution
randnum=np.random.randn(1000)
plt.hist(randnum)

#normal distribution

randnum2=2.5*np.random.randn(1000)+1.5
plt.hist(randnum2)
