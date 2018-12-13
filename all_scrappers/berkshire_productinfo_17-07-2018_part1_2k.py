# -*- coding: utf-8 -*-
import scrapy
import urllib

import os
import time
import re
import json


class BerkshireItems(scrapy.Item):
    list_price= scrapy.Field()
    your_price= scrapy.Field()
    model_number= scrapy.Field()
    number_of_items= scrapy.Field()
    bullet_point_description= scrapy.Field()
    hazardous= scrapy.Field()
    brand1= scrapy.Field()
    image_url= scrapy.Field()
    title= scrapy.Field()
    category= scrapy.Field()
    description= scrapy.Field()
    bullet_point_1= scrapy.Field()
    bullet_point_2= scrapy.Field()
    bullet_point_3= scrapy.Field()
    bullet_point_4= scrapy.Field()
    bullet_point_5= scrapy.Field()
    bullet_point_6= scrapy.Field()
    bullet_point_7= scrapy.Field()
    bullet_point_8= scrapy.Field()
    bullet_point_9= scrapy.Field()
    bullet_point_10= scrapy.Field()
    hazard_code = scrapy.Field()
    product_url = scrapy.Field()
    #timestamp = scrapy.Field()
    brand2 = scrapy.Field()
    shipping_info = scrapy.Field()
    product_id = scrapy.Field()
    item_no = scrapy.Field()
    features_dict = scrapy.Field()
    item_no = scrapy.Field()
    mfg_no = scrapy.Field()



