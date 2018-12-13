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
    #brand = scrapy.Field()
    response_url = scrapy.Field()
    category = scrapy.Field()
    product_id = scrapy.Field()
    asin = scrapy.Field()


class amazonSpider(scrapy.Spider):
    imgcount = 1
    name = "amz_brandurl_to_asin_20-12-2017"
    allowed_domains = []

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]  

    def parse(self,response):
        urls_done = []
        urls=[
["2","Picture Frames","https://www.amazon.com/Malden-2082-14-Manhattan-14-Inch-Black/dp/B001FBHZHE"],
["3","Picture Frames","https://www.amazon.com/Malden-Silver-Essential-Fashion-10-Inch/dp/B001FBHZU6"],
["4","Picture Frames","https://www.amazon.com/Malden-International-Designs-Classic-8x10-Inches/dp/B001FBDC3U"],
["5","Picture Frames","https://www.amazon.com/Malden-International-Designs-Fashion-Graywash/dp/B01BNYAOIO"],
["6","Picture Frames","https://www.amazon.com/Malden-International-Designs-Walnut-Picture/dp/B0036Q2VY8"],
["7","Picture Frames","https://www.amazon.com/Malden-International-Designs-Grandkids-Expressions/dp/B00N1SEDUG"],
["8","Keepsake Frames","https://www.amazon.com/Malden-International-Designs-Nursery-Picture/dp/B00005V5MU"],
["9","Picture Frames","https://www.amazon.com/Malden-International-Designs-Barnside-Portrait/dp/B00L5BGE5S"],
["10","Picture Frames","https://www.amazon.com/Malden-International-Designs-Concept-Picture/dp/B007K1QBRS"],
]

        for url in urls:
            try:
                #req = scrapy.Request(url[3] , headers={ 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Cache-Control': 'max-age=0' },callback=self.parse6)
                req = scrapy.Request(url[2] , headers={'Origin': 'https://www.amazon.com' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36' , 'Accept': '*/*' , 'Referer': 'https://www.amazon.com/' , 'X-Requested-With': 'XMLHttpRequest' , 'Connection': 'keep-alive' , 'Content-Length': '0'}, callback=self.parse6)
                #req = scrapy.Request(url[2] , callback=self.parse6)
                req.meta['product_id']=url[0]
                #req.meta['brand']=url[1]
                req.meta['category']=url[1]
                req.cookies = { 'x-wl-uid':'1y8ltVLwKU/L4uHVRT4wcyu32QxGmsLap3PS10lHQ8I4lHwvcV3mdItRxlTQQbVCy6hcltYxKLMM=', 's_nr':'1498670542228-New', 's_vnum':'1930670542228%26vn%3D1', 's_dslv':'1498670542232','amznacsleftnav-ac35e287-d67e-4607-a950-5d9ffd0c2ca9':'1', 'x-amz-captcha-1':'1499054178128406', 'x-amz-captcha-2':'f44Jo5PiWFZO/J2o05Otig==', 'session-token':'jmS4MZ+87cNOfytK07tpUCEGti+GXuHdZ0oZyPtYqY7t0jdykH+Ub7kXBm+uyaqfsw9okzU8c7KFuF577LQSOEOVzXGU6Ky1xqdZjaFUDfW6H5HbFByM0YxhwaB/i3TdgWzWRV7hvGo3qygmjkrIJ3ESRIOOM6YB4EJWL65CQUTq+Cp4ORjO1XQaGvfPERmPKJ8tKI4p77AQ0pKocXEOtyFku2Vp9HJzTUI9LN4bZVnXVtkV/ra/ElaVLqz1HqDJ', 'csm-hit':'s-GZBERSD0R10VXC0HBQZ6|1500714195597', 'session-id-time':'2082754801l', 'session-id':'261-2325209-6209161', 'ubid-acbde':'259-4651163-1859124' }
                #req.cookies = {'lc-main':'en_US', 's_nr':'1503816974090-New', 's_vnum':'1935816974090%26vn%3D1', 's_dslv':'1503816974091', 'x-main':'pHlb3N0WUwENeYPsqI@jzfF7PXLCCMcJSFiGwcdKfrlzzhc8yQR4kOovInsAXJRe', 'at-main':'Atza|IwEBIF45RJQgsZLrUGO7JaJnp1uVC-RDIfDCqwjV0PeKEDcSIP7e0Pvcm_n-R4iCtwyo7zXH7KLDakbXVsW-9UevBLsZEeSIH2YZJFCjQqDsNAySplN1BcQ1tUj5kmj24vddIVYyi7vx3S0B-tkr9EISA5O5_d5Tr--5JO2qiruKCKawd1MLIyk8KFGS2KdQJGW9wwb9fJf6C7Fk4_7UiW5C3D1DLeuP3VXdar3-_S3yvGXRindK-xRNl3O_YFLRo-a_yn9_Z1V8vNj6kvWgzui_fOIRGrsI9qCHAJpcpt5Nh4Ta5n6-ALqNPkS-zbWlmMkZMgWsZb5EwLk8qr5O_FUA9Be8bqkneub7AuYy2QcvE01rYqkAKgAm4QKR5MSCXDQg8Fquyibqt_a3TRBYXTOzPnoedkm7JdBsUtVGYs4TBNssF4KGFefA1cQRLvxAhHfZe58', 'x-wl-uid':'1QBgT0TBwoj9RQ+QP7eh8ocBTABgs1739+rzq1e3s1iwjoSRYnMpbAczaaknzT2id2ww9iSyiyXd3OQeaJ9Nm9xZrZOKqXNWIDJihS4V7CV+xlp+PQA7T/ILJyNBZ15so9XvNPTzCBQA=', 'session-token':'qLl3vjnjOse5+Cy5cC+3OlMT95d5wVC4bWvaoAbqyhOetjeYqWP24HhMNHJI9Ni3Y7rljL1VdkRzXeolkaGJX8cPCh2P8OzRCIL3t4dynzdXlADAwNZxyWK1BFxTvyUzw4CXSHIeNdq1l95h3SbsLhG4gOhSf5JLHUzfx9dKziC4SpGUaTP+/8VbIE886Ipz6wOjM1J1YwP4lwLQABPJPh/qNzYZWgWTmLW2sk2bkN1nGCJk9XWAoIA2ClwvqPRRIFg8mbX73GFXkSCPmdboKQ==', 'csm-hit':'HCCNKDAR5Q931G1FR5S1+s-HCCNKDAR5Q931G1FR5S1|1504589304054', 'ubid-main':'151-8001146-5395566', 'session-id-time':'2082787201l', 'session-id':'151-4943311-4733238'}
                #req.cookies ={'lc-main':'en_US', 's_nr':'1503816974090-New', 's_vnum':'1935816974090%26vn%3D1', 's_dslv':'1503816974091', 'x-main':'pHlb3N0WUwENeYPsqI@jzfF7PXLCCMcJSFiGwcdKfrlzzhc8yQR4kOovInsAXJRe', 'at-main':'Atza|IwEBIF45RJQgsZLrUGO7JaJnp1uVC-RDIfDCqwjV0PeKEDcSIP7e0Pvcm_n-R4iCtwyo7zXH7KLDakbXVsW-9UevBLsZEeSIH2YZJFCjQqDsNAySplN1BcQ1tUj5kmj24vddIVYyi7vx3S0B-tkr9EISA5O5_d5Tr--5JO2qiruKCKawd1MLIyk8KFGS2KdQJGW9wwb9fJf6C7Fk4_7UiW5C3D1DLeuP3VXdar3-_S3yvGXRindK-xRNl3O_YFLRo-a_yn9_Z1V8vNj6kvWgzui_fOIRGrsI9qCHAJpcpt5Nh4Ta5n6-ALqNPkS-zbWlmMkZMgWsZb5EwLk8qr5O_FUA9Be8bqkneub7AuYy2QcvE01rYqkAKgAm4QKR5MSCXDQg8Fquyibqt_a3TRBYXTOzPnoedkm7JdBsUtVGYs4TBNssF4KGFefA1cQRLvxAhHfZe58', 'x-wl-uid':'1QBgT0TBwoj9RQ+QP7eh8ocBTABgs1739+rzq1e3s1iwjoSRYnMpbAczaaknzT2id2ww9iSyiyXd3OQeaJ9Nm9xZrZOKqXNWIDJihS4V7CV+xlp+PQA7T/ILJyNBZ15so9XvNPTzCBQA=', 'x-amz-captcha-1':'1511784189246059', 'x-amz-captcha-2':'e+dIUFBcjimZCAzt1M7ENg==', 'session-token':'PyjCayhcDu7hHhYCfKE/HuBCBEOaahuY6CNwnoivzMed8qr0ZHDCUZ3JfJ2TRWZ5olesRRksGz+JukvNjXuAoGXc4BmeNH3JY9a7RAUFZ+JNXc3QdXMHK4mlTxF1/pnsFXg7mjivPGJE7qp7fcEexjQd2AE+QWjUanCL+3J3hlClu6GB212X/erRr/WVWf7LDVf3SmANI5rBx2spX6tqui9km7LBf+FKzhyPYARgj2C4728rqinQmeIdKFuJ5OQGHqOLhePWXsLrmry0f5DXow==', 'csm-hit':'%7B%22tb%22%3A%22s-40H2SRFEWW3KSNRY3K5G%7C1512035962489%22%2C%22adb%22%3A%22adblk_no%22%7D', 'ubid-main':'151-8001146-5395566', 'session-id-time':'2082787201l', 'session-id':'151-4943311-4733238'}
                if url[0] not in urls_done: 
                    yield req
                    time.sleep(.1)
            except: raise
        #print "URLS_DONE : ",urls_done


    def parse6(self,response):
        item=ComapreItem()
        asin=""
        featurelist=response.xpath('//*[@id="detailBullets_feature_div"]/ul/li')
        for features in featurelist:
            if "".join(features.xpath('span/span[1]/text()').extract()).find('ASIN') > -1:
                asin=features.xpath('span/span[2]/text()').extract()
                item['asin']=asin[0]
        if asin == "":
            featurelist1=response.xpath('//*[@id="prodDetails"]/div[2]/div[2]/div[1]/div[2]/div/div/table/tbody/tr')
            for features in featurelist1:
                if "".join(features.xpath('td[1]/text()').extract()).find('ASIN') > -1:
                    asin=features.xpath('td[2]/text()').extract()
                    item['asin']=asin[0]
        if asin == "":
            featurelist2=response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div/table/tbody/tr')
            for features in featurelist2:
                if "".join(features.xpath('td[1]/text()').extract()).find('ASIN') > -1:
                    asin=features.xpath('td[2]/text()').extract()
                    item['asin']=asin[0]
        if asin == "":
            featurelist2=response.xpath('//table[@id="productDetails_detailBullets_sections1"]/tr')
            for features in featurelist2:
                if "".join(features.xpath('th/text()').extract()).find('ASIN') > -1:
                    asin=features.xpath('td/text()').extract()
                    item['asin']=asin[0].replace(" ","").replace("\n","")
        if asin == "":
            featurelist2=response.xpath('//*[@id="prodDetails"]/div/div[2]/div[1]/div[2]/div/div/table/tbody/tr')
            for features in featurelist2:
                if "".join(features.xpath('td[1]/text()').extract()).find('ASIN') > -1:
                    asin=features.xpath('td[2]/text()').extract()
                    item['asin']=asin[0].replace(" ","").replace("\n","")

        #item['brand']=response.meta['brand']
        item['category']=response.meta['category']
        item['response_url']=response.url

        item['product_id']=response.meta['product_id']
        yield item