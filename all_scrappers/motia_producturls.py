



#Amazon seller list spider
import time
import scrapy
import json
    
	
	
class MotiaItem(scrapy.Item):
    categoryurl=scrapy.Field()
    producturl=scrapy.Field()


class MotiaSpider(scrapy.Spider):
    
    name = "motia_producturls"
    allowed_domain=[]
    start_urls = ['http://www.motea.com/']
    #start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ['https://www.amazon.com/musical-instruments-accessories-sound-recording/b/ref=nav_shopall_mi_ce?ie=UTF8&node=11091801']
    
    

    def parse(self, response):
        urls=[
"http://www.motea.com/en/sale-c4034.htm",
"http://www.motea.com/en/anodised--alu-parts-c483.htm",
"http://www.motea.com/en/exhausts-c3176.htm",
"http://www.motea.com/en/lighting--electrics-c4051.htm",
"http://www.motea.com/en/brake--and-clutch-levers-c985.htm",
"http://www.motea.com/en/belly-pans-c10.htm",
"http://www.motea.com/en/carbon-parts-c780.htm",
"http://www.motea.com/en/styling--protection-c400.htm",
"http://www.motea.com/en/footrests-brake--gear-lever-c3633.htm",
"http://www.motea.com/en/luggage-c3979.htm",
"http://www.motea.com/en/centre-stand-c3976.htm",
"http://www.motea.com/en/motorcycle-helmets-c379.htm",
"http://www.motea.com/en/tail-tidies-c2981.htm",
"http://www.motea.com/en/chain-guard-c4027.htm",
"http://www.motea.com/en/mud-guards-c44.htm",
"http://www.motea.com/en/radiator-covers-c4025.htm",
"http://www.motea.com/en/light-bar-c3977.htm",
"http://www.motea.com/en/handlebars--accessoires-c3972.htm",
"http://www.motea.com/en/paddock-stands-c495.htm",
"http://www.motea.com/en/disc-locks-c4164.htm",
"http://www.motea.com/en/multimedia-c3757.htm",
"http://www.motea.com/en/front-fender-protector-c3978.htm",
"http://www.motea.com/en/side-panels-c4029.htm",
"http://www.motea.com/en/sissy-bars-c3974.htm",
"http://www.motea.com/en/seats--accessories-c4071.htm",
"http://www.motea.com/en/pillion-grab-handles-c4026.htm",
"http://www.motea.com/en/rear-view-mirrors-c4019.htm",
"http://www.motea.com/en/mirror-extensions-c4028.htm",
"http://www.motea.com/en/crashbars-c3463.htm",
"http://www.motea.com/en/frame-sliders-c287.htm",
"http://www.motea.com/en/gas-caps-c530.htm",
"http://www.motea.com/en/tank-covers-c3969.htm",
"http://www.motea.com/en/engine-guard-c3975.htm",
"http://www.motea.com/en/fairing-elements-c4090.htm",
"http://www.motea.com/en/garage-c4077.htm",
"http://www.motea.com/en/wind-protection-c674.htm",
]
        
        for url in urls:
            try:
                req = scrapy.Request( url , callback=self.parse1, meta={'main_url': url})
                #req.meta['item_id']=url
                #req.cookies = { 'lc-main':'en_US', 'x-wl-uid':'1yE71wxptnrPGpU96MVpeAljDAxEwlHAMNmRkGH3kTDbQNlw65AKYm8JBd2Nm33DfONRPH48N1DRE/phePYv7b8VzqI5P36U503gVSzRJSBmwDQKne/e/xfe/X3r9TLt9Mq2dGxVnAVsmo8PkOTlUOw==', 'skin':'noskin', 'x-main':'X2Uw?4D0ZsoVUNTB1ND?IqOhj4jrdt3SQM?nwPoWs2Vra8r9I13YbE1V8fqOmIli', 'at-main':'Atza|IwEBIM6arSMDjanfYsyURnaqmNeb87cZy6ift3_Ewd6ai-VCWQxN1VU8u-feDM43rwF2oZopky98QowPRIgSVmpR_qWGQgSAAMl_YsBf2E0nGom_GkU0Vl5JNLdIaGZ9g-Je-Uld-_qAa3onwe2Q_rUKPCN6j5PAu_78gARA9l5GI48so08VSR_tDyWO8p_WHTqj2dJMXqKZ-6YuhyOYGPbSFgupS_O-PofP6d9lqKlLtruDVDv98__UgkmhRmUXWTt3X3G_2ALthXr4_8tBnT4VpdNEWYqZKsJF0xej6dixrNlFNWoKyK-jojctn-E95wf1GmItDzSmmwM-fzp8LRptCncE_vJEfXTPknNoUcz2qoYx2kBsuYOviBUZSAONWCXII68hZD4SILOFPKAMmAXRBswx', 'sess-at-main':'hTCj4tFy0geBzyuGIGBYRUfOmwxbmm3iJjvmeMi/emE=', 'JSESSIONID':'C70160F1BC7EC0B9D5E1BD946AA543DF', 'csm-hit':'J1CK3EMBJCQHNYC6PB4P+s-CB6DMAQSAGGJC2C8H354|1503728162175', 'session-token':'n2Bkr05TMvQYIlxStLEPDDdd8KmwvXszRPl41nyUA+1+hlViB/+whjJG3jQjbUov8lRYLkN78KFEgYKt3ZQZjLd8PKw5Sp8DO2anI7lIo5iA5ZlBkkhTAAEz6qxH9pejQawVHIgLmQ0WLVWeZup/JQGwjoNITTENdcZ9A+C55Nfj0eEwqpNI661A1pvmaG9Y2hCGn0xf/zWQnGeus1aGeF6u3GdgzUTVEoqoashearQ8cngRhV/i0uxZoqRJly4ivJIy43Khphvj7Z++9vFB3w==', 'ubid-main':'131-1502033-8002851', 'session-id-time':'2082787201l', 'session-id':'130-6537552-1339612'}
                #req.cookies = {'__csrf_token-1':'xKVo4VZJqkyblSjFlWzEehgUFyHAQg', 'nocache':'detail-1', 'x-ua-device':'tablet', '_ga':'GA1.2.2072088434.1505733636', '_gid':'GA1.2.1081983427.1506316742', 'session-1':'8e46a0f8054191632d15e31849c5862d483ca54447ec216fce4403cd7e3c21de' }
                yield req
            
            except: raise

    def parse1(self, response):
	
        
        #Header1= {'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://uk-motors.de/angebote/' , 'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0'}
        productlist=response.xpath('//*[@id="ctl10_ctl00_ctl00_divContent"]/div[@class="list_item"]')
        for products in productlist:
            producturl= products.xpath('div/div[2]/div/a/@href').extract()[0]
            item = MotiaItem()
            item['categoryurl']=response.url
            item['producturl']=producturl
            yield item
        
        if response.url == response.meta['main_url']:
            totalpages=len(response.xpath('//*[@id="ctl10_ctl00_ctl00_divContent"]/div/div/div[4]/div/select[@id="ddlpages"]/option'))/2
            url=response.meta['main_url']
            codestr=((url.rsplit('-',1)[1]).split('.')[0]).replace('c','')
            urlpart="?CT=" + codestr
            urlpart2="&n_dis=0&n_srt=7&n_ipp=16"
            #counter=response.meta['counter']
            #endcounter=700
            for i in range(2,totalpages+1):
                urlpart1="&n_pg="+str(i)
                try:
                    req = scrapy.Request( url+ urlpart +urlpart1+urlpart2, callback=self.parse1, meta={'main_url':url})
                    yield req
                except: raise
				
