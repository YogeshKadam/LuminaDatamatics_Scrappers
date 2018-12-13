#Amazon seller list spider
import time
import scrapy
class XoroItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    #breadcrumb = scrapy.Field()
    category = scrapy.Field()
	
    

class Spider(scrapy.Spider):
    
    name = "xoro"
    allowed_domain=[]
    #start_urls = ['http://www.fnwerkzeuge.de/akkugeraete.html']
    start_urls = ['https://www.zoro.de/garten-forst-landschaft/elektro-gartengerate']

    def parse(self, response):
        #urls = 'https://www.zoro.de/garten-forst-landschaft/elektro-gartengerate'
        #req = scrapy.Request(urls, headers={'Accept-Encoding': 'gzip, deflate, sdch, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' , 'Cache-Control': 'max-age=0' , 'Connection': 'keep-alive'},callback=self.parse1)
        #yield req
        #print "NAME : ",response.xpath('//*[@id="content-main"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/a/text()').extract()
        categoryurllist=response.xpath('//*[@id="content-filter"]/div/div[1]/div/div/ul/li/ul/li')
        #//*[@id="content-filter"]/div/div[1]/div/div/ul/li/div/a
        if len(categoryurllist)>0:
            for categoryurls in categoryurllist:
                item=XoroItem()
                categoryurl= categoryurls.xpath('a/@href').extract()
                #print categoryurl
                category=categoryurls.xpath('a/text()').extract()
                #print category
                item['category']=("".join(category)).replace("\n","").replace(" ","")
                item['url']=response.url
                yield item
                req=scrapy.Request(categoryurl[0],callback=self.parse)
                yield req
        #elif len(categoryurllist) == 0: