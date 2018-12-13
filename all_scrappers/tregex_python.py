

import json
import requests
import demjson
import nltk
from nltk.tree import ParentedTree


url = "http://localhost:9000/tregex"
#request_params = {"pattern": "(NP[$VP]>S)|(NP[$VP]>S\\n)|(NP\\n[$VP]>S)|(NP\\n[$VP]>S\\n)"}
#request_params = {"pattern": "(SBAR <2 (S <1 VP))"}
#request_params = {"pattern": "SBAR <1 (S < (VP < VP))"}


#request_params = {"pattern": "(VP > (S > SBAR))"}  #==>RULE 1
#text = "Pusheen and Smitha walked along the beach." 
#text = "However, Jefferson did not believe the Embargo Act, which restricted trade with Europe, would hurt the American economy."  #==>SENT 1


#request_params = {"pattern": "(VP < (VBD $ ADVP $ PP))"}  #==>RULE 2
#text = "Prime Minister Vladimir V. Putin, the countrys paramount leader, cut short a trip to Siberia."  #==>SENT 2

request_params = {"pattern": "(SBAR < (WHNP $ (S < VP)))"}  #==>RULE 3
text = "However Monrovia was named after James Monroe, who was president of the United States in 1822."  #==>SENT 3

#request_params = {"pattern": "(VP < (VP < (PP < (NP < NP))))"}  #==>RULE 3
#request_params = {"pattern": "(NP > (NP > (PP > (VP < VP))))"}
#request_params = {"pattern": "(VP < (VP < (PP < (NP < (NP !$ SBAR)))))"}
#request_params = {"pattern": "(VP < (VP < (PP < NP)))"}
#request_params = {"pattern": "(VP < {VP})"}
#text = "However Monrovia was named after James Monroe, who was president of the United States in 1822."  #==>SENT 3

r = requests.post(url, data=text, params=request_params)

"""
#QUE - 1
#print r
#print 
info = json.dumps(r.json())
#print info
sent=demjson.decode(info)

sent1= sent['sentences'][0]
#print sent['sentences'][0]
for key,values in sent1.items():
    que=[]
    que.append('What')
    #print type(values['match'])
    sent2=ParentedTree.fromstring(values['match'])
    sent3=sent2.leaves()
    print sent2.leaves()
    for x in sent3: que.append(x)
    #print x
    print que
"""
	
"""
#QUE - 2
#print r
#print 
info = json.dumps(r.json())
#print info
sent=demjson.decode(info)

sent1= sent['sentences'][0]
#print sent['sentences'][0]
for key,values in sent1.items():
    que=[]
    que.append('Who')
    #print type(values['match'])
    sent2=ParentedTree.fromstring(values['match'])
    sent3=sent2.leaves()
    #print sent2.leaves()
    for x in sent3: que.append(x)
    #print x
    print que
"""


#QUE - 3
#print r
#print 
info = json.dumps(r.json())
#print info
sent=demjson.decode(info)

sent1= sent['sentences'][0]
#print sent['sentences'][0]
for key,values in sent1.items():
    que=[]
    #print type(values['match'])
    sent2=ParentedTree.fromstring(values['match'])
    sent3=sent2.leaves()
    #print sent2.leaves()
    for x in sent3: que.append(x)
    #print x
    print que
