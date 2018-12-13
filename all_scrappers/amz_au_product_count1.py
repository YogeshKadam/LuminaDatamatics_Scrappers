# -*- coding: utf-8 -*-
import scrapy
import urllib
from pymongo import MongoClient
import os
import time
import re
import json
from scrapy.conf import settings
class ComapreItem(scrapy.Item):
    category_url = scrapy.Field()
    count = scrapy.Field()
    product_id = scrapy.Field()


class amazonSpider(scrapy.Spider):
    imgcount = 1
    name = "amz_au_product_count1"
    allowed_domains = []

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]  

    def parse(self,response):
        urls_done = []
        urls=[
["1","https://www.amazon.com.au/b?ie=UTF8&node=5130781051"],
["2","https://www.amazon.com.au/b?ie=UTF8&node=5131089051"],
["3","https://www.amazon.com.au/b?ie=UTF8&node=5131099051"],
["4","https://www.amazon.com.au/b?ie=UTF8&node=5131091051"],
["5","https://www.amazon.com.au/b?ie=UTF8&node=5131100051"],
["6","https://www.amazon.com.au/b?ie=UTF8&node=5131843051"],
["7","https://www.amazon.com.au/b?ie=UTF8&node=5131093051"],
["8","https://www.amazon.com.au/b?ie=UTF8&node=5131094051"],
["9","https://www.amazon.com.au/b?ie=UTF8&node=5131095051"],
["10","https://www.amazon.com.au/b?ie=UTF8&node=5131096051"],
["11","https://www.amazon.com.au/b?ie=UTF8&node=5131872051"],
["12","https://www.amazon.com.au/b?ie=UTF8&node=5131097051"],
["13","https://www.amazon.com.au/b?ie=UTF8&node=5131873051"],
["14","https://www.amazon.com.au/b?ie=UTF8&node=5131101051"],
["15","https://www.amazon.com.au/b?ie=UTF8&node=5131102051"],
["16","https://www.amazon.com.au/b?ie=UTF8&node=5131103051"],
["17","https://www.amazon.com.au/b?ie=UTF8&node=5131104051"],
["18","https://www.amazon.com.au/b?ie=UTF8&node=5131088051"],
["19","https://www.amazon.com.au/b?ie=UTF8&node=5131105051"],
["20","https://www.amazon.com.au/b?ie=UTF8&node=5131844051"],
["21","https://www.amazon.com.au/b?ie=UTF8&node=5131106051"],
["22","https://www.amazon.com.au/b?ie=UTF8&node=5131107051"],
["23","https://www.amazon.com.au/b?ie=UTF8&node=5131108051"],
["24","https://www.amazon.com.au/b?ie=UTF8&node=5130762051"],
["25","https://www.amazon.com.au/b?ie=UTF8&node=5130957051"],
["26","https://www.amazon.com.au/b?ie=UTF8&node=5130958051"],
["27","https://www.amazon.com.au/b?ie=UTF8&node=5131519051"],
["28","https://www.amazon.com.au/b?ie=UTF8&node=5130954051"],
["29","https://www.amazon.com.au/b?ie=UTF8&node=5130955051"],
["30","https://www.amazon.com.au/b?ie=UTF8&node=5130956051"],
["31","https://www.amazon.com.au/b?ie=UTF8&node=5130959051"],
["32","https://www.amazon.com.au/b?ie=UTF8&node=5130960051"],
["33","https://www.amazon.com.au/b?ie=UTF8&node=5130961051"],
["34","https://www.amazon.com.au/b?ie=UTF8&node=5130962051"],
["35","https://www.amazon.com.au/b?ie=UTF8&node=5130951051"],
["36","https://www.amazon.com.au/b?ie=UTF8&node=5130963051"],
["37","https://www.amazon.com.au/b?ie=UTF8&node=5131520051"],
["38","https://www.amazon.com.au/b?ie=UTF8&node=5130964051"],
["39","https://www.amazon.com.au/b?ie=UTF8&node=5130965051"],
["40","https://www.amazon.com.au/b?ie=UTF8&node=5130966051"],
["41","https://www.amazon.com.au/b?ie=UTF8&node=5130967051"],
]

        for url in urls:
            try:
                #req = scrapy.Request(url[3] , headers={ 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Cache-Control': 'max-age=0' },callback=self.parse6)
                #req = scrapy.Request(url , headers={'Origin': 'https://www.amazon.com' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36' , 'Accept': '*/*' , 'Referer': 'https://www.amazon.com/' , 'X-Requested-With': 'XMLHttpRequest' , 'Connection': 'keep-alive' , 'Content-Length': '0'}, callback=self.parse6)
                req = scrapy.Request(url[1] , headers={'authority': 'www.amazon.com.au' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9' }, callback=self.parse6)
                #req = scrapy.Request(url[2] , callback=self.parse6)
                req.meta['product_id']=url[0]
                #req.meta['brand']=url[1]
                #req.meta['category']=url[1]
                #req.cookies = { 'x-wl-uid':'1y8ltVLwKU/L4uHVRT4wcyu32QxGmsLap3PS10lHQ8I4lHwvcV3mdItRxlTQQbVCy6hcltYxKLMM=', 's_nr':'1498670542228-New', 's_vnum':'1930670542228%26vn%3D1', 's_dslv':'1498670542232','amznacsleftnav-ac35e287-d67e-4607-a950-5d9ffd0c2ca9':'1', 'x-amz-captcha-1':'1499054178128406', 'x-amz-captcha-2':'f44Jo5PiWFZO/J2o05Otig==', 'session-token':'jmS4MZ+87cNOfytK07tpUCEGti+GXuHdZ0oZyPtYqY7t0jdykH+Ub7kXBm+uyaqfsw9okzU8c7KFuF577LQSOEOVzXGU6Ky1xqdZjaFUDfW6H5HbFByM0YxhwaB/i3TdgWzWRV7hvGo3qygmjkrIJ3ESRIOOM6YB4EJWL65CQUTq+Cp4ORjO1XQaGvfPERmPKJ8tKI4p77AQ0pKocXEOtyFku2Vp9HJzTUI9LN4bZVnXVtkV/ra/ElaVLqz1HqDJ', 'csm-hit':'s-GZBERSD0R10VXC0HBQZ6|1500714195597', 'session-id-time':'2082754801l', 'session-id':'261-2325209-6209161', 'ubid-acbde':'259-4651163-1859124' }
                req.cookies = {'session-id':'357-8598835-1450545', 'ubid-acbau':'358-7115274-3106518', 'session-token':'EtcA9wzuqH3NdMV8l0NMDzLVMD5ZCKAqimbU9lkfgZ7IMmpXwyWbqe+ZdVC8iwXUko/0TzQyTYjxAailM7xCOSvCdCupaI2dGJH3+sGqTxZpLU6nyZ6DfqbrBsfUMa4g3XOjxj4aCnk7hlACvOhFyuJYnde84lZ8ZJJWZ1WkMU0JNCpKq+7cXh8BG1HtggP9', 'x-wl-uid':'1xclpOkIVA7W4Oijd0mDpN7mV8R+4Xx49ClfcDse75ltSGl63usivaoCwpaE7RxN689zsLM4V+zU=', 'lc-acbau':'en_AU', 'session-id-time':'2082758401l', 'csm-hit':'tb:s-6FM1ZKYHRJNN8G5NKXXW|1533201626022&adb:adblk_no'}
                #req.cookies = {'lc-main':'en_US', 's_nr':'1503816974090-New', 's_vnum':'1935816974090%26vn%3D1', 's_dslv':'1503816974091', 'x-main':'pHlb3N0WUwENeYPsqI@jzfF7PXLCCMcJSFiGwcdKfrlzzhc8yQR4kOovInsAXJRe', 'at-main':'Atza|IwEBIF45RJQgsZLrUGO7JaJnp1uVC-RDIfDCqwjV0PeKEDcSIP7e0Pvcm_n-R4iCtwyo7zXH7KLDakbXVsW-9UevBLsZEeSIH2YZJFCjQqDsNAySplN1BcQ1tUj5kmj24vddIVYyi7vx3S0B-tkr9EISA5O5_d5Tr--5JO2qiruKCKawd1MLIyk8KFGS2KdQJGW9wwb9fJf6C7Fk4_7UiW5C3D1DLeuP3VXdar3-_S3yvGXRindK-xRNl3O_YFLRo-a_yn9_Z1V8vNj6kvWgzui_fOIRGrsI9qCHAJpcpt5Nh4Ta5n6-ALqNPkS-zbWlmMkZMgWsZb5EwLk8qr5O_FUA9Be8bqkneub7AuYy2QcvE01rYqkAKgAm4QKR5MSCXDQg8Fquyibqt_a3TRBYXTOzPnoedkm7JdBsUtVGYs4TBNssF4KGFefA1cQRLvxAhHfZe58', 'x-wl-uid':'1QBgT0TBwoj9RQ+QP7eh8ocBTABgs1739+rzq1e3s1iwjoSRYnMpbAczaaknzT2id2ww9iSyiyXd3OQeaJ9Nm9xZrZOKqXNWIDJihS4V7CV+xlp+PQA7T/ILJyNBZ15so9XvNPTzCBQA=', 'session-token':'qLl3vjnjOse5+Cy5cC+3OlMT95d5wVC4bWvaoAbqyhOetjeYqWP24HhMNHJI9Ni3Y7rljL1VdkRzXeolkaGJX8cPCh2P8OzRCIL3t4dynzdXlADAwNZxyWK1BFxTvyUzw4CXSHIeNdq1l95h3SbsLhG4gOhSf5JLHUzfx9dKziC4SpGUaTP+/8VbIE886Ipz6wOjM1J1YwP4lwLQABPJPh/qNzYZWgWTmLW2sk2bkN1nGCJk9XWAoIA2ClwvqPRRIFg8mbX73GFXkSCPmdboKQ==', 'csm-hit':'HCCNKDAR5Q931G1FR5S1+s-HCCNKDAR5Q931G1FR5S1|1504589304054', 'ubid-main':'151-8001146-5395566', 'session-id-time':'2082787201l', 'session-id':'151-4943311-4733238'}
                #req.cookies ={'lc-main':'en_US', 's_nr':'1503816974090-New', 's_vnum':'1935816974090%26vn%3D1', 's_dslv':'1503816974091', 'x-main':'pHlb3N0WUwENeYPsqI@jzfF7PXLCCMcJSFiGwcdKfrlzzhc8yQR4kOovInsAXJRe', 'at-main':'Atza|IwEBIF45RJQgsZLrUGO7JaJnp1uVC-RDIfDCqwjV0PeKEDcSIP7e0Pvcm_n-R4iCtwyo7zXH7KLDakbXVsW-9UevBLsZEeSIH2YZJFCjQqDsNAySplN1BcQ1tUj5kmj24vddIVYyi7vx3S0B-tkr9EISA5O5_d5Tr--5JO2qiruKCKawd1MLIyk8KFGS2KdQJGW9wwb9fJf6C7Fk4_7UiW5C3D1DLeuP3VXdar3-_S3yvGXRindK-xRNl3O_YFLRo-a_yn9_Z1V8vNj6kvWgzui_fOIRGrsI9qCHAJpcpt5Nh4Ta5n6-ALqNPkS-zbWlmMkZMgWsZb5EwLk8qr5O_FUA9Be8bqkneub7AuYy2QcvE01rYqkAKgAm4QKR5MSCXDQg8Fquyibqt_a3TRBYXTOzPnoedkm7JdBsUtVGYs4TBNssF4KGFefA1cQRLvxAhHfZe58', 'x-wl-uid':'1QBgT0TBwoj9RQ+QP7eh8ocBTABgs1739+rzq1e3s1iwjoSRYnMpbAczaaknzT2id2ww9iSyiyXd3OQeaJ9Nm9xZrZOKqXNWIDJihS4V7CV+xlp+PQA7T/ILJyNBZ15so9XvNPTzCBQA=', 'x-amz-captcha-1':'1511784189246059', 'x-amz-captcha-2':'e+dIUFBcjimZCAzt1M7ENg==', 'session-token':'PyjCayhcDu7hHhYCfKE/HuBCBEOaahuY6CNwnoivzMed8qr0ZHDCUZ3JfJ2TRWZ5olesRRksGz+JukvNjXuAoGXc4BmeNH3JY9a7RAUFZ+JNXc3QdXMHK4mlTxF1/pnsFXg7mjivPGJE7qp7fcEexjQd2AE+QWjUanCL+3J3hlClu6GB212X/erRr/WVWf7LDVf3SmANI5rBx2spX6tqui9km7LBf+FKzhyPYARgj2C4728rqinQmeIdKFuJ5OQGHqOLhePWXsLrmry0f5DXow==', 'csm-hit':'%7B%22tb%22%3A%22s-40H2SRFEWW3KSNRY3K5G%7C1512035962489%22%2C%22adb%22%3A%22adblk_no%22%7D', 'ubid-main':'151-8001146-5395566', 'session-id-time':'2082787201l', 'session-id':'151-4943311-4733238'}
                if url[0] not in urls_done: 
                    yield req
                    time.sleep(.1)
            except: raise
        #print "URLS_DONE : ",urls_done


    def parse6(self,response):
        item=ComapreItem()
        count=response.xpath('//*[@id="s-result-count"]/text()').extract()[0]
        item['count']=count
        item['category_url']=response.url
        item['product_id']=response.meta['product_id']
        yield item