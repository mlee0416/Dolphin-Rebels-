# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 22:56:53 2018

@author: corey

Script for pulling data from government APIs, merging them into a 
pandas dataframe and saving the results in a csv sheet

"""
import requests
import json
import pandas as pd

# pull pop, ethnicity, gender, and age groups by censu tract
url = "https://data.lacounty.gov/resource/qc6w-c878.json"

response = requests.get(url)