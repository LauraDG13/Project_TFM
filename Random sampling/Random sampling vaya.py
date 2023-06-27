import os
import random
import pandas as pd
from bs4 import BeautifulSoup as BS
import math
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from collections import Counter
import csv
import re
from operator import add
import math
import seaborn as sns



df_filtered = pd.read_json('./dataset.json', orient ='split', compression = 'infer')


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


#We use Pandas cut() function to separate the array elements (dates) into different bins (setting 25 as interval)
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




#Pandas needed two variables in the for loop. We iterate on every row of the column Texts. 
for i, row in dftxt0.iteritems():
    print(i)
    my_dictionary = {}    

    print(type(row))
    text1=row
    
    try:
        print(len(text1))
        if len(text1) > 1000000:
            #We set a seed for obtaining the same random samples based on the input we have given
            random.seed(47548)
            #We use the flat list to obtain a list of 1000000 random samples
            sample = random.sample(text1, k=1000000)
        else:
            sample = text1
        print(len(sample))
        for line in sample: 
            
        #print(text1[1:10])
        #print(text[0:200])
            try:
                splitted=line.split() #We use split to take only the first element of the list (word form) composed of three elements (word form, lemma, label).  
                lemma=splitted[0].lower()
                
                    
                #We create an empty dictionary and add in it the word forms. If the iteration encounters a new word form, it is added in the 
                #dictionary, if the word form is in the dictionary, the iteration proceeds to the next row.  
                try: my_dictionary[lemma]+=1
                except: my_dictionary[lemma]=1
            except: print('badline')#We ignore the damaged files 
         
    except: print('emptybin')
    total = sum(my_dictionary.values())
    
    subj_dic = {}
    
    
    for elem in list_sub_verbs:
        try:
            subj_dic[elem] = my_dictionary[elem]/total
            my_dic3[elem].append(subj_dic[elem])

            #my_dic3[elem].append(math.log(1+subj_dic[elem],10))
        except: 
            if len(my_dictionary) > 0:
                my_dic3[elem].append(0)
        
        
sns.set_style("whitegrid")
    
x_axis = [1100,	1200, 1250,	1300, 1350,	1400,	1450,	1500,	1550]
shift= [12,5]*len(x_axis)


x_axis=list(map(add,x_axis,shift))



for elem in list_sub_verbs:
    plt.plot (x_axis, my_dic3[elem], linewidth=20, label = elem)
    plt.rcParams["figure.figsize"] = (200,100)

 
    
    #plt.title(f"Chronological evolution of 'vaya' with sample1M", fontsize=300)


    plt.xlabel('Periods', fontsize = 250)
    plt.ylabel('Frequency per million tokens', fontsize = 250)
    plt.xticks(np.arange(1100, 1625, step=50))
    
    plt.xticks(fontsize=250, rotation=45)
    plt.yticks(fontsize=250)


    plt.rcParams["axes.edgecolor"] = "black"
    plt.rcParams["axes.linewidth"] = 10

    plt.legend(fontsize=230)
    
    plt.savefig(elem+' with sample 1M.pdf', format="pdf", bbox_inches="tight")

    plt.show()






    
