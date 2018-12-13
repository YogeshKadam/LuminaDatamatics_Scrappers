



#Amazon seller list spider
import time
import scrapy
import json
    
	
	
class ZietechItem(scrapy.Item):
    categoryurl=scrapy.Field()


class ZietechSpider(scrapy.Spider):
    
    name = "zietech_categoryurls"
    allowed_domain=[]
    start_urls = ['http://www.zietech.de/?UseLayout=zietech_desktop_new']
    #start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ['https://www.amazon.com/musical-instruments-accessories-sound-recording/b/ref=nav_shopall_mi_ce?ie=UTF8&node=11091801']
    
    

    def parse(self, response):
        urls=[
'http://www.zietech.de/motorrad-teile/',
'http://www.zietech.de/scooter-teile/',
'http://www.zietech.de/auto-teile/',
'http://www.zietech.de/sonderangebote/',
]
        
        for url in urls:
            try:
                req = scrapy.Request( url , callback=self.parse1)
                yield req
            
            except: raise
        """categorylist=response.xpath('//*[@id="main_nav"]/li')
        for categories in categorylist:
            category=categories.xpath('a/@href').extract()[0]
            item=BtItem()
            item['categoryurl']=category
            yield item
            #req = scrapy.Request( category, callback=self.parse1)
            #yield req"""
			
			
    def parse1(self, response):
        categorylist=response.xpath('//*[@id="mainmiddle"]/div[3]/div/ul/li')
        if not categorylist: categorylist=response.xpath('//*[@id="mainmiddle"]/div[5]/div/ul/li')
        #print "LENGTH : ",len(categorylist)
        if len(categorylist)>0:
            for categories in categorylist:
                category=categories.xpath('a/@href').extract()[0]
                #print "CATEGORY : ",category
                try:
                    req = scrapy.Request( category , callback=self.parse1)
                    yield req
            
                except: raise
				
        elif len(categorylist) == 0:
            item =ZietechItem()
            item['categoryurl']=response.url
            yield item
			
			