



#Amazon seller list spider
import time
import scrapy
import json
    
	
	
class ZwItem(scrapy.Item):
    title = scrapy.Field()
    listprice = scrapy.Field()
    saleprice = scrapy.Field()
    url=scrapy.Field()
    brand=scrapy.Field()
    breadcrumb=scrapy.Field()
    mpn=scrapy.Field()
    uniqueid=scrapy.Field()
    ean=scrapy.Field()
    productstatus=scrapy.Field()


class ZwSpider(scrapy.Spider):
    
    name = "zw_productinfo"
    allowed_domain=[]
    start_urls = ['https://www.zweiradteile.net/']
    #start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ['https://www.amazon.com/musical-instruments-accessories-sound-recording/b/ref=nav_shopall_mi_ce?ie=UTF8&node=11091801']
    
    

    def parse(self, response):
        urls_done=[]
        urls=[
"https://www.zweiradteile.net/detail/index/sArticle/34582",
"https://www.zweiradteile.net/zubehoer/faltgarage/28827/faltgarage/abdeckplane-fuer-bmw-roller-c1-125ccm-200cm-ueberdacht",
"https://www.zweiradteile.net/detail/index/sArticle/35779",
]
        
        for url in urls:
            try:
                req = scrapy.Request( url , callback=self.parse1)
                #req.meta['item_id']=url
                #req.cookies = { 'lc-main':'en_US', 'x-wl-uid':'1yE71wxptnrPGpU96MVpeAljDAxEwlHAMNmRkGH3kTDbQNlw65AKYm8JBd2Nm33DfONRPH48N1DRE/phePYv7b8VzqI5P36U503gVSzRJSBmwDQKne/e/xfe/X3r9TLt9Mq2dGxVnAVsmo8PkOTlUOw==', 'skin':'noskin', 'x-main':'X2Uw?4D0ZsoVUNTB1ND?IqOhj4jrdt3SQM?nwPoWs2Vra8r9I13YbE1V8fqOmIli', 'at-main':'Atza|IwEBIM6arSMDjanfYsyURnaqmNeb87cZy6ift3_Ewd6ai-VCWQxN1VU8u-feDM43rwF2oZopky98QowPRIgSVmpR_qWGQgSAAMl_YsBf2E0nGom_GkU0Vl5JNLdIaGZ9g-Je-Uld-_qAa3onwe2Q_rUKPCN6j5PAu_78gARA9l5GI48so08VSR_tDyWO8p_WHTqj2dJMXqKZ-6YuhyOYGPbSFgupS_O-PofP6d9lqKlLtruDVDv98__UgkmhRmUXWTt3X3G_2ALthXr4_8tBnT4VpdNEWYqZKsJF0xej6dixrNlFNWoKyK-jojctn-E95wf1GmItDzSmmwM-fzp8LRptCncE_vJEfXTPknNoUcz2qoYx2kBsuYOviBUZSAONWCXII68hZD4SILOFPKAMmAXRBswx', 'sess-at-main':'hTCj4tFy0geBzyuGIGBYRUfOmwxbmm3iJjvmeMi/emE=', 'JSESSIONID':'C70160F1BC7EC0B9D5E1BD946AA543DF', 'csm-hit':'J1CK3EMBJCQHNYC6PB4P+s-CB6DMAQSAGGJC2C8H354|1503728162175', 'session-token':'n2Bkr05TMvQYIlxStLEPDDdd8KmwvXszRPl41nyUA+1+hlViB/+whjJG3jQjbUov8lRYLkN78KFEgYKt3ZQZjLd8PKw5Sp8DO2anI7lIo5iA5ZlBkkhTAAEz6qxH9pejQawVHIgLmQ0WLVWeZup/JQGwjoNITTENdcZ9A+C55Nfj0eEwqpNI661A1pvmaG9Y2hCGn0xf/zWQnGeus1aGeF6u3GdgzUTVEoqoashearQ8cngRhV/i0uxZoqRJly4ivJIy43Khphvj7Z++9vFB3w==', 'ubid-main':'131-1502033-8002851', 'session-id-time':'2082787201l', 'session-id':'130-6537552-1339612'}
                #req.cookies = {'__csrf_token-1':'xKVo4VZJqkyblSjFlWzEehgUFyHAQg', 'nocache':'detail-1', 'x-ua-device':'tablet', '_ga':'GA1.2.2072088434.1505733636', '_gid':'GA1.2.1081983427.1506316742', 'session-1':'8e46a0f8054191632d15e31849c5862d483ca54447ec216fce4403cd7e3c21de' }
                if url not in urls_done:
                    yield req
            
            except: raise

    def parse1(self, response):
        item=ZwItem()
        title=response.xpath('//*[@class="product--header"]/div/h1/text()').extract()
        item['title']=("".join(title)).replace("\t","").replace("\n","").replace("\r","")
        brand=response.xpath('//*[@class="product--header"]/div/div[@class="product--supplier"]/a/img/@alt').extract()
        item['brand']=brand[0].replace("\n","").replace("\t","").replace("\r","")
        uniqueid=response.xpath('//*[@class="base-info--entry entry--sku"]/span[@class="entry--content"]/text()').extract()
        item['uniqueid']=uniqueid[0].replace("\n","").replace("\t","").replace("\r","")
        breadcrumblist=response.xpath('//*[@class="breadcrumb--list"]/li/a/span/text()').extract()
        item['breadcrumb']=" > ".join(breadcrumblist)
        item['url']=response.url

        listprice=response.xpath('//*[@class="product--price price--default"]/span/text()').extract()
        item['listprice']="".join(listprice).replace("\n","")
        """if response.xpath('//*[@id="ab-textrechts"]/p[2]/text()[3]').extract():
            if response.xpath('//*[@id="ab-textrechts"]/p[2]/text()[3]').extract()[0].find('OEM Nr.:') > -1:
                mpn=response.xpath('//*[@id="ab-textrechts"]/p[2]/text()[3]').extract()[0]
                item['mpn']=mpn.replace("\n","").replace("\t","").replace("\r","").replace("OEM Nr.:","")
            else:
                item['mpn']=""
        else:
            item['mpn']=""
        if response.xpath('//*[@class="ab2 posdown"]/span[@class="throughblack"]/text()').extract():
            listprice=response.xpath('//*[@class="ab2 posdown"]/span[@class="throughblack"]/text()').extract()[0]
            item['listprice']=listprice
            salelist=response.xpath('//*[@id="preis-produkt"]/p[1]/text()').extract()
            saleprice="".join(salelist).replace("\n","").replace("\t","").replace("\r","").replace(" ","").replace("EUR", " EUR")
            item['saleprice']=saleprice
        else:
            listlist=response.xpath('//*[@id="preis-produkt"]/p[1]//text()').extract()
            listprice="".join(listlist).replace("\n","").replace("\t","").replace("\r","").replace(" ","").replace("EUR", " EUR")
            item['listprice']=listprice
            item['saleprice']=""
"""
        yield item
