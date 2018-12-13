



#Amazon seller list spider
import time
import scrapy
import json
    
	
	
class BtItem(scrapy.Item):
    title = scrapy.Field()
    listprice = scrapy.Field()
    saleprice = scrapy.Field()
    url=scrapy.Field()
    #brand=scrapy.Field()
    breadcrumb=scrapy.Field()
    mpn=scrapy.Field()
    uniqueid=scrapy.Field()
    ean=scrapy.Field()
    productstatus=scrapy.Field()


class BtSpider(scrapy.Spider):
    
    name = "bt_productinfo3"
    allowed_domain=[]
    start_urls = ['https://www.biketeile-service.de/']
    #start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ['https://www.amazon.com/musical-instruments-accessories-sound-recording/b/ref=nav_shopall_mi_ce?ie=UTF8&node=11091801']
    
    

    def parse(self, response):
        urls_done=[]
        urls=[
"https://www.biketeile-service.de/en/tyreserviceandaccessories/tyretransportbag/reifensackgrossrl100st.html",
"https://www.biketeile-service.de/en/tyreserviceandaccessories/tyretransportbag/reifensackrl100stueck300165.html",
"https://www.biketeile-service.de/en/tyreserviceandaccessories/tyretransportbag/reifensackrl100stueck309735.html",
"https://www.biketeile-service.de/en/workshopconsumables/wheelandtyres/tyreservice/tyreprotection/reifenschutz.html",
"https://www.biketeile-service.de/en/tyreserviceandaccessories/tyretransportbag/tyretransportbaglarge.html",
"https://www.biketeile-service.de/en/tyreserviceandaccessories/tyretransportbag/tyretransportbagsmall.html",
"https://www.biketeile-service.de/en/tyreserviceandaccessories/tyretransportbag/tyretransportbagmedium.html",
"https://www.biketeile-service.de/en/wheelandtyre/mowertyres/8inch/tyre/40084prst11set.html",
"https://www.biketeile-service.de/en/wheelandtyre/mowertyres/8inch/tyre/48040086prst81set.html",
"https://www.biketeile-service.de/en/wheelandtyre/mowertyres/8inch/tyre/reifen16x65084prtl.html",
"https://www.biketeile-service.de/en/wheelandtyre/mowertyres/8inch/tyre/reifen18x65084prtl.html",
"https://www.biketeile-service.de/en/wheelandtyre/mowertyres/8inch/tyre/reifen18x85084prtl.html",
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
        item=BtItem()
        title=response.xpath('//*[@id="sectionpad"]/section/div/div[2]/div[1]/div/h1/text()').extract()
        item['title']=("".join(title)).replace("\t","").replace("\n","").replace("\r","")
        #brand=response.xpath('//*[@class="col_275"]/div/a/img/@alt').extract()
        #item['brand']=brand[0]
        breadcrumblist=response.xpath('//*[@id="sectionpad"]/div[@class="navtrail"]/span//text()').extract()
                
        item['breadcrumb']=" > ".join(breadcrumblist)
        item['url']=response.url
        uniqueid=response.xpath('//*[@id="sectionpad"]/section/div/div[2]/div[2]/div[2]/span[@itemprop="productID"]/text()').extract()
        item['uniqueid']=uniqueid[0]
        ean=response.xpath('//*[@id="sectionpad"]/section/div/div[2]/div[2]/div[2]/meta/@content').extract()
        if ean:
            item['ean']=ean[0]
        else:
            item['ean']=""
        #modelnumber=response.xpath('//*[@class="col_275"]/div[3]/span/text()').extract()
        #item['modelnumber']=modelnumber[0]
        if response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[1]/text()').extract()[0].find("Hers") > -1 or response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[1]/text()').extract()[0].find("Manufacturer Nr.") > -1:
            mpn=response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[1]/text()').extract()[0]
        elif response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[2]/text()').extract()[0].find("Hers") > -1 or response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[2]/text()').extract()[0].find("Manufacturer Nr.") > -1:
            mpn=response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[2]/text()').extract()[0]
        elif response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[3]/text()').extract()[0].find("Hers") > -1 or response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[3]/text()').extract()[0].find("Manufacturer Nr.") > -1:
            mpn=response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[3]/text()').extract()[0]
        elif response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[4]/text()').extract()[0].find("Hers") > -1 or response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[4]/text()').extract()[0].find("Manufacturer Nr.") > -1:
            mpn=response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[4]/text()').extract()[0]
        elif response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[5]/text()').extract()[0].find("Hers") > -1 or response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[5]/text()').extract()[0].find("Manufacturer Nr.") > -1:
            mpn=response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[5]/text()').extract()[0]
        elif response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[6]/text()').extract()[0].find("Hers") > -1 or response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[6]/text()').extract()[0].find("Manufacturer Nr.") > -1:
            mpn=response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[6]/text()').extract()[0]
        elif response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[7]/text()').extract()[0].find("Hers") > -1 or response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[7]/text()').extract()[0].find("Manufacturer Nr.") > -1:
            mpn=response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[7]/text()').extract()[0]
        elif response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[8]/text()').extract()[0].find("Hers") > -1 or response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[8]/text()').extract()[0].find("Manufacturer Nr.") > -1:
            mpn=response.xpath('//*[@id="desc"]/article[@itemprop="description"]/p[8]/text()').extract()[0]
        item['mpn']=mpn.replace('Manufacturer Nr.:','')
        saleprice=response.xpath('//*[@id="product_info_price"]/div/span/text()').extract()
        if not saleprice: saleprice=response.xpath('//*[@id="product_info_price"]/span/span[2]/text()').extract()
        item['saleprice']=saleprice[0]
        listprice=response.xpath('//*[@id="product_info_price"]/span/span[@class="product_info_old"]/span/text()').extract()
        if listprice: item['listprice']=listprice[0]
        else: item['listprice']=saleprice[0]

        #productstatuscomment="".join(response.xpath('//*[@id="ctl10_ctl00_ctl04_divCart"]/a/text()').extract()).replace("\r","").replace("\n","").replace(" ","")
        if response.xpath('//*[@id="sectionpad"]/section/div/div[2]/div[2]/div[2]/img/@alt').extract()[0]=="100000":
            item['productstatus']="A"
        elif response.xpath('//*[@id="sectionpad"]/section/div/div[2]/div[2]/div[2]/img/@alt').extract()[0]=="0":
            item['productstatus']="NA"
        yield item