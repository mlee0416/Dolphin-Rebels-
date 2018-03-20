# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 18:21:15 2018

@author: corey

Doing final merge on yelp and census data

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('LA_County_Resturants_CensusTracts.csv', encoding='utf-8')
df = pd.concat([df, pd.get_dummies(df['category1'])], axis=1)

#top 25 resturant categories in LA
top25 = list(df['category1'].value_counts()[:50].index)

c_grp = df.groupby('CensusTract')
# pull averages from grouped datasets, do that to all the numerical columns
rating_averages = c_grp['rating'].mean() 


total_resturants = c_grp['category1'].count().rename('total_resturants')

types_rest = c_grp[top25].sum()

ydf = pd.concat([c_grp.mean()[['rating','review_count']].reset_index(), total_resturants, types_rest], axis=1)

cdf = pd.read_csv('kaggle_census.csv')



df = pd.merge(left=ydf,right=cdf, how='right', on='CensusTract')

df.to_csv('final_census_yelp.csv')

df.corr().to_csv('correlation.csv')

for x in df.columns:
    print(x)
    


plt.style.available
plt.style.use('fivethirtyeight')
sns.set_palette('pastel')
sns.jointplot(y='IncomePerCap', x='rating', data=df,
            kind='kde', stat_func=None,ylim=(0,100000), xlim=(2.5,5.2))
plt.tick_params(axis='both',width=2, labelsize=12)
#plt.text(2.5, 5400,"Poverty vs Higher Education by Census Tract",fontsize=25 )
#plt.ylabel('Tract Income per Cap')
#plt.xlabel('Average Yelp Resturant Rating')
#plt.xlim(0,100)
#plt.ylim(0,10000)
plt.show()
