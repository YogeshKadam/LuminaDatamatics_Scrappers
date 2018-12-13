import scrapy
import urllib
from pymongo import MongoClient
import os
import time
import re
import json
from scrapy.conf import settings
class ComapreItem(scrapy.Item):
    product_title = scrapy.Field()
    #article_no = scrapy.Field()
    price = scrapy.Field()
    brand1 = scrapy.Field()
    brand2 = scrapy.Field()
    ean = scrapy.Field()
    mpn = scrapy.Field()
    model_number = scrapy.Field()
    colour = scrapy.Field()
    #description = scrapy.Field()
    url_page = scrapy.Field()
    breadcrumb  = scrapy.Field()
    base_breadcrumb = scrapy.Field()
    attr_dict = scrapy.Field()
    quantity = scrapy.Field()
    response_url = scrapy.Field()
    seller_count =  scrapy.Field()
    ASIN = scrapy.Field()
    star_rating  = scrapy.Field()
    num_review = scrapy.Field()
    question_answered = scrapy.Field()
    price = scrapy.Field()
    ship_price = scrapy.Field()
    seller_name = scrapy.Field()
    product_id = scrapy.Field()
    comp = scrapy.Field()



class amazonSpider(scrapy.Spider):
    imgcount = 1
    name = "amz_in_productdata_25-10-2018"
    allowed_domains = []

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]

    def parse(self,response):
        urls_done = []
        urls=[
['1493','B07JG7DS1T'],
['1495','B071GXXJVT'],
['1496','B00MVV9NUY'],
['1497','B00VA7Z3TK'],
['1498','B00VA7YYUO'],
['1499','B07CZMPXBM'],
['1500','B01CEFCEM0'],
]

        for url in urls:
            try:
                #req = scrapy.Request( 'https://www.amazon.in/dp/' +url[1] +'/' , headers={'authority': 'www.amazon.in' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9' },callback=self.parse6)
                req = scrapy.Request( 'https://www.amazon.in/dp/' +url[1] +'/' , headers={'authority': 'www.amazon.in' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'referer': 'https://www.amazon.in/' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9' },callback=self.parse6)
                req.meta['item_id']=url[1]
                req.meta['product_id']=url[0]
                #req.cookies = {'amznacsleftnav-2fae121d-91d2-301d-81b2-4a58017ea130':'1', 'amznacsleftnav-8a2b9815-7551-345f-b470-1e072f3768fc':'1', 'amznacsleftnav-9a8b0038-1448-3b54-bc27-b4a94f69c325':'1', 'amznacsleftnav-cd0218f0-d59c-42cf-b706-54a33f639fd4':'1', 'p2ePopoverID_260-7627146-5266859':'1', 'ubid-acbin':'256-8706343-4559632', 'lc-acbin':'en_IN', 'amznacsleftnav-58fb3a4b-9a46-402b-b984-b5513dfd9292':'1', 'amznacsleftnav-52977081-7bc5-454a-a1ce-d0bc61087512':'1', 'ca':'AFVAAIAIAAAABAAiAQEAAgA=', 's_nr':'1532409073855-Repeat', 's_vnum':'1923475818970%26vn%3D8', 's_dslv':'1532409073857', 'session-id':'259-9691935-5588529', 'x-amz-captcha-1':'1540541761238641', 'x-amz-captcha-2':'WcDWVz7Na0N8RQgJoA7gQw==', 'a-ogbcbff':'1', 'session-token':"QctMf4FuGZ7MQneHABYD3vRgiEyyleuSwmYYOWoTSvWWqektm0T0OZm38TQxan2QKteG5DHEqAcc4WpTi3mZf4textKes7hFznuYdphNzrfoSatrerDo6HDvxVpp0eXc84a6P2IEVAxSIF5u4V9FcxyJEoHltZoGaWA/7DLHjyshS+Wpo1antHgtcfDLGmoNylPEhO1S8KNKdvALBrHQjfcn5xJByIc4Qwhs35mDbfWezqYsqDjCgtpAatbIjRYaX1aOK8f7Fvg=", 'x-acbin':"alFXCwe@4ARom4KuQ30USxmt1ifdV7Ad7HKLI4yQCMxtrpn0GmGapunpXNyXP@Qg", 'at-acbin':'Atza|IwEBIP2rnb9aMyOufqGFbTp8DEBZQa4fHMIoD_PqnzcEhi_jvwdaU7czx0XDmVIgdpOS8fPeE2CnNHA898zsnVj9RyVFURpgU4RpAm2BdpGG-hLpJhAjywb7p_xN4vRR8_CGClICodMTEHdXgY1-krTgyeVXdZUL-qK6GQp4kGKQlEldpKo7O-AVRD4Go8k5U9oZXiQfsH7WktYoji7hweBt504XnqyXJpG1KBk9Wa_Nruk_S92xQPhqRM6GoKOOk8B2Mno-QUjDEXZoxkAKh3NwhvNM8QHY7VtUcl45sWJBJ4kFHZ0DGB-JAh3VPEsAWy00h_T4dxHcoe8SriC5b3SUIcZ0QWD6GLahidRzBn6cAyEHdIUbDbK6rJ_1nJ167Kyv12xUcpepf5tl0SRd6pNdzY0K', 'sess-at-acbin':"XDNPepxgWg5b7D8DjmbqSTI+aazP0dhF3NBhV91uND0=", 'sst-acbin':'Sst1|PQGngrGf11jRDSnMCYLLod4OCzswQ-2Zz6lGCtQ_JK6UDHlKxWahNtdOsvC-7YaOBwuwvBm1GXtC_SB2CF15tazFHLr32VdD37t8gvtG5HLc76VPqLWkndlGSUjMaegb5v84iY02OGkfyUNvNrgm1REcUTz_Y3Dx_o2FqEUSWWrHsJBjg7nvvTbOmUHinIPGaS_nlX4v_iNSAX2CR44kHY3ciwT7PFXPFDfgXdU46cO1ILJSL4U8K3YMd41gTYTp0I9oj09SD12_o3j3U0z-QJjnTtbEN_icsQJtIUzbwB0Z7UEODs6722c-M09curCqUZg1bUh3tpLtKoODahFb7wthnw', 'x-wl-uid':'1CkS+Yf/dt02iQLxnZ8jF34iCvP/Mml5UmrId9IVSS81ZgCXSD0ByuUteT7/PGxddPAjD17VbkCK8fssdR4AqtnMYrQ0hhHgTEsiYX2D6gQNs2/NrqqA6sl6zOpLtFemWGFtryul7rZfYpGVR1ALGRw==', 'csm-hit':'tb:s-FEV24YR1JQ16F6K5EX17|1540534654391&adb:adblk_no&t:1539160611688', 'session-id-time':'2082758401l', 'visitCount':'1042'}
                req.cookies = {'amznacsleftnav-2fae121d-91d2-301d-81b2-4a58017ea130':'1', 'amznacsleftnav-8a2b9815-7551-345f-b470-1e072f3768fc':'1', 'amznacsleftnav-9a8b0038-1448-3b54-bc27-b4a94f69c325':'1', 'amznacsleftnav-cd0218f0-d59c-42cf-b706-54a33f639fd4':'1', 'p2ePopoverID_260-7627146-5266859':'1', 'ubid-acbin':'256-8706343-4559632', 'lc-acbin':'en_IN', 'amznacsleftnav-58fb3a4b-9a46-402b-b984-b5513dfd9292':'1', 'amznacsleftnav-52977081-7bc5-454a-a1ce-d0bc61087512':'1', 'ca':'AFVAAIAIAAAABAAiAQEAAgA=', 's_nr':'1532409073855-Repeat', 's_vnum':'1923475818970%26vn%3D8', 's_dslv':'1532409073857', 'session-id':'259-9691935-5588529', 'x-acbin':"alFXCwe@4ARom4KuQ30USxmt1ifdV7Ad7HKLI4yQCMxtrpn0GmGapunpXNyXP@Qg", 'at-acbin':'Atza|IwEBIP2rnb9aMyOufqGFbTp8DEBZQa4fHMIoD_PqnzcEhi_jvwdaU7czx0XDmVIgdpOS8fPeE2CnNHA898zsnVj9RyVFURpgU4RpAm2BdpGG-hLpJhAjywb7p_xN4vRR8_CGClICodMTEHdXgY1-krTgyeVXdZUL-qK6GQp4kGKQlEldpKo7O-AVRD4Go8k5U9oZXiQfsH7WktYoji7hweBt504XnqyXJpG1KBk9Wa_Nruk_S92xQPhqRM6GoKOOk8B2Mno-QUjDEXZoxkAKh3NwhvNM8QHY7VtUcl45sWJBJ4kFHZ0DGB-JAh3VPEsAWy00h_T4dxHcoe8SriC5b3SUIcZ0QWD6GLahidRzBn6cAyEHdIUbDbK6rJ_1nJ167Kyv12xUcpepf5tl0SRd6pNdzY0K', 'sess-at-acbin':"XDNPepxgWg5b7D8DjmbqSTI+aazP0dhF3NBhV91uND0=", 'sst-acbin':'Sst1|PQGngrGf11jRDSnMCYLLod4OCzswQ-2Zz6lGCtQ_JK6UDHlKxWahNtdOsvC-7YaOBwuwvBm1GXtC_SB2CF15tazFHLr32VdD37t8gvtG5HLc76VPqLWkndlGSUjMaegb5v84iY02OGkfyUNvNrgm1REcUTz_Y3Dx_o2FqEUSWWrHsJBjg7nvvTbOmUHinIPGaS_nlX4v_iNSAX2CR44kHY3ciwT7PFXPFDfgXdU46cO1ILJSL4U8K3YMd41gTYTp0I9oj09SD12_o3j3U0z-QJjnTtbEN_icsQJtIUzbwB0Z7UEODs6722c-M09curCqUZg1bUh3tpLtKoODahFb7wthnw', 'x-wl-uid':'1y+AKqGmBNUQUygpMuPGU2At/7ibhitgSM2SsZhlU1E8KprBY/ooCYGtruYCBS+quKH2CrJuFM+j2EDeuut+P+QxjMx54rpl9VWMUIZY6EEOj0bn74/L+8bMnRlfHQEcdlfih3qCA4JU=', 'session-token':"naCgWqWlIgZ92NDhiLsgs04JsKitpn0S36traTcxuPeKJdBycR2Z9uB3l6Q/afaq7OTXyW57jQbwzaRewELoHA8yv7+oCEHfPjoz6gHeswrN21HvIwaF9ZvdP3JfqpHpL5cLWEfItO77/r0qOjfgSppTTudC6GnCTWbpSbXiOtzsT/z2YlCcjtn84BmeBqJ7ZIoc9UzWP2AfI2NPBXgltccTPJwlrFAwWgjvBu38fHznP55h38navrPXKsa9VNAzADxcX3x3HGU=", 'x-amz-captcha-1':'1540801246892584', 'x-amz-captcha-2':'2AQIW0dt/kzkqFOnnBTtaA==', 'session-id-time':'2082758401l', 'visitCount':'1049', 'csm-hit':'tb:95GKXKFYHRX2EC1WNJ3B+s-95GKXKFYHRX2EC1WNJ3B|1540794067092&adb:adblk_no&t:1539160611688'}
                if url[1] not in urls_done: 
                    yield req
                    time.sleep(.1)
            except: raise
        #print "URLS_DONE : ",urls_done


    def parse6(self,response):
        #print response.url
        #print 'https://www.amazon.co.uk/gp/offer-listing/' + response.url.split("dp/")[1] + '/ref=dp_olp_new?ie=UTF8&condition=new'
        #print response.body
        try:
            try:title=response.xpath('//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li/span/a/text()').extract()[-1].replace('\n','').strip()
            except: title=''
            bredcrumb_temp = []
            try:
                for part in response.xpath('//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li/span/a/text()').extract():
                    bredcrumb_temp.append(part.replace('\n','').strip())
            except: pass
            #print title
            try: brand1 = response.xpath('//*[@id="brand"]/text()').extract()[0].replace("  ",'').replace("\n",'').replace('\t','').strip()
            except: brand1=""
            if not brand1:
                try:
                    brand1=response.xpath('//*[@id="bylineInfo"]/text()').extract()[0].replace("  ",'').replace("\n",'').replace('\t','').strip()
                except: 
                    try:
                        brand1=response.xpath('//*[@id="brand"]/@href').extract()[0].replace("  ",'').replace("\n",'').replace('\t','').strip().split('/')[1]
                    except: brand1=""

			
            try:
                price = "".join(response.xpath('//*[@id="priceblock_ourprice"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
                if not price: price = "".join(response.xpath('//*[@id="priceblock_businessprice"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            except: raise
            ship_price = "".join(response.xpath('//*[@id="ourprice_shippingmessage"]/span/b/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            if not ship_price :  ship_price =  "".join(response.xpath('//*[@id="price-shipping-message"]/span/b/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            if not ship_price :  ship_price =  "".join(response.xpath('//span[@id="price-shipping-message"]//text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            if not ship_price :  ship_price =  "".join(response.xpath('//*[@id="ourprice_shippingmessage"]//text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
          
			
            seller_name = " ".join(response.xpath('//*[@id="merchant-info"]/a//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not seller_name: seller_name = " ".join(response.xpath('//*[@id="merchant-info"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
			
            #print brand,image
            title=';'.join(response.xpath('//*[@id="productTitle"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            result=[]
            final_dict=[]
            brand_match_type = ''
            product_attr_key1 = '$#'.join(response.xpath('//*[@id="product-specification-table"]/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value1 = response.xpath('//*[@id="product-specification-table"]/tr/td')
            product_attr_key2 = '$#'.join(response.xpath('//*[@id="product-specification-table"]/tbody/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value2 = response.xpath('//*[@id="product-specification-table"]/tbody/tr/td')
            product_attr_key3 = '$#'.join(response.xpath('//*[@id="productDetails_techSpec_section_1"]/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value3 = response.xpath('//*[@id="productDetails_techSpec_section_1"]/tr/td')
            product_attr_key4 =  '$#'.join(response.xpath('//*[@id="productDetails_techSpec_section_2"]/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value4 = response.xpath('//*[@id="productDetails_techSpec_section_2"]/tr/td')
            product_attr_key5 = '$#'.join(response.xpath('//*[@id="productDetails_detailBullets_sections1"]/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value5 = response.xpath('//*[@id="productDetails_detailBullets_sections1"]/tr/td')
            product_attr_key6 = '$#'.join(response.xpath('//*[@id="productDetails_detailBullets_sections2"]/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value6 = response.xpath('//*[@id="productDetails_detailBullets_sections2"]/tr/td')
            product_attr_key7 = '$#'.join(response.xpath('//*[@id="detail-bullets"]/table/tr/td/div/ul/li/b/text()').extract()).replace("\n",'').replace('\t','').strip()
            product_attr_value7 = response.xpath('//*[@id="detail-bullets"]/table/tr/td/div/ul/li')
            product_attr_key8= '$#'.join(response.xpath('//*[@id="feature-bullets"]/ul/li/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value8 = response.xpath('//*[@id="feature-bullets"]/ul/li/span')
            product_attr_key31 = '$#'.join(response.xpath('//*[@id="productDetails_techSpec_section_1"]/tbody/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value31 = response.xpath('//*[@id="productDetails_techSpec_section_1"]/tbody/tr/td')
            product_attr_key41 =  '$#'.join(response.xpath('//*[@id="productDetails_techSpec_section_2"]/tbody/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value41 = response.xpath('//*[@id="productDetails_techSpec_section_2"]/tbody/tr/td')
            product_attr_key51 = '$#'.join(response.xpath('//*[@id="productDetails_detailBullets_sections1"]/tbody/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value51 = response.xpath('//*[@id="productDetails_detailBullets_sections1"]/tbody/tr/td')
            product_attr_key61 = '$#'.join(response.xpath('//*[@id="productDetails_detailBullets_sections2"]/tbody/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value61 = response.xpath('//*[@id="productDetails_detailBullets_sections2"]/tbody/tr/td')
            product_attr_key71 = '$#'.join(response.xpath('//*[@id="detail-bullets"]/table/tbody/tr/td/div/ul/li/b/text()').extract()).replace("\n",'').replace('\t','').strip()
            product_attr_value71 = response.xpath('//*[@id="detail-bullets"]/table/tbody/tr/td/div/ul/li')
            product_attr_value9 =response.xpath('//*[@id="prodDetails"]/span')
            if not product_attr_key7: product_attr_key7 = '$#'.join(response.xpath('//*[@id="detailBullets_feature_div"]/ul/li/span/span[1]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not product_attr_value7: product_attr_value7 = response.xpath('//*[@id="detailBullets_feature_div"]/ul/li/span/span[2]')
            result_dict = {}
            key= None
            if product_attr_key3 and (product_attr_value3  or product_attr_value31)  :
                try:
                    value = product_attr_value3
                    if not value: value = product_attr_value31
                except: value = product_attr_value31
                key = product_attr_key3.split("$#")

                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result =zip(key,value[0:len(key)-1])

            #print result       
            for i,j in result:
                result_dict[i.replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()           
            match_type = ''
            brand_match_type = ''
            item_no =''
            match_dim = ''
            mpn_match =''
            if result_dict:final_dict.append(result_dict)
            if result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip() :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()

            brand2 = result_dict.get('Brand','').strip()
            
            result_dict = {}
            key= None
            if product_attr_key1 and product_attr_value1   :
                try:
                    value = product_attr_value1
                    key = product_attr_key1.split("$#")

                    if  key and len(key) == len(value):
                        result = zip(key,value)
                    else:
			            result = zip(key,value[0:len(key)-1])
                except: pass

            #print result       
            for i,j in result:
                result_dict[i.replace(":",'').strip()] =  "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()

            if result_dict:final_dict.append(result_dict)
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip() 

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 
            result_dict = {}
            key= None
            if product_attr_key4  and product_attr_value4    :
                try:
                    value = product_attr_value4
                    key = product_attr_key4.split("$#")

                    if  key and len(key) == len(value):
                        result =zip(key,value)
                    else:
                        result = zip(key,value[0:len(key)-1])
                except: pass
            
            #print result       
            for i,j in result:
                result_dict[i.replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 
            
            result_dict = {}
            key= None
            value = response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div[2]/ul/li')
            if not value:value = response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div/ul/li')
            if product_attr_key5  and (product_attr_value5  or product_attr_value51 )  :
                try:
                    value = product_attr_value5
                    if not value: value = product_attr_value51                
                except: value = product_attr_value51
                key = product_attr_key5.split("$#")
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[:len(key)-1])

            for i,j in result:
                result_dict[i.replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()

            if result_dict:final_dict.append(result_dict)
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 

            result_dict = {}
            key= None
            if product_attr_key7  and (product_attr_value7  or product_attr_value71 )  :
                try:
                    value = product_attr_value7
                    if not value: value = product_attr_value71
                except: value = product_attr_value71
                key = product_attr_key7.split("$#")

                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

            for i,j in result:
                result_dict[i.replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()

            if result_dict:final_dict.append(result_dict)
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 


            #print brand,item_no



            product_attr_value7 = '$#'.join([i.strip() for i in response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div[2]/ul/li/text()').extract()]).replace("\n",'').replace('\t','').strip()
            product_attr_key7 = '$#'.join(response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div[2]/ul/li/b/text()').extract()).replace("\n",'').replace('\t','').strip()
            result_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                 product_attr_value7 = '$#'.join([i.strip() for i in response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div/ul/li/text()').extract()]).replace("\n",'').replace('\t','').strip()
                 product_attr_key7 = '$#'.join([i.strip() for i in response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div/ul/li/b/text()').extract()]).replace("\n",'').replace('\t','').strip()

            
            if product_attr_key7  and product_attr_value7    :
                try:
                    value = product_attr_value7
                except: value = ""
                key = product_attr_key7.split("$#")
                value = response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div[2]/ul/li')
                if not value:value = response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div/ul/li')

                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for key, val in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()

                    result_dict[key.strip()] = "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                #print result_dict
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 

            result_dict = {}
            key= None
            if result_dict:final_dict.append(result_dict)

            product_attr_value7 = response.xpath('//*[@id="technicalSpecifications_feature_div"]/div[2]/div/div[1]/div/table/tbody/tr/td')
            product_attr_key7 = '$#'.join(response.xpath('//*[@id="technicalSpecifications_feature_div"]/div[2]/div/div[1]/div/table/tbody/tr/th/text()').extract()).replace("\n",'').replace('\t','').strip()
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 = response.xpath('//*[@id="technicalSpecifications_feature_div"]/div[2]/div/div[1]/div/table/tr/td')
                product_attr_key7 = '$#'.join(response.xpath('//*[@id="technicalSpecifications_feature_div"]/div[2]/div/div[1]/div/table/tr/th/text()').extract()).replace("\n",'').replace('\t','').strip()

            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7.split("$#")

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[i.replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()

            if result_dict:final_dict.append(result_dict)
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 



            result_dict = {}
            key= None
		  

            product_attr_value7 = response.xpath('//*[@id="productDetailsTable"]/tbody/tr/td/div/ul/li')
            product_attr_key7 = response.xpath('//*[@id="productDetailsTable"]/tbody/tr/td/div/ul/li/b')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 = response.xpath('//*[@id="productDetailsTable"]/tr/td/div/ul/li')
                product_attr_key7 = response.xpath('//*[@id="productDetailsTable"]/tr/td/div/ul/li/b')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()

            if result_dict:final_dict.append(result_dict)
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 

            product_attr_value7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr/td[2]')
            product_attr_key7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr/td[1]')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tr/td[2]')
                product_attr_key7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tr/td[1]')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            #print result_dict, "1"
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 


            product_attr_value7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr/td[2]')
            product_attr_key7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr/td[1]')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tr/td[2]')
                product_attr_key7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tr/td[1]')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            #print result_dict, "2"
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 

   
            product_attr_value7 = response.xpath('//*[@id="technicalSpecifications_section_1"]/tbody/tr/td')
            product_attr_key7 = response.xpath('//*[@id="technicalSpecifications_section_1"]/tbody/tr/th')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 = response.xpath('//*[@id="technicalSpecifications_section_1"]/tr/td')
                product_attr_key7 = response.xpath('//*[@id="technicalSpecifications_section_1"]/tr/th')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            #print result_dict, "3"
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 



            product_attr_value7 = response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div[2]/div/div/table/tbody/tr/td[2]')
            product_attr_key7 = response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div[2]/div/div/table/tbody/tr/td[1]')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 =  response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div[2]/div/div/table/tr/td[2]')
                product_attr_key7 =  response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div[2]/div/div/table/tr/td[1]')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            #print result_dict, "3"
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 





            product_attr_value7 = response.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li')
            product_attr_key7 = response.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li/b')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 =  response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div/ul/li')
                product_attr_key7 =  response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div/ul/li/b')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            #print result_dict, "3"
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 




            product_attr_value7 = response.xpath('//*[@id="prodDetails"]/div/div[2]/div[1]/div[2]/div/div/table/tbody/tr/td[2]')
            product_attr_key7 = response.xpath('//*[@id="prodDetails"]/div/div[2]/div[1]/div[2]/div/div/table/tbody/tr/td[1]')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 =  response.xpath('//*[@id="prodDetails"]/div/div[2]/div[1]/div[2]/div/div/table/tr/td[2]')
                product_attr_key7 =  response.xpath('//*[@id="prodDetails"]/div/div[2]/div[1]/div[2]/div/div/table/tr/td[1]')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            #print result_dict, "3"
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 


        except:
            raise
		  
        ean = ""
        variation_ASIN = ""
        variation_ASIN = ",".join(response.xpath('//*[@id="variation_color_name"]/ul/li/@data-defaultasin').extract())
      
        variation_dp_url = response.xpath('//*[@id="variation_color_name"]/ul/li/@data-dp-url').extract()
        if len(variation_dp_url )>0:
            variation_dp_url_list = [ i[3:].split("/ref")[0] for i in variation_dp_url]
            variation_ASIN = variation_ASIN + ","+ ",".join(variation_dp_url_list)
        variation_ASIN = variation_ASIN +","+ ",".join(response.xpath('//*[@id="variation_platform_for_display"]/ul/li/@data-defaultasin').extract())

        variation_ASIN = variation_ASIN +","+ ",".join(response.xpath('//*[@id="variation_service_plan_term"]/ul/li/@data-defaultasin').extract())
        if variation_ASIN: variation_ASIN = variation_ASIN +","
        variation_ASIN  = variation_ASIN + ",".join(response.xpath('//*[@id="variation_size_name"]/ul/li/@data-defaultasin').extract())
        variation_size = response.xpath('//*[@id="native_dropdown_selected_size_name"]/option/@value').extract()
        if len(variation_size )>0:
            variation_size_list = [ i.split(",")[1] for i in variation_size[1:]]
            variation_ASIN = variation_ASIN + "," + ",".join(variation_size_list)
        variation_size = response.xpath('//*[@id="native_dropdown_selected_initial_character"]/option/@value').extract()
        #print variation_size
        if len(variation_size )>0:
            variation_size_list = [ i.split(",")[1] for i in variation_size[1:]]
            variation_ASIN = variation_ASIN + "," + ",".join(variation_size_list)
        attr_dict = dict([ (k,v)  for d in final_dict for k,v in d.items() ])
        if not item_no and( attr_dict.get('Modellnummer','').strip() or attr_dict.get('Teilenummer','').strip() ) :
            item_no = attr_dict.get('Modellnummer','').strip() or attr_dict.get('Teilenummer','').strip()
        if not ean and( attr_dict.get('EAN/UPC','').strip() or attr_dict.get('EAN / Artikelnummer','').strip() ) :
            ean =  attr_dict.get('EAN/UPC','').strip() or attr_dict.get('EAN / Artikelnummer','').strip() 
        if not brand2 and( attr_dict.get('Manufacturer','').strip() or attr_dict.get('Brand Name','').strip() ) :
            brand2 =  attr_dict.get('Manufacturer','').strip() or attr_dict.get('Brand Name','').strip() 
            #if not brand2:  brand2 =result_dict.get('Manufacturer','').strip()
		
                                                        
        try:
            count = "".join(response.xpath('//*[@id="olp_feature_div"]/div/span[1]/a/text()').extract()).strip()
            star_rating  = "".join(response.xpath('//*[@id="acrPopover"]/span[1]/a/i[1]/span/text()').extract()).replace('/n','').strip()
            num_review = "".join(response.xpath('//*[@id="acrCustomerReviewText"]/text()').extract()).replace('/n','').strip()
            question_answered = "".join(response.xpath('//*[@id="askATFLink"]/span/text()').extract()).replace('/n','').strip()
            item = ComapreItem()
            item['star_rating'] = star_rating
            item['num_review'] = num_review
            item['question_answered'] = question_answered
            item['product_title'] = title
            item['mpn'] = "'" +item_no+"'"
            item['attr_dict'] = json.dumps(attr_dict)
            item['brand1'] = brand1
            item['brand2'] = brand2
            item['response_url']=response.url
            item['ASIN']=response.meta['item_id']
            item['breadcrumb']="/".join(bredcrumb_temp)
            item['seller_count'] = count
            item['ship_price'] = ship_price
            item['price'] = price
            item['seller_name'] = seller_name
            if response.meta['product_id'].find('_') > -1:
                item['comp']='Alt'
                item['product_id']=response.meta['product_id'].split('_')[0]
            else: 
                item['comp']=''
                item['product_id']=response.meta['product_id']
            item['ean'] = ean
            #print item
            yield item
        except:
            raise