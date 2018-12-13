# -*- coding: utf-8 -*-
import scrapy
import urllib

import os
import time
import re
import json

class AmazonItems(scrapy.Item):
    titleurl = scrapy.Field()
    mainurl = scrapy.Field()
    category = scrapy.Field()
    department = scrapy.Field()
    position = scrapy.Field()
    page_id = scrapy.Field()


class amazonSpider(scrapy.Spider):
    imgcount = 1
    name = "amz_bestsellers_producturls_22-03-2018"
    allowed_domains = []

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]  

    def parse(self,response):
        urls_done = [
"page_id",
"2",
"3",
"2084",
"2098",
"2086",
"2088",
"2092",
"2081",
"2093",
"2076",
"2082",
"2083",
"2074",
"2073",
"2072",
"2078",
"2075",
"2071",
"2070",
"2066",
"2067",
"2069",
"2063",
"2080",
"2065",
"2064",
"2053",
"2062",
"2044",
"2056",
"2052",
"2043",
"2040",
"2051",
"2061",
"2042",
"2041",
"2034",
"2033",
"2037",
]
        urls=[
["1","Appliances","Appliances","https://www.amazon.com/Best-Sellers-Appliances/zgbs/appliances/ref=zg_bs_nav_0?pg=1&ajax=1"],
["2","Appliances","Appliances","https://www.amazon.com/Best-Sellers-Appliances/zgbs/appliances/ref=zg_bs_nav_0?pg=2&ajax=1"],
["3","Appliances","Appliances","https://www.amazon.com/Best-Sellers-Appliances/zgbs/appliances/ref=zg_bs_nav_0?pg=3&ajax=1"],
["4","Appliances","Appliances","https://www.amazon.com/Best-Sellers-Appliances/zgbs/appliances/ref=zg_bs_nav_0?pg=4&ajax=1"],
["5","Appliances","Appliances","https://www.amazon.com/Best-Sellers-Appliances/zgbs/appliances/ref=zg_bs_nav_0?pg=5&ajax=1"],
["6","Wine Cellars","Appliances","https://www.amazon.com/Best-Sellers-Appliances-Wine-Cellars/zgbs/appliances/3741521/ref=zg_bs_nav_la_1_la?pg=1&ajax=1"],
["7","Wine Cellars","Appliances","https://www.amazon.com/Best-Sellers-Appliances-Wine-Cellars/zgbs/appliances/3741521/ref=zg_bs_nav_la_1_la?pg=2&ajax=1"],
["8","Wine Cellars","Appliances","https://www.amazon.com/Best-Sellers-Appliances-Wine-Cellars/zgbs/appliances/3741521/ref=zg_bs_nav_la_1_la?pg=3&ajax=1"],
["9","Wine Cellars","Appliances","https://www.amazon.com/Best-Sellers-Appliances-Wine-Cellars/zgbs/appliances/3741521/ref=zg_bs_nav_la_1_la?pg=4&ajax=1"],
["10","Wine Cellars","Appliances","https://www.amazon.com/Best-Sellers-Appliances-Wine-Cellars/zgbs/appliances/3741521/ref=zg_bs_nav_la_1_la?pg=5&ajax=1"],
]

        for url in urls:
            try:
                req = scrapy.Request( url[3] , callback=self.parse1, meta={"page_id":url[0] ,"category":url[1], "department":url[2]})
                #print url[0]
                #req.meta['item_id']=url[1]
                #req.meta['product_id']=url[0]
                #req.cookies = { 'x-wl-uid':'1y8ltVLwKU/L4uHVRT4wcyu32QxGmsLap3PS10lHQ8I4lHwvcV3mdItRxlTQQbVCy6hcltYxKLMM=', 's_nr':'1498670542228-New', 's_vnum':'1930670542228%26vn%3D1', 's_dslv':'1498670542232','amznacsleftnav-ac35e287-d67e-4607-a950-5d9ffd0c2ca9':'1', 'x-amz-captcha-1':'1499054178128406', 'x-amz-captcha-2':'f44Jo5PiWFZO/J2o05Otig==', 'session-token':'jmS4MZ+87cNOfytK07tpUCEGti+GXuHdZ0oZyPtYqY7t0jdykH+Ub7kXBm+uyaqfsw9okzU8c7KFuF577LQSOEOVzXGU6Ky1xqdZjaFUDfW6H5HbFByM0YxhwaB/i3TdgWzWRV7hvGo3qygmjkrIJ3ESRIOOM6YB4EJWL65CQUTq+Cp4ORjO1XQaGvfPERmPKJ8tKI4p77AQ0pKocXEOtyFku2Vp9HJzTUI9LN4bZVnXVtkV/ra/ElaVLqz1HqDJ', 'csm-hit':'s-GZBERSD0R10VXC0HBQZ6|1500714195597', 'session-id-time':'2082754801l', 'session-id':'261-2325209-6209161', 'ubid-acbde':'259-4651163-1859124' }
                #req.cookies = {'lc-main':'en_US', 's_nr':'1503816974090-New', 's_vnum':'1935816974090%26vn%3D1', 's_dslv':'1503816974091', 'x-main':'pHlb3N0WUwENeYPsqI@jzfF7PXLCCMcJSFiGwcdKfrlzzhc8yQR4kOovInsAXJRe', 'at-main':'Atza|IwEBIF45RJQgsZLrUGO7JaJnp1uVC-RDIfDCqwjV0PeKEDcSIP7e0Pvcm_n-R4iCtwyo7zXH7KLDakbXVsW-9UevBLsZEeSIH2YZJFCjQqDsNAySplN1BcQ1tUj5kmj24vddIVYyi7vx3S0B-tkr9EISA5O5_d5Tr--5JO2qiruKCKawd1MLIyk8KFGS2KdQJGW9wwb9fJf6C7Fk4_7UiW5C3D1DLeuP3VXdar3-_S3yvGXRindK-xRNl3O_YFLRo-a_yn9_Z1V8vNj6kvWgzui_fOIRGrsI9qCHAJpcpt5Nh4Ta5n6-ALqNPkS-zbWlmMkZMgWsZb5EwLk8qr5O_FUA9Be8bqkneub7AuYy2QcvE01rYqkAKgAm4QKR5MSCXDQg8Fquyibqt_a3TRBYXTOzPnoedkm7JdBsUtVGYs4TBNssF4KGFefA1cQRLvxAhHfZe58', 'x-wl-uid':'1QBgT0TBwoj9RQ+QP7eh8ocBTABgs1739+rzq1e3s1iwjoSRYnMpbAczaaknzT2id2ww9iSyiyXd3OQeaJ9Nm9xZrZOKqXNWIDJihS4V7CV+xlp+PQA7T/ILJyNBZ15so9XvNPTzCBQA=', 'session-token':'qLl3vjnjOse5+Cy5cC+3OlMT95d5wVC4bWvaoAbqyhOetjeYqWP24HhMNHJI9Ni3Y7rljL1VdkRzXeolkaGJX8cPCh2P8OzRCIL3t4dynzdXlADAwNZxyWK1BFxTvyUzw4CXSHIeNdq1l95h3SbsLhG4gOhSf5JLHUzfx9dKziC4SpGUaTP+/8VbIE886Ipz6wOjM1J1YwP4lwLQABPJPh/qNzYZWgWTmLW2sk2bkN1nGCJk9XWAoIA2ClwvqPRRIFg8mbX73GFXkSCPmdboKQ==', 'csm-hit':'HCCNKDAR5Q931G1FR5S1+s-HCCNKDAR5Q931G1FR5S1|1504589304054', 'ubid-main':'151-8001146-5395566', 'session-id-time':'2082787201l', 'session-id':'151-4943311-4733238'}
                if url[0] not in urls_done: 
                    yield req
                    time.sleep(.1)
            except: raise
        #print "URLS_DONE : ",urls_done


    def parse1(self,response):
        titleurlslist=response.xpath('//div[@class="zg_itemImmersion"]')
        for titleurls in titleurlslist:
            titleurl=titleurls.xpath('div[2]/div/a/@href').extract()
            position=titleurls.xpath('div[1]/span/text()').extract()
            item=AmazonItems()
            item['titleurl']="https://www.amazon.com"+titleurl[0]
            item['mainurl']=response.url
            item['position']=position[0].replace("\n","").replace(" ","")
            item['category']=response.meta["category"]
            item['department']=response.meta["department"]
            item['page_id']=response.meta["page_id"]
            yield item