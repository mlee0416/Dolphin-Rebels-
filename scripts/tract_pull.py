import pandas as pd
from pprint import pprint
import numpy as np
import json
import censusgeocode as cg

df = pd.read_csv('LA_County_restaurants.csv', sep='\t', encoding='utf-8', index_col='Unnamed: 0')
df = df[df['city'] == "Los Angeles"]


results = []
for index,row in df.iterrows():
    print(row['Latitude'])
    print(row['Longitude'])
    response = cg.coordinates(x=row['Latitude'], y=row['Longitude'])
