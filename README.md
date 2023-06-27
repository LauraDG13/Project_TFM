# Project_TFM

------------------------------------- File *pre-processing.py* -------------------------------------

- We obtained a dataframe in which every column contains every information about the text for every text (Title, Author, Century, Genre, ID, Translation, Collection, Number of tokens) using Beatiful Soup
- We converted it into a .csv file
- After extracting the metadata, we observed that some documents were duplicated. We decided to keep only the text with the highest number of tokens of the oldest edition. This procedure, allowed us to preserve only the texts with the most representative corpus information
- After eliminating the duplicates, we save the new dataframe into a .json file because it permits us to spend less computational cost in terms of time. 

------------------------------------- FOLDER *plot corpus* -------------------------------------

- In the script Scatter.py corpus before pre-processing we obtained a scatter plot of the distribution of the corpus after the pre-processing. In the scatter plot the the x axis are the centuries (from the 12th to 16th centuries) and y axis the number of tokens
- In the script Scatter.py corpus after pre-processing we obtained a scatter plot of the distribution of the corpus after the pre-processing. In the scatter plot the the x axis are the centuries (from the 12th to 16th centuries) and y axis the number of tokens
- In the script Barchart texts per genre.py (prose, didactics, history, law, letters, medicine, poetry, and religion) 
we obtained a barchart of the distribution of the genre of the texts for each century.
- In the script Barchart corpus after pre-processing.py we we obtained a barchart of the distribution of the text per bin of 50 years. In the x axis there are the intervals of 50 years and in y axis the number of tokens

