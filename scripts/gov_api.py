# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 22:56:53 2018

@author: corey

Script for pulling data from government APIs, merging them into a 
pandas dataframe and saving the results in a csv sheet

"""

import pandas as pd
from sodapy import Socrata


# pull pop, ethnicity, gender, and age groups by censu tract
# from County of Los Angeles Open Data, see url for source
url = "https://data.lacounty.gov/resource/qc6w-c878.csv"

client = Socrata("data.lacounty.gov", None)

demographics_results = client.get("qc6w-c878")

df = pd.DataFrame.from_records(demographics_results)

df['census_tract']

edu_df = pd.read_excel('raw_data/educational_data.xlsx',
              sheetname="HCI_Educational_Attainment_355")

#filter down to just Census tracts
ct_edu_df = edu_df[edu_df['geotype'] == 'CT']

#filter down to just Los Angeles
la_edu_df = ct_edu_df[ct_edu_df['county_name'] == 'Los Angeles']

#filter down to just total pop not by ethnicity
total_la_df = la_edu_df[la_edu_df['race_eth_name'] == 'Total']

#filter down to just use the most recent version of the survey
recent_version_df = total_la_df[total_la_df['version'] == 'Thu Aug 03 13:10:05 2017']

#filter down to just the most recent survey
final_edu_df = recent_version_df[recent_version_df['reportyear'] == '2011-2015']


#remove the first 4 numbers of the census tract number so it matches the census tracts in the main df
short_tracts = []
for i in final_edu_df['geotypevalue']:
    print(i)
    print(str(i)[4:])
    short_tracts.append(str(i)[4:])

final_edu_df['census_tract'] = short_tracts


len(final_edu_df[['census_tract', 'estimate']].dropna(how='any'))

#pick columns to save from education dataframe
include = ['census_tract','estimate']

#save data to file
df = pd.merge(df, final_edu_df[include], how='left', on='census_tract')


#select only important columns rename estimate to reflect that it's a percentage of bachelor degree holders
columns_to_keep = ['africanamerican138', 'africanamerican200',
       'age_0_15_138', 'age_0_15_200', 'age_16_18_138', 'age_16_18_200',
       'age_19_20_138', 'age_19_20_200', 'age_21_25_138', 'age_21_25_200',
       'age_26_59_138', 'age_26_59_200', 'age_60_64_138', 'age_60_64_200',
       'age_65up_138', 'age_65up_200', 'asian138', 'asian200', 'census_tract',
       'cityname', 'female138', 'female200', 'latino138', 'latino200',
       'male138', 'male200', 'multi_race138', 'nativeamerican138',
       'nativeamerican200', 'other138', 'otherrace200', 'pacific_islander138',
       'pacificislander200', 'service_area', 'two_more200', 'white138',
       'white200', 'estimate']


df = df[columns_to_keep].rename(columns={'estimate':'percent_bachelors'})


# aggregate pop stats into totals, also convert the columns to integers
def get_total(column1, column2):
    #take off the FPL codes and rename total
    total_column_name = column1[:-3] + 'total'
    
    #convert columns to integers
    df[column1] = df[column1].astype('int')
    df[column2] = df[column2].astype('int')
    
    # sum up the pops for 138 line and 200 line to get the total
    df[total_column_name] = df[[column1,column2]].sum(axis=1)
    
    
columns_to_aggregate = [['africanamerican138', 'africanamerican200'],
       ['age_0_15_138', 'age_0_15_200'], ['age_16_18_138', 'age_16_18_200'],
       ['age_19_20_138', 'age_19_20_200'], ['age_21_25_138', 'age_21_25_200'],
       ['age_26_59_138', 'age_26_59_200'], ['age_60_64_138', 'age_60_64_200'],
       ['age_65up_138', 'age_65up_200'], ['asian138', 'asian200'],
       ['female138', 'female200'], ['latino138', 'latino200'],
       ['male138', 'male200'], ['multi_race138','two_more200'], ['nativeamerican138',
       'nativeamerican200'], ['other138', 'otherrace200'], ['pacific_islander138',
       'pacificislander200'], ['white138',
       'white200']]    

for column1, column2 in columns_to_aggregate:
    get_total(column1, column2)

# get total pop for census tract
df['total_pop'] = df[['femaletotal','maletotal']].sum(axis=1)


def get_percap(column_name):
    df[column_name + '_percap'] = df[column_name] / df['total_pop']
    

# get total bachelors degree holders
df['bachelors_percap'] = (6000 * (df['percent_bachelors'] / 100)) / 6000



df.head()     




# pull out total impoverished and not impoverished. 
df['138_percap'] = df[['male138', 'female138']].sum(axis=1) / 6000
df['200_percap'] = df[['male200', 'female200']].sum(axis=1)

# get broad census tracts based off of the first 3 numbers
tract_groups = []
for i in df['census_tract']:
    print(i)
    print(str(i)[:2])
    tract_groups.append(str(i)[:2])

df['tract_group'] = tract_groups

df['tract_group'].value_counts()[:50]

df[['tract_group','census_tract', 'total_pop','not_impoverished_percap','impoverished_percap', ]].to_csv('poverty_rates.csv')

len(df.groupby('tract_group')['total_pop'].sum())


df.to_csv('census_data.csv')