class BerkshireSpider(scrapy.Spider):
    imgcount = 1
    name = "berkshire_productinfo_17-07-2018_part1_2k"
    allowed_domains = []

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]  

    def parse(self,response):
        urls_done = [
]
        urls=[
["1","Workholding-Tooling-Acc-End-Shell-Mill-Holders-Shell-End-Mill-Holders","http://www.berkshireesupply.com/cgi/CGP2SRIM?PMITEM=GM2966651446M&PARTPG=CGP2LMXE&PAMENU=&PAHDID=000000191911576&PARDID=649597376887499"],
["2","Workholding-Tooling-Acc-End-Shell-Mill-Holders-Shell-End-Mill-Holders","http://www.berkshireesupply.com/cgi/CGP2SRIM?PMITEM=TG604511585&PARTPG=CGP2LMXE&PAMENU=&PAHDID=000000191911576&PARDID=649597376887499"],
["3","Workholding-Tooling-Acc-End-Shell-Mill-Holders-Shell-End-Mill-Holders","http://www.berkshireesupply.com/cgi/CGP2SRIM?PMITEM=HA70A6304132&PARTPG=CGP2LMXE&PAMENU=&PAHDID=000000191911576&PARDID=649597376887499"],
["4","Workholding-Tooling-Acc-End-Shell-Mill-Holders-Shell-End-Mill-Holders","http://www.berkshireesupply.com/cgi/CGP2SRIM?PMITEM=IC104510821&PARTPG=CGP2LMXE&PAMENU=&PAHDID=000000191911576&PARDID=649597376887499"],
["5","Workholding-Tooling-Acc-End-Shell-Mill-Holders-Shell-End-Mill-Holders","http://www.berkshireesupply.com/cgi/CGP2SRIM?PMITEM=HA7012505234Z3I&PARTPG=CGP2LMXE&PAMENU=&PAHDID=000000191911576&PARDID=649597376887499"],
["6","Workholding-Tooling-Acc-End-Shell-Mill-Holders-Shell-End-Mill-Holders","http://www.berkshireesupply.com/cgi/CGP2SRIM?PMITEM=GM62325040&PARTPG=CGP2LMXE&PAMENU=&PAHDID=000000191911576&PARDID=649597376887499"],
["7","Workholding-Tooling-Acc-End-Shell-Mill-Holders-Shell-End-Mill-Holders","http://www.berkshireesupply.com/cgi/CGP2SRIM?PMITEM=HA70A5004016&PARTPG=CGP2LMXE&PAMENU=&PAHDID=000000191911576&PARDID=649597376887499"],
["8","Workholding-Tooling-Acc-End-Shell-Mill-Holders-Shell-End-Mill-Holders","http://www.berkshireesupply.com/cgi/CGP2SRIM?PMITEM=GM96C50BC15SM4&PARTPG=CGP2LMXE&PAMENU=&PAHDID=000000191911576&PARDID=649597376887499"],
["9","Workholding-Tooling-Acc-End-Shell-Mill-Holders-Shell-End-Mill-Holders","http://www.berkshireesupply.com/cgi/CGP2SRIM?PMITEM=GM73B40013250&PARTPG=CGP2LMXE&PAMENU=&PAHDID=000000191911576&PARDID=649597376887499"],
["10","Workholding-Tooling-Acc-End-Shell-Mill-Holders-Shell-End-Mill-Holders","http://www.berkshireesupply.com/cgi/CGP2SRIM?PMITEM=HA70A63051112Z&PARTPG=CGP2LMXE&PAMENU=&PAHDID=000000191911576&PARDID=649597376887499"],
]
        for url in urls:
            try:
                #req = scrapy.Request( url[3] , callback=self.parse1,headers={ 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.8', 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' ,'Cache-Control': 'max-age=0' }, meta={"category":url[1], "position":url[2], "product_id":url[0]})
                req = scrapy.Request( url[2] , callback=self.parse1, meta={"category":url[1], "product_id":url[0]})
                #print url[0]
                #req.meta['item_id']=url[1]
                #req.meta['product_id']=url[0]
                #req.cookies = {'_ga':'GA1.2.341669427.1528975768', '_lo_uid':'78288-1528975768388-c4d067dc22160a6e', '__lotl':'http%3A%2F%2Fwww.berkshireesupply.com%2Fcgi%2FCGP2HOME', 'CoreID6':'45599990985315289758765&ci=90226171', 'cmTPSet':'Y', 'PTSP.COM':'000000191010326967951179001457', '_gid':'GA1.2.866831000.1530094662', 'CM_QS_REG':'%23LOGIN%7Eatjernlund@tjfans.com', '90226171_clogin':'v=1&l=86883201530169317084&e=1530172887543', '__ar_v4':'4ODRMKDK5RAI7CFQMGLXET%3A20180614%3A43%7CVSSDHAY6M5GK5E7JPCKNCL%3A20180614%3A43%7CJ6VFLDKT6BELRPWP7BAIHL%3A20180614%3A43', 'lo_session_in':'1', '_lorid':'78288-1530183186896-585fdb78eb24dc94', '_lo_v':'41'}
                #req.cookies = {'_ga':'GA1.2.484353849.1528975154', '_lo_uid':'78288-1528975155619-41c90201cb9173b6', '__lotl':'http%3A%2F%2Fwww.berkshireesupply.com%2Fcgi%2FCGP2HOME', 'CoreID6':'04454858049115289751676&ci=90226171', 'cmTPSet':'Y', 'PTSP.COM':'000000191237646887153983529263', '_gid':'GA1.2.403094579.1530522450', 'CM_QS_REG':'%23LOGIN%7Eatjernlund@tjfans.com', 'lo_session_in':'1', '_lorid':'78288-1530524259277-20558c17b6c089ae', '_lo_v':'56', '90226171_clogin':'l=77058581530522449541&v=1&e=1530526934461', '_gat_UA-4016961-16':'1', '__ar_v4':'4ODRMKDK5RAI7CFQMGLXET%3A20180614%3A43%7CVSSDHAY6M5GK5E7JPCKNCL%3A20180614%3A43%7CJ6VFLDKT6BELRPWP7BAIHL%3A20180614%3A43' }
                #req.cookies ={'_ga':'GA1.2.1853300903.1530529353', '_gid':'GA1.2.1419497447.1530529353', 'CoreID6':'51568533511115305293772&ci=90226171', 'cmTPSet':'Y', '_lo_uid':'78288-1530529377493-19d7ab969f4b944b', '__lotl':'http%3A%2F%2Fwww.berkshireesupply.com%2Fcgi%2FCGP2SRIM%3FPMITEM%3DAY50032%26PARTPG%3DCGP2LMXE%26PAMENU%3D%26PAHDID%3D000000191237646%26PARDID%3D887153983529263', 'PTSP.COM':'000000191365812938051820238145', 'CM_QS_REG':'%23LOGIN%7Eatjernlund@tjfans.com', 'lo_session_in':'1', '_lorid':'78288-1530858969337-8e590d445d39dd1c', '_lo_v':'23', '90226171_clogin':'v=1&l=91580681530858968586&e=1530860814755', '__ar_v4':'4ODRMKDK5RAI7CFQMGLXET%3A20180701%3A69%7CVSSDHAY6M5GK5E7JPCKNCL%3A20180701%3A69%7CJ6VFLDKT6BELRPWP7BAIHL%3A20180701%3A69'}
                #req.cookies ={'_ga':'GA1.2.1853300903.1530529353', 'CoreID6':'51568533511115305293772&ci=90226171', 'cmTPSet':'Y', '_lo_uid':'78288-1530529377493-19d7ab969f4b944b', '__lotl':'http%3A%2F%2Fwww.berkshireesupply.com%2Fcgi%2FCGP2SRIM%3FPMITEM%3DAY50032%26PARTPG%3DCGP2LMXE%26PAMENU%3D%26PAHDID%3D000000191237646%26PARDID%3D887153983529263', 'PTSP.COM':'000000191473797204245001172760', '_gid':'GA1.2.1277265550.1530951407', '_gat_UA-4016961-16':'1', 'lo_session_in':'1', '_lorid':'78288-1530951407872-0c0ed1af27d59077', '_lo_v':'26', 'CM_QS_REG':'%23LOGIN%7Eatjernlund@tjfans.com', '__ar_v4':'4ODRMKDK5RAI7CFQMGLXET%3A20180701%3A73%7CVSSDHAY6M5GK5E7JPCKNCL%3A20180701%3A73%7CJ6VFLDKT6BELRPWP7BAIHL%3A20180701%3A73', '90226171_clogin':'v=1&l=36803761530951407426&e=1530953227899' }
                #req.cookies ={'_ga':'GA1.2.341669427.1528975768', '_lo_uid':'78288-1528975768388-c4d067dc22160a6e', '__lotl':'http%3A%2F%2Fwww.berkshireesupply.com%2Fcgi%2FCGP2HOME', 'CoreID6':'45599990985315289758765&ci=90226171', 'cmTPSet':'Y', '_gid':'GA1.2.1289670166.1531145198', 'lo_session_in':'1', '_lo_v':'67', 'PTSP.COM':'000000191572572760495066996894', 'CM_QS_REG':'%23LOGIN%7Eatjernlund@tjfans.com', '__ar_v4':'J6VFLDKT6BELRPWP7BAIHL%3A20180614%3A120%7CVSSDHAY6M5GK5E7JPCKNCL%3A20180614%3A120%7C4ODRMKDK5RAI7CFQMGLXET%3A20180614%3A120', '90226171_clogin':'v=1&l=99282531531145690597&e=1531148661819', '_lorid':'78288-1531146570712-51d10d8a8b67eed4'}
                #req.cookies ={'_ga':'GA1.2.1853300903.1530529353', 'CoreID6':'51568533511115305293772&ci=90226171', '_lo_uid':'78288-1530529377493-19d7ab969f4b944b', '__lotl':'http%3A%2F%2Fwww.berkshireesupply.com%2Fcgi%2FCGP2SRIM%3FPMITEM%3DAY50032%26PARTPG%3DCGP2LMXE%26PAMENU%3D%26PAHDID%3D000000191237646%26PARDID%3D887153983529263', '_gid':'GA1.2.292101714.1531117169', 'PTSP.COM':'000000191753569581867575916400', 'cmTPSet':'Y', 'lo_session_in':'1', '_lorid':'78288-1531464840855-128132c0a8f8a243', '_lo_v':'77', 'CM_QS_REG':'%23LOGIN%7Eatjernlund@tjfans.com', '_gat_UA-4016961-16':'1', '90226171_clogin':'l=29590831531464769006&v=1&e=1531466827456', '__ar_v4':'J6VFLDKT6BELRPWP7BAIHL%3A20180701%3A160%7CVSSDHAY6M5GK5E7JPCKNCL%3A20180701%3A160%7C4ODRMKDK5RAI7CFQMGLXET%3A20180701%3A160' }
                req.cookies ={'_ga':'GA1.2.341669427.1528975768', '_lo_uid':'78288-1528975768388-c4d067dc22160a6e', '__lotl':'http%3A%2F%2Fwww.berkshireesupply.com%2Fcgi%2FCGP2HOME', 'CoreID6':'45599990985315289758765&ci=90226171', 'cmTPSet':'Y', 'CM_QS_REG':'%23LOGIN%7Eatjernlund@tjfans.com', 'PTSP.COM':'000000191911576649597376887499', '_gid':'GA1.2.1858235974.1531830705', 'lo_session_in':'1', '_lorid':'78288-1531830824621-9f0126503ba11269', '_lo_v':'80', '_gat_UA-4016961-16':'1', '90226171_clogin':'v=1&l=15276391531830749989&e=1531833164929', '__ar_v4':'J6VFLDKT6BELRPWP7BAIHL%3A20180716%3A10%7CVSSDHAY6M5GK5E7JPCKNCL%3A20180716%3A10%7C4ODRMKDK5RAI7CFQMGLXET%3A20180716%3A10'}
                if url[0] not in urls_done: 
                    yield req
                    time.sleep(.2)
            except: raise
        #print "URLS_DONE : ",urls_done


    def parse1(self,response):
        item=BerkshireItems()
        item['product_id']=response.meta["product_id"]
        title=response.xpath('//*[@id="main-content-inner"]/form/div/div[2]/div[1]/div[@class="product-main-info"]/div[@class="product-name"]/h1/text()').extract()
        #asin=response.url
        item_no=response.xpath('//*[@id="main-content-inner"]/form/div/div[2]/div[1]/div[1]/p[@class="product-ids"]/span[@class="item-num"]//text()').extract()
        mfg_no=response.xpath('//*[@id="main-content-inner"]/form/div/div[2]/div[1]/div[1]/p[@class="product-ids"]/span[@class="mfg-num"]//text()').extract()
        description=response.xpath('//*[@id="tab1"]/div[@class="product-info-additional"]/ul/li/text()').extract()
        shipping_info=response.xpath('//*[@id="tab2"]/div[@class="product-info-additional"]/ul/li//text()').extract()

		

        brand1=response.xpath('//*[@id="main-content-inner"]/form/div/div[2]/div[1]/div[@class="product-main-info"]/div[@class="product-name"]/h7/text()').extract()

        list_price = "".join(response.xpath('//*[@id="main-content-inner"]/form/div/div[2]/div[1]/div[1]/div[2]/span[1]/span[2]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        your_price = "".join(response.xpath('//*[@id="main-content-inner"]/form/div/div[2]/div[1]/div[1]/div[2]/span[2]/span[2]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        #if not price: price = "".join(response.xpath('//*[@id="priceblock_saleprice"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        #if not price: price ="".join(response.xpath('//*[@id="price-quantity-container"]/div[2]/div[1]/span[@class="a-size-large a-color-price guild_priceblock_ourprice"]/text()').extract()).replace("\n","").replace(" ","").strip()
        #if not price: price ="".join(response.xpath('//*[@id="price-quantity-container"]/div/div[1]/span[@class="a-size-large a-color-price guild_priceblock_ourprice"]/text()').extract()).replace("\n","").replace(" ","").strip()
        #if price: item['price']=price
        #else: item['price']=""

        if response.xpath('//*[@id="main-content-inner"]/form/div/div[2]/div[1]/div[1]/p[2]/span[@class="hazardous"]'):
            hazardous="".join(response.xpath('//*[@id="main-content-inner"]/form/div/div[2]/div[1]/div[1]/p[2]/span[@class="hazardous"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        else: hazardous=""
        features_dict={}
        features_list=response.xpath('//*[@id="product-info-table"]/tr')
        for features in features_list:
            key=features.xpath('td[1]/text()').extract()[0]
            value=features.xpath('td[2]/text()').extract()[0]
            features_dict[key]=value

        for key,value in features_dict.iteritems():
            if key.replace(" ","").lower().find("modelnumber") > -1:
                item['model_number']=value
            if key.replace(" ","").lower().find("itempartnumber") > -1:
                item['model_number']=value
            if key.replace(" ","").lower().find("partnumber") > -1:
                item['model_number']=value
            if key.replace(" ","").lower().find("numberofpieces") > -1:
                item['number_of_items']=value
            if key.replace(" ","").lower().find("count") > -1:
                item['number_of_items']=value
            if key.replace(" ","").lower().find("qty./pk.") > -1:
                item['number_of_items']=value
            if key.replace(" ","").lower().find("brandname") > -1:
                item['brand2']=value
            if key.replace(" ","").lower().find("hazardcode") > -1:
                item['hazard_code']=value
				
        images_list=response.xpath('//script[@type="text/javascript"]/text()').extract()
        image_url= [url for url in images_list if url.find('product-swatch-image') > -1]
        #print "55555555",image_url1
        item['image_url']="http://www.berkshireesupply.com"+image_url[0].split(',')[1].replace("'","")
        item['title']="".join(title).replace("\n","").replace("\t","").replace("    ","")
        item['hazardous']="".join(hazardous).replace("\n","").replace("\t","").replace("    ","")
        item['list_price']=list_price
        item['your_price']=your_price
        item['item_no']="".join(item_no).replace("\n","").replace("\t","").replace("\r","").replace("    ","")
        item['mfg_no']="".join(mfg_no).replace("\n","").replace("\t","").replace("\r","").replace("    ","")
        item['bullet_point_description']=" , ".join(description).replace("\n","").replace("\t","").replace("\r","").replace("    ","")
        if len(description)>0: item['bullet_point_1']= description[0]
        if len(description)>1: item['bullet_point_2']= description[1]
        if len(description)>2: item['bullet_point_3']= description[2]
        if len(description)>3: item['bullet_point_4']= description[3]
        if len(description)>4: item['bullet_point_5']= description[4]
        if len(description)>5: item['bullet_point_6']= description[5]
        if len(description)>6: item['bullet_point_7']= description[6]
        if len(description)>7: item['bullet_point_8']= description[7]
        if len(description)>8: item['bullet_point_9']= description[8]
        if len(description)>9: item['bullet_point_10']= description[9]

        if len(description)>10: item['description']= ", ".join(description[10:])
        item['shipping_info']=" , ".join(shipping_info).replace("\n","").replace("\t","").replace("\r","").replace("    ","")
        item['category']=response.meta["category"]
        item['features_dict']=features_dict
        item['product_url']=response.url
        item['brand1']="".join(brand1).replace("\n","").replace("\t","").replace("\r","").replace("    ","")
        yield item