
import os
import pandas as pd
from bs4 import BeautifulSoup as BS
import math
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import seaborn as sns

df = pd.read_csv("/Users/lauradegrazia/01_MTAL/TFM/tfm_diachrony-main/histogram/data_filtered.csv")


#We set the value of the variable bin_width as 50

lowest_year = 1100

highest_year = 1599

bin_width=50

dates=df['Date']



#We convert dates from strings to integer
for i in range(0,len(dates)):
    dates[i] = int(dates[i])
print(dates)


#We access to the column Number of tokens
Ntokens=df['Ntokens']


#We have to do this to check if the number of tokens is integer because before we divided the number of tokens by 3
for i in range(0,len(Ntokens)):
    Ntokens[i] = int(Ntokens[i])
    

#Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object. 
#The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never 
#raises a KeyError. It provides a default value for the key that does not exists.


#We create a dictionary for counting the number of tokens for every interval
count_number_of_tokens = defaultdict(int)


#The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed 
#iterator is paired together, and then the second item in each passed iterator are paired together 

for year, num_token in zip(dates, Ntokens):
    # We calculate the intervals of the bins. //Floor division
    interval = (year // bin_width) * bin_width
    
    # We add the number of tokens for interval
    count_number_of_tokens[interval] += num_token/1000000


plt.rcParams["figure.figsize"] = (70,50)


df = pd.DataFrame({ #'File': all_files,
                    'Periods': count_number_of_tokens.keys(),
                    'Millions of tokens': count_number_of_tokens.values()})


print(df)


ax = sns.barplot(x=df["Periods"], y=df["Millions of tokens"], color='orange', ci=None)
ax.set(xlabel='Periods', ylabel='Millions of tokens')

plt.xticks(rotation=45)


sns.set()
sns.set(font_scale=20)  


plt.yticks(np.arange(0, max(count_number_of_tokens.values(), 1000000)/1000000), fontsize=100)


#We save the plot into a PNG file
plt.savefig('plot_corpus_after_pre_processing.png', bbox_inches='tight')



#We configure the numbers showed in the Y-Axis
plt.yticks(np.arange(0, max('Ntokens'), 2))


plt.show()

