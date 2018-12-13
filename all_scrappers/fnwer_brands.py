





#Amazon seller list spider
import time
import scrapy
import json
    
	
	
class FnwerItem(scrapy.Item):
    # define the fields for your item here like:
    brand = scrapy.Field()
    
    
	

class Spider(scrapy.Spider):
    
    name = "fn_brand"
    allowed_domain=[]
    start_urls = ['http://www.fnwerkzeuge.de/']
    #start_urls = ['https://www.amazon.com/musical-instruments-accessories-sound-recording/b/ref=nav_shopall_mi_ce?ie=UTF8&node=11091801']
    
    

    def parse(self, response):

	
        brandlist=response.xpath('//*[@id="main_nav"]/li[13]/ul/li')
        for brands in brandlist:
            item=FnwerItem()
            brand=brands.xpath('a/span/text()').extract()
            item['brand'] = brand[0]
            yield item