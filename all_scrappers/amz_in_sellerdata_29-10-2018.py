
import scrapy
import urllib
import os
import time
import json

class Amazon_upc_out(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    product_id = scrapy.Field()
    spider = scrapy.Field()
    dpid = scrapy.Field()
    seller_info = scrapy.Field()
    date_timestamp = scrapy.Field()
    #job_id = scrapy.Field()
    #upc = scrapy.Field()
    seller_count = scrapy.Field()
    title = scrapy.Field()
    #body = scrapy.Field()
    #comp = scrapy.Field()

class amazonSpider(scrapy.Spider):
    imgcount = 1
    name = "amz_in_sellerdata_29-10-2018"
    allowed_domains = []

    start_urls = ["http://www.flipkart.com/search?q=9780005996218" ]  

    def parse(self,response):

        urls_done = []

        urls =[
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
                #req = scrapy.Request( "https://www.amazon.com/gp/offer-listing/" + url[1] +"/ref=dp_olp_new?ie=UTF8&condition=new" , headers={'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://www.amazon.com/Inspiron-Performance-Flagship-Touchscreen-Bluetooth/dp/B071GPZB2M/ref=sr_1_2?s=pc&ie=UTF8&qid=1503680901&sr=1-2-spons&keywords=laptop&psc=1' }, callback=self.parse6)
                req = scrapy.Request( "https://www.amazon.in/gp/offer-listing/" + url[1] +"/ref=dp_olp_new?ie=UTF8&condition=new" , headers={'authority': 'www.amazon.in' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9'}, callback=self.parse6)
                req.meta['item_id']=url[1]
                req.meta['product_id']=url[0]
                #req.cookies = { 'lc-main':'en_US', 'x-wl-uid':'1yE71wxptnrPGpU96MVpeAljDAxEwlHAMNmRkGH3kTDbQNlw65AKYm8JBd2Nm33DfONRPH48N1DRE/phePYv7b8VzqI5P36U503gVSzRJSBmwDQKne/e/xfe/X3r9TLt9Mq2dGxVnAVsmo8PkOTlUOw==', 'skin':'noskin', 'x-main':'X2Uw?4D0ZsoVUNTB1ND?IqOhj4jrdt3SQM?nwPoWs2Vra8r9I13YbE1V8fqOmIli', 'at-main':'Atza|IwEBIM6arSMDjanfYsyURnaqmNeb87cZy6ift3_Ewd6ai-VCWQxN1VU8u-feDM43rwF2oZopky98QowPRIgSVmpR_qWGQgSAAMl_YsBf2E0nGom_GkU0Vl5JNLdIaGZ9g-Je-Uld-_qAa3onwe2Q_rUKPCN6j5PAu_78gARA9l5GI48so08VSR_tDyWO8p_WHTqj2dJMXqKZ-6YuhyOYGPbSFgupS_O-PofP6d9lqKlLtruDVDv98__UgkmhRmUXWTt3X3G_2ALthXr4_8tBnT4VpdNEWYqZKsJF0xej6dixrNlFNWoKyK-jojctn-E95wf1GmItDzSmmwM-fzp8LRptCncE_vJEfXTPknNoUcz2qoYx2kBsuYOviBUZSAONWCXII68hZD4SILOFPKAMmAXRBswx', 'sess-at-main':'hTCj4tFy0geBzyuGIGBYRUfOmwxbmm3iJjvmeMi/emE=', 'JSESSIONID':'C70160F1BC7EC0B9D5E1BD946AA543DF', 'csm-hit':'J1CK3EMBJCQHNYC6PB4P+s-CB6DMAQSAGGJC2C8H354|1503728162175', 'session-token':'n2Bkr05TMvQYIlxStLEPDDdd8KmwvXszRPl41nyUA+1+hlViB/+whjJG3jQjbUov8lRYLkN78KFEgYKt3ZQZjLd8PKw5Sp8DO2anI7lIo5iA5ZlBkkhTAAEz6qxH9pejQawVHIgLmQ0WLVWeZup/JQGwjoNITTENdcZ9A+C55Nfj0eEwqpNI661A1pvmaG9Y2hCGn0xf/zWQnGeus1aGeF6u3GdgzUTVEoqoashearQ8cngRhV/i0uxZoqRJly4ivJIy43Khphvj7Z++9vFB3w==', 'ubid-main':'131-1502033-8002851', 'session-id-time':'2082787201l', 'session-id':'130-6537552-1339612'}
                req.cookies = {'amznacsleftnav-2fae121d-91d2-301d-81b2-4a58017ea130':'1', 'amznacsleftnav-8a2b9815-7551-345f-b470-1e072f3768fc':'1', 'amznacsleftnav-9a8b0038-1448-3b54-bc27-b4a94f69c325':'1', 'amznacsleftnav-cd0218f0-d59c-42cf-b706-54a33f639fd4':'1', 'p2ePopoverID_260-7627146-5266859':'1', 'ubid-acbin':'256-8706343-4559632', 'lc-acbin':'en_IN', 'amznacsleftnav-58fb3a4b-9a46-402b-b984-b5513dfd9292':'1', 'amznacsleftnav-52977081-7bc5-454a-a1ce-d0bc61087512':'1', 'ca':'AFVAAIAIAAAABAAiAQEAAgA=', 's_nr':'1532409073855-Repeat', 's_vnum':'1923475818970%26vn%3D8', 's_dslv':'1532409073857', 'session-id':'259-9691935-5588529', 'x-acbin':"alFXCwe@4ARom4KuQ30USxmt1ifdV7Ad7HKLI4yQCMxtrpn0GmGapunpXNyXP@Qg", 'at-acbin':'Atza|IwEBIP2rnb9aMyOufqGFbTp8DEBZQa4fHMIoD_PqnzcEhi_jvwdaU7czx0XDmVIgdpOS8fPeE2CnNHA898zsnVj9RyVFURpgU4RpAm2BdpGG-hLpJhAjywb7p_xN4vRR8_CGClICodMTEHdXgY1-krTgyeVXdZUL-qK6GQp4kGKQlEldpKo7O-AVRD4Go8k5U9oZXiQfsH7WktYoji7hweBt504XnqyXJpG1KBk9Wa_Nruk_S92xQPhqRM6GoKOOk8B2Mno-QUjDEXZoxkAKh3NwhvNM8QHY7VtUcl45sWJBJ4kFHZ0DGB-JAh3VPEsAWy00h_T4dxHcoe8SriC5b3SUIcZ0QWD6GLahidRzBn6cAyEHdIUbDbK6rJ_1nJ167Kyv12xUcpepf5tl0SRd6pNdzY0K', 'sess-at-acbin':"XDNPepxgWg5b7D8DjmbqSTI+aazP0dhF3NBhV91uND0=", 'sst-acbin':'Sst1|PQGngrGf11jRDSnMCYLLod4OCzswQ-2Zz6lGCtQ_JK6UDHlKxWahNtdOsvC-7YaOBwuwvBm1GXtC_SB2CF15tazFHLr32VdD37t8gvtG5HLc76VPqLWkndlGSUjMaegb5v84iY02OGkfyUNvNrgm1REcUTz_Y3Dx_o2FqEUSWWrHsJBjg7nvvTbOmUHinIPGaS_nlX4v_iNSAX2CR44kHY3ciwT7PFXPFDfgXdU46cO1ILJSL4U8K3YMd41gTYTp0I9oj09SD12_o3j3U0z-QJjnTtbEN_icsQJtIUzbwB0Z7UEODs6722c-M09curCqUZg1bUh3tpLtKoODahFb7wthnw', 'x-wl-uid':'1y+AKqGmBNUQUygpMuPGU2At/7ibhitgSM2SsZhlU1E8KprBY/ooCYGtruYCBS+quKH2CrJuFM+j2EDeuut+P+QxjMx54rpl9VWMUIZY6EEOj0bn74/L+8bMnRlfHQEcdlfih3qCA4JU=', 'x-amz-captcha-1':'1540801246892584', 'x-amz-captcha-2':'2AQIW0dt/kzkqFOnnBTtaA==', 'session-id-time':'2082758401l', 'visitCount':'1052', 'session-token':'no9pfW8geeCNVeihf/oJOihIa4OtnC6WF6JXGfcRWbKOZA/xe1iiULdTdZ+xiAiispoQFBI3E3WVCa/Jnky2Q6JqtZk0ST+UjrWxS0GXTqi5SqXadhKiWmEMLH/wvmiuihHRCyg1rdnIdRtPLlprqdr3SiduXIflLVsfov45aHj6Ha0pYVctLqrvjHNOH9diSPPGq1Y80euK1Jr5UXL4X9mdJYi5IntbORHGQtpu2RuMSu/t2602ozlkILslarkVWOsJ8Xckig8=', 'csm-hit':'tb:P0MKSDYY4ADZTA0QE09F+s-P0MKSDYY4ADZTA0QE09F|1540796748677&adb:adblk_no&t:1539160611688' }
                try:
                    if url[2]:
                        req.meta['is_competitor']="C"
                except:
                    req.meta['is_competitor']="R"

                req.meta['id']=url[1]
                req.meta['upc']=url[1]
                if url[1] not in urls_done: 
                    yield req
                    time.sleep(.3)
            except: raise

    def parse6(self,response):
        #f1=open("amz_seller_page.html","w")
        #f1.write(response.body)
        #f1.close()
        try:
            try:
                title= " ".join(response.xpath('//*[@id="olpProductDetails"]/div[1]/h1//text()').extract()).replace("\n",'').replace('\t','').strip()
                if not title: title= " ".join(response.xpath('//*[@id="olpProductDetails"]/h1//text()').extract()).replace("\n",'').replace('\t','').replace('   ','').strip()
            except: title=''
            if title=='':
                try: title= " ".join(response.xpath('//*[@id="btAsinTitle"]/text()').extract()).replace("\n",'').replace('\t','').strip()
                except: title=''
            try:bd=response.xpath('//*[@class="nav-search-field"]').extract()[0]
            except:bd=''
            no_found = response.xpath('//*[@id="olpOfferList"]/div/p').extract()
            #attr=response.meta['attr']
            #json_acceptable_string = attr.replace("'", "\"")
            #attr = json.loads(json_acceptable_string)
            res = response.xpath('//div[@class="a-row a-spacing-mini olpOffer"]')
            if res:
                sellers_info = []
                for data in res:
                    add_to_cart=""
                    try:
                        #price = data.xpath('div/span[@class="a-size-large a-color-price olpOfferPrice a-text-bold"]//text()').extract()[0].encode('ascii','ignore').strip()
                        #print "PRICEEEEEE : ",data.xpath('div[1]/span[@class="a-size-large a-color-price olpOfferPrice a-text-bold"]//text()').extract()[0]
                        price = "".join(data.xpath('div[1]/span[@class="a-size-large a-color-price olpOfferPrice a-text-bold"]//text()').extract()).replace('\n','').replace('\t','').replace('   ','').encode('ascii','ignore')
                    except: 
                        price=''
                        add_to_cart= "".join(data.xpath('div/text()').extract()).encode('ascii','ignore').replace("\n",'').replace('\t','').replace("   ",' ').strip()
                    shipping_price = " ".join(data.xpath('div/p[@class="olpShippingPrice"]/span//text()').extract()).replace("\n",'').replace('\t','').strip()
                    if not shipping_price:shipping_price = " ".join(data.xpath('div/p/span/span//text()').extract()).replace("\n",'').replace('\t','').strip()
                    if not shipping_price: shipping_price = " ".join(data.xpath('div/p[@class="olpShippingInfo"]/span//text()').extract()).replace("\n",'').replace('\t','').strip()
                    comments = " ".join(data.xpath('div/div/text()').extract()).replace("\n",'').replace('\t','').strip() +" "+ " ".join(data.xpath('div/div/div/text()').extract()).replace("\n",'').replace('\t','').strip()
                    seller_name =   " ".join(data.xpath('div/h3/span/a/text()').extract()).replace("\n",'').replace('\t','').strip()
                    seller_alt = "".join(data.xpath('div/h3/img/@alt').extract()).replace("\n",'').replace('\t','').strip()
                    if not seller_alt: seller_alt = "".join(data.xpath('div/h3/a/img/@alt').extract()).replace("\n",'').replace('\t','').strip()
                    seller_link =   " ".join(data.xpath('div/h3/span/a/@href').extract()).replace("\n",'').replace('\t','').strip()
                    seller_rating_percents = " ".join(data.xpath('div/p/a/b/text()').extract()).replace("\n",'').replace('\t','').strip()
                    seller_ratinngs = " ".join(data.xpath('div/p/text()').extract()).replace("\n",'').replace('\t','').strip()
                    amz_fullfill=" ".join(data.xpath('div[3]/div/div/span/a/text()').extract()).replace("\n",'').replace('\t','').strip()
                    if not amz_fullfill: amz_fullfill=" ".join(data.xpath('div[@class="a-column a-span3 olpDeliveryColumn"]/div/div/span/a/img/@src').extract()).replace("\n",'').replace('\t','').strip()
                    if amz_fullfill: amz_fullfill='FBA'
                    else : amz_fullfill='MFN'
                    sellers_info.append({'price':price,'ship_price':shipping_price, 'seller':seller_name,'add_to_cart':add_to_cart, 'seller_alt':seller_alt, 'seller_link':seller_link, 'comment':comments, 'seller_rating_percents':seller_rating_percents,'seller_ratinngs':seller_ratinngs, 'amazon_fulfilled':amz_fullfill})

                    #print sellers_info, comments
                #print response.xpath('//span[@class="a-button a-button-selected a-button-toggle"]/span/a/text()').extract()
                try: color = response.xpath('//span[@class="a-button a-button-selected a-button-toggle"]/span/a/text()').extract()[1].replace("\n",'').replace('\t','').strip()
                except: color="" 
                try: size = response.xpath('//span[@class="a-button a-button-selected a-button-toggle"]/span/a/text()').extract()[0].replace("\n",'').replace('\t','').strip()
                except: size="" 
                #print color, "dddddddd"
                item = Amazon_upc_out()
                item['title'] =  title
                item['product_id'] = response.meta['id']
                item['seller_info'] = json.dumps(sellers_info)
                item['seller_count'] = len(sellers_info)
                item['url']=response.url
                #if attr.get('UPC','').find("_")>-1: 
                #    item['upc']=attr.get('UPC','').split("_")[0]
                #    item['comp']= 'Alt'
                #else: 
                #    item['upc']=attr.get('UPC','')
                #    item['comp']= ''
                item['date_timestamp']= int(time.time())
                item['spider'] = self.name
                #item['job_id'] = attr['job_id']
                #item['body'] = response.body
                #print base64.decodestring(item['body'])
                yield item
            else:
                if no_found:
                    item = Amazon_upc_out()
                    item['product_id'] = response.meta['id']
                    item['url']=response.url
                    item['upc']=attr.get('UPC','')
                    item['seller_info'] =  []
                    item['seller_count'] = 0
                    item['date_timestamp']= int(time.time())
                    item['spider'] = self.name
                    #item['job_id'] = attr['job_id']
                    #if attr.get('UPC','').find("_")>-1: 
                    #    item['upc']=attr.get('UPC','').split("_")[0]
                    #    item['comp'] = 'Alt'
                    #else: 
                    #    item['upc']=attr.get('UPC','')
                    #    item['comp'] = ''
                    #item['body'] = response.body  

                    yield item
                else:
                    try:
                        result = response.xpath('//meta[2]/@content').extract()[0].find('404.html')
                        if result>-1:
                            item = Amazon_upc_out()
                            item['product_id'] = response.meta['id']
                            item['url']=response.url
                            #item['upc']=attr.get('UPC','')
                            item['seller_info'] =  []
                            item['seller_count'] = 0
                            item['date_timestamp']= int(time.time())
                            item['spider'] = self.name
                            #item['job_id'] = attr['job_id']
                            item['title'] = 'Not Found'
                            #if attr.get('UPC','').find("_")>-1: 
                            #    item['upc']=attr.get('UPC','').split("_")[0]
                            #    item['comp'] = 'Alt'
                            #else: 
                            #    item['upc']=attr.get('UPC','')
                            #    item['comp'] = ''
                            #item['body'] = response.body                              
                            yield item
                        result = response.xpath('//meta[2]/@content').extract()[0].find('amazon.com')
                        if result>-1:
                            item = Amazon_upc_out()
                            item['product_id'] = response.meta['id']
                            item['url']=response.url
                            #item['upc']=attr.get('UPC','')
                            item['seller_info'] =  []
                            item['seller_count'] = 0
                            item['date_timestamp']= int(time.time())
                            item['spider'] = self.name
                            #item['job_id'] = attr['job_id']
                            item['title'] = response.xpath('//meta[2]/@content').extract()[0]
                            #if attr.get('UPC','').find("_")>-1: 
                            #    item['upc']=attr.get('UPC','').split("_")[0]
                            #    item['comp'] = 'Alt'
                            #else: 
                            #    item['upc']=attr.get('UPC','')
                            #    item['comp'] = ''
                            #item['body'] = response.body  
                            yield item                 
                    except:raise
        except:
            raise