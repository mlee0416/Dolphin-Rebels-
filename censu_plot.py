# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 23:05:05 2018

@author: corey

Heat map and basic scatterplots of LA Census data

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('census_data.csv', index_col='Unnamed: 0')


df.columns

totals_df = df[['total_bachelors', 'africanamericantotal', 'age_0_15_total',
       'age_16_18_total', 'age_19_20_total', 'age_21_25_total',
       'age_26_59_total', 'age_60_64_total', 'age_65up_total', 'asiantotal',
       'femaletotal', 'latinototal', 'maletotal', 'multi_racetotal',
       'nativeamericantotal', 'othertotal', 'pacific_islandertotal',
       'whitetotal', 'total_pop', 'total_bachelors', 'bachelors_percap']]

plt.rcParams["figure.figsize"] = (12,10)
sns.set_context('paper')
corr_map = sns.heatmap(totals_df.corr(),cmap='autumn', annot=True)

fig = corr_map.get_figure()
fig.savefig("census_corr_heatmap.png")

plt.scatter(df['total_bachelors'], df['total_pop'])
plt.title("total population vs total number of bachelors holders")
plt.ylabel('total population')
plt.xlabel('total_bachelors')
plt.savefig('total_pop_bachelors_scatterplot.png')


g = sns.PairGrid(totals_df)
g.map_diag(sns.kdeplot)
g.map_offdiag(sns.kdeplot, cmap="Blues_d", n_levels=6)
