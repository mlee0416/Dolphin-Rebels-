# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 23:27:45 2018

@author: corey
"""

## Data explanation for Census_data.csv

essentially all the columns start with either an age range, ethnic group,
or a gender. 

Following each first characteristic is either 138 or 200. These numbers relate
to Federal Poverty lines and are used for eligibility for certain forms 
of social assistance in CA. populations labeled with 138 lie at or bellow 138% of the
Federal Poverty Line. For a family household of 4 the 138% Federal Poverty line is
around 34k in combined household income. For this dataset 200 relates to populations
that are earn 200% or above the Federal Poverty line, for a family of 4 this is
$49k

census tract is the last 4 digits of the official federal Census bureau tracts,
for LA County all census tracts start with 6037:
    
While not clearly laid out in the source I'm assuming these numbers are in the 
thousands. 