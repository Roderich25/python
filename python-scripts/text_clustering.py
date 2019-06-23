import pandas as pd
import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
import re
import string

#Step 1
con  = sqlite3.connect('site.db')
df = pd.read_sql_query("SELECT id, title||' '||content as content from post", con)
con.close()
posts = np.asarray(df.content)

#Step 2
def preprocessing(line):
    line = line.lower()
    line = re.sub(r"[{}]".format(string.punctuation), " ", line)
    return line


#Step 3
tfidf_vectorizer = TfidfVectorizer(preprocessor=preprocessing)
tfidf = tfidf_vectorizer.fit_transform(posts)

kmeans = KMeans(n_clusters=2, random_state=1987).fit(tfidf)

print(kmeans.labels_+1)