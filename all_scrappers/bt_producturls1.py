



#Amazon seller list spider
import time
import scrapy
import json
    
	
	
class BtItem(scrapy.Item):
    categoryurl=scrapy.Field()
    producturl=scrapy.Field()


class BtSpider(scrapy.Spider):
    
    name = "bt_producturls1"
    allowed_domain=[]
    start_urls = ['https://www.biketeile-service.de/']
    #start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ['https://www.amazon.com/musical-instruments-accessories-sound-recording/b/ref=nav_shopall_mi_ce?ie=UTF8&node=11091801']
    
    

    def parse(self, response):
        urls=[
"https://www.biketeile-service.de/en/filtersandaccessories/hydrauliklfilter/",
"https://www.biketeile-service.de/en/sellingaidsandcatalogues/trainingplan/",
"https://www.biketeile-service.de/en/electrics/switchingrelay/",
"https://www.biketeile-service.de/en/rollerscooterteile/zubehoerwerkzeug/zubehoer/",
"https://www.biketeile-service.de/en/rollerscooterteile/zubehoerwerkzeug/werkzeuge/",
"https://www.biketeile-service.de/en/rollerscooterteile/zubehoerwerkzeug/windschilde/",
"https://www.biketeile-service.de/en/wheelandtyre/mowertyres/tyre/-1/-1/",
"https://www.biketeile-service.de/en/wheelandtyre/mowertyres/tyre/-1/",
"https://www.biketeile-service.de/en/wheelandtyre/mowertyres/tubesparts/",
]
        
        for url in urls:
            try:
                req = scrapy.Request( url , callback=self.parse1, meta={'main_url': url})
                yield req
            
            except: raise

    def parse1(self, response):
	
        
        #Header1= {'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://uk-motors.de/angebote/' , 'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0'}
        productlist=response.xpath('//*[@id="sectionpad"]/section/div/div/div[@class="product_box"]')
        for products in productlist:
            producturl= products.xpath('div[2]/h3/a/@href').extract()[0]
            item = BtItem()
            item['categoryurl']=response.url
            item['producturl']=producturl
            yield item
        
        if response.url == response.meta['main_url']:
            totalpages=int(response.xpath('//*[@id="sectionpad"]/section/div/div/div[@class="ac"]/b[3]/text()').extract()[0])/20
            #print "No. of pages : ",totalpages
            url=response.meta['main_url']
            
            for i in range(2,totalpages+2):
                urlpart1="&page="+str(i)
                try:
                    req = scrapy.Request( url + urlpart1, callback=self.parse1, meta={'main_url':url})
                    yield req
                except: raise
