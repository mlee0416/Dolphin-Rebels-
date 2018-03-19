# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 23:05:05 2018

@author: corey

Heat map and basic scatterplots of LA Census data

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('kaggle_census.csv', index_col='Unnamed: 0')


df.columns

totals_df = df[['total_bachelors', 'africanamericantotal', 'age_0_15_total',
       'age_16_18_total', 'age_19_20_total', 'age_21_25_total',
       'age_26_59_total', 'age_60_64_total', 'age_65up_total', 'asiantotal',
       'femaletotal', 'latinototal', 'maletotal', 'multi_racetotal',
       'nativeamericantotal', 'othertotal', 'pacific_islandertotal',
       'whitetotal', 'total_pop', 'percent_bachelors',]]

plt.rcParams["figure.figsize"] = (12,10)
sns.set_context('paper')
corr_map = sns.heatmap(totals_df.corr(),cmap='autumn', annot=True)

fig = corr_map.get_figure()
fig.savefig("census_corr_heatmap.png")

plt.style.use('fivethirtyeight')
plt.scatter(df['percent_bachelors'], df['total_pop'])
plt.title("Poverty vs Higher Education by census tract")
plt.ylabel('total population qualifying for social assistance')
plt.xlabel('percent of pop holding a bachelors degree')
plt.savefig('poverty_bachelors_scatterplot.png')

sns.regplot(y='total_pop', x='percent_bachelors', data=df, color='forestgreen',
            logx=True, x_bins=30, truncate=True, fit_reg=False)
plt.tick_params(axis='both',width=2,labelsize=12)
plt.text(15, 5400,"Poverty vs Higher Education by Census Tract",fontsize=25 )
plt.ylabel('total population qualifying for social assistance')
plt.xlabel('percent of pop holding a bachelors degree')
#plt.xlim(0,100)
#plt.ylim(0,10000)
plt.savefig('poverty_bachelors_regplot.png')


plt.scatter(df['age_0_15_total'], df['maletotal'])



for x in df[['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']]:
    sns.distplot(df[x], hist=False)
    plt.title(f"distribution of ethnicity:{x} in LA Census Tracts")
    plt.show()

for x in df[['IncomePerCap', 'ChildPoverty', 'Unemployment']]:
    sns.kdeplot(df[x], shade=True, kernel='cos')
    plt.title(f"distribution of {x} in LA Census Tracts")
    plt.show()


sns.regplot(y=df['IncomePerCap'], x=df['ChildPoverty'])

