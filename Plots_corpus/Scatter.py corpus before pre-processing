import os
import pandas as pd
from bs4 import BeautifulSoup as BS
import math
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import seaborn as sns
sns.set()


#We read as a dataframe the .csv file obtained with the extraction of the metadata
df = pd.read_csv('/Users/lauradegrazia/01_MTAL/TFM/tfm_diachrony-main/output_tables_with_texts.csv')




plt.figure(figsize=(15,10))


# Create catter plot
sns.scatterplot(x = df["Date"], y = df["Ntokens"],
                sizes=(1000,1120),
                palette = "orange")
           
# Give title
#plt.title('Distribution of the texts in the corpus', fontsize=30)

plt.xlabel('Centuries', fontsize = 30)
# Set y-axis label
plt.ylabel('Number of tokens', fontsize = 30)


plt.xticks(fontsize=30, rotation=45)
plt.yticks(fontsize=30)

plt.savefig("corpus_plot_before_prep.pdf", format="pdf", bbox_inches="tight")


plt.show()










