
import os
import pandas as pd
from bs4 import BeautifulSoup as BS
import math
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from collections import Counter
import csv
from operator import add


df_filtered = pd.read_json('./dataframe.json', orient ='split', compression = 'infer')



#We save the years of the texts in a list called 'dates'
dates = df_filtered['Date']


#We used Counter for calculating the number of documents for each year and we sort the result
dic_freq_dates = sorted(Counter(dates).items())
#print(dic_freq_dates)

#We set the interval that we want for our bins
INTERVAL = 50


#We create a list of periods using our interval
'''We need to extract 1 to our starting point since the starting point of the np.arrange() is exclusive
We need to add the interval to the ending point so as to make sure it is not excluded
if the last period is not a divisor of our interval'''


periods = np.arange(1100-1, 1599 + INTERVAL, INTERVAL).tolist()


#We use Pandas cut() function to separate the array elements (dates) into different bins (setting 50 as interval)
df_filtered['bins']=pd.cut(df_filtered['Date'], periods)


#We use Pandas .groupby() to group and sum the list 'Texts' into different bins
#We use .reset_index() to avoid taken the first column as the index
df2 = df_filtered.groupby('bins', group_keys=True)['Texts'].sum().reset_index()
#print(df2[0:20])


cont=1100        
dftxt0=df2['Texts']
#print(dftxt0.head())

list_sub_verbs = ["vaya"]


my_dic3 = {}

for elem in list_sub_verbs:
    my_dic3[elem] = []


def return_context(text, word, types, window_size):
    
    occurrence = []
    
    if len(text) <= window_size:
       return text
    for i in range(len(text)- window_size + 1):
        sottolista = text[i:i+window_size]
        line = sottolista[10].split() 
    
        #line2 = sottolista[4].split() 
        try:            
            if word == line[0].lower():
                occurrence.append(sottolista)
        except: print('badline')
            
            #if word2 == line2[0].lower()
            

    print(occurrence)
    return(occurrence)        
           

#Pandas needed two variables in the for loop. We iterate on every row of the column Texts. 
for i, row in dftxt0.iteritems():
    print(i)
    my_dictionary = {}
    print(type(row))
    text1=row
    context=[]

    try:
        precontext = return_context(text1, "vaya", "label", 7)
        for example in precontext:
            contextinner=[]
            for line in example:
                splitted=line.split()
                contextinner.append(splitted[0])
            context.append(contextinner)
    except: print('badline')
    
    df_context = pd.DataFrame({'Context': context})


    df_context.to_csv("Context" + str(i) + ".csv", sep='\n', encoding='utf-8')



      
















       
    
