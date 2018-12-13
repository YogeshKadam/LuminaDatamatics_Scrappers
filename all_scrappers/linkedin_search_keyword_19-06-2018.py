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


class LinkedinItems(scrapy.Item):
    firstName = scrapy.Field()
    lastName = scrapy.Field()
    Industry = scrapy.Field()
    uniqueID = scrapy.Field()
    Location = scrapy.Field()
    Occupation = scrapy.Field()
    urlID = scrapy.Field()
    product_id = scrapy.Field()
    response_url = scrapy.Field()
    main_page_url = scrapy.Field()


class LinkedinSpider(scrapy.Spider):
    imgcount = 1
    name = "linkedin_search_keyword_19-06-2018"
    allowed_domains = ["linkedin.com"]
    #allowed_domains = ["https://www.linkedin.com/"]

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ["https://www.linkedin.com/"]
    #start_urls = ["https://www.linkedin.com/pub/dir/Yogesh/Kadam"]


    def parse555(self, response):
        #url="https://www.linkedin.com/pub/dir/Yogesh/Kadam"
        #url="https://www.linkedin.com/search/results/index/?keywords=general%20counsel&origin=GLOBAL_SEARCH_HEADER"
        url="https://www.linkedin.com/uas/login-submit"
        #req=scrapy.Request(url , headers={'authority': 'www.linkedin.com' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'referer': 'https://www.google.co.in/' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9'}, callback=self.parse1)
        req=scrapy.Request(url , headers={'authority': 'www.linkedin.com' , 'cache-control': 'max-age=0' , 'origin': 'https://www.linkedin.com' , 'upgrade-insecure-requests': '1' , 'content-type': 'application/x-www-form-urlencoded' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'referer': 'https://www.linkedin.com/' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9' }, callback=self.parse11)
        #req=scrapy.Request(url , headers={'authority': 'www.linkedin.com' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'referer': 'https://www.linkedin.com/' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9'}, callback=self.parse1)
        #req=scrapy.Request(url ,callback=self.parse1) 
        req.cookies={'visit':"v=1&M", '_chartbeat2':'DNoI1RB8-KIuCF80M4.1500966876379.1504264415172.0000000000000001', '_ga':'GA1.2.314132270.1490338107', 'bcookie':"v=2&cd36f31a-9c90-4dde-8f5c-882ea9ea0ad7", 'bscookie':"v=1&2018040907420239ce131b-e3bb-40f8-807b-165fea2f4e98AQGGTIxfino3WrcF-GtVPU6r7L4pZv38", '_guid':'bc4b62e0-201e-4a09-8533-63c7614be2dc', '__utmc':'226841088', 'lang':"v=2&lang=en-us", '__utma':'226841088.314132270.1490338107.1526384861.1526446575.15', '__utmz':'226841088.1526446575.15.13.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)', '_lipt':'CwEAAAFjaOR4fL1Udxu80Ee-2MNINE-0Prqses5VGz-FfdEHFe6BbmYTOvmMtVuYHwF-M4Uf5D60_8bIOS0AFMgjGfGeQo0ss1HQED7aPiS7vy8YrYC9-NRWhHm3mM0Untsn1YS64kObTHsnh_yonK3mlrwtW_7xyXN6rkwOF58oSp5eils8T-fgNOIv_U8csXpKZW5LA8-u92eWu816rNS3ZFyUyKzitUZakDhw-JOITYhBgq8soxbk6rtiHDpexZdO-1Db7gBD2oGQUkztWo10Yq37Ix8Tks6LuX2aTU6TDdj_FbKf5Ogrj6ljfc8ejbcwieqnlGdKOw', 'JSESSIONID':"ajax:8587083525452884837", 'lidc':"b=SGST02:g=5:u=1:i=1526473201:t=1526559601:s=AQFQtFmzvZZBPjIUxDSpwYvWxzZqRtRX", '_gat':'1', 'leo_auth_token':"GST:Z8xhKLRHPN8KniwTJadFlRRvnx8oaFtQ8AsuQMTyhvlkfbVQmn_uqD:1526539930:c1a81a839e8ff45216fdfe4a9a2cb36d957b8900" , 'session_key':'yogeshkadam1394%40gmail.com&session_password=ygk007%40srescoek&isJsEnabled=false&loginCsrfParam=cd36f31a-9c90-4dde-8f5c-882ea9ea0ad7'}
        yield req
		

    def parse(self, response):
        #url="https://www.linkedin.com/search/results/index/?keywords=Ian%20Sideco%20Corporate%20Counsel&origin=GLOBAL_SEARCH_HEADER"
        urls=[
#["1","fname","lname","title"],
#["2","Timothy","Marsh","Intellectual Property and Licensing Counsel, Senior Manager"],
["1","https://www.linkedin.com/search/results/people/?company=&facetGeoRegion=%5B%22us%3A412%22%5D&facetIndustry=%5B%229%22%2C%2210%22%5D&firstName=&lastName=&origin=FACETED_SEARCH&school=&title=counsel"],
["2","https://www.linkedin.com/search/results/people/?company=&facetGeoRegion=%5B%22us%3A70%22%5D&facetIndustry=%5B%229%22%2C%2210%22%5D&firstName=&lastName=&origin=FACETED_SEARCH&school=&title=general%20counsel"],
["3","https://www.linkedin.com/search/results/people/?company=&facetGeoRegion=%5B%22us%3A70%22%5D&facetIndustry=%5B%229%22%2C%2210%22%5D&facetSchool=%5B%2218995%22%5D&firstName=&lastName=&origin=FACETED_SEARCH&school=&title=counsel"],
["4","https://www.linkedin.com/search/results/people/?company=&facetGeoRegion=%5B%22us%3A70%22%5D&facetIndustry=%5B%229%22%2C%2210%22%5D&facetSchool=%5B%2218923%22%5D&firstName=&lastName=&origin=FACETED_SEARCH&school=&title=counsel"],
["5","https://www.linkedin.com/search/results/people/?company=&facetGeoRegion=%5B%22us%3A70%22%5D&facetIndustry=%5B%229%22%2C%2210%22%5D&facetSchool=%5B%2218958%22%5D&firstName=&lastName=&origin=FACETED_SEARCH&school=&title=counsel"],
["6","https://www.linkedin.com/search/results/people/?company=&facetGeoRegion=%5B%22us%3A70%22%5D&facetIndustry=%5B%229%22%2C%2210%22%5D&facetSchool=%5B%2218944%22%5D&firstName=&lastName=&origin=FACETED_SEARCH&school=&title=counsel"],
["7","https://www.linkedin.com/search/results/people/?company=&facetGeoRegion=%5B%22us%3A70%22%5D&facetIndustry=%5B%229%22%2C%2210%22%5D&facetSchool=%5B%2218919%22%5D&firstName=&lastName=&origin=FACETED_SEARCH&school=&title=counsel"],
["8","https://www.linkedin.com/search/results/people/?company=&facetGeoRegion=%5B%22us%3A152%22%5D&facetIndustry=%5B%229%22%2C%2210%22%5D&firstName=&lastName=&origin=FACETED_SEARCH&school=&title=counsel"],
["9","https://www.linkedin.com/search/results/people/?company=&facetGeoRegion=%5B%22us%3A51%22%5D&facetIndustry=%5B%229%22%2C%2210%22%5D&firstName=&lastName=&origin=FACETED_SEARCH&school=&title=counsel"],
["10","https://www.linkedin.com/search/results/people/?company=&facetGeoRegion=%5B%22us%3A82%22%5D&facetIndustry=%5B%229%22%2C%2210%22%5D&firstName=&lastName=&origin=FACETED_SEARCH&school=&title=counsel"],
["11","https://www.linkedin.com/search/results/people/?company=&facetGeoRegion=%5B%22us%3A828%22%2C%22us%3A596%22%5D&facetIndustry=%5B%229%22%2C%2210%22%5D&firstName=&lastName=&origin=FACETED_SEARCH&school=&title=counsel"],
["12","https://www.linkedin.com/search/results/people/?company=&facetGeoRegion=%5B%22us%3A844%22%2C%22us%3A376%22%2C%22us%3A904%22%5D&facetIndustry=%5B%229%22%2C%2210%22%5D&firstName=&lastName=&origin=FACETED_SEARCH&school=&title=counsel"],
]
        for url in urls:
            #urlpattern="https://www.linkedin.com/search/results/index/?keywords="+url[1].replace('.','').replace(',','%2C').replace(' ','%20')+"%20"+url[2].replace('.','').replace(',','%2C').replace(' ','%20')+"%20"+url[3].replace('.','').replace(',','%2C').replace(' ','%20')+"&origin=GLOBAL_SEARCH_HEADER"
            #url="https://www.linkedin.com/pub/dir/Yogesh/Kadam"
            #url="https://www.linkedin.com/search/results/index/?keywords=general%20counsel&origin=GLOBAL_SEARCH_HEADER"
            #req=scrapy.Request(url , headers={'authority': 'www.linkedin.com' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'referer': 'https://www.google.co.in/' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9'}, callback=self.parse1)
            #req=scrapy.Request(url , headers={'authority': 'www.linkedin.com' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'referer': 'https://www.linkedin.com/' , 'accept-encoding':'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9' }, callback=self.parse1)
            #req=scrapy.Request(urlpattern , headers={'authority': 'www.linkedin.com' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'referer': 'https://www.linkedin.com/' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9' }, callback=self.parse1, meta={'product_id':url[0]})
            req=scrapy.Request(url[1] , headers={'authority': 'www.linkedin.com' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'referer': 'https://www.linkedin.com/' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9' }, callback=self.parse1, meta={'product_id':url[0]})
            #req=scrapy.Request(url ,callback=self.parse1)
            #raise CloseSpider("Just for understanding")
            #req.cookies={'visit':'v=1&M', '_chartbeat2':'DNoI1RB8-KIuCF80M4.1500966876379.1504264415172.0000000000000001', '_ga':'GA1.2.314132270.1490338107', 'bcookie':'v=2&cd36f31a-9c90-4dde-8f5c-882ea9ea0ad7', 'bscookie':'v=1&2018040907420239ce131b-e3bb-40f8-807b-165fea2f4e98AQGGTIxfino3WrcF-GtVPU6r7L4pZv38', '_guid':'bc4b62e0-201e-4a09-8533-63c7614be2dc', '__utma':'226841088.314132270.1490338107.1525435525.1525435525.1', '__utmc':'226841088', '__utmz':'226841088.1525435525.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)', 'lang':'v=2&lang=en-us', 'sdsc':'22%3A1%2C1525677272300%7ECONN%2C0KoGLfHRG8S7m9nYwhy3eYpzWv2A%3D', '_lipt':'CwEAAAFjOXuQDVj6kRUiJrioDPq0PqBQV24rNGKy9jC1cf3Je64Xabjcn2zsBf-dexE0RztlHUg-v8R1O61bSXHMzVGtw1eefJ3clHafZHJfaPU86jBheXl1o4o61kHlmEDKYxiaT4Y1ixkI1e1XsV4keYpJNjNqlVuMSDWCEeG3fSp0HpaS9ZERIH0owYvodWwVGMb0oAJNTL9FlG6Y5Y76X7idQ3XILl4xpNiprzY1xJs-Javwppi8DwvWojkqhCT2Ctw5c-GTjeazDhH3lpVQrdhKJoUFjkBOk6Jyr05a8-YpgAdv7X0rHqYjdjulbHnz5f_gmen4yQ', 'JSESSIONID':'ajax:4744771991265787761', 'lidc':'b=OGST08:g=556:u=1:i=1525677815:t=1525764215:s=AQGGRNli4lGigJchMempb2ulMe7sHlDP'}
            #req.cookies={'visit':"v=1&M", '_chartbeat2':'DNoI1RB8-KIuCF80M4.1500966876379.1504264415172.0000000000000001', '_ga':'GA1.2.314132270.1490338107', 'bcookie':"v=2&cd36f31a-9c90-4dde-8f5c-882ea9ea0ad7", 'bscookie':"v=1&2018040907420239ce131b-e3bb-40f8-807b-165fea2f4e98AQGGTIxfino3WrcF-GtVPU6r7L4pZv38", '_guid':'bc4b62e0-201e-4a09-8533-63c7614be2dc', 'JSESSIONID':"ajax:7257142032599256502", '__utmc':'226841088', 'lang':"v=2&lang=en-us", '__utma':'226841088.314132270.1490338107.1526384861.1526446575.15', '__utmz':'226841088.1526446575.15.13.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)', 'leo_auth_token':"GST:Z9ztoYz_uYCEJ4t745RSNpzxLWaKrMVj_1zG-7kEDV1k0rt9rlmBvT:1526447233:c61c16272449110a3441f657060c05e28d3f4091", 'sl':"v=1&mlC-9", 'li_at':'AQEDARnBXAcFJCVhAAABY2dYWfQAAAFji2Td9FEApnE-RCl2x_axvTtiT_Z7kjBxyElNtjGAObvisoAN457k-W6y8vFi9b1LEf-vMMqG8OlD5XPWNnPiAPDQEktm24bWKh7ZvCA6cBMwPBDHwZXldNLz', 'liap':'true', 'RT':'s=1526448321391&r=https%3A%2F%2Fwww.linkedin.com%2Fgroups%2F4136932%2Fprofile', 'lidc':"b=SB07:g=52:u=22:i=1526448451:t=1526533634:s=AQGsq4NkYg69C_-WhnCgBjTDKCTUnVij", '_lipt':'CwEAAAFjZ2rv_TSPcoRLlm6zGpf1x2vW0Y4_qBCFDfO49kxSvp8j7AEv_vDh7cV5_BuYPqVkzNX2EBkjIYoj-IGJLt91CWxgzjy7OwOxwHUdhc9zo7eKLLczYIo4F_qOCyMTIaQz0r6OKnumtPXmUwmtSdl0QVO88Hx82CtbNIwjB6ptbmwdTsSoZ5NvNY52INEJ3M4Ep4oiX477ra2vvIZ2h49UhMTsyx1LTibOE60kGtAYZbu3UHGMuuJhkwXMOWupSqmF76X4Jycx9SHAGAgQJienntnUT1JsFCJyWVMoJC0M4S9mePk_9s3HwaoG9Rt8UAovHTp3xQ'}
            #req.cookies={'visit':"v=1&M", '_chartbeat2':'DNoI1RB8-KIuCF80M4.1500966876379.1504264415172.0000000000000001', '_ga':'GA1.2.314132270.1490338107', 'bcookie':"v=2&cd36f31a-9c90-4dde-8f5c-882ea9ea0ad7", 'bscookie':"v=1&2018040907420239ce131b-e3bb-40f8-807b-165fea2f4e98AQGGTIxfino3WrcF-GtVPU6r7L4pZv38", '_guid':'bc4b62e0-201e-4a09-8533-63c7614be2dc', '__utma':'226841088.314132270.1490338107.1526384861.1526446575.15', '__utmz':'226841088.1526446575.15.13.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)', 'lang':"v=2&lang=en-us", 'sdsc':'1%3A1SZM1shxDNbLt36wZwCgPgvN58iw%3D', 'JSESSIONID':"ajax:1654638649399931205", '_gat':'1', 'leo_auth_token':"GST:ZE7JGabBtFIqqn2yEV2JjSnMXmd2XFoyEq6v584-PSxA7iqYqqMFL9:1527138905:bef71c3b83950d1d1033b4345a47ac8eff3697b7", 'sl':"v=1&qoEfS", 'liap':'true', 'li_at':'AQEDARnBXAcFr1_pAAABY5CScBcAAAFjtJ70F00ADowr4sHDk1PGaTBKczUCe-QTJOyzxBnvHf6VLQ_WgudtxDr3mHyN9_bUNuGrZzqhrx0Urroz9rn1mJ3cVzMm5jJ9AMZsAmXsEoPFX66kuegAl9eo', 'RT':'s=1527138899639&r=https%3A%2F%2Fwww.linkedin.com%2F', 'lidc':"b=OB07:g=1113:u=23:i=1527138932:t=1527225306:s=AQGuoT2zIcyGrK0O_ln3g3DUhYZ_QFzc", '_lipt':'CwEAAAFjkJODlE2k52-AN4387YYGOgBtHIsO7cKs7OGWgTZAyzLP5z9B8N7Rn3dSLm9XtF2MA-JMy5HLzDAjQhM_1Wm3D1iR88W_5i5kKunFglf_g_JFPoRkaTkmM_dOitMS_VEKeEuvCCOch1P5lJXnH4wnyvMXQwgEntHPxgbLoWUYNxuv05ZLE2C7vNCzwP4c3g6kShJtUx9h91naXFquYxpGQA3b0m9Obj_W0N6bcVbytjkQXtJZZmKRthoNdjzzbSNCiNNXMrw9mYcIgCYcTdpSSOVDAoq7WzxjZ3fXav79FHWECEq1Q1hMoNsYEjPM_kTcvuMOE26F1z8'}
            #req.cookies={'bcookie':"v=2&e05dda29-c820-4650-8373-3ed9e858cd8e", 'bscookie':"v=1&20180606070922414dfe25-4954-42a4-8f7b-f04af257c141AQGK97-GaBlmNcLuVdDOq96FO93JyI5c", '_ga':'GA1.2.1454141722.1528268939', '_gat':'1', 'lang':"v=2&lang=en-us", 'leo_auth_token':"GST:U4ovFnjyh0NyuFcinZoBnQxJ5ZorjOsM5ijmOFdYPQgrqm_ylhhrMC:1528269001:2cc65ee09e289c052679f618df54c0f8a2a1c9d1", 'sl':"v=1&cW3xB", 'liap':'true', 'JSESSIONID':"ajax:2237063414829956073", 'li_at':'AQEDASeMOT0CTE5DAAABY9PuVMEAAAFj9_rYwU0ArvzEqcz2nmFNDU54calGg1F-EPd6xUtAGpJt4evOyPKBvTrjjT4H5zqFtLnDub3Cp2-2lj4InIKxYKCR1z-t3cJsSKINQub1VxsYeMhX8M1px4gd', 'RT':'s=1528268978445&r=https%3A%2F%2Fwww.linkedin.com%2F', 'sdsc':'22%3A1%2C1528267013170%7ECONN%2C08AZKbC8arqJm%2FXe5fWl%2B8dVWQ90%3D', 'visit':"v=1&M", '_guid':'4c64a23c-52c1-4866-bc74-3ad09611535d', 'lidc':"b=OB17:g=1117:u=2:i=1528269039:t=1528354086:s=AQET8qYj5Fq929X-G3jcrCalnSVH81LH", '_lipt':'CwEAAAFj0_IgjQQWeA6ohqcjxfL3dS_jE2lzpbgLShFSFu5C6Z0-aVES8m9hKKenXGugnLxYyqkZjdchhlPiAUXoZZrpqYLRslBrGt0en7bHYCO6muHpQpjqiUk'}
            req.cookies={'bcookie':"v=2&82486297-7cad-4bd7-87b1-1c7df940c421", 'bscookie':"v=1&2018061905472104a1ac6c-771c-4a2d-8163-9d73c9c52c12AQFGlKAEb7Yb7IhcCIhuNp2SelaCTPik", '_ga':'GA1.2.1079469735.1529387242', 'lang':"v=2&lang=en-us", 'sl':"v=1&2nh6J", 'JSESSIONID':"ajax:0370159712632440138", 'liap':'true', 'li_at':'AQEDASeMOT0Ay1UHAAABZBaV65wAAAFkOqJvnFEAb8tXrySG_XEKSqlbUCpPmSKRDSmlv81tKyLVuE_q36NXOqZKPepdZ-TGfaQhVOEJ93kP4dRIJZEUs-1xex18Gua5XLandmzjLNmN2bTdwtB2xKPc', 'visit':"v=1&M", '_guid':'fd8c960b-fae5-463a-8202-831fe5480291', 'li_oatml':'AQGLfcNrrX2X9wAAAWQWlgREHbse7LN8Se7-Hfyyni112WTeDmgMtF1jDWvM-IhoAan_12RS_gD6Dy8jvwjEUnhbz7tokkD7', 'lidc':"b=SB17:g=88:u=6:i=1529390792:t=1529420192:s=AQF0UoKV0SB_o4WnwDjxTtD7OkIiKW6g", '_lipt':'CwEAAAFkFsx4M68APwjkYsKOSOD4Syxw7tugzVQuqUZg_XO-8f29DYdLSqNLeGh8VcdQUhWV1IGak1d35Iz4GWEqzqPGEexggpETMBTdJpv7kZHYVzWmvg6G5ytCNHGf9sF6rVB9SjhxPe4EfF2_4qKo-TvDpeRl0r4ioo977qZ0hCKvvi70LLUDXD5nnj-wSDGMiAMQhFV05i9-c4fVLg'}
            #req.cookies={'version':'0', 'bcookie':'"v=2&a259f1c2-9956-44c3-8503-300be7615f98"', 'port':'None', 'port_specified':'False', 'domain':'.linkedin.com', 'domain_specified':'True', 'domain_initial_dot':'True', 'path':'/', 'path_specified':'True', 'secure':'False', 'expires':'1590340032', 'discard':'False', 'comment':'None', 'comment_url':'None', 'rfc2109':'False', 'lang':'v=2&lang=en-us', 'lidc':'"b=SGST09:g=3:u=1:i=1527226180:t=1527312580:s=AQFadrSiGMdN7LCYb_2-xEYDlePVvMmH"', 'JSESSIONID':'ajax:7837853262663876103', 'bscookie':'"v=1&2018052505294062bc5df5-e0b3-4149-858c-95f03b6b5a5aAQFmi3LHPHgWABa2VYlWX9VS0OpdHfy6"', 'rest':{'HttpOnly': None}}
            yield req

    def parse1(self,response):
        data=response.xpath('//code[17]//text()').extract()[0]
        data=demjson.decode(data)
        #for key,value in data['included'].items():
        fnames=[fname for fname in data['included'] if fname.has_key("firstName")]
        names= [{'firstName':dicts["firstName"],'lastName':dicts["lastName"],'uniqueID':dicts["objectUrn"],'Occupation':dicts["occupation"],'urlID':dicts["publicIdentifier"]} for dicts in fnames]
        #print [{'firstName':dicts["firstName"],'lastName':dicts["lastName"],'uniqueID':dicts["objectUrn"]} for dicts in fnames]
        finding_ids= [dict1.update({'Location':dict2['location'], 'Industry':dict2['industry']}) for dict1 in names for dict2 in data['included'] if dict2.has_key("backendUrn") if dict1['uniqueID'] == dict2["backendUrn"]]
        #details= [{} location for location in data['included'] if ]
        #all_details=[dict1.update(dict2) for dict1 in names for dict2 in ]
        #all_html=all_html.replace("&quot;","").replace("&#61;","=")
        #print finding_ids
        #print names
        for dict3 in names:
            item=LinkedinItems()
            item['firstName']=dict3['firstName']
            item['lastName']=dict3['lastName']
            item['uniqueID']=dict3['uniqueID']
            item['Occupation']=dict3['Occupation']
            item['urlID']="https://www.linkedin.com/in/"+dict3['urlID']
            item['response_url']=response.url
            item['product_id']=response.meta['product_id']
            try : item['Location']=dict3['Location']
            except: item['Location']=""
            try : item['Industry']=dict3['Industry']
            except: item['Industry']=""
            yield item
			
        for i in range(2,101):
            urlpattern=str(response.url)+"&page="+str(i)
            req=scrapy.Request(urlpattern , headers={'authority': 'www.linkedin.com' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'referer': 'https://www.linkedin.com/' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9' }, callback=self.parse2, meta={'product_id':response.meta['product_id']})
            #req.cookies={'bcookie':"v=2&e05dda29-c820-4650-8373-3ed9e858cd8e", 'bscookie':"v=1&20180606070922414dfe25-4954-42a4-8f7b-f04af257c141AQGK97-GaBlmNcLuVdDOq96FO93JyI5c", '_ga':'GA1.2.1454141722.1528268939', '_gat':'1', 'lang':"v=2&lang=en-us", 'leo_auth_token':"GST:U4ovFnjyh0NyuFcinZoBnQxJ5ZorjOsM5ijmOFdYPQgrqm_ylhhrMC:1528269001:2cc65ee09e289c052679f618df54c0f8a2a1c9d1", 'sl':"v=1&cW3xB", 'liap':'true', 'JSESSIONID':"ajax:2237063414829956073", 'li_at':'AQEDASeMOT0CTE5DAAABY9PuVMEAAAFj9_rYwU0ArvzEqcz2nmFNDU54calGg1F-EPd6xUtAGpJt4evOyPKBvTrjjT4H5zqFtLnDub3Cp2-2lj4InIKxYKCR1z-t3cJsSKINQub1VxsYeMhX8M1px4gd', 'RT':'s=1528268978445&r=https%3A%2F%2Fwww.linkedin.com%2F', 'sdsc':'22%3A1%2C1528267013170%7ECONN%2C08AZKbC8arqJm%2FXe5fWl%2B8dVWQ90%3D', 'visit':"v=1&M", '_guid':'4c64a23c-52c1-4866-bc74-3ad09611535d', 'lidc':"b=OB17:g=1117:u=2:i=1528269039:t=1528354086:s=AQET8qYj5Fq929X-G3jcrCalnSVH81LH", '_lipt':'CwEAAAFj0_IgjQQWeA6ohqcjxfL3dS_jE2lzpbgLShFSFu5C6Z0-aVES8m9hKKenXGugnLxYyqkZjdchhlPiAUXoZZrpqYLRslBrGt0en7bHYCO6muHpQpjqiUk'}
            req.cookies={'bcookie':"v=2&82486297-7cad-4bd7-87b1-1c7df940c421", 'bscookie':"v=1&2018061905472104a1ac6c-771c-4a2d-8163-9d73c9c52c12AQFGlKAEb7Yb7IhcCIhuNp2SelaCTPik", '_ga':'GA1.2.1079469735.1529387242', 'lang':"v=2&lang=en-us", 'sl':"v=1&2nh6J", 'JSESSIONID':"ajax:0370159712632440138", 'liap':'true', 'li_at':'AQEDASeMOT0Ay1UHAAABZBaV65wAAAFkOqJvnFEAb8tXrySG_XEKSqlbUCpPmSKRDSmlv81tKyLVuE_q36NXOqZKPepdZ-TGfaQhVOEJ93kP4dRIJZEUs-1xex18Gua5XLandmzjLNmN2bTdwtB2xKPc', 'visit':"v=1&M", '_guid':'fd8c960b-fae5-463a-8202-831fe5480291', 'li_oatml':'AQGLfcNrrX2X9wAAAWQWlgREHbse7LN8Se7-Hfyyni112WTeDmgMtF1jDWvM-IhoAan_12RS_gD6Dy8jvwjEUnhbz7tokkD7', 'lidc':"b=SB17:g=88:u=6:i=1529390792:t=1529420192:s=AQF0UoKV0SB_o4WnwDjxTtD7OkIiKW6g", '_lipt':'CwEAAAFkFsx4M68APwjkYsKOSOD4Syxw7tugzVQuqUZg_XO-8f29DYdLSqNLeGh8VcdQUhWV1IGak1d35Iz4GWEqzqPGEexggpETMBTdJpv7kZHYVzWmvg6G5ytCNHGf9sF6rVB9SjhxPe4EfF2_4qKo-TvDpeRl0r4ioo977qZ0hCKvvi70LLUDXD5nnj-wSDGMiAMQhFV05i9-c4fVLg'}
            yield req
        #f=open("linkedin_region_search.html","w")
        #f.write(response.body)
        #f.close()
				
    def parse2(self,response):
        data=response.xpath('//code[17]//text()').extract()[0]
        data=demjson.decode(data)
        #for key,value in data['included'].items():
        fnames=[fname for fname in data['included'] if fname.has_key("firstName")]
        names= [{'firstName':dicts["firstName"],'lastName':dicts["lastName"],'uniqueID':dicts["objectUrn"],'Occupation':dicts["occupation"],'urlID':dicts["publicIdentifier"]} for dicts in fnames]
        #print [{'firstName':dicts["firstName"],'lastName':dicts["lastName"],'uniqueID':dicts["objectUrn"]} for dicts in fnames]
        finding_ids= [dict1.update({'Location':dict2['location'], 'Industry':dict2['industry']}) for dict1 in names for dict2 in data['included'] if dict2.has_key("backendUrn") if dict1['uniqueID'] == dict2["backendUrn"]]
        #details= [{} location for location in data['included'] if ]
        #all_details=[dict1.update(dict2) for dict1 in names for dict2 in ]
        #all_html=all_html.replace("&quot;","").replace("&#61;","=")
        #print finding_ids
        #print names
        for dict3 in names:
            item=LinkedinItems()
            item['firstName']=dict3['firstName']
            item['lastName']=dict3['lastName']
            item['uniqueID']=dict3['uniqueID']
            item['Occupation']=dict3['Occupation']
            item['urlID']="https://www.linkedin.com/in/"+dict3['urlID']
            item['response_url']=response.url
            item['product_id']=response.meta['product_id']
            try : item['Location']=dict3['Location']
            except: item['Location']=""
            try : item['Industry']=dict3['Industry']
            except: item['Industry']=""
            yield item