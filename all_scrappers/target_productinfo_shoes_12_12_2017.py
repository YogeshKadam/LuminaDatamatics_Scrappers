# -*- coding: utf-8 -*-
import scrapy
import urllib

import os
import time
import re
import json
import demjson

class TargetItems(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    titleurl = scrapy.Field()



class TargetSpider(scrapy.Spider):
    imgcount = 1
    name = "target_productinfo_shoes_12_12_2017"
    allowed_domains = []

    #start_urls = ["http://www.flipkart.com/search?q=9780005996218"]  
    start_urls = ["https://www.target.com"]
    #start_urls = ["https://www.amazon.in/Daniel-Klein-Analog-Blue-Watch-DK11178-7/dp/B06XKM79QY/ref=sr_1_4?s=apparel&ie=UTF8&qid=1512629386&sr=1-4&nodeID=6648217031&psd=1&keywords=daniel+klein+watches+men"]

    def parse(self,response):
        urls_done = [
]
        urls=[
"https://www.target.com/c/men-s-watches-accessories/-/N-5xu2g",
]

        #urlpart1="https://www.ebay.com/b/Wristwatches/31387/bn_2408451?"
        #urlpart2="&_udlo="
        #urlpart3="&_udhi="
        #urlpart4="&_pgn="

        for url in urls:
            try:
                #req = scrapy.Request( url , callback=self.parse1, headers={'origin': 'https://www.target.com' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36' , 'accept': 'application/json, text/javascript, */*; q=0.01' , 'referer': 'https://www.target.com/' }, meta={'main_url':url})
                #yield req
                #time.sleep(.1)
                #for i in range(0,100):
                i=0
                while i<=1200:
                    urlpart1="https://redsky.target.com/v1/plp/search?count=24&offset="+str(i)
                    urlpart2="&sort_by=bestselling&category=5xtd1&visitorId=016044118A54020190B1854E0B38F460&channel=web&pageId=/c/"
                    req = scrapy.Request( urlpart1+urlpart2 , callback=self.parse1, meta={'main_url':url+urlpart1})
                    i += 24
                    #req = scrapy.Request( "https://www.ebay.com/b/Mens-Wristwatches/31387/bn_2971674?_udlo=99&_udhi=100" , callback=self.parse1, meta={'main_url':})
                    if url not in urls_done: 
                        yield req
                        time.sleep(.1)
                #print url[0]
                #req.meta['item_id']=url[1]
                #req.meta['product_id']=url[0]
                #req.cookies = { 'x-wl-uid':'1y8ltVLwKU/L4uHVRT4wcyu32QxGmsLap3PS10lHQ8I4lHwvcV3mdItRxlTQQbVCy6hcltYxKLMM=', 's_nr':'1498670542228-New', 's_vnum':'1930670542228%26vn%3D1', 's_dslv':'1498670542232','amznacsleftnav-ac35e287-d67e-4607-a950-5d9ffd0c2ca9':'1', 'x-amz-captcha-1':'1499054178128406', 'x-amz-captcha-2':'f44Jo5PiWFZO/J2o05Otig==', 'session-token':'jmS4MZ+87cNOfytK07tpUCEGti+GXuHdZ0oZyPtYqY7t0jdykH+Ub7kXBm+uyaqfsw9okzU8c7KFuF577LQSOEOVzXGU6Ky1xqdZjaFUDfW6H5HbFByM0YxhwaB/i3TdgWzWRV7hvGo3qygmjkrIJ3ESRIOOM6YB4EJWL65CQUTq+Cp4ORjO1XQaGvfPERmPKJ8tKI4p77AQ0pKocXEOtyFku2Vp9HJzTUI9LN4bZVnXVtkV/ra/ElaVLqz1HqDJ', 'csm-hit':'s-GZBERSD0R10VXC0HBQZ6|1500714195597', 'session-id-time':'2082754801l', 'session-id':'261-2325209-6209161', 'ubid-acbde':'259-4651163-1859124' }
                #req.cookies = {'lc-main':'en_US', 's_nr':'1503816974090-New', 's_vnum':'1935816974090%26vn%3D1', 's_dslv':'1503816974091', 'x-main':'pHlb3N0WUwENeYPsqI@jzfF7PXLCCMcJSFiGwcdKfrlzzhc8yQR4kOovInsAXJRe', 'at-main':'Atza|IwEBIF45RJQgsZLrUGO7JaJnp1uVC-RDIfDCqwjV0PeKEDcSIP7e0Pvcm_n-R4iCtwyo7zXH7KLDakbXVsW-9UevBLsZEeSIH2YZJFCjQqDsNAySplN1BcQ1tUj5kmj24vddIVYyi7vx3S0B-tkr9EISA5O5_d5Tr--5JO2qiruKCKawd1MLIyk8KFGS2KdQJGW9wwb9fJf6C7Fk4_7UiW5C3D1DLeuP3VXdar3-_S3yvGXRindK-xRNl3O_YFLRo-a_yn9_Z1V8vNj6kvWgzui_fOIRGrsI9qCHAJpcpt5Nh4Ta5n6-ALqNPkS-zbWlmMkZMgWsZb5EwLk8qr5O_FUA9Be8bqkneub7AuYy2QcvE01rYqkAKgAm4QKR5MSCXDQg8Fquyibqt_a3TRBYXTOzPnoedkm7JdBsUtVGYs4TBNssF4KGFefA1cQRLvxAhHfZe58', 'x-wl-uid':'1QBgT0TBwoj9RQ+QP7eh8ocBTABgs1739+rzq1e3s1iwjoSRYnMpbAczaaknzT2id2ww9iSyiyXd3OQeaJ9Nm9xZrZOKqXNWIDJihS4V7CV+xlp+PQA7T/ILJyNBZ15so9XvNPTzCBQA=', 'session-token':'qLl3vjnjOse5+Cy5cC+3OlMT95d5wVC4bWvaoAbqyhOetjeYqWP24HhMNHJI9Ni3Y7rljL1VdkRzXeolkaGJX8cPCh2P8OzRCIL3t4dynzdXlADAwNZxyWK1BFxTvyUzw4CXSHIeNdq1l95h3SbsLhG4gOhSf5JLHUzfx9dKziC4SpGUaTP+/8VbIE886Ipz6wOjM1J1YwP4lwLQABPJPh/qNzYZWgWTmLW2sk2bkN1nGCJk9XWAoIA2ClwvqPRRIFg8mbX73GFXkSCPmdboKQ==', 'csm-hit':'HCCNKDAR5Q931G1FR5S1+s-HCCNKDAR5Q931G1FR5S1|1504589304054', 'ubid-main':'151-8001146-5395566', 'session-id-time':'2082787201l', 'session-id':'151-4943311-4733238'}

            except: raise
        #print "URLS_DONE : ",urls_done


    def parse1(self,response):
        #print response.body
        #json11=response.xpath('/html/body/pre/text()[1]').extract()
        #print json11
        datadict=demjson.decode(response.body)
        titleurlslist=datadict['search_response']['items']['Item']
        #print titleurlslist
        for dict in titleurlslist:
            #print dict
            titleurl="https://www.target.com" + dict['url']
            price = dict['offer_price']['formatted_price']
            title = dict['title']
            item=TargetItems()
            item['titleurl']=titleurl
            item['title']=title
            item['price']=price
            #print titleurl
            #print title
            #print price
            yield item