



#Amazon seller list spider
import time
import scrapy
import json
    
	
	
class UkmotorsItem(scrapy.Item):
    title = scrapy.Field()
    listprice = scrapy.Field()
    saleprice = scrapy.Field()
    url=scrapy.Field()
    brand=scrapy.Field()
    breadcrumb=scrapy.Field()
    mpn=scrapy.Field()
    uniqueid=scrapy.Field()



class UkmotorsSpider(scrapy.Spider):
    
    name = "ukmotors_productinfo2"
    allowed_domain=[]
    start_urls = ['https://uk-motors.de/']
    #start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ['https://www.amazon.com/musical-instruments-accessories-sound-recording/b/ref=nav_shopall_mi_ce?ie=UTF8&node=11091801']
    
    

    def parse(self, response):
        Header1= {'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://uk-motors.de/angebote/' , 'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0'}
        urls_done=[]
        urls=[
"https://uk-motors.de/pflegemittel/felge-reifen-gummi/34987/3m-schutz-und-pflegecreme-handprotect-250ml-hautschutz?c=267",
"https://uk-motors.de/pflegemittel/felge-reifen-gummi/34026/presto-felgen-schutz-wachs-383465-500ml-felge-reinigung-felgenpflege?c=267",
"https://uk-motors.de/pflegemittel/felge-reifen-gummi/34025/presto-felgenreiniger-383328-500ml-felge-reinigung-felgenpflege?c=267",
"https://uk-motors.de/pflegemittel/felge-reifen-gummi/31908/presto-reifenglanz-383458-600ml?c=267",
"https://uk-motors.de/pflegemittel/felge-reifen-gummi/31912/presto-gummi-kunststoff-pflege-383441-600ml?c=267",
"https://uk-motors.de/pflegemittel/felge-reifen-gummi/31765/presto-silikon-spray-429774-150ml-gummi-und-kunststoffpflege?c=267",
"https://uk-motors.de/pflegemittel/felge-reifen-gummi/31541/sonax-felgenbuerste-ultra-soft-417541?c=267",
"https://uk-motors.de/pflegemittel/felge-reifen-gummi/29274/sonax-gummipflegestift-18g-499000?c=267",
"https://uk-motors.de/pflegemittel/felge-reifen-gummi/29227/sonax-felgenversiegelung-400ml-436300?c=267",
"https://uk-motors.de/pflegemittel/felge-reifen-gummi/29226/sonax-reifenpfleger-400ml-435300?c=267",
]
        
        for url in urls:
            try:
                req = scrapy.Request( url , headers=Header1, callback=self.parse1)
                req.cookies = {'__csrf_token-1':'xKVo4VZJqkyblSjFlWzEehgUFyHAQg', 'nocache':'detail-1', 'x-ua-device':'tablet', '_ga':'GA1.2.2072088434.1505733636', '_gid':'GA1.2.1081983427.1506316742', 'session-1':'8e46a0f8054191632d15e31849c5862d483ca54447ec216fce4403cd7e3c21de' }
                #req.meta['item_id']=url
                #req.cookies = { 'lc-main':'en_US', 'x-wl-uid':'1yE71wxptnrPGpU96MVpeAljDAxEwlHAMNmRkGH3kTDbQNlw65AKYm8JBd2Nm33DfONRPH48N1DRE/phePYv7b8VzqI5P36U503gVSzRJSBmwDQKne/e/xfe/X3r9TLt9Mq2dGxVnAVsmo8PkOTlUOw==', 'skin':'noskin', 'x-main':'X2Uw?4D0ZsoVUNTB1ND?IqOhj4jrdt3SQM?nwPoWs2Vra8r9I13YbE1V8fqOmIli', 'at-main':'Atza|IwEBIM6arSMDjanfYsyURnaqmNeb87cZy6ift3_Ewd6ai-VCWQxN1VU8u-feDM43rwF2oZopky98QowPRIgSVmpR_qWGQgSAAMl_YsBf2E0nGom_GkU0Vl5JNLdIaGZ9g-Je-Uld-_qAa3onwe2Q_rUKPCN6j5PAu_78gARA9l5GI48so08VSR_tDyWO8p_WHTqj2dJMXqKZ-6YuhyOYGPbSFgupS_O-PofP6d9lqKlLtruDVDv98__UgkmhRmUXWTt3X3G_2ALthXr4_8tBnT4VpdNEWYqZKsJF0xej6dixrNlFNWoKyK-jojctn-E95wf1GmItDzSmmwM-fzp8LRptCncE_vJEfXTPknNoUcz2qoYx2kBsuYOviBUZSAONWCXII68hZD4SILOFPKAMmAXRBswx', 'sess-at-main':'hTCj4tFy0geBzyuGIGBYRUfOmwxbmm3iJjvmeMi/emE=', 'JSESSIONID':'C70160F1BC7EC0B9D5E1BD946AA543DF', 'csm-hit':'J1CK3EMBJCQHNYC6PB4P+s-CB6DMAQSAGGJC2C8H354|1503728162175', 'session-token':'n2Bkr05TMvQYIlxStLEPDDdd8KmwvXszRPl41nyUA+1+hlViB/+whjJG3jQjbUov8lRYLkN78KFEgYKt3ZQZjLd8PKw5Sp8DO2anI7lIo5iA5ZlBkkhTAAEz6qxH9pejQawVHIgLmQ0WLVWeZup/JQGwjoNITTENdcZ9A+C55Nfj0eEwqpNI661A1pvmaG9Y2hCGn0xf/zWQnGeus1aGeF6u3GdgzUTVEoqoashearQ8cngRhV/i0uxZoqRJly4ivJIy43Khphvj7Z++9vFB3w==', 'ubid-main':'131-1502033-8002851', 'session-id-time':'2082787201l', 'session-id':'130-6537552-1339612'}
                #req.cookies = {'__csrf_token-1':'xKVo4VZJqkyblSjFlWzEehgUFyHAQg', 'nocache':'detail-1', 'x-ua-device':'tablet', '_ga':'GA1.2.2072088434.1505733636', '_gid':'GA1.2.1081983427.1506316742', 'session-1':'8e46a0f8054191632d15e31849c5862d483ca54447ec216fce4403cd7e3c21de' }
                if url not in urls_done:
                    yield req
            
            except: raise

    def parse1(self, response):
        item=UkmotorsItem()
        title=response.xpath('//*[@class="product--info"]/h1/text()').extract()
        item['title']=("".join(title)).replace("\t","").replace("\n","").replace("\r","")
        brand=response.xpath('//*[@class="product--header"]/div/div[@class="product--supplier"]/a/img/@alt').extract()
        if brand: item['brand']=brand[0].replace("\n","").replace("\t","").replace("\r","")
        else: item['brand']=""
        uniqueid=response.xpath('//*[@class="base-info--entry entry--sku"]/span[@class="entry--content"]/text()').extract()
        item['uniqueid']=uniqueid[0].replace("\n","").replace("\t","").replace("\r","")
        breadcrumblist=response.xpath('//*[@class="breadcrumb--list"]/li/a/span/text()').extract()
        item['breadcrumb']=" > ".join(breadcrumblist)
        item['url']=response.url


        if response.xpath('//*[@class="content--discount"]/span/text()').extract():
            listprice=response.xpath('//*[@class="content--discount"]/span/text()').extract()
            item['listprice']="".join(listprice).replace("\n","").replace("*","")
            salelist=response.xpath('//*[@class="price--content content--default"]/text()').extract()
            saleprice="".join(salelist).replace("\n","").replace("\t","").replace("\r","").replace(" ","").replace("*","")
            item['saleprice']=saleprice
        else:
            listlist=response.xpath('//*[@class="price--content content--default"]/text()').extract()
            listprice="".join(listlist).replace("\n","").replace("\t","").replace("\r","").replace(" ","").replace("*","")
            item['listprice']=listprice
            item['saleprice']=""
            
        if response.xpath('//*[@class="product--base-info list--unstyled"]/li[3]/span/text()').extract():
            mpn=response.xpath('//*[@class="product--base-info list--unstyled"]/li[3]/span/text()').extract()[0]
            item['mpn']=mpn.replace("\n","").replace("\t","").replace("\r","")

        yield item
