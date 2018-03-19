# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 00:33:30 2018

@author: corey
"""

import pandas as pd

df = pd.read_csv('2015_census_tract_data.csv')

df.columns

la = df[df['County'] == 'Los Angeles']

pov_edu = pd.read_csv('census_data.csv')

censustracts = []

for i in pov_edu['census_tract']:
    censustracts.append(int("6037" + str(i)))

pov_edu['CensusTract'] = censustracts

df = pd.merge(la, pov_edu, how='left', on='CensusTract')


df.to_csv('kaggle_census.csv')
