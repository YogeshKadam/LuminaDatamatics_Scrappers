

#Amazon seller list spider
import time
import scrapy
import json
import demjson
from scrapy.http import FormRequest
import requests
from lxml import etree, html
from StringIO import StringIO
class AsinItem(scrapy.Item):
    # define the fields for your item here like:
    asin = scrapy.Field()
    ean = scrapy.Field()
    

class Spider(scrapy.Spider):
    
    name = "jurisquare_ajax"
    allowed_domain=[]
    start_urls = ['https://www.flipkart.com/search?q=9780005996218']
    handle_httpstatus_list = [302]

    def parse(self,response):
        asins_done=[]
        asins=['https://www.jurisquare.be/en/index.html']
        for asin in asins:
            #req = FormRequest(ajaxurl, method='POST', formdata=frmdata, callback=self.parse4 ,headers={'origin': 'https://www.erwinmayer.com' , 'accept-encoding': 'gzip, deflate, br' , 'x-requested-with': 'XMLHttpRequest' , 'accept-language': 'en-US,en;q=0.8' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' , 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8' , 'accept': '*/*' , 'referer': 'https://www.erwinmayer.com/emlabs/asin2ean/' , 'authority': 'www.erwinmayer.com'}, meta={'asin':asin} )
            req = FormRequest(asin, callback=self.parse4)
            #req.cookies ={'__cfduid':'d0b5f40a702bc1d7ebabeea906f5d2ff01505481988', 'qtrans_front_language':'en', '_gat':'1', '_ga':'GA1.2.971994258.1505481935', '_gid':'GA1.2.1957159615.1505712306'}
            if asin not in asins_done:
                yield req
                #time.sleep(.3)

            
    def parse4(self,response):
        list1=["https://www.jurisquare.be/en/"+x for x in response.xpath('//*[@id="banner"]/div[2]/div/div/a/@href').extract()]
        print list1
        for ind,li in enumerate(list1):
            print ind
            req = FormRequest(li, callback=self.parse5)
            yield req
			
			
    def parse5(self,response):
        #list1=["https://www.jurisquare.be/en/"+x for x in response.xpath('//*[@id="banner"]/div[2]/div/div/a/@href').extract()]
        print response.body