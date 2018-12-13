



#Amazon seller list spider
import time
import scrapy
import json
    
	
	
class ZietechItem(scrapy.Item):
    categoryurl=scrapy.Field()
    producturl=scrapy.Field()


class ZietechSpider(scrapy.Spider):
    
    name = "zietech_producturls1"
    allowed_domain=[]
    start_urls = ['http://www.zietech.de/?UseLayout=zietech_desktop_new']
    #start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ['https://www.amazon.com/musical-instruments-accessories-sound-recording/b/ref=nav_shopall_mi_ce?ie=UTF8&node=11091801']
    
    

    def parse(self, response):
        urls=[
"http://www.zietech.de/sonderangebote/",
"http://www.zietech.de/scooter-teile/anbauteile/downhill-lenker/",
"http://www.zietech.de/motorrad-teile/zubehoer/schloesser/",
"http://www.zietech.de/motorrad-teile/verschleissteile/zuendung/",
"http://www.zietech.de/motorrad-teile/verschleissteile/zuendkerzen/",
"http://www.zietech.de/motorrad-teile/reise-zubehoer/zubehoer/",
"http://www.zietech.de/motorrad-teile/verschleissteile/wellen-zuege/",
"http://www.zietech.de/scooter-teile/tuning-und-technik/zylinderkits/malaguti/",
"http://www.zietech.de/motorrad-teile/bekleidung/sturmhauben/",
"http://www.zietech.de/scooter-teile/tuning-und-technik/zylinderkits/derbi/",
]
        
        for url in urls:
            try:
                req = scrapy.Request( url , callback=self.parse1)
                yield req
            
            except: raise

    def parse1(self, response):
	
        urlpart="http://www.zietech.de"
        #Header1= {'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://uk-motors.de/angebote/' , 'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0'}
        productlist= response.xpath('//*[@id="container"]/div/div[@id="mainmiddle"]/form')
        for products in productlist:
            producturl= products.xpath('div/div/div[3]/h2/@onclick').extract()[0]
            producturl1=producturl.replace("self.location.href=","").replace("'","")
            item = ZietechItem()
            item['categoryurl']=response.url
            item['producturl']=urlpart+producturl1
            yield item
        
        if response.xpath('//*[@id="mainmiddle"]/div[@class="akurm tl-navigation"]/div[@class="tl-next grey2"]/a/@href').extract():
            #print "No. of pages : ",totalpages
            url=response.xpath('//*[@id="mainmiddle"]/div[@class="akurm tl-navigation"]/div[@class="tl-next grey2"]/a/@href').extract()[0]
            #print "NEXT PAGE URL IS : ",url
            try:
                req = scrapy.Request( url , callback=self.parse1)
                yield req
            except: raise
