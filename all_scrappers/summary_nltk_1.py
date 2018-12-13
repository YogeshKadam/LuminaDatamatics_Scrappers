from bs4 import BeautifulSoup
text = ""
from nltk.corpus import gutenberg

for file_id in gutenberg.fileids():
    text += gutenberg.raw(file_id)
print len(text)
soup = BeautifulSoup(open("D:\\YK Python\\xmltodict\\LUMNLRB3.BL23899175.xml").read(), 'html.parser')
from pprint import pprint

from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktTrainer

trainer = PunktTrainer()

trainer.INCLUDE_ALL_COLLOCS = True

trainer.train(text)

tokenizer = PunktSentenceTokenizer(trainer.get_params())

sentences = soup.get_text(' ')

sentence_list= tokenizer.tokenize(sentences)

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db=client['nlp']

coll=db['Keywords_list']

extracted_sentences=[]

all_keywords_list=list(coll.find({},{"_id":0}))

from nltk.tokenize import sent_tokenize, word_tokenize

for keywords in all_keywords_list:
    for sentence in sentence_list:
        if keywords["PresentWord"] in word_tokenize(sentence):
            if sentence not in extracted_sentences : extracted_sentences.append(sentence)
        elif keywords["TenseGiven"]=="Y":
            if keywords["SimplePastWord"] in word_tokenize(sentence):
                if sentence not in extracted_sentences : extracted_sentences.append(sentence)
            elif keywords["PastParticipleWord"] in word_tokenize(sentence):
                if sentence not in extracted_sentences : extracted_sentences.append(sentence)
            elif keywords["PresentParticipleWord"] in word_tokenize(sentence):
                if sentence not in extracted_sentences : extracted_sentences.append(sentence)

len(extracted_sentences)

from sklearn.feature_extraction.text import TfidfVectorizer

import datetime, re, sys

def tokenize_and_stem(text):
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

tfidf = TfidfVectorizer(tokenizer=tokenize_and_stem, stop_words='english', decode_error='ignore')

import nltk

from nltk.stem.porter import *

stemmer = PorterStemmer()

tdm = tfidf.fit_transform(open("D:\\YK Python\\YK Nltk\\LexisNexis\\Sample input files\\learning_vectorizer_file_1.txt","r").read().split('.'))

feature_names = tfidf.get_feature_names()

len(feature_names)

def n_sum(article_text):
    #import pdb; pdb.set_trace()
    article_id = randint(0, tdm.shape[0] - 1)
    sent_scores = []
    for sentence in nltk.sent_tokenize(article_text):
        score = 0
        sent_tokens = tokenize_and_stem(sentence)
        for token in (t for t in sent_tokens if t in feature_names):
            score += tdm[article_id, feature_names.index(token)]
        sent_scores.append((score / len(sent_tokens), sentence))
    summary_length = int(math.ceil(len(sent_scores) / 5))
    #sent_scores.sort(key=lambda sent: sent[0], reverse=True)
    #sorted(zip(score, name), reverse=True)[:3]
    first_three=sorted(sent_scores , reverse=True)[:3]
    #print('*** SUMMARY ***')
    summary=[]
    for summary_sentence in sent_scores[:summary_length]:
        tmp = summary_sentence[1]
        summary.append(tmp)
    return first_three

from random import randint

import math

print(n_sum(" ".join(extracted_sentences)))
[(0.0077996385493916253, u'The single allegation that the Respondent violated  Section 8(a)(3)  and  (1)  by issuing Stauffer a warning letter in reprisal for engagin
g in protected union activity does not, by itself, establish that there is a claim of employer animosity to employees&apos; exercise of protected statutory rights.'),
 (0.0, u'n4 n4 The Board also observed that "arbitrators frequently find that customs and past practices may become part of the &apos;law of the shop&apos; and thus e
nforceable through arbitration, even if they are not a part of the written contract, and the Supreme Court has recognized arbitrators&apos; authority to do so," citin
g  Steelworkers v. On March 12, 2015, the Board issued an order transferring the proceeding to the Board and Notice to Show Cause why the motion should not be granted
.'), (0.0, u'n4  Similarly here, the fact that the Respondent and the Union have previously used the grievance-arbitration procedure to process claims of unjust disci
pline less than discharge indicates that they both consider such disputes to be subject to the grievance-arbitration process.')]