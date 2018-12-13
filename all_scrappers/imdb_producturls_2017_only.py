



#Amazon seller list spider
import time
import scrapy
import json
    
	
	
class ImdbItem(scrapy.Item):
    #year=scrapy.Field()
    pageurl=scrapy.Field()
    titleurl=scrapy.Field()


class ImdbSpider(scrapy.Spider):
    
    name = "imdb_producturls_2017_only"
    allowed_domain=[]
    start_urls = ['http://www.imdb.com/year/']
    #start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ['https://www.amazon.com/musical-instruments-accessories-sound-recording/b/ref=nav_shopall_mi_ce?ie=UTF8&node=11091801']
    
    
    def parse(self, response):
        urls_done=[]
        urls=[
["http://www.imdb.com/search/title?release_date=2017&ref_=rlm_yr"],
["http://www.imdb.com/search/title?release_date=2017&page=2&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=3&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=4&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=5&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=6&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=7&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=8&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=9&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=10&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=11&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=12&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=13&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=14&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=15&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=16&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=17&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=18&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=19&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=20&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=21&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=22&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=23&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=24&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=25&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=26&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=27&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=28&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=29&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=30&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=31&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=32&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=33&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=34&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=35&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=36&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=37&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=38&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=39&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=40&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=41&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=42&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=43&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=44&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=45&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=46&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=47&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=48&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=49&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=50&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=51&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=52&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=53&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=54&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=55&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=56&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=57&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=58&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=59&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=60&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=61&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=62&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=63&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=64&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=65&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=66&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=67&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=68&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=69&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=70&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=71&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=72&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=73&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=74&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=75&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=76&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=77&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=78&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=79&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=80&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=81&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=82&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=83&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=84&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=85&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=86&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=87&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=88&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=89&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=90&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=91&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=92&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=93&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=94&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=95&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=96&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=97&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=98&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=99&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=100&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=101&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=102&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=103&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=104&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=105&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=106&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=107&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=108&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=109&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=110&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=111&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=112&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=113&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=114&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=115&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=116&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=117&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=118&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=119&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=120&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=121&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=122&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=123&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=124&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=125&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=126&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=127&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=128&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=129&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=130&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=131&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=132&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=133&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=134&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=135&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=136&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=137&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=138&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=139&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=140&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=141&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=142&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=143&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=144&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=145&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=146&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=147&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=148&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=149&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=150&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=151&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=152&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=153&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=154&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=155&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=156&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=157&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=158&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=159&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=160&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=161&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=162&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=163&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=164&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=165&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=166&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=167&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=168&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=169&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=170&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=171&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=172&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=173&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=174&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=175&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=176&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=177&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=178&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=179&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=180&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=181&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=182&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=183&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=184&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=185&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=186&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=187&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=188&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=189&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=190&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=191&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=192&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=193&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=194&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=195&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=196&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=197&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=198&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=199&ref_=adv_nxt"],
["http://www.imdb.com/search/title?release_date=2017&page=200&ref_=adv_nxt"],
]

        for url in urls:
            try:
                req = scrapy.Request( url[0] , callback=self.parse1)
                #req.meta['item_id']=url
                #req.cookies = { 'lc-main':'en_US', 'x-wl-uid':'1yE71wxptnrPGpU96MVpeAljDAxEwlHAMNmRkGH3kTDbQNlw65AKYm8JBd2Nm33DfONRPH48N1DRE/phePYv7b8VzqI5P36U503gVSzRJSBmwDQKne/e/xfe/X3r9TLt9Mq2dGxVnAVsmo8PkOTlUOw==', 'skin':'noskin', 'x-main':'X2Uw?4D0ZsoVUNTB1ND?IqOhj4jrdt3SQM?nwPoWs2Vra8r9I13YbE1V8fqOmIli', 'at-main':'Atza|IwEBIM6arSMDjanfYsyURnaqmNeb87cZy6ift3_Ewd6ai-VCWQxN1VU8u-feDM43rwF2oZopky98QowPRIgSVmpR_qWGQgSAAMl_YsBf2E0nGom_GkU0Vl5JNLdIaGZ9g-Je-Uld-_qAa3onwe2Q_rUKPCN6j5PAu_78gARA9l5GI48so08VSR_tDyWO8p_WHTqj2dJMXqKZ-6YuhyOYGPbSFgupS_O-PofP6d9lqKlLtruDVDv98__UgkmhRmUXWTt3X3G_2ALthXr4_8tBnT4VpdNEWYqZKsJF0xej6dixrNlFNWoKyK-jojctn-E95wf1GmItDzSmmwM-fzp8LRptCncE_vJEfXTPknNoUcz2qoYx2kBsuYOviBUZSAONWCXII68hZD4SILOFPKAMmAXRBswx', 'sess-at-main':'hTCj4tFy0geBzyuGIGBYRUfOmwxbmm3iJjvmeMi/emE=', 'JSESSIONID':'C70160F1BC7EC0B9D5E1BD946AA543DF', 'csm-hit':'J1CK3EMBJCQHNYC6PB4P+s-CB6DMAQSAGGJC2C8H354|1503728162175', 'session-token':'n2Bkr05TMvQYIlxStLEPDDdd8KmwvXszRPl41nyUA+1+hlViB/+whjJG3jQjbUov8lRYLkN78KFEgYKt3ZQZjLd8PKw5Sp8DO2anI7lIo5iA5ZlBkkhTAAEz6qxH9pejQawVHIgLmQ0WLVWeZup/JQGwjoNITTENdcZ9A+C55Nfj0eEwqpNI661A1pvmaG9Y2hCGn0xf/zWQnGeus1aGeF6u3GdgzUTVEoqoashearQ8cngRhV/i0uxZoqRJly4ivJIy43Khphvj7Z++9vFB3w==', 'ubid-main':'131-1502033-8002851', 'session-id-time':'2082787201l', 'session-id':'130-6537552-1339612'}
                #req.cookies = {'__csrf_token-1':'xKVo4VZJqkyblSjFlWzEehgUFyHAQg', 'nocache':'detail-1', 'x-ua-device':'tablet', '_ga':'GA1.2.2072088434.1505733636', '_gid':'GA1.2.1081983427.1506316742', 'session-1':'8e46a0f8054191632d15e31849c5862d483ca54447ec216fce4403cd7e3c21de' }
                if url not in urls_done:
                    yield req
            
            except: raise
    def parse1(self, response):
        #year=response.meta['year']
        titleurllist=response.xpath('//*[@id="main"]/div/div/div[3]/div')
        for titleurls in titleurllist:
            try:
                titleurl=titleurls.xpath('div[3]/h3/a[2]/@href').extract()[0]
            except:
                titleurl=titleurls.xpath('div[3]/h3/a/@href').extract()[0]
            item=ImdbItem()
            #item['year']=year
            item['pageurl']=response.url
            item['titleurl']="http://www.imdb.com"+titleurl
            yield item