import os
import pandas as pd
from bs4 import BeautifulSoup as BS
import math
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from collections import Counter
import csv
import re



df = pd.read_json('./dataframe.json', orient ='split', compression = 'infer')


#We save the years of the texts in a list called 'dates'
dates = df['Date']


#We used Counter for calculating the number of documents for each year and we sort the result
dic_freq_dates = sorted(Counter(dates).items())
#print(dic_freq_dates)

#We set the interval that we want for our bins
INTERVAL = 50


#We create a list of periods using our interval
'''We need to extract 1 to our starting point since the starting point of the np.arrange() is exclusive
We need to add the interval to the ending point so as to make sure it is not excluded
if the last period is not a divisor of our interval'''


periods = np.arange(1200-1, 1349 + INTERVAL, INTERVAL).tolist()
print(periods)

#We use Pandas cut() function to separate the array elements (dates) into different bins (setting 25 as interval)
df['bins']=pd.cut(df['Date'], periods)

#We use Pandas .groupby() to group and sum the list 'Texts' into different bins
#We use .reset_index() to avoid taken the first column as the index
df2 = df.groupby('bins', group_keys=True)['Texts'].sum().reset_index()
#print(df2[0:20])

print(df2.head(5))

cont=1200        
dftxt0=df2['Texts']
#print(dftxt0.head())

my_dictionary = {}    


#Pandas needed two variables in the for loop. We iterate on every row of the column Texts. 
for i, row in dftxt0.iteritems():
    print(i)
    
    print(type(row))
    text1=row
    try:
        for line in text1: 
            
        #print(text1[1:10])
        #print(text[0:200])
            try:
                splitted=line.split() #We use split to take only the first element of the list (word form) composed of three elements (word form, lemma, label).  
                wordform=splitted[0].lower()
                if re.match("(VMSP1S0|VMSP3S0)", splitted[2]):
          
                    
                #We create an empty dictionary and add in it the word forms. If the iteration encounters a new word form, it is added in the 
                #dictionary, if the word form is in the dictionary, the iteration proceeds to the next row.  
                    try: my_dictionary[wordform]+=1
                    except: my_dictionary[wordform]=1
            except: print('badline')#We ignore the damaged files 
         
    except: print('emptybin')
    
    
(pd.DataFrame.from_dict(data=my_dictionary, orient='index').to_csv('verbs_subj_1_3_sing_filtered.csv', header=False))
    
   

    



