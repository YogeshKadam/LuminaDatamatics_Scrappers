import xmltodict
from collections import OrderedDict
import pandas as pd
 
# It doesn't work with Python 3! Read on for the solution!
def convert(xml_file, xml_attribs=True):
    with open(xml_file) as f:
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        return d



res=convert("D:\\YK Python\\xmltodict\\M_HJR=S_HBJ=V_2017-10-01=Datenbank_Gerichte=C_HJR-XML.xml")
temp_data=[]
for dicts in res['redtext']['redtext-teil']['datenbank']['datenbank-text']['datensatz']:
    finaldict={}
    finaldict['UniqueNo']=dicts['@satzschluessel']
    for lists in dicts['datenfeld']:
        try:
            if type(lists['absatz'])==OrderedDict:
                finaldict[lists['@feldname']]=lists['absatz']['#text']
            else:
                finaldict[lists['@feldname']]=lists['absatz']
        except:
            finaldict[lists['@feldname']]="None"
    temp_data.append(finaldict)



final=pd.DataFrame(temp_data)


final.to_csv("D:\\YK Python\\xmltodict\\Datenbank_Gerichte.csv")