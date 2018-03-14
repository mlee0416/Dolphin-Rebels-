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

#filter down to just LA
la_edu_df = edu_df

ct_edu_df = edu_df[edu_df['geotype'] == 'CT']

la_edu_df = ct_edu_df[ct_edu_df['county_name'] == 'Los Angeles']

total_la_df = la_edu_df[la_edu_df['race_eth_name'] == 'Total']

final_edu_df = total_la_df[total_la_df['reportyear'] == '2011-2015']

#remove the first 4 numbers of the census tract number so it matches the census tracts in the main df
short_tracts = []
for i in final_edu_df['geotypevalue']:
    print(i)
    print(str(i)[4:])
    short_tracts.append(str(i)[4:])

final_edu_df['census_tract'] = short_tracts
    



final_edu_df[['census_tract', 'estimate']].dropna(how='any')

pd.merge(df, final_edu_df[['census_tract', 'estimate']], how='left', on='census_tract').head()
