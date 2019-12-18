import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
from nltk import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import re        
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import csv

stemmer = PorterStemmer()
stops = set(stopwords.words("indonesian"))
with open('output.csv', 'r') as f:
    spamreader = csv.reader(f) 
    for row in spamreader:
        print(row)  
# with open('output.csv', 'rb') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',')

    for row in spamreader:
        if len(row) >= 2:
            word_tokens1 = nltk.tokenize.word_tokenize(row[0])
            word_tokens2 = nltk.tokenize.word_tokenize(row[1])
            remo1 = [w for w in word_tokens1 if w in re.sub("[^a-zA-Z]", " ", w)]
            remo2 = [w for w in word_tokens2 if w in re.sub("[^a-zA-Z]", " ", w)]
            list1 = [w for w in remo1 if not w in stops]
            list2 = [w for w in remo2 if not w in stops]

            stemmed_first = ""
            c = 0

            for w in list1:
                if c < len(list1)-1:
                    stemmed_first += stemmer.stem(w) + " "
                else:
                    stemmed_first += stemmer.stem(w)
                c += 1

            stemmed_second = ""
            c = 0

            for w in list2:
                if c < len(list2)-1:
                    stemmed_second += stemmer.stem(w) + " "
                else:
                    stemmed_second += stemmer.stem(w)
                c += 1

            print (stemmed_first)
            print (stemmed_second)
