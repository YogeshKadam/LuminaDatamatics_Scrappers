



#Amazon seller list spider
import time
import scrapy
import json
    
	
	
class ZwItem(scrapy.Item):
    categoryurl=scrapy.Field()


class ZwSpider(scrapy.Spider):
    
    name = "zw_categoryurls"
    allowed_domain=[]
    start_urls = ['https://www.zweiradteile.net/']
    #start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ['https://www.amazon.com/musical-instruments-accessories-sound-recording/b/ref=nav_shopall_mi_ce?ie=UTF8&node=11091801']
    
    

    def parse(self, response):
        categorylist=response.xpath('//*[@class="navigation--list-wrapper  is--open"]/ul/li')
        for categories in categorylist:
            category=categories.xpath('a/@href').extract()
            item=ZwItem()
            item['categoryurl']=category
            yield item