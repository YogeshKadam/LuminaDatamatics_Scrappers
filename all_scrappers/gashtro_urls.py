#Amazon seller list spider
import time
import scrapy
    
	
	
class GastroItem(scrapy.Item):
    # define the fields for your item here like:
    url=scrapy.Field()
    breadcrumb=scrapy.Field()
    
	

class Spider(scrapy.Spider):
    
    name = "gashtro_url"
    allowed_domain=[]
    #start_urls = ['http://www.gastro24.de/Kuehltechnik-und-Kaeltetechnik']
    #start_urls=['http://www.gastro24.de/Aufschnittmaschinen']
    #start_urls=['http://www.gastro24.de/Cafebedarf-und-Cafezubehoer']
    start_urls=['http://www.gastro24.de/Aufschaeumkannen']
    #start_urls=['http://www.gastro24.de/Grosskuechentechnik']

    
    

    def parse(self, response):
        #print "Current URL : ",response.url
        """
        categorylist=response.xpath('//*[@id="outer_wrapper"]/div/div[2]/div[1]/div/div[1]/div[1]/ul/li/ul/li[10]/ul/li')
        for categories in categorylist:
            #subcategorytext=categories.xpath('@class').extract()
            #print "Sub Category Text : ",subcategorytext
            category=categories.xpath('a/@href').extract()
            url="http://www.gastro24.de/"+category[0]
            print "The URL is : ",url
            try:
                req = scrapy.Request(url,callback=self.parse2)
                yield req
                time.sleep(.3)
            except: raise
        """
        #firstcategoryurl=response.xpath('//*[@id="outer_wrapper"]/div/div[2]/div[1]/div/div[1]/div[1]/ul/li/ul/li[10]/ul/li[1]/a/@href').extract()
        firstcategoryurl=response.xpath('//*[@id="outer_wrapper"]/div/div[2]/div[1]/div/div[1]/div[1]/ul/li/ul/li[1]/a/@href').extract()
        #firstcategoryurl=response.xpath('//*[@id="kk-mega-menu"]/li[8]/a/@href').extract()
        #//*[@id="outer_wrapper"]/div/div[2]/div[1]/div/div[1]/div[1]/ul/li/ul/li[10]/ul/li[1]/a
		#//*[@id="outer_wrapper"]/div/div[2]/div[1]/div/div[1]/div[1]/ul/li/ul/li[4]/ul/li[1]/a
        #//*[@id="outer_wrapper"]/div/div[2]/div[1]/div/div[1]/div[1]/ul/li/ul/li[1]/a
        #firstcategoryurl=response.xpath('//*[@id="outer_wrapper"]/div/div[2]/div[1]/div/div[1]/div[1]/ul/li["node active"]/ul/li[1]/a/@href').extract()
		#//*[@id="outer_wrapper"]/div/div[2]/div[1]/div/div[1]/div[1]/ul/li/ul/li[1]/a
		#//*[@id="outer_wrapper"]/div/div[2]/div[1]/div/div[1]/div[1]/ul/li/ul/li[1]/a/text()
        firsturl="http://www.gastro24.de/"+firstcategoryurl[0]
        print "FirstCategoryURL : ",firsturl
        req = scrapy.Request(firsturl,callback=self.parse3)
        yield req
		
		

    def parse3(self,response):
	
        categorylist=response.xpath('//*[@id="outer_wrapper"]/div/div[2]/div[1]/div/div[1]/div[1]/ul/li/ul/li')
        for categories in categorylist:
            subcategorytext=categories.xpath('@class').extract()
            if subcategorytext[0].replace(" ","").upper()=="NODENO-CHILDREN" or subcategorytext[0].replace(" ","").upper()=="NODENO-CHILDRENACTIVE":
                #print "FOUND"
                #item=GastroItem()
                category=categories.xpath('a/@href').extract()
                url="http://www.gastro24.de/"+category[0]
                item=GastroItem()

                item['url']=url
                item['breadcrumb']="/".join(response.xpath('//*[@id="outer_wrapper"]/div/div[1]/div[1]/div/span/a/text()').extract()).replace("\n","").replace(" ","")
                yield item
            
	
            elif subcategorytext[0].replace(" ","").upper()=="NODEHAS-CHILDREN" or subcategorytext[0].replace(" ","").upper()=="NODEHAS-CHILDRENACTIVE":
                #print "CHILDREN FOUND"
                category=categories.xpath('ul/li')
                for subcategory in category:
                    subcategoryurl=subcategory.xpath('a/@href').extract()
                    url="http://www.gastro24.de/"+subcategoryurl[0]
                    #print "The SUB CATEGORY URL is : ",url
                    try:
                        req = scrapy.Request(url,callback=self.parse3)
                        yield req
                        #time.sleep(.3)
                    except : raise			

        