# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 00:26:28 2018

@author: corey



"""

import pandas as pd

df = pd.read_csv('poverty_rates.csv')



full_tracts = []
for tract in df['census_tract']:
    append_tract = '6037' + str(tract)
    print(int(append_tract))
    full_tracts.append(append_tract)
    
df['tract'] = full_tracts

