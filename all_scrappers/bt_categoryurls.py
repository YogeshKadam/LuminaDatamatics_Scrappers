



#Amazon seller list spider
import time
import scrapy
import json
    
	
	
class BtItem(scrapy.Item):
    categoryurl=scrapy.Field()


class BtSpider(scrapy.Spider):
    
    name = "bt_categoryurls"
    allowed_domain=[]
    start_urls = ['https://www.biketeile-service.de/']
    #start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ['https://www.amazon.com/musical-instruments-accessories-sound-recording/b/ref=nav_shopall_mi_ce?ie=UTF8&node=11091801']
    
    

    def parse(self, response):
        categorylist=response.xpath('//*[@id="main_nav"]/li')
        for categories in categorylist:
            category=categories.xpath('a/@href').extract()[0]
            item=BtItem()
            item['categoryurl']=category
            yield item
            #req = scrapy.Request( category, callback=self.parse1)
            #yield req
			
			
    def parse1(self, response):
        categorylist=response.xpath('//*[@id="sectionpad"]/section/div/div/div[@class="cat_box"]')
        if len(categorylist)>0:
            for categories in categorylist:
                category=categories.xpath('h3/a/@href').extract()[0]
                #print "CATEGORY : ",category
                try:
                    req = scrapy.Request( category , callback=self.parse1)
                    yield req
            
                except: raise
				
        elif len(categorylist) == 0:
            item =BtItem()
            item['categoryurl']=response.url
            yield item