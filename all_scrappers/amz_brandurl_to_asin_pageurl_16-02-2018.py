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
    pageurl = scrapy.Field()
    category = scrapy.Field()



class amazonSpider(scrapy.Spider):
    imgcount = 1
    name = "amz_brandurl_to_asin_pageurl_16-02-2018"
    allowed_domains = []

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]  

    def parse(self,response):
        urls_done = []
        urls=[
#["iRobot","Home & Kitchen","https://www.amazon.com/s/ref=sr_in_i_p_89_1?fst=as%3Aoff&rh=n%3A1055398%2Ck%3AiRobot%2Cp_89%3AiRobot&bbn=1055398&keywords=iRobot&ie=UTF8&qid=1518577594&rnid=2528832011"]
["Business Envelopes","https://www.amazon.com/s/ref=lp_1069694_nr_n_1?fst=as%3Aoff&rh=n%3A1064954%2Cn%3A%211084128%2Cn%3A1069242%2Cn%3A1068972%2Cn%3A1069694%2Cn%3A1069696&bbn=1069694&ie=UTF8&qid=1518678075&rnid=1069694"],
["Clasp Envelopes","https://www.amazon.com/s/ref=lp_1069694_nr_n_2?fst=as%3Aoff&rh=n%3A1064954%2Cn%3A%211084128%2Cn%3A1069242%2Cn%3A1068972%2Cn%3A1069694%2Cn%3A490800011&bbn=1069694&ie=UTF8&qid=1518678075&rnid=1069694"],
["Coin & Small Parts Envelopes","https://www.amazon.com/s/ref=lp_1069694_nr_n_3?fst=as%3Aoff&rh=n%3A1064954%2Cn%3A%211084128%2Cn%3A1069242%2Cn%3A1068972%2Cn%3A1069694%2Cn%3A490801011&bbn=1069694&ie=UTF8&qid=1518678075&rnid=1069694"],
["Coin Envelopes","https://www.amazon.com/s/ref=lp_490801011_nr_n_0?fst=as%3Aoff&rh=n%3A1064954%2Cn%3A%211084128%2Cn%3A1069242%2Cn%3A1068972%2Cn%3A1069694%2Cn%3A490801011%2Cn%3A705327011&bbn=490801011&ie=UTF8&qid=1518678474&rnid=490801011"],
["Small Parts Envelopes","https://www.amazon.com/s/ref=lp_490801011_nr_n_1?fst=as%3Aoff&rh=n%3A1064954%2Cn%3A%211084128%2Cn%3A1069242%2Cn%3A1068972%2Cn%3A1069694%2Cn%3A490801011%2Cn%3A705328011&bbn=490801011&ie=UTF8&qid=1518678474&rnid=490801011"],
["Expansion & Jumbo Envelopes","https://www.amazon.com/s/ref=lp_1069694_nr_n_4?fst=as%3Aoff&rh=n%3A1064954%2Cn%3A%211084128%2Cn%3A1069242%2Cn%3A1068972%2Cn%3A1069694%2Cn%3A1069700&bbn=1069694&ie=UTF8&qid=1518678075&rnid=1069694"],
["Filing Envelopes","https://www.amazon.com/s/ref=lp_1069694_nr_n_5?fst=as%3Aoff&rh=n%3A1064954%2Cn%3A%211084128%2Cn%3A1069242%2Cn%3A1068972%2Cn%3A1069694%2Cn%3A490802011&bbn=1069694&ie=UTF8&qid=1518678075&rnid=1069694"],
["Forms & Check Envelopes","https://www.amazon.com/s/ref=lp_1069694_nr_n_6?fst=as%3Aoff&rh=n%3A1064954%2Cn%3A%211084128%2Cn%3A1069242%2Cn%3A1068972%2Cn%3A1069694%2Cn%3A490803011&bbn=1069694&ie=UTF8&qid=1518678075&rnid=1069694"],
["Greeting Card Envelopes","https://www.amazon.com/s/ref=lp_1069694_nr_n_7?fst=as%3Aoff&rh=n%3A1064954%2Cn%3A%211084128%2Cn%3A1069242%2Cn%3A1068972%2Cn%3A1069694%2Cn%3A490804011&bbn=1069694&ie=UTF8&qid=1518678075&rnid=1069694"],
["Interoffice & Routing Envelopes","https://www.amazon.com/s/ref=lp_1069694_nr_n_8?fst=as%3Aoff&rh=n%3A1064954%2Cn%3A%211084128%2Cn%3A1069242%2Cn%3A1068972%2Cn%3A1069694%2Cn%3A1069698&bbn=1069694&ie=UTF8&qid=1518678075&rnid=1069694"],
["Legal Envelopes","https://www.amazon.com/s/ref=lp_1069694_nr_n_9?fst=as%3Aoff&rh=n%3A1064954%2Cn%3A%211084128%2Cn%3A1069242%2Cn%3A1068972%2Cn%3A1069694%2Cn%3A490805011&bbn=1069694&ie=UTF8&qid=1518678075&rnid=1069694"],
["Packing List Envelopes","https://www.amazon.com/s/ref=lp_1069694_nr_n_10?fst=as%3Aoff&rh=n%3A1064954%2Cn%3A%211084128%2Cn%3A1069242%2Cn%3A1068972%2Cn%3A1069694%2Cn%3A490806011&bbn=1069694&ie=UTF8&qid=1518678075&rnid=1069694"],
["Pay & Expense Envelopes","https://www.amazon.com/s/ref=lp_1069694_nr_n_11?fst=as%3Aoff&rh=n%3A1064954%2Cn%3A%211084128%2Cn%3A1069242%2Cn%3A1068972%2Cn%3A1069694%2Cn%3A490807011&bbn=1069694&ie=UTF8&qid=1518678075&rnid=1069694"],
]

        for url in urls:
            try:
                req = scrapy.Request(url[1] , headers={ 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Cache-Control': 'max-age=0' },callback=self.parse6)
                #req.meta['brand']=url[0]
                req.meta['category']=url[0]
                req.cookies = { 'x-wl-uid':'1y8ltVLwKU/L4uHVRT4wcyu32QxGmsLap3PS10lHQ8I4lHwvcV3mdItRxlTQQbVCy6hcltYxKLMM=', 's_nr':'1498670542228-New', 's_vnum':'1930670542228%26vn%3D1', 's_dslv':'1498670542232','amznacsleftnav-ac35e287-d67e-4607-a950-5d9ffd0c2ca9':'1', 'x-amz-captcha-1':'1499054178128406', 'x-amz-captcha-2':'f44Jo5PiWFZO/J2o05Otig==', 'session-token':'jmS4MZ+87cNOfytK07tpUCEGti+GXuHdZ0oZyPtYqY7t0jdykH+Ub7kXBm+uyaqfsw9okzU8c7KFuF577LQSOEOVzXGU6Ky1xqdZjaFUDfW6H5HbFByM0YxhwaB/i3TdgWzWRV7hvGo3qygmjkrIJ3ESRIOOM6YB4EJWL65CQUTq+Cp4ORjO1XQaGvfPERmPKJ8tKI4p77AQ0pKocXEOtyFku2Vp9HJzTUI9LN4bZVnXVtkV/ra/ElaVLqz1HqDJ', 'csm-hit':'s-GZBERSD0R10VXC0HBQZ6|1500714195597', 'session-id-time':'2082754801l', 'session-id':'261-2325209-6209161', 'ubid-acbde':'259-4651163-1859124' }
                #req.cookies = {'lc-main':'en_US', 's_nr':'1503816974090-New', 's_vnum':'1935816974090%26vn%3D1', 's_dslv':'1503816974091', 'x-main':'pHlb3N0WUwENeYPsqI@jzfF7PXLCCMcJSFiGwcdKfrlzzhc8yQR4kOovInsAXJRe', 'at-main':'Atza|IwEBIF45RJQgsZLrUGO7JaJnp1uVC-RDIfDCqwjV0PeKEDcSIP7e0Pvcm_n-R4iCtwyo7zXH7KLDakbXVsW-9UevBLsZEeSIH2YZJFCjQqDsNAySplN1BcQ1tUj5kmj24vddIVYyi7vx3S0B-tkr9EISA5O5_d5Tr--5JO2qiruKCKawd1MLIyk8KFGS2KdQJGW9wwb9fJf6C7Fk4_7UiW5C3D1DLeuP3VXdar3-_S3yvGXRindK-xRNl3O_YFLRo-a_yn9_Z1V8vNj6kvWgzui_fOIRGrsI9qCHAJpcpt5Nh4Ta5n6-ALqNPkS-zbWlmMkZMgWsZb5EwLk8qr5O_FUA9Be8bqkneub7AuYy2QcvE01rYqkAKgAm4QKR5MSCXDQg8Fquyibqt_a3TRBYXTOzPnoedkm7JdBsUtVGYs4TBNssF4KGFefA1cQRLvxAhHfZe58', 'x-wl-uid':'1QBgT0TBwoj9RQ+QP7eh8ocBTABgs1739+rzq1e3s1iwjoSRYnMpbAczaaknzT2id2ww9iSyiyXd3OQeaJ9Nm9xZrZOKqXNWIDJihS4V7CV+xlp+PQA7T/ILJyNBZ15so9XvNPTzCBQA=', 'session-token':'qLl3vjnjOse5+Cy5cC+3OlMT95d5wVC4bWvaoAbqyhOetjeYqWP24HhMNHJI9Ni3Y7rljL1VdkRzXeolkaGJX8cPCh2P8OzRCIL3t4dynzdXlADAwNZxyWK1BFxTvyUzw4CXSHIeNdq1l95h3SbsLhG4gOhSf5JLHUzfx9dKziC4SpGUaTP+/8VbIE886Ipz6wOjM1J1YwP4lwLQABPJPh/qNzYZWgWTmLW2sk2bkN1nGCJk9XWAoIA2ClwvqPRRIFg8mbX73GFXkSCPmdboKQ==', 'csm-hit':'HCCNKDAR5Q931G1FR5S1+s-HCCNKDAR5Q931G1FR5S1|1504589304054', 'ubid-main':'151-8001146-5395566', 'session-id-time':'2082787201l', 'session-id':'151-4943311-4733238'}
                if url[1] not in urls_done: 
                    yield req
                    time.sleep(.1)
            except: raise
        #print "URLS_DONE : ",urls_done


    def parse6(self,response):
        try:
            totalcount="".join(response.xpath('//*[@id="s-result-count"]/text()').extract()).split('of')[1].replace(' ','').replace('resultsfor','').replace('over','').replace(',','')
        except:
            totalcount="".join(response.xpath('//*[@id="s-result-count"]/text()').extract()).replace(' ','').replace('resultsfor','').replace('resultfor','').replace(',','')
        item=ComapreItem()
        #urlpart="&page="+str(i)
        #item['brand']=response.meta['brand']
        item['category']=response.meta['category']
        item['response_url']=response.url
        item['pageurl']=response.url
        yield item
        totalpages=int(totalcount)/24
        for i in range(2,totalpages+2):
            item=ComapreItem()
            urlpart="&page="+str(i)
            #item['brand']=response.meta['brand']
            item['category']=response.meta['category']
            item['response_url']=response.url
            item['pageurl']=response.url+urlpart
            yield item