>>>
>>>
>>>
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(open("D:\\YK Python\\xmltodict\\LUMNLRB3.BL23898903.xml").read(), 'html.parser')
>>>
>>> from pprint import pprint
>>>
>>> from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktTrainer
>>>
>>> trainer = PunktTrainer()
>>>
>>> trainer.INCLUDE_ALL_COLLOCS = True
>>>
>>> trainer.train(text)
>>>
>>> tokenizer = PunktSentenceTokenizer(trainer.get_params())
>>>
>>>
>>> sentences = soup.get_text(' ')
>>>
>>> sentence_list= tokenizer.tokenize(sentences)
>>>
>>> import pandas as pd
>>>
>>> cols=["PresentWord","SimplePastWord","PastParticipleWord","PresentParticipleWord","TenseGiven"]
>>>
>>>
>>> df=pd.read_excel('D:\\YK Python\\xmltodict\\US labor Board.xlsx', sheetname="KeyWord_Details", usecols=cols)
>>>
>>> df1=df.fillna('')
>>>
>>>
>>> from pymongo import MongoClient
>>>
>>>
>>> client = MongoClient('mongodb://localhost:27017/')
>>>
>>>
>>> db=client['nlp']
>>>
>>> coll=db['Keywords_list']
>>>
>>>
>>> coll.insert_many(df1.to_dict('records'))
<pymongo.results.InsertManyResult object at 0x000000001ADFC240>
>>>
>>>