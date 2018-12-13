



#Amazon seller list spider
import time
import scrapy
import json
    
	
	
class ZwItem(scrapy.Item):
    categoryurl=scrapy.Field()
    producturl=scrapy.Field()


class ZwSpider(scrapy.Spider):
    
    name = "zw_producturls"
    allowed_domain=[]
    start_urls = ['https://www.zweiradteile.net/']
    #start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ['https://www.amazon.com/musical-instruments-accessories-sound-recording/b/ref=nav_shopall_mi_ce?ie=UTF8&node=11091801']
    
    

    def parse(self, response):
        urls=[
"https://www.zweiradteile.net/sale/",
"https://www.zweiradteile.net/e-bike-chiptuning/",
"https://www.zweiradteile.net/fahrrad-ersatzteile-zubehoer/",
"https://www.zweiradteile.net/auspuffanlagen/",
"https://www.zweiradteile.net/batterien/",
"https://www.zweiradteile.net/ersatz-und-tuning-zylinder/",
"https://www.zweiradteile.net/elektrik/",
"https://www.zweiradteile.net/ersatzteile/",
"https://www.zweiradteile.net/fahrwerk-und-bremsen/",
"https://www.zweiradteile.net/kleidung/",
"https://www.zweiradteile.net/ketten-kettenraeder-und-ritzel/",
"https://www.zweiradteile.net/motorteile/",
"https://www.zweiradteile.net/oele-und-fluessigkeiten/",
"https://www.zweiradteile.net/rahmen-und-anbauteile/",
"https://www.zweiradteile.net/reifen/",
"https://www.zweiradteile.net/zubehoer/",
"https://www.zweiradteile.net/werkzeug/",
]
        
        for url in urls:
            try:
                req = scrapy.Request( url , callback=self.parse1, meta={'main_url': url})
                yield req
            
            except: raise

    def parse1(self, response):
	
        
        #Header1= {'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://uk-motors.de/angebote/' , 'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0'}
        productlist=response.xpath('//*[@class="listing--container"]/div/div')
        for products in productlist:
            producturl= products.xpath('div/div[2]/a[2]/@href').extract()[0]
            item = ZwItem()
            item['categoryurl']=response.url
            item['producturl']=producturl
            yield item
        
        if response.url == response.meta['main_url']:
            totalpages=int(response.xpath('//*[@class="listing-header--count"]/span/text()').extract()[0])/12
            print "No. of pages : ",totalpages
            url=response.meta['main_url']
            
            for i in range(2,totalpages+2):
                urlpart1="?p="+str(i)
                try:
                    req = scrapy.Request( url + urlpart1, callback=self.parse1, meta={'main_url':url})
                    yield req
                except: raise
