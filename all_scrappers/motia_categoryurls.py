



#Amazon seller list spider
import time
import scrapy
import json
    
	
	
class MotiaItem(scrapy.Item):
    categoryurl=scrapy.Field()


class MotiaSpider(scrapy.Spider):
    
    name = "motia_categoryurls"
    allowed_domain=[]
    start_urls = ['http://www.motea.com/']
    #start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ['https://www.amazon.com/musical-instruments-accessories-sound-recording/b/ref=nav_shopall_mi_ce?ie=UTF8&node=11091801']
    
    

    def parse(self, response):
        categorylist=response.xpath('//*[@id="ctl31_ctl00_ulCategories"]/li')
        for categories in categorylist:
            category=categories.xpath('a/@href').extract()
            item=MotiaItem()
            item['categoryurl']=category
            yield item