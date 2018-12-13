


import urllib
import json

data=raw_input("Enter any string : ")
#print data
data = urllib.urlencode({"text": data})
u = urllib.urlopen("http://text-processing.com/api/sentiment/", data)
the_page = u.read()
out=json.loads(the_page)
#print out
if out['label']=="neg":
    print "Polarity == NEGATIVE"
elif out['label']=="pos":
    print "Polarity == POSITIVE"
elif out['label']=="neutral":
    print "Polarity == NEUTRAL"