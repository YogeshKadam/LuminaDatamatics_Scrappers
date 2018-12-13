

#Amazon seller list spider
import time
import scrapy
class GastroItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    articleno = scrapy.Field()
    price = scrapy.Field()
    url=scrapy.Field()
    brand=scrapy.Field()
    breadcrumb=scrapy.Field()
    description=scrapy.Field()
	
    

class Spider(scrapy.Spider):
    
    name = "gashtro246"
    allowed_domain=[]
    start_urls = ['http://www.gastro24.de/']
    

    def parse(self, response):

        urls_done = []
        
        urls= [["1","http://www.gastro24.de/Einkammer-Pizzaoefen"]]

        for url in urls:
            try:
                req = scrapy.Request(url[1] , callback=self.parse3 , meta={'allpagesdict':{}})
                req.meta['item_id'] = url[0]
                req.meta['req'] = url[1]
                if url[0] not in urls_done: 
                    yield req
                    time.sleep(.3)
            except: raise

    def parse3(self,response):
        titleurllist=response.xpath('//*[@id="outer_wrapper"]/div/div[2]/div[2]/div/div[7]/div[1]/ul/li["list_item list"]')
        #print "LENGTH of titles is : ",len(titlelist)
        for titleurls in titleurllist:
            
            titlesuburl=titleurls.xpath('div/div[1]/a/@href').extract()
            #print title
            if titlesuburl:
                titleurl="http://www.gastro24.de/"+titlesuburl[0]
                #print "TITLEURL IS : ",titleurl
                try:
                    req = scrapy.Request(titleurl,callback=self.parse4)
                    yield req
                    #time.sleep(.3)
                except : raise
				
            else:
                pass
        
			
        print "AFTER YIELD STATEMENT"
        allpagesdict1=response.meta['allpagesdict']
        #print "ALLPAGESDICT : ",allpagesdict
        allpageslist=response.xpath('//*[@id="outer_wrapper"]/div/div[2]/div[2]/div/div[6]/div[1]/div/span[2]/ul/li')
 
        for page in allpageslist:
            nextpageurl=page.xpath('a/@href').extract()
            #print "NEXT PAGE URL : ",nextpageurl
            nextpageno=page.xpath('a/text()').extract()
            #print "NEXT PAGE No. : ",nextpageno
          
            if nextpageno in allpagesdict1.keys():
                pass
            else:
                if nextpageurl[0].replace(" ","")=="":
                    #print "SELECTED URL : "
                    allpagesdict1[nextpageno[0]]="selected"
                else:
                    allpagesdict1[nextpageno[0]]=nextpageurl[0]
                    try:
                        req = scrapy.Request(nextpageurl[0],callback=self.parse3,meta={'allpagesdict':allpagesdict1})
                        yield req
                        #time.sleep(.3)
                    except: raise
					
    def parse4(self,response):
        item=GastroItem()
        title=response.xpath('//*[@id="buy_form"]/div/div/div[1]/h1/text()').extract()
        item['title']=("".join(title)).replace("\t","").replace("\n","")
        articleno=response.xpath('//*[@class="gastro_content_box price_box headless"]/li[1]/span/text()').extract()
        #print articleno
        item['articleno']="".join(articleno)
        #cost=response.xpath('//*[@class="gastro_content_box price_box headless"]/li[2]/span[2]/text()').extract()
        cost=response.xpath('//*[@id="buy_form"]/div/div/div[2]/ul[1]/li[4]/span/text()').extract()
        if not cost: cost=response.xpath('//*[@id="buy_form"]/div/div/div[2]/ul[1]/li[5]/span/text()').extract()
        if not cost: cost=response.xpath('//*[@id="buy_form"]/div/div/div[3]/ul[1]/li[4]/span/text()').extract()
        if not cost: cost=response.xpath('//*[@id="buy_form"]/div/div/div[3]/ul[1]/li[4]/span/text()').extract()
        #print cost
        cost1=cost[0].split(":")[1]
        item['price']=cost1.encode('ascii','ignore').replace('.','').replace(',','.').replace(" ","").replace("\n","")
        brand=response.xpath('//*[@id="buy_form"]/div/div/div[1]/div[2]/ul/li[1]/a/@href').extract()
        item['brand']=brand[0]
        item['url']=response.url
        desc=response.xpath('//*[@id="description"]/div//text()').extract()
        item['description']=(",".join(desc)).replace("\n","").replace("\t","")
        breadcrumblist=response.xpath('//*[@id="content"]/div[1]/span/a//text()').extract()
        item['breadcrumb']=">".join(breadcrumblist)
        yield item
		