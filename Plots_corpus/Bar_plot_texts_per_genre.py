

import os
import pandas as pd
from bs4 import BeautifulSoup as BS
import math
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
from collections import defaultdict
from collections import Counter
import csv
from operator import add
import seaborn as sns


df_filtered = pd.read_json('./dataframe.json', orient ='split', compression = 'infer')


#We save the years of the texts in a list called 'dates'
dates = df_filtered['Date']


#We used Counter for calculating the number of documents for each year and we sort the result
dic_freq_dates = sorted(Counter(dates).items())
#print(dic_freq_dates)

#We set the interval that we want for our bins
INTERVAL = 100


#We create a list of periods using our interval
'''We need to extract 1 to our starting point since the starting point of the np.arrange() is exclusive
We need to add the interval to the ending point so as to make sure it is not excluded
if the last period is not a divisor of our interval'''


periods = np.arange(1100-1, 1599 + INTERVAL, INTERVAL).tolist()


#We use Pandas cut() function to separate the array elements (dates) into different bins (setting 25 as interval)
df_filtered['bins']=pd.cut(df_filtered['Date'], periods)

dfsmall=df_filtered[['bins','Genre','Title']]
#for every bin and genre, we do a unique text. In this way, we can obtain the relative frequency for all the texts in that bin and genre
df2 = dfsmall.groupby(['bins', 'Genre'], group_keys=True).count().reset_index()

pivot = pd.pivot_table(data=df2, index=['bins'], columns=['Genre'], values='Title')
#dftot = df.groupby(['bins'], group_keys=True)['Ntokens'].sum().reset_index()

ax = pivot.plot.bar(stacked=True, figsize=(40,30))


ax.set_xlabel("Centuries")
ax.set_ylim(0,500)
ax.set_xticklabels(['1100','1200','1300','1400','1500'], rotation=45)

plt.legend(fontsize=80)
plt.xlabel('Centuries', fontsize=100)
plt.ylabel('Number of documents', fontsize=100)

plt.xticks(fontsize=100)
plt.yticks(fontsize=100)
