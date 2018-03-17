# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 00:26:28 2018

@author: corey

Merging Zip Codes to the census data

"""

import pandas as pd

df = pd.read_csv('poverty_rates.csv')
zip_df = pd.read_excel('ZIP_TRACT_122017.xlsx',sheetname='Sheet1')


full_tracts = []
for tract in df['census_tract']:
    append_tract = '06037' + str(tract)
    full_tracts.append(append_tract)
    
df['tract'] = full_tracts
    
pd.merge(df, zip_df, on='tract', how='outer')
