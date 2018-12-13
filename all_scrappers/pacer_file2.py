

import pandas as pd

excel_file1=pd.ExcelFile('url_maaping.xlsx')
excel_file2=pd.ExcelFile('WK_Content_Acquisition_App-Tracker.xlsx')


#df1 = pd.read_excel(excel_file, 'MICs List by CC', skiprows=1, skip_footer= 1721)
#df2 = pd.read_excel(excel_file, 'MICs List by CC', nrows=1)

data_df1 = pd.read_excel(excel_file1,'Sheet6')
data_df2 = pd.read_excel(excel_file2,'Sites')
#data_df=pd.read_csv("Book3.xlsx")
#print data_df

data_df1=data_df1.fillna('')
data_df2=data_df2.fillna('')

for ind1,val1 in data_df1.iterrows():
    for ind2,val2 in data_df2.iterrows():
        if val1['url']==val2['Website']:
            #print "found", val2['ID']
            data_df1['denodo_id'][ind1]=val2['ID']

print data_df1
data_df1.to_excel('url_mapping_output.xlsx','w')