# Project_TFM

This repository contains the scripts used for developing my final thesis, "The grammaticalization path of 'vaya': a computational approach", for the Master in Theoretical and Applied Linguistics (edition 2022/2023). The motivation of the study is to contribute to the quantitative study of grammaticalization in Spanish, focusing on the verbal form "vaya" (lit. go). Currently, "vaya" is used as a form of the movement verb "it" (to go) and as a verbal discourse marker. The current uses of "vaya" are the results of a historical process. Our work wants to examine under
what conditions started the shift from lexical meaning and how vaya acquired its grammaticalized meanings across time. To reach this goal, we analyze the increase of the frequency and the spread to multiple contexts with respect to the original use. The study demonstrates that frequency increase is an essential indicator of the grammaticalization of "vaya". 

------------------------------------- File *pre-processing.py* -------------------------------------

- We obtained a dataframe in which each column contains information for every text (Title, Author, Century, Genre, ID, Translation, Collection, Number of tokens) using Beautiful Soup
- We converted it into a .csv file (metadata.xlsx)
- After extracting the metadata, we observed that some documents were duplicated. We decided to keep only the text with the highest number of tokens of the oldest edition. This procedure allowed us to preserve only the texts with the most representative corpus information
- After eliminating the duplicates, we saved the new dataframe into a .json file because it allows us to spend less computational cost in terms of time

------------------------------------- FOLDER *plot corpus* -------------------------------------

- In the script Scatter.py corpus before pre-processing, we obtained a scatter plot of the distribution of the corpus after the pre-processing. In the scatter plot, the x-axis is the centuries (from the 12th to 16th centuries), and the y-axis is the number of tokens
- In the script Scatter.py corpus after pre-processing, we obtained a scatter plot of the distribution of the corpus after the pre-processing. In the scatter plot, the x-axis is the centuries (from the 12th to 16th centuries), and the y-axis is the number of tokens
- In the script Barchart texts per genre.py, we obtained a bar chart of the distribution of the genre of the texts (prose, didactics, history, law, letters, medicine, poetry, and religion) for each century
- In the script Barchart corpus after pre-processing.py, we obtained a bar chart of the distribution of the texts per bin of 50 years. On the x-axis, there are intervals of 50 years, and on the y-axis is the number of tokens

------------------------------------- FOLDER *frequency study* -------------------------------------

- In the script Line plot chronological evolution of vaya.py, we obtained a plot of the normalized frequency of "vaya". Since the typical number of total items is of the order of the million, we express the relative frequency as the number of occurrences per million, obtained by multiplying the relative frequency by one million
- In the script Relative frequency of verbs.py, we computed the relative frequency of verbs from the 12th to 16th centuries and converted the results into a .csv file. We extracted by hand five verbs with the frequency closest to that of "vaya"
- In the script Comparison between vaya and the present subjunctive of ir.py, we plotted the comparison between the frequency of vaya to the verbal form of the present subjunctive of ir
- In the script Comparison of the relative frequency.py, we plotted the comparison between the frequency of "vaya" to five verbs with the frequency closest to that of "vaya"

------------------------------------- FOLDER *context study* -------------------------------------

  - In the script Extraction of the context.py, we obtained the contexts of each appearance of "vaya"
  - In the script Extraction of interjection and presentational construction.py, we obtained the contexts of "vaya" used as an interjection and in the presentation construction (vaya + DP/NP)
  - In the script Relative frequency of the contexts.py, we obtained the frequency of "vaya" used as an interjection and in the presentation construction (vaya + DP/NP)

------------------------------------- FOLDER *random sampling* -------------------------------------

  - To validate the frequency analysis from the plots (FOLDER *frequency study*), we repeat the analysis, randomly selecting sub-samples from the corpus. In particular, we randomly select 1000000 tokens for every bin – without replacement, meaning that each random token is taken at most once, and if there are less than 1000000 tokens, we take them all 



  




