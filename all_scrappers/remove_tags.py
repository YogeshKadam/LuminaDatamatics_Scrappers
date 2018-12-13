import re


text = re.sub('<[^<]+>', " ", open("D:\\YK Python\\xmltodict\\LUMNLRB3.BL23898903.xml").read())

with open("D:\\YK Python\\xmltodict\\BL23898903.xml", "w") as f:
    f.write(text)

