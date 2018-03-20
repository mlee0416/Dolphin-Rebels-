# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 20:56:04 2018

@author: corey


Cleaning up the  Yelp Dataset

"""
import pandas as pd
from pprint import pprint
import numpy as np
import json 

df = pd.read_csv('LA_SAMPLE.csv', sep='\t', encoding='utf-8', index_col = )


# this variable is for testing extract_location
loc_sample = "{'address1': '349 N State College Blvd', 'address2': None, 'address3': None, 'city': 'Fullerton', 'zip_code': '92831', 'country': 'US', 'state': 'CA', 'display_address': ['349 N State College Blvd', 'Fullerton, CA 92831']}"
 

def extract_location(df):
    '''
    breaks yelp's location data along the key that we want and then
    splits the value away via it's commas
    '''
    cities = []
    zip_codes = []
    for row in df['location']:
        city = row.split("'city': ")[1].split(",")[0].strip("'")
        cities.append(city)
        try:
            zip_code = row.split("'zip_code': ")[1].split(",")[0].strip("'")
        except:
            zip_code = np.nan
        zip_codes.append(zip_code)
    df['city'] = cities
    df['zipcode'] = zip_codes
        
extract_location(df)


def extract_category(df):
    category1 = []
    category2 = []
    category3 = []
    for x in df['categories']:
        json_rec = json.loads(x.replace("'", '"'))
        category1.append(json_rec[0]['title'])
        try:
            category2.append(json_rec[1]['title'])
        except:
            category2.append('')
        try:
            category3.append(json_rec[2]['title'])
        except:
            category3.append('')
    df['category1'] = category1
    df['category2'] = category2
    df['category3'] = category3
    
extract_category(df)

df.to_csv('LA_Yelp_Sample.csv', encoding='utf-8')



