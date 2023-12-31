# To use this program, it is required to have Python and Pip installed
# To install BS, the following line will be executed in terminal: pip install beautifulsoup4

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


#Creation of a list of objects with the key 'letter' (the first letter of each file to split),
#the key 'counter' (a counter dedicated for each objet) and the key 'path' (the path of the file to split)
corpuslist = [{'letter': 'A',
               'path': '/.oldes_tagged/AA/'},
              {'letter': 'B',
               'path': '/./oldes_tagged/BB/'},
              {'letter': 'C',
               'path': '/oldes_tagged/CC/'},
              {'letter': 'D',
               'path': '/oldes_tagged/DD/'},
              {'letter': 'E',
               'path': '/oldes_tagged/EE/'}]


#We create empty lists with each attribute of the metadata
titles = []
authors = []
dates = []
centuries = []
collections = []
genres = []
ids = []
translations = []
texts = []
ntokens =[]

all_files = []

for i in corpuslist:
    letter = i['letter']
    path = i['path']

    subfolder = [f for f in os.listdir(path) if not f.startswith('.')] #We list the name of all files in each subfolder
    subfolder.sort(key=lambda x: '{0:0>8}'.format(x).lower()) #We sort the list
    
    for file in subfolder:
        all_files.append(file)
        
        corpus = open(path + file)
        
        soup = BS(corpus)  #BeautifulSoup is used for web scrapping, with BS() we apply the BS model to our file
        
        elem = soup.findAll('text') #It returns the content of every label that coincides with a given string
        '''The purpose of the soup.findAll() step is to separate each text
        and save them as separate elements in a list, since every text is
        inserted between <text></text> and the metadata is included by giving attributes
        to that label (for example, 'author=' or 'date=''are both attributes of <text>)'''
        #print(elem[:5])               
          
        
        #The purpose of the "if" is to ignore the texts that do not have all the metadata. We have to do this because 
        #the array must be of the same lenght for every column
        
        for j in elem:
            if len([j['title'],j['author'], j['date'],j['century'],j['collection'],j['genre'],j['id'],j['translation']])==8:
                titles.append(j['title']) #It will save the value of every attribute called, in this case, 'title'
                authors.append(j['author'])
                dates.append(int(j['date']))
                centuries.append(j['century'])
                collections.append(j['collection'])
                genres.append(j['genre'])
                ids.append(j['id'])
                translations.append(j['translation'])
                texts.append(j.text.splitlines()) #We use splitlines to split the text into a list where each line is a list item
                ntokens.append(len(j.text.splitlines())) #We use len to find the number of tokens for every text (find the lenght 
                #of the list text)
               

#We create a dataframe and assign every list to a new column
df = pd.DataFrame({ #'File': all_files,
                    'Title': titles,
                    'Author': authors,
                    'Date': dates,
                    'Century': centuries,
                    'Genre': genres,
                    'ID': ids,
                    'Translation': translations,
                    'Collection': collections,
                    'Texts': texts,
                    'Ntokens':ntokens})

#We eliminate the duplicates of the texts selecting the ID of the documents that we want to delete
df_filtered = df[~df.ID.isin(["PN9", "PN2", "ENC", "CGS", "FN2", "FNA", "FNP", "FNL", 
                              "FNR", "FNG", "FNE", "FNK", "FNC", "FNF", "FNN", "FNM", "FNJ", 
                              "FNI", "FNQ", "FND", "FNS", "FNO", "FNH", "FN1", "G5R", "ULT", "SLI", 
                              "C01", "C08", "C17", "C02", "C21", "C03", "C10", "C04", "C09", "C05", 
                              "C11", "C13", "C12", "C06", "C14", "C15", "C16", "C18", "C19", "C20", "LZ3", "LZ2", "BC4"
                              "AC3", "BC1", "AC2", "APL", "TFL", "TFH", "TFE", "TFC", "TFM", "TFB", "TFQ", "TFD", "TFJ", "TFF", "TFK", 
                              "TFN", "TFI", "TFG", "TFP", "TFA", "M19", "LC2", "OA1", "TA1", "TR2"])] 
                                


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


#We convert the dataframe into different .csv for each bin composed of 50 years. 
(pd.DataFrame(data=df_filtered).to_csv(str(cont)+'.csv', header=False))
    
cont=cont+50

    
      



