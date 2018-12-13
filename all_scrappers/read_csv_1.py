

#!/usr/local/bin/python

#^[ \t\v]*#.*?coding[:=][ \t]*([-_.a-zA-Z0-9]+)
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import xmltodict
from collections import OrderedDict
import pandas as pd
 

df1=pd.read_csv("C:\\Users\\yogesh.k\\Downloads\\20171110_import-data\\Datenbank_Abteilungen.csv", encoding="utf-8")
import pdb;pdb.set_trace()
print df1['Name'][24]