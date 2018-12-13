"""
Preprocessing text and html (Tokenizing words and sentences, clean HTML, clean text, removing stopwords, stemming and lemmatization)
__author__ : Triskelion user@Kaggle (Thanks: Abhishek Thakur & Foxtrot user@Kaggle)
"""

# -*- coding: utf-8 -*-

from nltk import clean_html
from nltk import SnowballStemmer
from nltk import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import re

# Tokenizing (Document to list of sentences. Sentence to list of words.)
def tokenize(str):
    '''Tokenizes into sentences, then strips punctuation/abbr, converts to lowercase and tokenizes words'''
    return     [word_tokenize(" ".join(re.findall(r'\w+', t,flags = re.UNICODE | re.LOCALE)).lower()) 
            for t in sent_tokenize(str.replace("'", ""))]

#Removing stopwords. Takes list of words, outputs list of words.
def remove_stopwords(l_words, lang='english'):
    l_stopwords = stopwords.words(lang)
    content = [w for w in l_words if w.lower() not in l_stopwords]
    return content
        
#Clean HTML / strip tags TODO: remove page boilerplate (find main content), support email, pdf(?)
def html2text(str):
    soup = BeautifulSoup(str, 'html.parser')
    sentences = soup.get_text(' ')
    return sentences
        
#Stem all words with stemmer of type, return encoded as "encoding"
def stemming(words_l, type="PorterStemmer", lang="english", encoding="utf8"):
    supported_stemmers = ["PorterStemmer","SnowballStemmer","LancasterStemmer","WordNetLemmatizer"]
    if type is False or type not in supported_stemmers:
        return words_l
    else:
        l = []
        if type == "PorterStemmer":
            stemmer = PorterStemmer()
            for word in words_l:
                l.append(stemmer.stem(word).encode(encoding))
        if type == "SnowballStemmer":
            stemmer = SnowballStemmer(lang)
            for word in words_l:
                l.append(stemmer.stem(word).encode(encoding))
        if type == "LancasterStemmer":
            stemmer = LancasterStemmer()
            for word in words_l:
                l.append(stemmer.stem(word).encode(encoding))
        if type == "WordNetLemmatizer": #TODO: context
            wnl = WordNetLemmatizer()
            for word in words_l:
                l.append(wnl.lemmatize(word).encode(encoding))
        return l

#The preprocess pipeline. Returns as lists of tokens or as string. If stemmer_type = False or not supported then no stemming.        
#def preprocess_pipeline(str, lang="english", stemmer_type="PorterStemmer", return_as_str=False, do_remove_stopwords=False, do_clean_html=False):
def preprocess_pipeline(str, lang, stemmer_type, return_as_str, do_remove_stopwords, do_clean_html):
    l = []
    words = []
    if do_clean_html:
        sentences = tokenize(html2text(str))
    else:
        sentences = tokenize(str)
    for sentence in sentences:
        if do_remove_stopwords:
            words = remove_stopwords(sentence, lang)
        else:
            words = sentence
        words = stemming(words, stemmer_type)
        if return_as_str:
            l.append(" ".join(words))
        else:
            l.append(words)
    if return_as_str:
        return " ".join(l)
    else:
        return l

test_sentence = "User-Testing Tester Tests! She had me at 'hello'?!? But then <abbr>ESPN</abbr> fainted... and Eighty cars drove past."
# print "\nOriginal:\n", test_sentence
# print "\nPorter:\n", preprocess_pipeline(test_sentence, "english", "PorterStemmer", True, False, True)
print "\nLancaster:\n", preprocess_pipeline(test_sentence, "english", "LancasterStemmer", True, True, True)
# print "\nWordNet:\n", preprocess_pipeline(test_sentence, "english", "WordNetLemmatizer", True, False, True)
# print "\nStopword Tokenized Lancaster:\n", preprocess_pipeline(test_sentence, "english", "LancasterStemmer", False, True, True)
print "\nOnly cleaning (HTML+Text):\n", preprocess_pipeline(test_sentence, "english", False, True, False, True)


from bs4 import BeautifulSoup

soup = BeautifulSoup(open("D:\\YK Python\\YK Nltk\\LexisNexis\\Sample input files\\LUMNLRB3.BL23898903.xml").read(), 'html.parser')

from nltk.corpus import gutenberg

text = ""
#for file_id in gutenberg.fileids():
#    text += gutenberg.raw(file_id)



#print len(text)

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

#print all_keywords_list
"""for keywords in all_keywords_list:
    for sentence in sentence_list:
        if keywords["PresentWord"].lower() in sentence.lower():
            if sentence not in extracted_sentences : extracted_sentences.append(sentence)
        elif keywords["TenseGiven"]=="Y":
            if keywords["SimplePastWord"].lower() in sentence.lower():
                if sentence not in extracted_sentences : extracted_sentences.append(sentence)
            elif keywords["PastParticipleWord"].lower() in sentence.lower():
                if sentence not in extracted_sentences : extracted_sentences.append(sentence)
            elif keywords["PresentParticipleWord"].lower() in sentence.lower():
                if sentence not in extracted_sentences : extracted_sentences.append(sentence)"""
				
"""for keywords in all_keywords_list:
    for sentence in sentence_list:
        if keywords["PresentWord"] in word_tokenize(sentence):
            if sentence not in extracted_sentences : extracted_sentences.append(sentence)
        elif keywords["TenseGiven"]=="Y":
            if keywords["SimplePastWord"] in word_tokenize(sentence):
                if sentence not in extracted_sentences : extracted_sentences.append(sentence)
            elif keywords["PastParticipleWord"] in word_tokenize(sentence):
                if sentence not in extracted_sentences : extracted_sentences.append(sentence)
            elif keywords["PresentParticipleWord"] in word_tokenize(sentence):
                if sentence not in extracted_sentences : extracted_sentences.append(sentence)  ==> 84"""
				
"""for keywords in all_keywords_list:
    for sentence in sentence_list:
        if keywords["PresentWord"].lower() in word_tokenize(sentence.lower()):
            if sentence not in extracted_sentences : extracted_sentences.append(sentence)
        elif keywords["TenseGiven"]=="Y":
            if keywords["SimplePastWord"].lower() in word_tokenize(sentence.lower()):
                if sentence not in extracted_sentences : extracted_sentences.append(sentence)
            elif keywords["PastParticipleWord"].lower() in word_tokenize(sentence.lower()):
                if sentence not in extracted_sentences : extracted_sentences.append(sentence)
            elif keywords["PresentParticipleWord"].lower() in word_tokenize(sentence.lower()):
                if sentence not in extracted_sentences : extracted_sentences.append(sentence)"""
	

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
#print "The extracted sentences : ",extracted_sentences

print len(extracted_sentences)

stemmed_sentences=[]

for lines in extracted_sentences:
    print "Original text : ",lines
    #print "Lancaster: ", preprocess_pipeline(lines, "english", "LancasterStemmer", True, True, False)
    print "Porter:", preprocess_pipeline(lines, "english", "PorterStemmer", True, True, False)
    #stemmed_sentences.append(preprocess_pipeline(lines, "english", "LancasterStemmer", True, True, False))
    stemmed_sentences.append(preprocess_pipeline(lines, "english", "PorterStemmer", True, True, False))
	
print "STEMMED SENTENCES : ",stemmed_sentences