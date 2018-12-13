



#Amazon seller list spider
import time
import scrapy
import json
    
	
	
class MotiaItem(scrapy.Item):
    title = scrapy.Field()
    listprice = scrapy.Field()
    saleprice = scrapy.Field()
    url=scrapy.Field()
    brand=scrapy.Field()
    breadcrumb=scrapy.Field()
    modelnumber=scrapy.Field()
    mpn=scrapy.Field()
    uniqueid=scrapy.Field()
    productstatus=scrapy.Field()


class MotiaSpider(scrapy.Spider):
    
    name = "motia_productinfo2"
    allowed_domain=[]
    start_urls = ['http://www.motea.com/']
    #start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ['https://www.amazon.com/musical-instruments-accessories-sound-recording/b/ref=nav_shopall_mi_ce?ie=UTF8&node=11091801']
    
    

    def parse(self, response):
        urls_done=[]
        urls=[
"http://www.motea.com/side-panels/side-cover-panel-puig-ktm-1190-adventure-r-13-16-black-mat-i4029-49496-0.htm",
"http://www.motea.com/side-panels/cooler-side-cover-puig-yamaha-mt-09-13-16-black-mat-i4029-33116-0.htm",
"http://www.motea.com/side-panels/side-cover-panel-puig-yamaha-xt-1200-z-super-tenere-10-17-black-mat-i4029-49498-0.htm",
"http://www.motea.com/side-panels/side-cover-panel-puig-bmw-r-ninet/scrambler/pure/racer/urban-g/s-14-17-silver-i4029-287783-0.htm",
"http://www.motea.com/side-panels/side-cover-panel-puig-bmw-r-1200-r-15-16-black-mat-i4029-269497-0.htm",
"http://www.motea.com/side-panels/side-cover-panel-puig-ktm-1290-super-adventure-s-2017-black-mat-i4029-278902-0.htm",
"http://www.motea.com/side-panels/cooler-side-cover-puig-yamaha-mt-07-13-17-black-mat-i4029-41679-0.htm",
"http://www.motea.com/side-panels/side-cover-panel-puig-yamaha-mt-09-13-17-black-mat-i4029-49494-0.htm",
"http://www.motea.com/side-panels/side-cover-panel-puig-bmw-r-1200-rt-14-16-black-mat-i4029-86664-0.htm",
"http://www.motea.com/side-panels/side-cover-panel-puig-ktm-1290-super-adventure-15-16-black-mat-i4029-87914-0.htm",
"http://www.motea.com/side-panels/side-cover-panel-puig-bmw-r-1200-gs-13-17-black-i4029-32772-0.htm",
"http://www.motea.com/side-panels/side-cover-panel-puig-yamaha-mt-09-tracer-15-17-black-mat-i4029-269477-0.htm",
"http://www.motea.com/side-panels/side-cover-panel-puig-ktm-1050-adventure-15-16-black-mat-i4029-60325-0.htm",
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
        item=MotiaItem()
        title=response.xpath('//*[@class="col_530"]/div[1]/h1//text()').extract()
        item['title']=("".join(title)).replace("\t","").replace("\n","").replace("\r","").replace("                        ","")
        brand=response.xpath('//*[@class="col_275"]/div/a/img/@alt').extract()
        if brand:
            item['brand']=brand[0]
        else:
            item['brand']=''
        breadcrumblist=response.xpath('//*[@class="breadcrumb clear"]/*[not(self::div/@class="breadcrumb_arrow")]')
        breadcrumblist1=[]
        for breadcrumbs in breadcrumblist:
            if breadcrumbs.xpath('a/text()').extract():
                breadcrumblist1.append(breadcrumbs.xpath('a/text()').extract()[0].replace("\r","").replace("\n","").replace(" ",""))
            else:
                breadcrumblist1.append(breadcrumbs.xpath('text()').extract()[0])
        #print "BREADCRUMB : ",breadcrumblist1
        item['breadcrumb']=" > ".join(breadcrumblist1)
        item['url']=response.url
        uniqueid=response.xpath('//*[@class="col_275"]/p/span/text()').extract()
        item['uniqueid']=uniqueid[0]
        modelnumber=response.xpath('//*[@class="col_275"]/div[3]/span/text()').extract()
        item['modelnumber']=modelnumber[0]

        item['mpn']=modelnumber[0]
        listprice=response.xpath('//*[@id="ctl10_ctl00_ctl04_lblPrice"]/span[@class="priceDiscount"]/text()').extract()
        if listprice:
            item['listprice']=listprice[0]
        else:
            item['listprice']=''
        saleprice=response.xpath('//*[@id="ctl10_ctl00_ctl04_lblPrice"]/span/span/text()').extract()
        item['saleprice']=saleprice[0]
        productstatuscomment="".join(response.xpath('//*[@id="ctl10_ctl00_ctl04_divCart"]/a/text()').extract()).replace("\r","").replace("\n","").replace(" ","")
        if productstatuscomment.upper() == 'INDENWARENKORB':
            item['productstatus']="A"
        else:
            item['productstatus']="NA"
        yield item
