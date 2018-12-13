# -*- coding: utf-8 -*-
import scrapy
import urllib

import os
import time
import re
import json


class CatalogItems(scrapy.Item):
    product_id= scrapy.Field()
    company_name= scrapy.Field()
    hall= scrapy.Field()
    address= scrapy.Field()
    country= scrapy.Field()
    phone_number= scrapy.Field()
    email_id= scrapy.Field()
    website= scrapy.Field()
    publication_topics= scrapy.Field()
    profession_trade= scrapy.Field()
    description= scrapy.Field()


class CatalogSpider(scrapy.Spider):
    imgcount = 1
    name = "catalog_productinfo_12-07-2018"
    allowed_domains = []

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]  

    def parse(self,response):
        urls_done = [
"product_id",
"13",
"14",
"10",
"11",
"12",
]
        urls=[
["1","https://catalog.services.book-fair.com/en/exhibitors-and-directories/exhibitors-a-z/exhibitors-a-z-details/ID/840224/action/detail/controller/Exhibitors/"],
["2","https://catalog.services.book-fair.com/en/exhibitors-and-directories/exhibitors-a-z/exhibitors-a-z-details/ID/838992/action/detail/controller/Exhibitors/"],
["3","https://catalog.services.book-fair.com/en/exhibitors-and-directories/exhibitors-a-z/exhibitors-a-z-details/ID/815592/action/detail/controller/Exhibitors/"],
["4","https://catalog.services.book-fair.com/en/exhibitors-and-directories/exhibitors-a-z/exhibitors-a-z-details/ID/813425/action/detail/controller/Exhibitors/"],
["5","https://catalog.services.book-fair.com/en/exhibitors-and-directories/exhibitors-a-z/exhibitors-a-z-details/ID/814418/action/detail/controller/Exhibitors/"],
["6","https://catalog.services.book-fair.com/en/exhibitors-and-directories/exhibitors-a-z/exhibitors-a-z-details/ID/836854/action/detail/controller/Exhibitors/"],
["7","https://catalog.services.book-fair.com/en/exhibitors-and-directories/exhibitors-a-z/exhibitors-a-z-details/ID/825716/action/detail/controller/Exhibitors/"],
["8","https://catalog.services.book-fair.com/en/exhibitors-and-directories/exhibitors-a-z/exhibitors-a-z-details/ID/840250/action/detail/controller/Exhibitors/"],
["9","https://catalog.services.book-fair.com/en/exhibitors-and-directories/exhibitors-a-z/exhibitors-a-z-details/ID/838997/action/detail/controller/Exhibitors/"],
["10","https://catalog.services.book-fair.com/en/exhibitors-and-directories/exhibitors-a-z/exhibitors-a-z-details/ID/827961/action/detail/controller/Exhibitors/"],
]

        for url in urls:
            try:
                #req = scrapy.Request( url[3] , callback=self.parse1,headers={ 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.8', 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' ,'Cache-Control': 'max-age=0' }, meta={"category":url[1], "position":url[2], "product_id":url[0]})
                req = scrapy.Request( url[1] , callback=self.parse1, meta={"product_id":url[0]})
                #print url[0]
                #req.meta['item_id']=url[1]
                #req.meta['product_id']=url[0]
                #req.cookies = {'_ga':'GA1.2.341669427.1528975768', '_lo_uid':'78288-1528975768388-c4d067dc22160a6e', '__lotl':'http%3A%2F%2Fwww.berkshireesupply.com%2Fcgi%2FCGP2HOME', 'CoreID6':'45599990985315289758765&ci=90226171', 'cmTPSet':'Y', 'PTSP.COM':'000000191010326967951179001457', '_gid':'GA1.2.866831000.1530094662', 'CM_QS_REG':'%23LOGIN%7Eatjernlund@tjfans.com', '90226171_clogin':'v=1&l=86883201530169317084&e=1530172887543', '__ar_v4':'4ODRMKDK5RAI7CFQMGLXET%3A20180614%3A43%7CVSSDHAY6M5GK5E7JPCKNCL%3A20180614%3A43%7CJ6VFLDKT6BELRPWP7BAIHL%3A20180614%3A43', 'lo_session_in':'1', '_lorid':'78288-1530183186896-585fdb78eb24dc94', '_lo_v':'41'}
                #req.cookies = {'_ga':'GA1.2.484353849.1528975154', '_lo_uid':'78288-1528975155619-41c90201cb9173b6', '__lotl':'http%3A%2F%2Fwww.berkshireesupply.com%2Fcgi%2FCGP2HOME', 'CoreID6':'04454858049115289751676&ci=90226171', 'cmTPSet':'Y', 'PTSP.COM':'000000191237646887153983529263', '_gid':'GA1.2.403094579.1530522450', 'CM_QS_REG':'%23LOGIN%7Eatjernlund@tjfans.com', 'lo_session_in':'1', '_lorid':'78288-1530524259277-20558c17b6c089ae', '_lo_v':'56', '90226171_clogin':'l=77058581530522449541&v=1&e=1530526934461', '_gat_UA-4016961-16':'1', '__ar_v4':'4ODRMKDK5RAI7CFQMGLXET%3A20180614%3A43%7CVSSDHAY6M5GK5E7JPCKNCL%3A20180614%3A43%7CJ6VFLDKT6BELRPWP7BAIHL%3A20180614%3A43' }
                #req.cookies ={'_ga':'GA1.2.1853300903.1530529353', '_gid':'GA1.2.1419497447.1530529353', 'CoreID6':'51568533511115305293772&ci=90226171', 'cmTPSet':'Y', '_lo_uid':'78288-1530529377493-19d7ab969f4b944b', '__lotl':'http%3A%2F%2Fwww.berkshireesupply.com%2Fcgi%2FCGP2SRIM%3FPMITEM%3DAY50032%26PARTPG%3DCGP2LMXE%26PAMENU%3D%26PAHDID%3D000000191237646%26PARDID%3D887153983529263', 'PTSP.COM':'000000191365812938051820238145', 'CM_QS_REG':'%23LOGIN%7Eatjernlund@tjfans.com', 'lo_session_in':'1', '_lorid':'78288-1530858969337-8e590d445d39dd1c', '_lo_v':'23', '90226171_clogin':'v=1&l=91580681530858968586&e=1530860814755', '__ar_v4':'4ODRMKDK5RAI7CFQMGLXET%3A20180701%3A69%7CVSSDHAY6M5GK5E7JPCKNCL%3A20180701%3A69%7CJ6VFLDKT6BELRPWP7BAIHL%3A20180701%3A69'}
                #req.cookies ={'_ga':'GA1.2.1853300903.1530529353', 'CoreID6':'51568533511115305293772&ci=90226171', 'cmTPSet':'Y', '_lo_uid':'78288-1530529377493-19d7ab969f4b944b', '__lotl':'http%3A%2F%2Fwww.berkshireesupply.com%2Fcgi%2FCGP2SRIM%3FPMITEM%3DAY50032%26PARTPG%3DCGP2LMXE%26PAMENU%3D%26PAHDID%3D000000191237646%26PARDID%3D887153983529263', 'PTSP.COM':'000000191473797204245001172760', '_gid':'GA1.2.1277265550.1530951407', '_gat_UA-4016961-16':'1', 'lo_session_in':'1', '_lorid':'78288-1530951407872-0c0ed1af27d59077', '_lo_v':'26', 'CM_QS_REG':'%23LOGIN%7Eatjernlund@tjfans.com', '__ar_v4':'4ODRMKDK5RAI7CFQMGLXET%3A20180701%3A73%7CVSSDHAY6M5GK5E7JPCKNCL%3A20180701%3A73%7CJ6VFLDKT6BELRPWP7BAIHL%3A20180701%3A73', '90226171_clogin':'v=1&l=36803761530951407426&e=1530953227899' }
                #req.cookies ={'_ga':'GA1.2.341669427.1528975768', '_lo_uid':'78288-1528975768388-c4d067dc22160a6e', '__lotl':'http%3A%2F%2Fwww.berkshireesupply.com%2Fcgi%2FCGP2HOME', 'CoreID6':'45599990985315289758765&ci=90226171', 'cmTPSet':'Y', '_gid':'GA1.2.1289670166.1531145198', 'lo_session_in':'1', '_lo_v':'67', 'PTSP.COM':'000000191572572760495066996894', 'CM_QS_REG':'%23LOGIN%7Eatjernlund@tjfans.com', '__ar_v4':'J6VFLDKT6BELRPWP7BAIHL%3A20180614%3A120%7CVSSDHAY6M5GK5E7JPCKNCL%3A20180614%3A120%7C4ODRMKDK5RAI7CFQMGLXET%3A20180614%3A120', '90226171_clogin':'v=1&l=99282531531145690597&e=1531148661819', '_lorid':'78288-1531146570712-51d10d8a8b67eed4'}                
                if url[0] not in urls_done: 
                    yield req
                    #time.sleep(.2)
            except: raise
        #print "URLS_DONE : ",urls_done


    def parse1(self,response):
        item=CatalogItems()
        item['product_id']=response.meta["product_id"]
        phone_number=""
        email_id=""
        website=""
        company_name="".join(response.xpath('//*[@id="details"]/div[1]/div[1]/h2/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        address="".join(response.xpath('//*[@id="details"]/div[2]/div[1]/div[@class="address"]/div/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        country="".join(response.xpath('//*[@id="details"]/div[2]/div[1]/div[@class="address"]/div[@class="address_country"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        hall="".join(response.xpath('//*[@id="details"]/div[1]/div[3]/div[@class="staende_wrap"]/small/text()').extract()).replace("\n",'').replace('\t','').strip()
        attr_list=response.xpath('//*[@id="details"]/div[2]/div[2]/table/tr')
        for attr in attr_list:
            if "".join(attr.xpath('td[1]//text()').extract()).replace(" ",'').replace("\n",'').replace('\t','').replace('\r','').strip().lower().find('phone') > -1:
                phone_number="".join(attr.xpath('td[@class="t_value"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').replace('\r','').strip()
            if "".join(attr.xpath('td[1]//text()').extract()).replace(" ",'').replace("\n",'').replace('\t','').replace('\r','').strip().lower().find('e-mail') > -1:
                email_id="".join(attr.xpath('td[@class="t_value"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').replace('\r','').strip()
            if "".join(attr.xpath('td[1]//text()').extract()).replace(" ",'').replace("\n",'').replace('\t','').replace('\r','').strip().lower().find('website') > -1:
                website="".join(attr.xpath('td[@class="t_value"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').replace('\r','').strip()

        description="".join(response.xpath('//*[@id="tab_0"]/div/div/div[@class="row zusatztext_text"]/div[@class="col-sm-12"]/p/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').replace('\r','').strip()

        publication_dict={}
        publication_list=response.xpath('//*[@id="tab_1"]/div/div/table/tr')
        for pl in publication_list:
            key="".join(pl.xpath('td/div/span[@class="zusatzinfo small"]/a/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').replace('\r','').strip()
            value="".join(pl.xpath('td/div/div[@class="targetTag ublue"]/a/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').replace('\r','').strip()
            publication_dict[key]=value
			
        profession_dict={}
        profession_list=response.xpath('//*[@id="tab_2"]/div/div/div[@class="row entry"]')
        for pl in profession_list:
            key="".join(pl.xpath('div[2]/span[@class="zusatzinfo small"]/a/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').replace('\r','').strip()
            value="".join(pl.xpath('div[2]/div[@class="maincategory"]/a/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').replace('\r','').strip()
            profession_dict[key]=value
		
        item['company_name']=company_name
        item['address']=address
        item['country']=country
        item['hall']=hall
        item['phone_number']=phone_number
        item['email_id']=email_id
        item['website']=website
        item['description']=description
        item['publication_topics']=publication_dict
        item['profession_trade']=profession_dict
        yield item