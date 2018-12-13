
# -*- coding: utf-8 -*-
import scrapy
import urllib

import os
import time
import re
import json
import re
import datetime
import demjson
from scrapy.http.cookies import CookieJar
import scrapy
import urllib
#from shop.items1 import TyreItem,MatchItem,Refurb
import os
from scrapy.exceptions import CloseSpider


class HomedepotItems(scrapy.Item):
    item_id=scrapy.Field()
    producturl=scrapy.Field()


class HomedepotSpider(scrapy.Spider):
    imgcount = 1
    name = "homedepot_producturls_06-07-2018"
    allowed_domains = ["homedepot.com"]
    #allowed_domains = ["https://www.linkedin.com/"]

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ["https://www.linkedin.com/"]
    #start_urls = ["https://www.linkedin.com/pub/dir/Yogesh/Kadam"]


    def parse(self, response):
        urls_done=[
]
        #url="https://www.linkedin.com/search/results/index/?keywords=Ian%20Sideco%20Corporate%20Counsel&origin=GLOBAL_SEARCH_HEADER"
        urls=[
["1","https://www.homedepot.com/b/Plumbing-Pipes-Fittings-Plastic-Pipe-Tubing/N-5yc1vZbuxy"],
["2","https://www.homedepot.com/b/Appliances-Washers-Dryers-Washing-Machines-Top-Load-Washers/N-5yc1vZc3oc"],
]
        
        for url in urls:
            try:
                #urlpattern1="https://www.homedepot.com/p/svcs/frontEndModel/"+url[1]
                req = scrapy.Request( url[1] , headers={'authority': 'www.homedepot.com' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9'}, meta={'main_url':url[1]}, callback=self.parse1)
                req.cookies={'HD_DC':'origin', 'THD_FORCE_LOC':'1', 'check':'true', 'AMCVS_F6421253512D2C100A490D45%40AdobeOrg':'1', 'THD_CACHE_NAV_PERSIST':'', 'RES_TRACKINGID':'895354131831062', 'ResonanceSegment':'', 'cto_lwid':'91e95255-ef25-46f8-a529-8f80cf7567a8', '_ga':'GA1.2.208324430.1529567125', 'aam_uuid':'91189372835669781092423751423903140869', '_CT_RS_':'Recording', 'WRUID15e':'1793994368270430', '_mibhv':'anon-1529567126670-7198012935_4577', 'CT_THD_FORCE_LOC':'1', 'ftr_ncd':'6', '_abck':'4ACD8EBCCEAFF2C261B2FFCEF718E57117D4328A6603000090572B5B22F1AE2D~0~5eyVSbVZn5NzhXJThph1wShLUl74xVzEtuNFslQZS2c=~-1~-1', 'ats-cid-AM-141099-sid':'59029963x', 'LPVID':'JlM2Y3Y2ViZjA2YTA5MmUx', 'THD_CACHE_NAV_SESSION':'C20%7E8119_%7EC20_EXP%7E_%7EC22%7E1710_%7EC22_EXP%7E_%7EC26%7ENone_%7EC26_EXP%7E', '_gid':'GA1.2.1028106834.1530783614', 'THD_MCC_ID':'b9498ceb-e51f-493a-aa6a-a2236e434571', 'ak_bmsc':'ADCBF2A879914447E5510318F2E8478F7C7CFC94D3420000E8373F5B3B55FC25~plSaT0z6OsxC4DUQ7q/HB9q/IjybxC5NjUNEWkxAmSohTuRhPROvLCxy3jgnaKi8Q1srVspXaX3QTeVLfNNPg1Y1qF1+31alfLnwzDDQ27GJdTL7dwiVC0ybZ+xVsqtTxP6aYBNCBU26qZlYFvPYccPIwZFWcS45jdzAbSRYOOdwH9wdaODTjfKw8GI5L+9CPBx7cRC3E0xlFA8GTPwd6SeN2F6w3QmMIMIqlbEW+kTSRMwwaJ9b/6dOqXmaP3plpR', 'THD-LOC-STORE':'', 'ShowMiniCart':'true', 's_dfa':'homedepotprod', 'CT_LOC_STORE':'', 'LPSID-31564604':'Ybl3OHRCRWKSHycB_IxTzQ', 'ecrSessionId':'E9CCEFD6DCBE80A17EF4CB369AA68568', 'THD_SESSION':'', '_br_uid_2':'uid%3D1645695940395%3Av%3D12.0%3Ats%3D1529567126677%3Ahc%3D16', 'AMCV_F6421253512D2C100A490D45%40AdobeOrg':'-894706358%7CMCIDTS%7C17718%7CMCMID%7C91455857754636887762433555680828564080%7CMCAAMLH-1531203035%7C3%7CMCAAMB-1531475787%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1530876940s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C-661508390%7CvVersion%7C2.3.0', 'THD_PERSIST':'C4%3D1710%2BGuam%2B-%2BTamuning%20-%20Tamuning%2C%20GU%2B%3A%3BC4_EXP%3D1581407121%3A%3BC24%3D96913%3A%3BC24_EXP%3D1581407121%3A%3BC34%3D32.0%3A%3BC34_EXP%3D1530957389', 'akaau':'1530871379~id=33e2b1897fb82d9fd867afcbb87bd8c4', 'bm_sv':'F53210998D2AB7277786E5EE61FDB279~um4a7iWnRZ6cQd7EypkaxTIT9KV5IUS0tObqnZWbQQEUPi2TrF6ljcjwrWuZ2/KM29VSumc/xwJ72KGCY71dCLVcvEDqer3FWxhnDiBjMEuxZcgstosIb/2lCOiKBTGcBgDjTUaIsH4gkAZFMVqp8Yg8KscsFmn/7k91cYdJooY=', 'bm_sz':'808368533F78DF08E26594224B9B8A57~QAAQijLUFwbSoWJkAQAA85sYb/MobSE3exFyi8yTE7xNndh3UrgscI95HFFupAAdQ3zHxztKsv0wsuLVDLNh6J+EzTMvYN/++/7WHhksZxPQtTn74BYbr7Mpv4sfSlTswZzHPqW2NSC+Tgn+EiX4A/3ma817sxLX+CMPM1VzbnTxVyIvy1a0mpSSwjItqQzZBR8=', 's_pers':'%20s_nr%3D1530872242306-Repeat%7C1562408242306%3B%20s_dslv%3D1530872242308%7C1625480242308%3B%20s_dslv_s%3DLess%2520than%25201%2520day%7C1530874042308%3B', 'mbox':'PC#c5dda6291304411da60dff188a0020a0.22_16#1592811926|session#a718ae7bce42403a838f094413abbfb7#1530874103', 's_sess':'%20s_sq%3D%3B%20s_cc%3Dtrue%3B%20s_pv_pName%3Dmini%2520cart%2520overlay%3B%20s_pv_pType%3Dmini%2520cart%2520overlay%3B%20s_pv_cmpgn%3D%3B%20stsh%3D%3B', '_px':'ZeuJS3mS8qZcbiUPDvGem0R9DJBHA/b/aa6eqXQfQCOh01xBJdLm20P+UtUGQrcyVoZoh2skP+rHi9Bea9rk7w==:1000:HqgYMA6PRLj+P6dLErrLjLZS98DnJ1wi722vRfqkx2ULlG8HnfyqRTlFXeG4Ri1mLzwwfXKWCyT60D+VGXLZggh66/OJxRQdeRGy0Nh94PGQ7/QxvfROILrEgKzWpKT01J6ZdkQ79JNQCdZR79Bgk7dgvO4jdETYvP7I1jDb/aEzO8Ed7YCY0KG47MfW/WENtVj/92FztlrJRRn18EWy885+lWdLSWDWMlgF1FOJJ3r518bg65lAgn+I8fyz9ceTskrlb0z6v7ZVYKNAz1VJ8w==', '_uetsid':'_uet9109e939', 'ctRefUrl':'https://www.homedepot.com/mycart/minicart#/?_k=4zpukj', 'forterToken':'8ccb5cac4b0b4a5c975055a2359bb15c_1530872242795__UDF43_6', '__CT_Data':'gpv=20&ckp=tld&dm=homedepot.com&apv_4_www23=20&cpv_4_www23=20&rpv_4_www23=20', 'ctm':'{\'pgv\':3910924518967985|\'vst\':3363691994335637|\'vstr\':5326201115753699|\'intr\':1530873607126|\'v\':1|\'lvst\':207}', '_4c_':'hZNtT9swEMe%2FyuQXvGoTPz9UQlNhbNqk8TCYJu0NShyHRqRNZDsUhPrdObeEARVa39R397uz7%2FK%2FR7ReuBWaEcGwVkxjYTCZoFv3ENDsEfmmSn93aIaw4AQTyURpKllQxRTDnFBjFS80qwiaoPttHcU4I1CN8M0EeTvmRz%2B4PYbLxMRnpi7a4N4iHHMBiF3Z9r%2FQja%2FHSrt2sIGWDNuD06W2f0Yf0eChNlrE2IdZnq%2FX62zRLV3l%2Bi5mtlvmZX7eDsuyWd1Mz5vehenXJkawwvS8LUJs7NY9vRoSkp9OxYMld3%2FL4f4B%2BrVd5aA6MRnPKNj10NZN217GzrvvXyACvn7wdlGExJ2CWbpYwLHzzU2zAvu4beztVdG639sEogwzhjOpqcKc4ZThu3VwHoLHCw9v%2FyRVugpaRBRrRjlgGRHUCKkIFRDr4POiP82qgkQwvaud99sKYIUmpre8mQK4o%2FPLlAbHs59Xv66PTubHZ6evRhfWRbB7wwshf3H1vqtygvMfl1OasQznwRiKCaaCSqO4%2Fjy%2FODokB8umOjSEC6GFUoJL6FUrJSlnTAghNdZUC8mxxgfzi5PDpL0%2BaYzDoe0sjAoMkPUEfZtf76b2wRwq0D6qXF0MbUQgi51SsBGwC2kdoOsI6tBwWfoBkS7aCoe%2F0FpxYaAFs0%2FvvszHOQyW7X0OPGeU8YinbknCWYrDm3c7NT78LcYITavXjFTxPq7FdjXX%2F5YlBSimmtDX6M4DKHyPsRipbG15QcqqFM5hWfBSG11L6gxxpUoSfy4guVCccM02m80T'}
                req.meta['item_id']=url[0]
                #req.cookies = { 'lc-main':'en_US', 'x-wl-uid':'1yE71wxptnrPGpU96MVpeAljDAxEwlHAMNmRkGH3kTDbQNlw65AKYm8JBd2Nm33DfONRPH48N1DRE/phePYv7b8VzqI5P36U503gVSzRJSBmwDQKne/e/xfe/X3r9TLt9Mq2dGxVnAVsmo8PkOTlUOw==', 'skin':'noskin', 'x-main':'X2Uw?4D0ZsoVUNTB1ND?IqOhj4jrdt3SQM?nwPoWs2Vra8r9I13YbE1V8fqOmIli', 'at-main':'Atza|IwEBIM6arSMDjanfYsyURnaqmNeb87cZy6ift3_Ewd6ai-VCWQxN1VU8u-feDM43rwF2oZopky98QowPRIgSVmpR_qWGQgSAAMl_YsBf2E0nGom_GkU0Vl5JNLdIaGZ9g-Je-Uld-_qAa3onwe2Q_rUKPCN6j5PAu_78gARA9l5GI48so08VSR_tDyWO8p_WHTqj2dJMXqKZ-6YuhyOYGPbSFgupS_O-PofP6d9lqKlLtruDVDv98__UgkmhRmUXWTt3X3G_2ALthXr4_8tBnT4VpdNEWYqZKsJF0xej6dixrNlFNWoKyK-jojctn-E95wf1GmItDzSmmwM-fzp8LRptCncE_vJEfXTPknNoUcz2qoYx2kBsuYOviBUZSAONWCXII68hZD4SILOFPKAMmAXRBswx', 'sess-at-main':'hTCj4tFy0geBzyuGIGBYRUfOmwxbmm3iJjvmeMi/emE=', 'JSESSIONID':'C70160F1BC7EC0B9D5E1BD946AA543DF', 'csm-hit':'J1CK3EMBJCQHNYC6PB4P+s-CB6DMAQSAGGJC2C8H354|1503728162175', 'session-token':'n2Bkr05TMvQYIlxStLEPDDdd8KmwvXszRPl41nyUA+1+hlViB/+whjJG3jQjbUov8lRYLkN78KFEgYKt3ZQZjLd8PKw5Sp8DO2anI7lIo5iA5ZlBkkhTAAEz6qxH9pejQawVHIgLmQ0WLVWeZup/JQGwjoNITTENdcZ9A+C55Nfj0eEwqpNI661A1pvmaG9Y2hCGn0xf/zWQnGeus1aGeF6u3GdgzUTVEoqoashearQ8cngRhV/i0uxZoqRJly4ivJIy43Khphvj7Z++9vFB3w==', 'ubid-main':'131-1502033-8002851', 'session-id-time':'2082787201l', 'session-id':'130-6537552-1339612'}
                #req.cookies = {'__csrf_token-1':'xKVo4VZJqkyblSjFlWzEehgUFyHAQg', 'nocache':'detail-1', 'x-ua-device':'tablet', '_ga':'GA1.2.2072088434.1505733636', '_gid':'GA1.2.1081983427.1506316742', 'session-1':'8e46a0f8054191632d15e31849c5862d483ca54447ec216fce4403cd7e3c21de' }
                if url[0] not in urls_done:
                    yield req
            
            except: raise
			
    def parse1(self, response):
        if response.url==response.meta['main_url']:
            #url_list=response.xpath('//*[@id="products"]/div/div[@data-component="productpod"]/div/div[3]/div[1]/a/@href').extract()
            #print len(url_list)
            location=response.xpath('//script[@type="application/ld+json"]/text()').extract()[0]
            location=demjson.decode(location)
            for dicts in location['mainEntity']['offers']['itemOffered']:
                item=HomedepotItems()
                item['producturl']=dicts['url']
                item['item_id']=response.meta['item_id']
                yield item
            #url_list=["https://www.homedepot.com"+url for url in url_list]
            #print url_list
            #for urls in url_list:
            #    item=HomedepotItems()
            #    item['producturl']=urls
            #    item['item_id']=response.meta['item_id']
            #    yield item
            total_products="".join(response.xpath('//*[@id="allProdCount"]/text()').extract())
            if int(total_products)>24:
                pages=int(total_products)/24
                page_counter=24
                for i in range(0,pages):
                    urlpattern=response.meta['main_url']+"?Nao="+str(page_counter)+"&Ns=None"
                    req=scrapy.Request( urlpattern , headers={'authority': 'www.homedepot.com' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9'}, meta={'main_url':urlpattern, 'item_id':response.meta['item_id']}, callback=self.parse1)
                    req.cookies={'HD_DC':'origin', 'THD_FORCE_LOC':'1', 'check':'true', 'AMCVS_F6421253512D2C100A490D45%40AdobeOrg':'1', 'THD_CACHE_NAV_PERSIST':'', 'RES_TRACKINGID':'895354131831062', 'ResonanceSegment':'', 'cto_lwid':'91e95255-ef25-46f8-a529-8f80cf7567a8', '_ga':'GA1.2.208324430.1529567125', 'aam_uuid':'91189372835669781092423751423903140869', '_CT_RS_':'Recording', 'WRUID15e':'1793994368270430', '_mibhv':'anon-1529567126670-7198012935_4577', 'CT_THD_FORCE_LOC':'1', 'ftr_ncd':'6', '_abck':'4ACD8EBCCEAFF2C261B2FFCEF718E57117D4328A6603000090572B5B22F1AE2D~0~5eyVSbVZn5NzhXJThph1wShLUl74xVzEtuNFslQZS2c=~-1~-1', 'ats-cid-AM-141099-sid':'59029963x', 'LPVID':'JlM2Y3Y2ViZjA2YTA5MmUx', 'THD_CACHE_NAV_SESSION':'C20%7E8119_%7EC20_EXP%7E_%7EC22%7E1710_%7EC22_EXP%7E_%7EC26%7ENone_%7EC26_EXP%7E', '_gid':'GA1.2.1028106834.1530783614', 'THD_MCC_ID':'b9498ceb-e51f-493a-aa6a-a2236e434571', 'ak_bmsc':'ADCBF2A879914447E5510318F2E8478F7C7CFC94D3420000E8373F5B3B55FC25~plSaT0z6OsxC4DUQ7q/HB9q/IjybxC5NjUNEWkxAmSohTuRhPROvLCxy3jgnaKi8Q1srVspXaX3QTeVLfNNPg1Y1qF1+31alfLnwzDDQ27GJdTL7dwiVC0ybZ+xVsqtTxP6aYBNCBU26qZlYFvPYccPIwZFWcS45jdzAbSRYOOdwH9wdaODTjfKw8GI5L+9CPBx7cRC3E0xlFA8GTPwd6SeN2F6w3QmMIMIqlbEW+kTSRMwwaJ9b/6dOqXmaP3plpR', 'THD-LOC-STORE':'', 'ShowMiniCart':'true', 's_dfa':'homedepotprod', 'CT_LOC_STORE':'', 'LPSID-31564604':'Ybl3OHRCRWKSHycB_IxTzQ', 'ecrSessionId':'E9CCEFD6DCBE80A17EF4CB369AA68568', 'THD_SESSION':'', '_br_uid_2':'uid%3D1645695940395%3Av%3D12.0%3Ats%3D1529567126677%3Ahc%3D16', 'AMCV_F6421253512D2C100A490D45%40AdobeOrg':'-894706358%7CMCIDTS%7C17718%7CMCMID%7C91455857754636887762433555680828564080%7CMCAAMLH-1531203035%7C3%7CMCAAMB-1531475787%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1530876940s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C-661508390%7CvVersion%7C2.3.0', 'THD_PERSIST':'C4%3D1710%2BGuam%2B-%2BTamuning%20-%20Tamuning%2C%20GU%2B%3A%3BC4_EXP%3D1581407121%3A%3BC24%3D96913%3A%3BC24_EXP%3D1581407121%3A%3BC34%3D32.0%3A%3BC34_EXP%3D1530957389', 'akaau':'1530871379~id=33e2b1897fb82d9fd867afcbb87bd8c4', 'bm_sv':'F53210998D2AB7277786E5EE61FDB279~um4a7iWnRZ6cQd7EypkaxTIT9KV5IUS0tObqnZWbQQEUPi2TrF6ljcjwrWuZ2/KM29VSumc/xwJ72KGCY71dCLVcvEDqer3FWxhnDiBjMEuxZcgstosIb/2lCOiKBTGcBgDjTUaIsH4gkAZFMVqp8Yg8KscsFmn/7k91cYdJooY=', 'bm_sz':'808368533F78DF08E26594224B9B8A57~QAAQijLUFwbSoWJkAQAA85sYb/MobSE3exFyi8yTE7xNndh3UrgscI95HFFupAAdQ3zHxztKsv0wsuLVDLNh6J+EzTMvYN/++/7WHhksZxPQtTn74BYbr7Mpv4sfSlTswZzHPqW2NSC+Tgn+EiX4A/3ma817sxLX+CMPM1VzbnTxVyIvy1a0mpSSwjItqQzZBR8=', 's_pers':'%20s_nr%3D1530872242306-Repeat%7C1562408242306%3B%20s_dslv%3D1530872242308%7C1625480242308%3B%20s_dslv_s%3DLess%2520than%25201%2520day%7C1530874042308%3B', 'mbox':'PC#c5dda6291304411da60dff188a0020a0.22_16#1592811926|session#a718ae7bce42403a838f094413abbfb7#1530874103', 's_sess':'%20s_sq%3D%3B%20s_cc%3Dtrue%3B%20s_pv_pName%3Dmini%2520cart%2520overlay%3B%20s_pv_pType%3Dmini%2520cart%2520overlay%3B%20s_pv_cmpgn%3D%3B%20stsh%3D%3B', '_px':'ZeuJS3mS8qZcbiUPDvGem0R9DJBHA/b/aa6eqXQfQCOh01xBJdLm20P+UtUGQrcyVoZoh2skP+rHi9Bea9rk7w==:1000:HqgYMA6PRLj+P6dLErrLjLZS98DnJ1wi722vRfqkx2ULlG8HnfyqRTlFXeG4Ri1mLzwwfXKWCyT60D+VGXLZggh66/OJxRQdeRGy0Nh94PGQ7/QxvfROILrEgKzWpKT01J6ZdkQ79JNQCdZR79Bgk7dgvO4jdETYvP7I1jDb/aEzO8Ed7YCY0KG47MfW/WENtVj/92FztlrJRRn18EWy885+lWdLSWDWMlgF1FOJJ3r518bg65lAgn+I8fyz9ceTskrlb0z6v7ZVYKNAz1VJ8w==', '_uetsid':'_uet9109e939', 'ctRefUrl':'https://www.homedepot.com/mycart/minicart#/?_k=4zpukj', 'forterToken':'8ccb5cac4b0b4a5c975055a2359bb15c_1530872242795__UDF43_6', '__CT_Data':'gpv=20&ckp=tld&dm=homedepot.com&apv_4_www23=20&cpv_4_www23=20&rpv_4_www23=20', 'ctm':'{\'pgv\':3910924518967985|\'vst\':3363691994335637|\'vstr\':5326201115753699|\'intr\':1530873607126|\'v\':1|\'lvst\':207}', '_4c_':'hZNtT9swEMe%2FyuQXvGoTPz9UQlNhbNqk8TCYJu0NShyHRqRNZDsUhPrdObeEARVa39R397uz7%2FK%2FR7ReuBWaEcGwVkxjYTCZoFv3ENDsEfmmSn93aIaw4AQTyURpKllQxRTDnFBjFS80qwiaoPttHcU4I1CN8M0EeTvmRz%2B4PYbLxMRnpi7a4N4iHHMBiF3Z9r%2FQja%2FHSrt2sIGWDNuD06W2f0Yf0eChNlrE2IdZnq%2FX62zRLV3l%2Bi5mtlvmZX7eDsuyWd1Mz5vehenXJkawwvS8LUJs7NY9vRoSkp9OxYMld3%2FL4f4B%2BrVd5aA6MRnPKNj10NZN217GzrvvXyACvn7wdlGExJ2CWbpYwLHzzU2zAvu4beztVdG639sEogwzhjOpqcKc4ZThu3VwHoLHCw9v%2FyRVugpaRBRrRjlgGRHUCKkIFRDr4POiP82qgkQwvaud99sKYIUmpre8mQK4o%2FPLlAbHs59Xv66PTubHZ6evRhfWRbB7wwshf3H1vqtygvMfl1OasQznwRiKCaaCSqO4%2Fjy%2FODokB8umOjSEC6GFUoJL6FUrJSlnTAghNdZUC8mxxgfzi5PDpL0%2BaYzDoe0sjAoMkPUEfZtf76b2wRwq0D6qXF0MbUQgi51SsBGwC2kdoOsI6tBwWfoBkS7aCoe%2F0FpxYaAFs0%2FvvszHOQyW7X0OPGeU8YinbknCWYrDm3c7NT78LcYITavXjFTxPq7FdjXX%2F5YlBSimmtDX6M4DKHyPsRipbG15QcqqFM5hWfBSG11L6gxxpUoSfy4guVCccM02m80T'}
                    page_counter+=24
                    yield req
        else:
            url_list=response.xpath('//*[@id="products"]/div/div[@data-component="productpod"]/div/div[3]/div[1]/a/@href').extract()
            #print len(url_list)
            url_list=["https://www.homedepot.com"+url for url in url_list]
            #print url_list
            for urls in url_list:
                item=HomedepotItems()
                item['producturl']=urls
                item['item_id']=response.meta['item_id']
                yield item