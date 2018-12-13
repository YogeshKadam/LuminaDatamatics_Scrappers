




import scrapy
import time
import json

class EbayItem(scrapy.Item):
    product_title = scrapy.Field()
    price = scrapy.Field()
    brand = scrapy.Field()
    ean = scrapy.Field()
    article_no = scrapy.Field()
    attr_dict = scrapy.Field()
    breadcrumb  = scrapy.Field()
    url=scrapy.Field()
    seller=scrapy.Field()

	
	

class Spider(scrapy.Spider):
    name = "ebay123"
    allowed_domain=[]
    start_urls = ['https://www.ebay.de/b/Motorsagen/136242/bn_13648531']
    
    
	
    def parse(self, response):
        #print "Current URL : ",response.url
        titleurllist=response.xpath('//*[@id="mainContent"]/section/ul/li["s-item"]')
        for titleurls in titleurllist:
            #subcategorytext=categories.xpath('@class').extract()
            #print "Sub Category Text : ",subcategorytext
            titleurl=titleurls.xpath('div/div[2]/a/@href').extract()
            
            print "The URL is : ",titleurl
            try:
                req = scrapy.Request(titleurl[0],callback=self.parse2)
                yield req
                time.sleep(.3)
            except: raise
        
        f.close()	
                
    def parse2(self,response):
        #f=open("ebay_attrdict.json","a")
        variantdict={}		
        item=EbayItem()
        breadcrumb=[]
        item['url']=response.url
        title=response.xpath('//*[@id="CenterPanelInternal"]/div[2]/h1["itemTitle"]//text()').extract()
        #print title
        item['product_title']=("".join(title)).replace("\t","").replace("\n","")
        #articleno=titles.xpath('div/div[2]/ul[2]/li[1]/strong/text()').extract()
        #print articleno
        #item['articleno']="".join(articleno)
        cost=response.xpath('//*[@id="vi-mskumap-none"]/span[1]/text()').extract()
        #print cost
        item['price']=("".join(cost)).replace("\t","").replace("\n","")
        seller=response.xpath('//*[@id="mbgLink"]/span/text()').extract()
        #print "SELLER INFO : ",seller
        item['seller']=seller[0]
        breadcrumblist=response.xpath('//*[@id="vi-VR-brumb-lnkLst"]/table/tr/td/h2/ul/li')
        #print "Breadcrumblist : ",breadcrumblist
        for breadcrumbs in breadcrumblist:
            singlebreadcrumb=breadcrumbs.xpath('a/span/text()').extract()
            if not singlebreadcrumb:
                pass
            else:
                breadcrumb.append(singlebreadcrumb[0])
        
		
        #print "Breadcrumb : ",breadcrumb
        item['breadcrumb']=">".join(breadcrumb)
        variantslist=response.xpath('//*[@id="vi-desc-maincntr"]/div["itemAttr"]/div/table/tr')
        #print "Variants List : ",variantslist
        for variants in variantslist:
            variantkey=variants.xpath('td[1]/text()').extract()
            #print "Key 1 : ",variantkey
            variantvalue=variants.xpath('td[2]//text()').extract()
            #print "Value 1 : ",variantvalue
            variantdict[("".join(variantkey)).replace("\n","").replace("\t","").replace(" ","").replace(":","")]=("".join(variantvalue)).replace("\n","").replace("\t","").replace(" ","")
            variantkey2=variants.xpath('td[3]/text()').extract()
            #print "Key 2 : ",variantkey2
            variantvalue2=variants.xpath('td[4]//text()').extract()
            #print "Value 2 : ",variantvalue2
            variantdict[("".join(variantkey2)).replace("\n","").replace("\t","").replace(" ","").replace(":","")]=("".join(variantvalue2)).replace("\n","").replace("\t","").replace(" ","")
        #print variantdict
		
        for x in variantdict.keys():
            if variantdict[x] == "":
                del variantdict[x]
				
		
        item['attr_dict']=json.dumps(variantdict)
        #json.dump()
        
        brand="Marke"
        mpn="Herstellernummer"
        ean="EAN"
        if brand in variantdict.keys():
            item['brand']=variantdict[brand]
			
        if mpn in variantdict.keys():
            item['article_no']="'"+variantdict[mpn]+"'"
			
        if ean in variantdict.keys():
            item['ean']="'"+variantdict[ean]+"'"
        yield item