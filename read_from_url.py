# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 19:35:57 2017

@author: Sadhna Kathuria
"""

# read from url

import csv
import urllib2

url = 'http://winterolympicsmedals.com/medals.csv'
response = urllib2.urlopen(url)
cr = csv.reader(response)

for rows in cr:
    print rows