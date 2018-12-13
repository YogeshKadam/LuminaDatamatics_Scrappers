



#Amazon seller list spider
import time
import scrapy
import json
    
	
	
class ImdbItem(scrapy.Item):
    year=scrapy.Field()
    pageurl=scrapy.Field()
    titleurl=scrapy.Field()


class ImdbSpider(scrapy.Spider):
    
    name = "imdb_productinfo_slot1_below10k"
    allowed_domain=[]
    start_urls = ['http://www.imdb.com/year/']
    #start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ['https://www.amazon.com/musical-instruments-accessories-sound-recording/b/ref=nav_shopall_mi_ce?ie=UTF8&node=11091801']
    
    
    def parse(self, response):
        urls_done=[]
        urls=[
["http://www.imdb.com/search/title?release_date=1891&ref_=rlm_yr","1891"],
["http://www.imdb.com/search/title?release_date=1889&ref_=rlm_yr","1889"],
["http://www.imdb.com/search/title?release_date=1884&ref_=rlm_yr","1884"],
["http://www.imdb.com/search/title?release_date=1886&ref_=rlm_yr","1886"],
["http://www.imdb.com/search/title?release_date=1887&ref_=rlm_yr","1887"],
["http://www.imdb.com/search/title?release_date=1883&ref_=rlm_yr","1883"],
["http://www.imdb.com/search/title?release_date=1890&ref_=rlm_yr","1890"],
["http://www.imdb.com/search/title?release_date=1885&ref_=rlm_yr","1885"],
["http://www.imdb.com/search/title?release_date=1882&ref_=rlm_yr","1882"],
["http://www.imdb.com/search/title?release_date=1881&ref_=rlm_yr","1881"],
["http://www.imdb.com/search/title?release_date=1880&ref_=rlm_yr","1880"],
["http://www.imdb.com/search/title?release_date=1888&ref_=rlm_yr","1888"],
["http://www.imdb.com/search/title?release_date=1879&ref_=rlm_yr","1879"],
["http://www.imdb.com/search/title?release_date=1878&ref_=rlm_yr","1878"],
["http://www.imdb.com/search/title?release_date=1877&ref_=rlm_yr","1877"],
["http://www.imdb.com/search/title?release_date=1876&ref_=rlm_yr","1876"],
["http://www.imdb.com/search/title?release_date=1955&ref_=rlm_yr","1955"],
]

        for url in urls:
            try:
                req = scrapy.Request( url[0] , callback=self.parse1, meta={'year':url[1]})
                #req.meta['item_id']=url
                #req.cookies = { 'lc-main':'en_US', 'x-wl-uid':'1yE71wxptnrPGpU96MVpeAljDAxEwlHAMNmRkGH3kTDbQNlw65AKYm8JBd2Nm33DfONRPH48N1DRE/phePYv7b8VzqI5P36U503gVSzRJSBmwDQKne/e/xfe/X3r9TLt9Mq2dGxVnAVsmo8PkOTlUOw==', 'skin':'noskin', 'x-main':'X2Uw?4D0ZsoVUNTB1ND?IqOhj4jrdt3SQM?nwPoWs2Vra8r9I13YbE1V8fqOmIli', 'at-main':'Atza|IwEBIM6arSMDjanfYsyURnaqmNeb87cZy6ift3_Ewd6ai-VCWQxN1VU8u-feDM43rwF2oZopky98QowPRIgSVmpR_qWGQgSAAMl_YsBf2E0nGom_GkU0Vl5JNLdIaGZ9g-Je-Uld-_qAa3onwe2Q_rUKPCN6j5PAu_78gARA9l5GI48so08VSR_tDyWO8p_WHTqj2dJMXqKZ-6YuhyOYGPbSFgupS_O-PofP6d9lqKlLtruDVDv98__UgkmhRmUXWTt3X3G_2ALthXr4_8tBnT4VpdNEWYqZKsJF0xej6dixrNlFNWoKyK-jojctn-E95wf1GmItDzSmmwM-fzp8LRptCncE_vJEfXTPknNoUcz2qoYx2kBsuYOviBUZSAONWCXII68hZD4SILOFPKAMmAXRBswx', 'sess-at-main':'hTCj4tFy0geBzyuGIGBYRUfOmwxbmm3iJjvmeMi/emE=', 'JSESSIONID':'C70160F1BC7EC0B9D5E1BD946AA543DF', 'csm-hit':'J1CK3EMBJCQHNYC6PB4P+s-CB6DMAQSAGGJC2C8H354|1503728162175', 'session-token':'n2Bkr05TMvQYIlxStLEPDDdd8KmwvXszRPl41nyUA+1+hlViB/+whjJG3jQjbUov8lRYLkN78KFEgYKt3ZQZjLd8PKw5Sp8DO2anI7lIo5iA5ZlBkkhTAAEz6qxH9pejQawVHIgLmQ0WLVWeZup/JQGwjoNITTENdcZ9A+C55Nfj0eEwqpNI661A1pvmaG9Y2hCGn0xf/zWQnGeus1aGeF6u3GdgzUTVEoqoashearQ8cngRhV/i0uxZoqRJly4ivJIy43Khphvj7Z++9vFB3w==', 'ubid-main':'131-1502033-8002851', 'session-id-time':'2082787201l', 'session-id':'130-6537552-1339612'}
                #req.cookies = {'__csrf_token-1':'xKVo4VZJqkyblSjFlWzEehgUFyHAQg', 'nocache':'detail-1', 'x-ua-device':'tablet', '_ga':'GA1.2.2072088434.1505733636', '_gid':'GA1.2.1081983427.1506316742', 'session-1':'8e46a0f8054191632d15e31849c5862d483ca54447ec216fce4403cd7e3c21de' }
                if url not in urls_done:
                    yield req
            
            except: raise
    def parse1(self, response):
        year=response.meta['year']
        titleurllist=response.xpath('//*[@id="main"]/div/div/div[3]/div')
        for titleurls in titleurllist:
            titleurl=titleurls.xpath('div[3]/h3/a/@href').extract()[0]
            item=ImdbItem()
            item['year']=year
            item['pageurl']=response.url
            item['titleurl']="http://www.imdb.com"+titleurl
            yield item