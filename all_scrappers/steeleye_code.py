

import pandas as pd
import json

excel_file=pd.ExcelFile('steeleye.xls')


#df1 = pd.read_excel(excel_file, 'MICs List by CC', skiprows=1, skip_footer= 1721)
#df2 = pd.read_excel(excel_file, 'MICs List by CC', nrows=1)

data_df = pd.read_excel(excel_file, 'MICs List by CC')

data_df=data_df.fillna('')

#list_of_dict=[]
#for cols in data_df.columns:
#    dict1={}
#    dict1[cols]=data_df[cols]
#    list_of_dict.append(dict1)

list_of_dict=[]
for cols in data_df.columns:
    dict1={}
    dict1[cols]=[str(dt.encode('utf-8')) for dt in data_df[cols]]
    list_of_dict.append(dict1)

#json_data=json.dumps(list_of_dict)
with open('final_output3.json','w') as outfile:
    json.dump(json.dumps(list_of_dict), outfile)
	
print "DONE"