
# coding: utf-8

# In[2]:


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
import censusgeocode as cg

df = pd.read_csv('LA_County_restaurants.csv', sep='\t', encoding='utf-8', index_col='Unnamed: 0')
df.head()

df = df[df['city'] == "Los Angeles"]


# In[100]:


# this variable is for testing extract_location
loc_sample = "{'address1': '349 N State College Blvd', 'address2': None, 'address3': None, 'city': 'Fullerton', 'zip_code': '92831', 'country': 'US', 'state': 'CA', 'display_address': ['349 N State College Blvd', 'Fullerton, CA 92831']}"


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


# In[87]:


#pprint(loc_sample)


def extract_location(df):
    '''
    breaks yelp's location data along the key that we want and then
    returns it as a new dataframe
    '''
    cities = []
    zip_codes = []
    streets = []
    #print(df['location'])
    #print(json.dumps(df['location']))
    placeholder = []
    for row in df['location']:
        try:
            address = row.split("'display_address': ['")[1].rstrip("']}").split("', '")
            city = address[1].split(",")[0]
            #print(city)
            cities.append(city)
            street = address[0]
            print(street, city)
            streets.append(address[0])
            #print(address)
        except:
            print('error: \n')
            print(row)
            cities.append('none')
            streets.append('none')
        
        try:
            zip_code = row.split("'zip_code': ")[1].split(",")[0].strip("'")
        except:
            zip_code = np.nan
            
        zip_codes.append(zip_code)
    df['city'] = cities
    df['street'] = streets
    df['zipcode'] = zip_codes
        

       
extract_location(df)    


# In[101]:


df.info()


# In[ ]:


import pandas as pd
from pprint import pprint
import numpy as np
import json
import censusgeocode as cg

df = pd.read_csv('LA_County_restaurants.csv', sep='\t', encoding='utf-8', index_col='Unnamed: 0')


results = []
for index,row in df.iterrows():
    lat = round(row['Latitude'],5)
    print(lat)
    lon = round(row['Longitude'],5)
    print(lon)
    
    try:
        response = cg.coordinates(x=lat, y=lon)
        tract = response['2010 Census Blocks'][0]['TRACT']
        print(tract)
        results.append(f"6037{tract}")
    except:
        results.append(np.nan)
        pass
    


# In[7]:


result = {'Counties': [{'OID': 275901063468976, 'STATE': '06', 'FUNCSTAT': 'A', 'AREAWATER': 1794659470, 'NAME': 'Los Angeles County', 'LSADC': '06', 'CENTLON': '-118.2617650', 'BASENAME': 'Los Angeles', 'INTPTLAT': '+34.1963983', 'COUNTYCC': 'H1', 'MTFCC': 'G4020', 'COUNTY': '037', 'GEOID': '06037', 'CENTLAT': '+34.1957768', 'INTPTLON': '-118.2618616', 'AREALAND': 10510687541, 'COUNTYNS': '00277283', 'OBJECTID': 398, 'CENT': (-118.261765, 34.1957768), 'INTPT': (-118.2618616, 34.1963983)}], 'Census Tracts': [{'OID': 207901115289836, 'STATE': '06', 'FUNCSTAT': 'S', 'NAME': 'Census Tract 1993', 'AREAWATER': 40785, 'LSADC': 'CT', 'CENTLON': '-118.1992140', 'BASENAME': '1993', 'INTPTLAT': '+34.0941911', 'MTFCC': 'G5020', 'COUNTY': '037', 'GEOID': '06037199300', 'CENTLAT': '+34.0926249', 'INTPTLON': '-118.2003961', 'AREALAND': 2550540, 'OBJECTID': 6991, 'TRACT': '199300', 'CENT': (-118.199214, 34.0926249), 'INTPT': (-118.2003961, 34.0941911)}], '2010 Census Blocks': [{'BLKGRP': '1', 'OID': 210404056348637, 'FUNCSTAT': 'S', 'STATE': '06', 'AREAWATER': 0, 'NAME': 'Block 1000', 'SUFFIX': '', 'LSADC': 'BK', 'CENTLON': '-118.1942484', 'LWBLKTYP': 'L', 'BASENAME': '1000', 'BLOCK': '1000', 'INTPTLAT': '+34.1001521', 'MTFCC': 'G5040', 'COUNTY': '037', 'GEOID': '060371993001000', 'CENTLAT': '+34.1001521', 'INTPTLON': '-118.1942484', 'AREALAND': 428518, 'OBJECTID': 3068287, 'TRACT': '199300', 'CENT': (-118.1942484, 34.1001521), 'INTPT': (-118.1942484, 34.1001521)}], 'States': [{'OID': 2749018475066, 'STATE': '06', 'FUNCSTAT': 'A', 'NAME': 'California', 'AREAWATER': 20484627967, 'LSADC': '00', 'CENTLON': '-119.5277460', 'STUSAB': 'CA', 'BASENAME': 'California', 'INTPTLAT': '+37.1551773', 'DIVISION': '9', 'MTFCC': 'G4000', 'STATENS': '01779778', 'GEOID': '06', 'CENTLAT': '+37.1547352', 'INTPTLON': '-119.5434183', 'REGION': '4', 'AREALAND': 403483191859, 'OBJECTID': 14, 'CENT': (-119.527746, 37.1547352), 'INTPT': (-119.5434183, 37.1551773)}]}
# 6037101110 
print(f"6037{result['2010 Census Blocks'][0]['TRACT']}")


# In[7]:


df['CensusTract'] = results
len(df['CensusTract'])


# In[5]:


df.to_csv('LA_County_Resturants_CensusTracts.csv', encoding='utf-8')


# In[6]:


len(results)


# In[11]:


df.groupby('CensusTract')['price'].value_counts()


# In[9]:


df.columns

