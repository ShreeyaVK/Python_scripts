# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 13:40:10 2017

@author: Sadhna Kathuria
"""

import numpy as np
import matplotlib.pyplot as plt

randnum = np.random.uniform(1,100,10000)

plt.hist(randnum,100)
