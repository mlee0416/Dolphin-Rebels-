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

yelp_df = pd.read_csv('LA_County_Resturants_CensusTracts.csv', encoding='utf-8')




df = pd.concat([yelp_df, pd.get_dummies(yelp_df['category1'])], axis=1)

df['price'].replace(['$', '$$', np.nan, '$$$', '$$$$'],[1,2,0,3,4], inplace=True)

#top 15 resturant categories in LA
top15 = list(df['category1'].value_counts()[:15].index)


x_axis=df['category1'].value_counts()[:15].index
heights = df['category1'].value_counts()[:15].values
plt.bar(x_axis, heights)


c_grp = df.groupby('CensusTract')
# pull averages from grouped datasets, do that to all the numerical columns
rating_averages = c_grp['rating'].mean()

pd.get_dummies(c_grp['price'].count())


total_resturants = c_grp['category1'].count().rename('total_resturants')

types_rest = c_grp[top25].sum()



ydf = pd.concat([c_grp.mean()[['rating','review_count']].reset_index(),
                 ,
                 total_resturants, types_rest], axis=1)

ydf['average resturant price'] = round(c_grp['price'].mean(),0)


cdf = pd.read_csv('kaggle_census.csv')



df = pd.merge(left=ydf, right=cdf, how='right', on='CensusTract')

df.to_csv('final_census_yelp.csv')

for x in df.columns:
    print(x)
    

# yelp ratings by IncomePerCap
plt.style.available
plt.style.use('fivethirtyeight')
sns.set_palette('pastel')
sns.jointplot(y='IncomePerCap', x='rating', data=df,
            kind='scatter', stat_func=None,ylim=(0,100000), xlim=(2.5,5.2))
plt.tick_params(axis='both',width=2, labelsize=12)
#plt.text(2.5, 5400,"Poverty vs Higher Education by Census Tract",fontsize=25 )
#plt.ylabel('Tract Income per Cap')
#plt.xlabel('Average Yelp Resturant Rating')
#plt.xlim(0,100)
#plt.ylim(0,10000)
plt.show()



sns.set_palette('pastel')
sns.countplot(y='Poverty', hue='average price', data=df)
plt.tick_params(axis='both',width=2, labelsize=12)
plt.show()


# resturant prices in census tracts bellow the median income
low_df = df[df['IncomePerCap'] < df['IncomePerCap'].median()].dropna(axis=0)


sns.distplot(low_df['average resturant price'])


#charting out resturant preferences
left=yelp_df[[]]
df = pd.merge(left=yelp_df, right=cdf, how='outer', on='CensusTract')

#top 15 kinds of resturants in LA
top15 = yelp_df['category1'].value_counts()[:15]
top15.plot("barh", stacked=True,color='#ae7181')
plt.text(100,10.3,'Top 15 Types of Resturants for LA',fontsize=15)           
plt.xticks(rotation=40)
plt.show()

def rest_filter(demo, by):                 
    filter_df = df[df[demo] > by]
    value_counts = filter_df['category1'].value_counts(normalize=True)[:15]
    print(value_counts)
    return value_counts
top15_white = rest_filter('White',60)                
top15_black = rest_filter('Black',60)                 
                 
