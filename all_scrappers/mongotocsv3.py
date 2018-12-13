

from pymongo import MongoClient
import pprint
import time


client = MongoClient('mongodb://localhost:27017/')


db=client['imdb']


coll=db['title_basics']

coll1=db['name_basics']

all_tconst=[]


import pandas as pd

temp_data=[]

all_title_basics_data=list(coll.find({"startYear" : "2015"}, {"tconst":1, "_id":0}))

	
df=pd.DataFrame(all_title_basics_data)
df.to_csv('2015_year_data1.csv', sep=',', encoding='utf-8')

    
#{"hid":{"$regex": u"9"}
#pprint.pprint("The Count is : ",len(all_tconst))