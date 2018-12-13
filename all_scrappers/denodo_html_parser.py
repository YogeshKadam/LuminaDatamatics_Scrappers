from bs4 import BeautifulSoup
import os
		
import pandas as pd

list1=[]

for filename in os.listdir(os.getcwd()):
    f1=open(filename,'r')
    data=f1.read()
    f1.close()
    soup = BeautifulSoup(data, 'html.parser')
    for link in soup.find_all('tr'):
        link1=link.find_all('td')
        try :
            if link1[0]['id']=="court_name":
                list2=[]
                list2.append(link1[0].string)
                list2.append(link1[1].string)
                list2.append(link1[2].string)
                list2.append(filename)
                list1.append(list2)
        except: pass


df = pd.DataFrame(list1, columns=['Court_Name','URL','Folder_Path', 'Html_File_Name'])

f2=open('sample3.csv','w')
df.to_csv(f2)
f2.close()

"""
for link in soup.find_all('tr'):
    try:
        if link.td['id']=="court_name":
            print link.td.string
            print link.td[2].string
    except:
        pass
		
for link in soup.find_all('tr'):
    try:
        link.td['id']
    except:
        pass
		
		
for link in soup.find_all('tr'):
    try:
        if link.td['id']=='URL':
            print link.td.string
    except:
        pass
		
		
for link in soup.find_all('tr'):
    link1=link.find_all('td')
    link1.td[1].string
	
for link in soup.find_all('tr'):
    link1=link.find_all('td')
    try : 
        if link1[0].td['id']=='court_name':
            print link1[0].string
    except: pass
	
for link in soup.find_all('tr'):
    link1=link.find_all('td')
    try : 
        print link1[0]['id']
    except: pass
	
for link in soup.find_all('tr'):
    link1=link.find_all('td')
    try : 
        if link1[0]['id']=="court_name":
            print link1[0].string
        if link1[1]['id']=="URL":
            print link1[1].string
            print link1[2].string
    except: pass
	
list1=[]
for link in soup.find_all('tr'):
    link1=link.find_all('td')
    try :
        if link1[0]['id']=="court_name":
            list2=[]
            list2.append(link1[0].string)
            list2.append(link1[1].string)
            list2.append(link1[2].string)
            list1.append(list2)
    except: pass
	
import os
for filename in os.listdir(os.getcwd()):
    f1=open(filename,'r')
    data=f1.read()
    f1.close()
"""