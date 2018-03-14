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

demo_df = pd.DataFrame.from_records(demographics_results)




