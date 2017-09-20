# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 00:32:38 2017

@author: Sadhna Kathuria
"""

## create dummy data frame

import pandas as pd
import numpy as np

df=pd.DataFrame({'A':np.random.randn(10),'B':np.random.randn(10)},index=range(15,25))

print df