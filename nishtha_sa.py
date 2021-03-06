# -*- coding: utf-8 -*-
"""2017302_Nishtha_SA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jpYXpUj3qasYmfLw914510q_5_dXzPN0
"""

import nltk, string, random, re, pickle
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from google.colab import drive
drive.mount('/content/drive')

datafake = pd.read_csv("/content/drive/My Drive/data/politifact_fake - politifact_fake.csv")
datareal = pd.read_csv("/content/drive/My Drive/data/politifact_real - politifact_real.csv")
datafake.drop(columns=['id','news_url'],inplace=True)
datareal.drop(columns=['id','news_url'],inplace=True)

ps = PorterStemmer()
lem = WordNetLemmatizer()
stopword = set(stopwords.words( 'english' ))

def clean(data):
  return re.sub(r'[^(a-zA-Z)\s]','', data)
def remstop(data):
  global stopword
  return [w for w in data if w not in stopword]
def tagpos(data):
  return nltk.pos_tag(data)

documents=[]

def addindocs(data,flag):
  global documents
  for p in data.title:
    documents.append((p.lower(),flag))

addindocs(datareal, "true")
addindocs(datafake,"false")
random.shuffle(documents)

words=[]
allowedpos=["IN","NN" ,"NNP","PRP","PRP$" , "RP","VBP"]

def addinwords(data):
  global allowedpos, words
  for p in data.title:
    tokenized = word_tokenize(clean(p))
    stopremoved=remstop(tokenized)
    postagged = nltk.pos_tag(tokenized)
    for w in postagged:
      if w[1] in allowedpos:
        words.append(lem.lemmatize(w[0].lower()))

addinwords(data_real)
addinwords(data_fake)

words = nltk.FreqDist(words)

wordfeatures=[]
for word in words:
  if(words[word]>2):
    wordfeatures.append(word)

def docfeatures(doc):
    docwords = word_tokenize(doc)
    features = {}
    for word in wordfeatures:
        features[word] = (lem.lemmatize(word) in docwords)
    return features

featuresets = [(docfeatures(d), c) for (d,c) in documents]
trainset, testset = featuresets[:800], featuresets[800:]

classifier = nltk.NaiveBayesClassifier.train(trainset)
print(nltk.classify.accuracy(classifier, testset)*100)

classifier.show_most_informative_features(20)

currclassifier = open( "/content/drive/My Drive/data/naivebayes.pickle", "wb" )
pickle.dump (classifier, currclassifier)
currclassifier.close ()

