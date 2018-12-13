# -*- coding: utf-8 -*-
import scrapy
import urllib
from pymongo import MongoClient
import os
import time
import re
import json
from scrapy.conf import settings
class AmazonItem(scrapy.Item):
    url = scrapy.Field()
    category = scrapy.Field()


class amazonSpider(scrapy.Spider):
    imgcount = 1
    name = "amz_category_30-08-2018"
    allowed_domains = []

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]  

    def parse(self,response):
        urls_done = [
]
        urls=[
["1","https://www.amazon.com/home-garden-kitchen-furniture-bedding/b?ie=UTF8&node=1055398"],
["2","https://www.amazon.com/Shop-by-Room/b?ie=UTF8&node=14544458011"],
["3","https://www.amazon.com/home-d%C3%A9cor/b?ie=UTF8&node=1063278"],
["4","https://www.amazon.com/Furniture/b?ie=UTF8&node=1063306"],
["5","https://www.amazon.com/kitchen-dining/b?ie=UTF8&node=284507"],
["6","https://www.amazon.com/bedding-bath-sheets-towels/b?ie=UTF8&node=1057792"],
["7","https://www.amazon.com/Patio-Lawn-Garden/b?ie=UTF8&node=2972638011"],
["8","https://www.amazon.com/Tools-and-Home-Improvement/b?ie=UTF8&node=228013"],
["9","https://www.amazon.com/smart-home-devices/b?ie=UTF8&node=6563140011"],
["10","https://www.amazon.com/Tools-and-Home-Improvement/b/ref=sd_allcat_hi2?ie=UTF8&node=228013"],
]

        for url in urls:
            try:
                #req = scrapy.Request(url[3] , headers={ 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Cache-Control': 'max-age=0' },callback=self.parse6)
                #req = scrapy.Request(url[3] , headers= {'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Cache-Control': 'max-age=0' , 'Connection': 'keep-alive'}, callback=self.parse6)
                #req = scrapy.Request(url[2] , callback=self.parse6)
                #req = scrapy.Request(url[2] , headers={'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive' }, callback=self.parse6)
                req = scrapy.Request(url[1] , callback=self.parse6)
                req.meta['page_id']=url[0]
                #req.meta['category']=url[1]
                #req.cookies = {'lc-main':'en_US', 's_nr':'1503816974090-New', 's_vnum':'1935816974090%26vn%3D1', 's_dslv':'1503816974091', 'x-main':'pHlb3N0WUwENeYPsqI@jzfF7PXLCCMcJSFiGwcdKfrlzzhc8yQR4kOovInsAXJRe', 'at-main':'Atza|IwEBIF45RJQgsZLrUGO7JaJnp1uVC-RDIfDCqwjV0PeKEDcSIP7e0Pvcm_n-R4iCtwyo7zXH7KLDakbXVsW-9UevBLsZEeSIH2YZJFCjQqDsNAySplN1BcQ1tUj5kmj24vddIVYyi7vx3S0B-tkr9EISA5O5_d5Tr--5JO2qiruKCKawd1MLIyk8KFGS2KdQJGW9wwb9fJf6C7Fk4_7UiW5C3D1DLeuP3VXdar3-_S3yvGXRindK-xRNl3O_YFLRo-a_yn9_Z1V8vNj6kvWgzui_fOIRGrsI9qCHAJpcpt5Nh4Ta5n6-ALqNPkS-zbWlmMkZMgWsZb5EwLk8qr5O_FUA9Be8bqkneub7AuYy2QcvE01rYqkAKgAm4QKR5MSCXDQg8Fquyibqt_a3TRBYXTOzPnoedkm7JdBsUtVGYs4TBNssF4KGFefA1cQRLvxAhHfZe58', 'x-wl-uid':'1QBgT0TBwoj9RQ+QP7eh8ocBTABgs1739+rzq1e3s1iwjoSRYnMpbAczaaknzT2id2ww9iSyiyXd3OQeaJ9Nm9xZrZOKqXNWIDJihS4V7CV+xlp+PQA7T/ILJyNBZ15so9XvNPTzCBQA=', 'x-amz-captcha-1':'1511784189246059', 'x-amz-captcha-2':'e+dIUFBcjimZCAzt1M7ENg==', 'skin':'noskin', 'session-token':'iLbxbiSqExhaR4LPazKup8FEME8wVof1IaYWHpuSZwkY9Pk99Za2t1nVKi07sKUQrt7vqJ1e8hVd+j+XnNR0sr/z1MFubVFga4Gs7V0Ex2bhH+zFs7fU23+xahjvRAHWjVywkXsJyB8REkaRCDWd5GhE6loyew2Ibyol3vtiEyuebDuB1Y1hwVGYY+DGF8ujzqDQvV0psuzZg3JwtZCgfaymOM9XSIYP8OlojdlhdY8g6texOGn+IwTndrN3g5zYg4TsvZU7oWYXp6bVS8QP+A==', 'csm-hit':'s-YCC0NCGB2CHZFXZA740S|1513777168018', 'ubid-main':'151-8001146-5395566', 'session-id-time':'2082787201l', 'session-id':'151-4943311-4733238' }
                #req.cookies = { 'x-wl-uid':'1y8ltVLwKU/L4uHVRT4wcyu32QxGmsLap3PS10lHQ8I4lHwvcV3mdItRxlTQQbVCy6hcltYxKLMM=', 's_nr':'1498670542228-New', 's_vnum':'1930670542228%26vn%3D1', 's_dslv':'1498670542232','amznacsleftnav-ac35e287-d67e-4607-a950-5d9ffd0c2ca9':'1', 'x-amz-captcha-1':'1499054178128406', 'x-amz-captcha-2':'f44Jo5PiWFZO/J2o05Otig==', 'session-token':'jmS4MZ+87cNOfytK07tpUCEGti+GXuHdZ0oZyPtYqY7t0jdykH+Ub7kXBm+uyaqfsw9okzU8c7KFuF577LQSOEOVzXGU6Ky1xqdZjaFUDfW6H5HbFByM0YxhwaB/i3TdgWzWRV7hvGo3qygmjkrIJ3ESRIOOM6YB4EJWL65CQUTq+Cp4ORjO1XQaGvfPERmPKJ8tKI4p77AQ0pKocXEOtyFku2Vp9HJzTUI9LN4bZVnXVtkV/ra/ElaVLqz1HqDJ', 'csm-hit':'s-GZBERSD0R10VXC0HBQZ6|1500714195597', 'session-id-time':'2082754801l', 'session-id':'261-2325209-6209161', 'ubid-acbde':'259-4651163-1859124' }
                #req.cookies = {'lc-main':'en_US', 's_nr':'1503816974090-New', 's_vnum':'1935816974090%26vn%3D1', 's_dslv':'1503816974091', 'x-main':'pHlb3N0WUwENeYPsqI@jzfF7PXLCCMcJSFiGwcdKfrlzzhc8yQR4kOovInsAXJRe', 'at-main':'Atza|IwEBIF45RJQgsZLrUGO7JaJnp1uVC-RDIfDCqwjV0PeKEDcSIP7e0Pvcm_n-R4iCtwyo7zXH7KLDakbXVsW-9UevBLsZEeSIH2YZJFCjQqDsNAySplN1BcQ1tUj5kmj24vddIVYyi7vx3S0B-tkr9EISA5O5_d5Tr--5JO2qiruKCKawd1MLIyk8KFGS2KdQJGW9wwb9fJf6C7Fk4_7UiW5C3D1DLeuP3VXdar3-_S3yvGXRindK-xRNl3O_YFLRo-a_yn9_Z1V8vNj6kvWgzui_fOIRGrsI9qCHAJpcpt5Nh4Ta5n6-ALqNPkS-zbWlmMkZMgWsZb5EwLk8qr5O_FUA9Be8bqkneub7AuYy2QcvE01rYqkAKgAm4QKR5MSCXDQg8Fquyibqt_a3TRBYXTOzPnoedkm7JdBsUtVGYs4TBNssF4KGFefA1cQRLvxAhHfZe58', 'x-wl-uid':'1QBgT0TBwoj9RQ+QP7eh8ocBTABgs1739+rzq1e3s1iwjoSRYnMpbAczaaknzT2id2ww9iSyiyXd3OQeaJ9Nm9xZrZOKqXNWIDJihS4V7CV+xlp+PQA7T/ILJyNBZ15so9XvNPTzCBQA=', 'session-token':'qLl3vjnjOse5+Cy5cC+3OlMT95d5wVC4bWvaoAbqyhOetjeYqWP24HhMNHJI9Ni3Y7rljL1VdkRzXeolkaGJX8cPCh2P8OzRCIL3t4dynzdXlADAwNZxyWK1BFxTvyUzw4CXSHIeNdq1l95h3SbsLhG4gOhSf5JLHUzfx9dKziC4SpGUaTP+/8VbIE886Ipz6wOjM1J1YwP4lwLQABPJPh/qNzYZWgWTmLW2sk2bkN1nGCJk9XWAoIA2ClwvqPRRIFg8mbX73GFXkSCPmdboKQ==', 'csm-hit':'HCCNKDAR5Q931G1FR5S1+s-HCCNKDAR5Q931G1FR5S1|1504589304054', 'ubid-main':'151-8001146-5395566', 'session-id-time':'2082787201l', 'session-id':'151-4943311-4733238'}
                #req.cookies = {'s_nr':'1514464459649-Repeat', 's_vnum':'1935816974090%26vn%3D2', 's_dslv':'1514464459650', 'amznacsleftnav-74393fbe-66a6-3a52-840b-37b54d8c76ce':'1', 'ubid-main':'151-8001146-5395566', 'session-id':'143-2570392-1761151', 'session-id-time':'2082787201l', 'x-amz-captcha-1':'1518087751656922', 'x-amz-captcha-2':'TAtOiFxNP39/4JXr1HRtRQ==', 'sst-main':'Sst1|PQEIWOSKQkmRJNiLdAIpYuxvCAgSf8fU0zrPqIDU7VYVKFCOVnWBgJtiBpdxZRVT3-poc3ti0PuawPx6vNYyBVldZhbnizavxNe9Bk4hO_sfGatBlE4qbUfAffoSGZ6yY5qCSewJxENQdMoYJdd2iGeltGkf31I7IedHWFkRNqIMeLvDhOTN6hqKpQTN9hDBPQMu5cmGO5GyahsVZgdQHW7nBs2FLMophIEpjxCVzavMHwn4aHwIdloCWgkG6TfVmKcDiLUXWWoEXfBKp1QLdH2Mrg', 'x-wl-uid':'1yxWFE65rJfR+kOyS6k2hEnyGw4GjqsLYgzk8HpBprCTXNRb3M/MHB8cr9TuingY8KMY1MTFD/DRDFDi8l+aNIzcMf1WnUCGQpyuxT03VbXPERI+scQGnJsJeQnc9o4RlV2Ma6WJrdc4=', 'session-token':'rxLcGYC0NRCcoO4VkktmBsPxOQ9ijb7A7y+U04K11tUdm56q5+IfofrwXNkASd2VRmrzzjMAZYXSYCfNpYtun/TVNDL2W9szbccnXIwNl1WCwn0nSmKS252Ny1WqkdB0gWJem0QYwk9DIcz/Rm27nFidGDvO0QUKDRuqDXoXvxNDciWc86l/HX+vFS9RNG55PPuLoxeSz4isAn6TjnB+DLpNoO/6XZbi4IcZUvEonMZ6fnsL1Ut/RDk/6sxP5vOa', 'csm-hit':'1EK1B8SRZQ7J0XNH96X2+s-1EK1B8SRZQ7J0XNH96X2|1522756475463' }
                if url[0] not in urls_done: 
                    yield req
                    #time.sleep(.1)
            except: raise
        #print "URLS_DONE : ",urls_done


    def parse6(self,response):
        categorylist=response.xpath('//*[@id="merchandised-content"]/div[@class="acsUxWidget"]/div/div/div/div/div/div/a')
        #categorylist1=response.xpath('//*[@id="leftNavContainer"]/ul[1]/ul/div/li/span/a')
        product_count=response.xpath('//*[@id="s-result-count"]/text()').extract()
        if product_count:
            item=AmazonItem()
            #categoryname=response.xpath('//*[@id="mainContent"]/div[3]/h1/text()').extract()[0]
            categoryname="".join(response.xpath('//*[@id="fst-hybrid-dynamic-h1"]/div/h1//text()').extract())
            if not categoryname: categoryname="".join(response.xpath('//*[@id="leftNavContainer"]/ul[1]/li/span/h4//text()').extract())
            if not categoryname: categoryname="".join(response.xpath('//*[@id="s-result-count"]/span/span/text()').extract())
            if not categoryname: categoryname="".join(response.xpath('//*[@id="leftNav"]/ul[1]/li/span/h4/text()').extract())
            categoryurl=response.url
            item['url']=categoryurl
            item['category'] =categoryname
            yield item
        elif len(categorylist)>0:
            for categories in categorylist:
                #item=LowesItem()
                #categoryurl="https://www.amazon.com" + categories.xpath('span/a/@href').extract()[0]
                #categoryname= categories.xpath('span/a/span/text()').extract()[0]
                categoryurl="https://www.amazon.com"+categories.xpath('@href').extract()[0]
                #categoryname=categories.xpath('span/text()').extract()[0]
                req=scrapy.Request(categoryurl,callback=self.parse6)
                #item['url']=categoryurl
                #item['category'] =categoryname
                #yield item
                yield req