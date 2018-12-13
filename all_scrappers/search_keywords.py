
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("D:\\YK Python\\xmltodict\\LUMNLRB3.BL23898903.xml").read(), 'html.parser')

from nltk.corpus import gutenberg

text = ""
for file_id in gutenberg.fileids():
    text += gutenberg.raw(file_id)



print len(text)

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
				
for keywords in all_keywords_list:
    for sentence in sentence_list:
        if keywords["PresentWord"].lower() in word_tokenize(sentence.lower()):
            if sentence not in extracted_sentences : extracted_sentences.append(sentence)
        elif keywords["TenseGiven"]=="Y":
            if keywords["SimplePastWord"].lower() in word_tokenize(sentence.lower()):
                if sentence not in extracted_sentences : extracted_sentences.append(sentence)
            elif keywords["PastParticipleWord"].lower() in word_tokenize(sentence.lower()):
                if sentence not in extracted_sentences : extracted_sentences.append(sentence)
            elif keywords["PresentParticipleWord"].lower() in word_tokenize(sentence.lower()):
                if sentence not in extracted_sentences : extracted_sentences.append(sentence)
				
print "The extracted sentences : ",extracted_sentences

print len(extracted_sentences)