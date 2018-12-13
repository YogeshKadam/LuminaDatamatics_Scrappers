



#Amazon seller list spider
import time
import scrapy
    
	
	
class FnwerItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    cost = scrapy.Field()
    variants = scrapy.Field()
    breadcrumb=scrapy.Field()
    url=scrapy.Field()
    
	

class Spider(scrapy.Spider):
    
    name = "fn1"
    allowed_domain=[]
    start_urls = ['http://www.fnwerkzeuge.de/akkugeraete.html']
    #start_urls = ['https://www.amazon.com/musical-instruments-accessories-sound-recording/b/ref=nav_shopall_mi_ce?ie=UTF8&node=11091801']
    
    

    def parse(self, response):

        categorylist=response.xpath('//*[@id="main_nav"]/li[1]/ul/li')
        for categories in categorylist:
            category=categories.xpath('a/@href').extract()
            url=category[0]
            print url
            try:
                req = scrapy.Request(url,callback=self.parse2)
                yield req
                time.sleep(.3)
            except: raise
        
 
     
                
                
    def parse2(self,response):
        
        
        titleurllist=response.xpath('//*[@class="category-products"]/ol["products-list"]/li')
		
        for titleurls in titleurllist:
            
            titleurl=titleurls.xpath('div[1]/div/h3[1]/a/@href').extract()
            #print titleurl
            try:
                req = scrapy.Request(titleurl[0],callback=self.parse3)
                yield req
                time.sleep(.3)
            except: raise
            
        nextpageurllist=response.xpath('//*[@class="toolbar-bottom"]/div["toolbar"]/div["pager"]/div[1]/div[3]/ol/li')
        if len(nextpageurllist)>=0:
            for nextpageurls in nextpageurllist:
                classname=nextpageurls.xpath('a/@class').extract()
                
                #print "CLASSNAME : ",classname
                if classname[0].replace(" ","").upper()=="NEXTI-NEXT":
                    print "THIS IS NEXT PAGE@@@@@@@@@@@@@@@@"
                    nextpageurl=nextpageurls.xpath('a/@href').extract()
                    try:
                        req = scrapy.Request(nextpageurl[0],callback=self.parse2)
                        yield req
                        time.sleep(.3)
                    except: raise
                else:
                    pass
        #item=FnwerItem()
        #breadcrumblist=("".join(response.xpath('//*[@class="breadcrumbs"]/ul/li//text()').extract())).replace("\n","").replace(" ","")
        #breadcrumblist=("".join(response.xpath('//*[@class="breadcrumbs"]/ul/li//*[not(self::strong)]/text()').extract())).replace("\n","").replace(" ","").rstrip("/")
        #item['breadcrumb']=breadcrumblist
        #item['url']=response.url
        #yield item
			
    def parse3(self,response):
        
        item=FnwerItem()
        variantdict={}
        title=response.xpath('//*[@id="product_addtocart_form"]/div/div[1]/div[1]/div[3]/h1/text()').extract()
        if not title:
            title=response.xpath('//*[@id="product_addtocart_form"]/div/div[1]/div[1]/div[4]/h1/text()').extract()
        #//*[@id="product_addtocart_form"]/div/div[1]/div[1]/div[4]/h1/text()
        #//*[@id="product_addtocart_form"]/div/div[1]/div[1]/div[4]/h1/text()
        #print title
        item['title']=("".join(title)).replace("\n","").replace("\t","").replace(" ","")
        price=response.xpath('//*[@class="shop_infos"]/div[2]/span/span[1]/text()').extract()
        if not price:
            price =response.xpath('//*[@class="shop_infos"]/div[2]/p[2]/span[1]/span[2]/text()').extract()
        #//*[@id="price-including-tax-89662"]
        #print price
        item['cost']=("".join(price)).replace("\n","").replace("\t","").replace(" ","")
        variantslist=response.xpath('//*[@id="product-attribute-specs-table"]/li')
        for variants in variantslist:
            variantkey=variants.xpath('span[1]/text()').extract()
            variantvalue=variants.xpath('span[2]/text()').extract()
            variantdict[("".join(variantkey)).replace("\n","").replace("\t","").replace(" ","")]=("".join(variantvalue)).replace("\n","").replace("\t","").replace(" ","")
            #print "Variant Key : ",variantkey
            #print "Variant Value : ",variantvalue
        #print "Variants List : ",variantdict
        item['variants']=variantdict
        #breadcrumblist=("".join(response.xpath('//*[@class="breadcrumbs"]/ul/li//text()').extract())).replace("\n","").replace(" ","")
        breadcrumblist=("".join(response.xpath('//*[@class="breadcrumbs"]/ul/li//*[not(self::strong)]/text()').extract())).replace("\n","").replace(" ","").rstrip("/")
        item['breadcrumb']=breadcrumblist
        item['url']=response.url
        yield item