# import Sastrawi package

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
import pandas as pd
import nltk

import csv
import string
import re
from nltk.tokenize import word_tokenize 
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

#create stopword remover
factory2 = StopWordRemoverFactory()
stopword = factory2.create_stop_word_remover()
# stem

namaFilee = "#KadoNatalUntukPapua.csv"
userid = []
tweet = []
csvfile = [i.split() for i in namaFilee]

with open(namaFilee, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader) #skip header
    for row in reader:
        userid.append(row[0])
        tweet.append(row[1])

# Using for loop 
for i in tweet: 
    print(i)

sentence = i
# string = sentence[~sentence.applymap(lambda x: str.startswith(str(x), '--')).any(1)]
# case folding bertujuan untuk mengubah semua huruf dalam sebuah dokumen teks menjadi huruf kecil (lowercase).

tandabaca = sentence.translate(str.maketrans("","",string.punctuation))

angka = re.sub(r"\d+", "", tandabaca)
# case_folding = [[sentence.lower() for sentence in line.split()] for line in sentence]
#stop word merupakan kata yang diabaikan dalam pemrosesan,
#kata-kata ini biasanya disimpan ke dalam stop lists.
#Karakteristik utama dalam pemilihan stop word biasanya adalah kata yang mempunyai frekuensi kemunculan yang tinggi

stop = stopword.remove(angka)

#Regular expression (regex) digunakan untuk menghapus karakter angka


case_folding = stop.lower()


#Untuk menghapus spasi di awal dan akhir, anda dapat menggunakan fungsi strip()
whitepace = case_folding.strip()


#stemmer merupakan proses untuk mengubah kata berimbuhan bahasa Indonesia menjadi bentuk dasarnya.
steming   = stemmer.stem(whitepace)

#Tokenizing adalah proses pemisahan teks menjadi potongan-potongan yang disebut sebagai token untuk kemudian di analisa. Kata, angka, simbol, tanda baca dan entitas penting lainnya dapat dianggap sebagai token.
#Fungsi split()pada pyhton dapat digunakan untuk memisahkan teks.
# pisah = steming .split()

tokens = nltk.tokenize.word_tokenize(steming)

kemunculan = nltk.FreqDist(tokens)
kemunculan.plot(30,cumulative=False)
plt.show()
# output = sentence[~sentence.applymap(lambda x: str.startswith(str(x), '--')).any(1)]
# print(case_folding)
#print(kemunculan.most_common())
# token = pd.to_excel('output_modified.csv')

# ekonomi indonesia sedang dalam tumbuh yang bangga



# print(stemmer.stem('Mereka meniru-nirukannya'))
# mereka tiru


#read csv and get the content column
