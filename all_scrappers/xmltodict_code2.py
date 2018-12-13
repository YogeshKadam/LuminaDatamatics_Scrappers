import xmltodict
from collections import OrderedDict
import pandas as pd
 
# It doesn't work with Python 3! Read on for the solution!
def convert(xml_file, xml_attribs=True):
    with open(xml_file) as f:
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        return d



res=convert("LUMNLRB3.BL23898862.xml")

tile=res["AGENCYDEC-FLAT"]["lnv:CITE"]["#text"].split(';')[0]