# -*- coding: utf-8 -*-
import scrapy
import time
import json

class EbayItem(scrapy.Item):
    product_title = scrapy.Field()
    product_id = scrapy.Field()
    price = scrapy.Field()
    brand = scrapy.Field()
    ean = scrapy.Field()
    mpn = scrapy.Field()
    attr_dict = scrapy.Field()
    breadcrumb  = scrapy.Field()
    url=scrapy.Field()
    seller=scrapy.Field()

	
	

class Spider(scrapy.Spider):
    name = "ebay_productinfo_category2"
    allowed_domain=[]
    start_urls = ['https://www.ebay.de/b/Motorsagen/136242/bn_13648531']
    
    
	
    def parse(self, response):
        urls_done = [
]
        urls=[
["2","https://www.ebay.com/itm/New-Fashion-Women-Winter-Hooded-Slim-Coat-Jacket-Casual-Warm-Sportwear-Outwear/372157217577?hash=item56a64c7b29:m:mnj65CY7HPnNlxTKWrURHsQ"],
["3","https://www.ebay.com/itm/New-Women-Tassel-Shawl-Knitted-Wrap-Cape-Scarf-Knitwear-Long-Sleeve-Coat-Outwear/182945084304?hash=item2a98607390:m:miaxhqSx0ieNWwkxpASnFhg"],
["4","https://www.ebay.com/itm/Women-Long-Sleeve-Oversized-Loose-Knitted-Sweater-Jumper-Cardigan-Outwear-Coat/152814224557?hash=item23947004ad:m:m3kBYru8znO7-Ip7od1H65A"],
["5","https://www.ebay.com/itm/Womens-Irregular-Tassel-Cardigan-Sweater-Poncho-Shawl-Coat-Jacket-Tops-Outwear/292356942013?hash=item4411d4e8bd:m:myGpLGjbirkV8jUt0lur8sg"],
["6","https://www.ebay.com/itm/Womens-Warm-Coat-Jacket-Outwear-Trench-Winter-Hooded-Long-Parka-Overcoat-Top-New/122810000090?hash=item1c980be2da:m:mmbsAoNugpAfl1h2eg1iAQg"],
["7","https://www.ebay.com/itm/Women-Knitted-Sweater-Long-Sleeve-Casual-Cardigan-Knitwear-Jumper-Coat-Jacket/182945253389?hash=item2a9863080d:m:msbJPIkr3XO5PuxGB-o7Itg"],
["8","https://www.ebay.com/itm/womens-jacket-Miss-Chevious-x-large-reversible-with-hood-zip-up-pink-and-black/362179105747?hash=item54538e93d3:g:pmYAAOSwnipWYhRd"],
["9","https://www.ebay.com/itm/Womens-Trendy-Short-Bomber-Jacket-Loose-Casual-Thin-Zip-Padded-Coat-Blue-M/222746551460?hash=item33dcbaa4a4:g:bPQAAOSwBjdaIM9Q"],
["10","https://www.ebay.com/itm/Womens-Winter-Wollen-Coat-Jacket-Fashion-Lapel-Trench-Parka-Outwear-Cardigan/152667042742?hash=item238baa33b6:m:mzHjKyLxuiww_XC7X9i1ZCg"],
]

        #urlpart1="https://www.ebay.com/b/Wristwatches/31387/bn_2408451?"
        #urlpart2="&_udlo="
        #urlpart3="&_udhi="
        #urlpart4="&_pgn="

        for url in urls:
            try:
                req = scrapy.Request( url[1] , callback=self.parse1, meta={'product_id':url[0]})
                #req = scrapy.Request( "https://www.ebay.com/b/Mens-Wristwatches/31387/bn_2971674?_udlo=99&_udhi=100" , callback=self.parse1, meta={'main_url':})
                if url[0] not in urls_done: 
                    yield req
                    time.sleep(.1)
                #print url[0]
                #req.meta['item_id']=url[1]
                #req.meta['product_id']=url[0]
                #req.cookies = { 'x-wl-uid':'1y8ltVLwKU/L4uHVRT4wcyu32QxGmsLap3PS10lHQ8I4lHwvcV3mdItRxlTQQbVCy6hcltYxKLMM=', 's_nr':'1498670542228-New', 's_vnum':'1930670542228%26vn%3D1', 's_dslv':'1498670542232','amznacsleftnav-ac35e287-d67e-4607-a950-5d9ffd0c2ca9':'1', 'x-amz-captcha-1':'1499054178128406', 'x-amz-captcha-2':'f44Jo5PiWFZO/J2o05Otig==', 'session-token':'jmS4MZ+87cNOfytK07tpUCEGti+GXuHdZ0oZyPtYqY7t0jdykH+Ub7kXBm+uyaqfsw9okzU8c7KFuF577LQSOEOVzXGU6Ky1xqdZjaFUDfW6H5HbFByM0YxhwaB/i3TdgWzWRV7hvGo3qygmjkrIJ3ESRIOOM6YB4EJWL65CQUTq+Cp4ORjO1XQaGvfPERmPKJ8tKI4p77AQ0pKocXEOtyFku2Vp9HJzTUI9LN4bZVnXVtkV/ra/ElaVLqz1HqDJ', 'csm-hit':'s-GZBERSD0R10VXC0HBQZ6|1500714195597', 'session-id-time':'2082754801l', 'session-id':'261-2325209-6209161', 'ubid-acbde':'259-4651163-1859124' }
                #req.cookies = {'lc-main':'en_US', 's_nr':'1503816974090-New', 's_vnum':'1935816974090%26vn%3D1', 's_dslv':'1503816974091', 'x-main':'pHlb3N0WUwENeYPsqI@jzfF7PXLCCMcJSFiGwcdKfrlzzhc8yQR4kOovInsAXJRe', 'at-main':'Atza|IwEBIF45RJQgsZLrUGO7JaJnp1uVC-RDIfDCqwjV0PeKEDcSIP7e0Pvcm_n-R4iCtwyo7zXH7KLDakbXVsW-9UevBLsZEeSIH2YZJFCjQqDsNAySplN1BcQ1tUj5kmj24vddIVYyi7vx3S0B-tkr9EISA5O5_d5Tr--5JO2qiruKCKawd1MLIyk8KFGS2KdQJGW9wwb9fJf6C7Fk4_7UiW5C3D1DLeuP3VXdar3-_S3yvGXRindK-xRNl3O_YFLRo-a_yn9_Z1V8vNj6kvWgzui_fOIRGrsI9qCHAJpcpt5Nh4Ta5n6-ALqNPkS-zbWlmMkZMgWsZb5EwLk8qr5O_FUA9Be8bqkneub7AuYy2QcvE01rYqkAKgAm4QKR5MSCXDQg8Fquyibqt_a3TRBYXTOzPnoedkm7JdBsUtVGYs4TBNssF4KGFefA1cQRLvxAhHfZe58', 'x-wl-uid':'1QBgT0TBwoj9RQ+QP7eh8ocBTABgs1739+rzq1e3s1iwjoSRYnMpbAczaaknzT2id2ww9iSyiyXd3OQeaJ9Nm9xZrZOKqXNWIDJihS4V7CV+xlp+PQA7T/ILJyNBZ15so9XvNPTzCBQA=', 'session-token':'qLl3vjnjOse5+Cy5cC+3OlMT95d5wVC4bWvaoAbqyhOetjeYqWP24HhMNHJI9Ni3Y7rljL1VdkRzXeolkaGJX8cPCh2P8OzRCIL3t4dynzdXlADAwNZxyWK1BFxTvyUzw4CXSHIeNdq1l95h3SbsLhG4gOhSf5JLHUzfx9dKziC4SpGUaTP+/8VbIE886Ipz6wOjM1J1YwP4lwLQABPJPh/qNzYZWgWTmLW2sk2bkN1nGCJk9XWAoIA2ClwvqPRRIFg8mbX73GFXkSCPmdboKQ==', 'csm-hit':'HCCNKDAR5Q931G1FR5S1+s-HCCNKDAR5Q931G1FR5S1|1504589304054', 'ubid-main':'151-8001146-5395566', 'session-id-time':'2082787201l', 'session-id':'151-4943311-4733238'}

            except: raise
        #print "URLS_DONE : ",urls_done
                
    def parse1(self,response):
        #f=open("ebay_attrdict.json","a")
        variantdict={}		
        item=EbayItem()
        breadcrumb=[]
        item['product_id']=response.meta['product_id']
        item['url']=response.url
        title=response.xpath('//*[@id="CenterPanelInternal"]/div[2]/h1["itemTitle"]//text()').extract()
        #print title
        item['product_title']=("".join(title)).replace("\t","").replace("\n","")
        #articleno=titles.xpath('div/div[2]/ul[2]/li[1]/strong/text()').extract()
        #print articleno
        #item['articleno']="".join(articleno)
        cost=response.xpath('//*[@id="vi-mskumap-none"]/span[1]/text()').extract()
        if not cost: cost=response.xpath('//span[@id="mm-saleDscPrc"]/text()').extract()
        if not cost: cost=response.xpath('//span[@id="prcIsum"]/text()').extract()
        if not cost: cost=response.xpath('//*[@id="prcIsum_bidPrice"]/text()').extract()
        #print cost
        item['price']=("".join(cost)).replace("\t","").replace("\n","")
        try:
            seller=response.xpath('//*[@id="mbgLink"]/span/text()').extract()
            #print "SELLER INFO : ",seller
            item['seller']=seller[0]
        except:item['seller']=""
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
        
        brand="Brand"
        mpn="MPN"
        ean="EAN"
        if brand in variantdict.keys():
            item['brand']=variantdict[brand]
			
        if mpn in variantdict.keys():
            item['mpn']="'"+variantdict[mpn]+"'"
			
        if ean in variantdict.keys():
            item['ean']="'"+variantdict[ean]+"'"
        yield item