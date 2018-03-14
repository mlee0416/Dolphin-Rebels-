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
include = ['census_tract','estimate','CA_decile']

#save data to file
df = pd.merge(df, final_edu_df[include], how='left', on='census_tract')



df.to_csv('census_data.csv')

health_df = pd.read_csv()


