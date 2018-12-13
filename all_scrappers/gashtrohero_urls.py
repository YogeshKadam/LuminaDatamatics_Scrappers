#Amazon seller list spider
import time
import scrapy
    
	
	
class GastroHeroItem(scrapy.Item):
    # define the fields for your item here like:
    url=scrapy.Field()
    
    
	

class Spider(scrapy.Spider):
    
    name = "gashtrohero_url"
    allowed_domain=[]
    #start_urls = ['http://www.gastro24.de/Kuehltechnik-und-Kaeltetechnik']
    #start_urls=['http://www.gastro24.de/Aufschnittmaschinen']
    #start_urls=['http://www.gastro24.de/Cafebedarf-und-Cafezubehoer']
    #start_urls=['http://www.gastro24.de/Aufschaeumkannen']
    #start_urls=['http://www.gastro24.de/Grosskuechentechnik']
    #start_urls=['https://www.gastro-hero.de/K%C3%BChltechnik']
    #start_urls=['https://www.gastro-hero.de/Kochger%C3%A4te']
    start_urls=['https://www.gastro-hero.de/Pizzeria-und-Grill']

    
    

    
    def parse(self,response):
        allurllist=[]
        categorylist=response.xpath('//*[@id="page-columns"]/div[2]/div[1]/div[2]/ul/li[3]/ul/li')

        for categories in categorylist:
            subcategorytext=categories.xpath('@class').extract()
            if subcategorytext[0].replace(" ","").upper().find('PARENT'):
                
                allurllist.append(categories.xpath('a/@href').extract()[0])
                
                category=categories.xpath('ul/li')
                for subcategory in category:
                    
                    
                    subcategorytext1=subcategory.xpath('@class').extract()
                    if subcategorytext1[0].replace(" ","").upper().find('PARENT'):
                        
                        allurllist.append(subcategory.xpath('a/@href').extract()[0])
                        
                        category1=subcategory.xpath('ul/li')
                        for subcategory1 in category1:
                            subcategoryurl1=subcategory1.xpath('a/@href').extract()
                            url=subcategoryurl1[0]
                            
                            allurllist.append(url)
                    else:
                        subcategoryurl=subcategory.xpath('a/@href').extract()
                        url=subcategoryurl[0]
                    
                        allurllist.append(url)
                            
                    
	
            else:
                #print "FOUND"
                #item=GastroItem()
                category=categories.xpath('a/@href').extract()
                url=category[0]
                
                allurllist.append(url)
                
        allurllist.append(response.url)
		
        for url in allurllist:
            item=GastroHeroItem()
            item['url']=url
            yield item
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
"""    https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChlschr%C3%A4nke
def parse(self,response):
        allurllist=[]
        categorylist=response.xpath('//*[@id="page-columns"]/div[2]/div[1]/div[2]/ul/li[1]/ul/li')

        for categories in categorylist:
            subcategorytext=categories.xpath('@class').extract()
            if subcategorytext[0].replace(" ","").upper().find('PARENT'):
                
                allurllist.append(categories.xpath('a/@href').extract()[0])
                
                category=categories.xpath('ul/li')
                for subcategory in category:
                    subcategoryurl=subcategory.xpath('a/@href').extract()
                    url=subcategoryurl[0]
                    
                    allurllist.append(url)
                    
                    subcategorytext1=subcategory.xpath('@class').extract()
                    if subcategorytext1[0].replace(" ","").upper().find('PARENT'):
                        
                        allurllist.append(subcategory.xpath('a/@href').extract()[0])
                        
                        category1=subcategory.xpath('ul/li')
                        for subcategory1 in category1:
                            subcategoryurl1=subcategory1.xpath('a/@href').extract()
                            url=subcategoryurl1[0]
                            
                            allurllist.append(url)
                            
                    
	
            else:
                #print "FOUND"
                #item=GastroItem()
                category=categories.xpath('a/@href').extract()
                url=category[0]
                
                allurllist.append(url)
                
        allurllist.append(response.url)
		
        for url in allurllist:
            item=GastroHeroItem()
            item['url']=url
            yield item
			
			
			
def parse(self,response):
        try:
            allurllist1=response.meta['allurllist']
        except:
            print "RESPONSE NOT FOUND"
            allurllist1=[]
        categorylist=response.xpath('//*[@id="page-columns"]/div[2]/div[1]/div[2]/ul/li[1]/ul/li')
        #//*[@id="page-columns"]/div[2]/div[1]/div[2]/ul/li[1]/ul/li[1]/a
        #//*[@id="page-columns"]/div[2]/div[1]/div[2]/ul/li[1]/ul/li[1]/ul/li[1]/a
        
        for categories in categorylist:
            subcategorytext=categories.xpath('@class').extract()
            if subcategorytext[0].replace(" ","").upper().find('PARENT'):
                category=categories.xpath('ul/li')
                for subcategory in category:
                    subcategoryurl=subcategory.xpath('a/@href').extract()
                    url=subcategoryurl[0]
                    try:
                        req = scrapy.Request(url,callback=self.parse, meta={'allurllist':allurllist1})
                        yield req
                        #time.sleep(.3)
                    except: raise
                    
	
            else:
                #print "FOUND"
                #item=GastroItem()
                category=categories.xpath('a/@href').extract()
                url=category[0]
                if url not in allurllist1:
                    item=GastroHeroItem()
                    allurllist1.append(url)
                    #print "The FINAL URL is : ",url
                    item['url']=url
                    yield item
                
                
        item=GastroHeroItem()
        item['url']=response.url
        yield item"""