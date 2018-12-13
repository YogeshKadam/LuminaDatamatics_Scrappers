import scrapy
import urllib
from amazon_new.items2 import Amazon_upc_out
import os
import time
import json

class amazonSpider(scrapy.Spider):
    imgcount = 1
    name = "amz_seller_de"
    allowed_domains = []

    start_urls = ["http://www.flipkart.com/search?q=9780005996218" ]  

    def parse(self,response):

        urls_done = [

]

        urls =[
["1","B000122BS6"],
["2","B000SO2IPI"],
["3","B000U3WHQW"],
["4","B00X0VNDPU"],
["5","B000122SC0"],
["6","B0013FB51E"],
["7","B0013DEJ7S"],
["8","B00IHJZRWC"],
["9","B000KJMIIS"],
["10","B000TK7VK8"],
["11","B01J629SS2"],
["12","B0012QCIUG"],
["13","B014721YZ6"],
["14","B01N294KL1"],
["15","B01B5A9IVA"],
["16","B01B5Z6RGE"],
["17","B000TKB9WE"],
["18","B01DZXWVE6"],
["1","B00304ROY8","competitor"],
["2","B000I5SAUO","competitor"],
]
        for url in urls:
            try:
                req = scrapy.Request( "https://www.amazon.de/gp/offer-listing/" + url[1] +"/ref=dp_olp_new?ie=UTF8&condition=new" , headers={'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://www.amazon.com/Inspiron-Performance-Flagship-Touchscreen-Bluetooth/dp/B071GPZB2M/ref=sr_1_2?s=pc&ie=UTF8&qid=1503680901&sr=1-2-spons&keywords=laptop&psc=1' }, callback=self.parse6)
                req.meta['item_id']=url[1]
                req.meta['product_id']=url[0]
                req.cookies = { 'lc-main':'en_US', 'x-wl-uid':'1yE71wxptnrPGpU96MVpeAljDAxEwlHAMNmRkGH3kTDbQNlw65AKYm8JBd2Nm33DfONRPH48N1DRE/phePYv7b8VzqI5P36U503gVSzRJSBmwDQKne/e/xfe/X3r9TLt9Mq2dGxVnAVsmo8PkOTlUOw==', 'skin':'noskin', 'x-main':'X2Uw?4D0ZsoVUNTB1ND?IqOhj4jrdt3SQM?nwPoWs2Vra8r9I13YbE1V8fqOmIli', 'at-main':'Atza|IwEBIM6arSMDjanfYsyURnaqmNeb87cZy6ift3_Ewd6ai-VCWQxN1VU8u-feDM43rwF2oZopky98QowPRIgSVmpR_qWGQgSAAMl_YsBf2E0nGom_GkU0Vl5JNLdIaGZ9g-Je-Uld-_qAa3onwe2Q_rUKPCN6j5PAu_78gARA9l5GI48so08VSR_tDyWO8p_WHTqj2dJMXqKZ-6YuhyOYGPbSFgupS_O-PofP6d9lqKlLtruDVDv98__UgkmhRmUXWTt3X3G_2ALthXr4_8tBnT4VpdNEWYqZKsJF0xej6dixrNlFNWoKyK-jojctn-E95wf1GmItDzSmmwM-fzp8LRptCncE_vJEfXTPknNoUcz2qoYx2kBsuYOviBUZSAONWCXII68hZD4SILOFPKAMmAXRBswx', 'sess-at-main':'hTCj4tFy0geBzyuGIGBYRUfOmwxbmm3iJjvmeMi/emE=', 'JSESSIONID':'C70160F1BC7EC0B9D5E1BD946AA543DF', 'csm-hit':'J1CK3EMBJCQHNYC6PB4P+s-CB6DMAQSAGGJC2C8H354|1503728162175', 'session-token':'n2Bkr05TMvQYIlxStLEPDDdd8KmwvXszRPl41nyUA+1+hlViB/+whjJG3jQjbUov8lRYLkN78KFEgYKt3ZQZjLd8PKw5Sp8DO2anI7lIo5iA5ZlBkkhTAAEz6qxH9pejQawVHIgLmQ0WLVWeZup/JQGwjoNITTENdcZ9A+C55Nfj0eEwqpNI661A1pvmaG9Y2hCGn0xf/zWQnGeus1aGeF6u3GdgzUTVEoqoashearQ8cngRhV/i0uxZoqRJly4ivJIy43Khphvj7Z++9vFB3w==', 'ubid-main':'131-1502033-8002851', 'session-id-time':'2082787201l', 'session-id':'130-6537552-1339612'}
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
        try:

            res = response.xpath('//div[@class="a-row a-spacing-mini olpOffer"]')
            try: title= " ".join(response.xpath('//*[@id="olpProductDetails"]/div[1]/h1/text()').extract()).replace("\n",'').replace('\t','').strip()
            except: title=''
            if res:
                sellers_info = [] 
                for data in res:
                    
                    try:price = data.xpath('div/span[@class="a-size-large a-color-price olpOfferPrice a-text-bold"]/text()').extract()[0].encode('ascii','ignore').strip()
                    except: raise
                    shipping_price = " ".join(data.xpath('div/p[@class="olpShippingPrice"]/span/text()').extract()).replace("\n",'').replace('\t','').strip()
                    if not shipping_price:shipping_price = " ".join(data.xpath('div/p/span/span/text()').extract()).replace("\n",'').replace('\t','').strip()
                    if not shipping_price: shipping_price = " ".join(data.xpath('div/p[@class="olpShippingInfo"]/span/text()').extract()).replace("\n",'').replace('\t','').strip()
                    comments = " ".join(data.xpath('div/div/text()').extract()).replace("\n",'').replace('\t','').strip() +" "+ " ".join(data.xpath('div/div/div/text()').extract()).replace("\n",'').replace('\t','').strip()
                    seller_name =   " ".join(data.xpath('div/h3/span/a/text()').extract()).replace("\n",'').replace('\t','').strip()
                    seller_alt = "".join(data.xpath('div/h3/img/@alt').extract()).replace("\n",'').replace('\t','').strip()
                    if not seller_alt: seller_alt = "".join(data.xpath('div/h3/a/img/@alt').extract()).replace("\n",'').replace('\t','').strip()
                    seller_link =   " ".join(data.xpath('div/h3/span/a/@href').extract()).replace("\n",'').replace('\t','').strip()
                    seller_rating_percents = " ".join(data.xpath('div/p/a/b/text()').extract()).replace("\n",'').replace('\t','').strip()
                    seller_ratinngs = " ".join(data.xpath('div/p/text()').extract()).replace("\n",'').replace('\t','').strip()
                    amz_fullfill=" ".join(data.xpath('div[3]/div/div/span/a/text()').extract()).replace("\n",'').replace('\t','').strip()
                    if not amz_fullfill: amz_fullfill=" ".join(data.xpath('div[4]/div/div/span/a/text()').extract()).replace("\n",'').replace('\t','').strip()
                    if amz_fullfill: amz_fullfill='FBA'
                    else : amz_fullfill='MFN'
                    sellers_info.append({'price':price,'ship_price':shipping_price, 'seller':seller_name, 'seller_alt':seller_alt, 'seller_link':seller_link, 'comment':comments, 'seller_rating_percents':seller_rating_percents,'seller_ratinngs':seller_ratinngs, 'amazon_fulfilled':amz_fullfill})

                    #print sellers_info, comments
                print response.xpath('//span[@class="a-button a-button-selected a-button-toggle"]/span/a/text()').extract()
                try: color = response.xpath('//span[@class="a-button a-button-selected a-button-toggle"]/span/a/text()').extract()[1].replace("\n",'').replace('\t','').strip()
                except: color="" 
                try: size = response.xpath('//span[@class="a-button a-button-selected a-button-toggle"]/span/a/text()').extract()[0].replace("\n",'').replace('\t','').strip()
                except: size="" 
                #print color, "dddddddd"
                item = Amazon_upc_out()
                item['title'] =  title
                item['dpid'] = response.meta['id']
                item['seller_info'] =  json.dumps(sellers_info)
                item['url']=response.url
                item['upc']="'"+response.meta['upc']+ "'"
                item['date_timestamp']= int(time.time())
                item['spider'] = self.name
                item['product_id']=response.meta['product_id']
                item['is_competitor']=response.meta['is_competitor']
                item['body'] = response.body
                yield item


        except:
            raise