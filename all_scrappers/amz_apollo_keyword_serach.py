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

class AmazonItems(scrapy.Item):
    id1 = scrapy.Field()
    id2 = scrapy.Field()
    asin_title_dict= scrapy.Field()
    mpn = scrapy.Field()
    product_id = scrapy.Field()
    result_count = scrapy.Field()
    response_url = scrapy.Field()

class amazonSpider(scrapy.Spider):
    imgcount = 1
    name = "amz_apollo_keyword_serach"
    allowed_domains = []

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]

    def parse(self, response):
        urls_done=[]
        urls=[
["2","7674","94280","1012"],
["3","7724","94281","1013"],
["4","4791","94283","1016"],
["5","15648","94284","1017"],
["6","8535","94285","1018"],
["7","12518","94286","1019"],
["8","5034","94287","1051"],
]
        for url in urls:
            urlpattern="https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="+url[3].replace(' ','+').replace('/','%2F')
            #requesturl = scrapy.FormRequest(urlpattern,callback=self.parse1,headers={'Origin': 'https://www.amazon.com', 'Referer':'https://www.amazon.com', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.8', 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36, LuminadBot/1.0 (Apollo@Luminad.com)', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' ,'Cache-Control': 'max-age=0' }, dont_filter=True)
            #requesturl = scrapy.FormRequest(urlpattern,callback=self.parse1,headers={'Origin': 'https://www.amazon.com', 'Referer':'https://www.amazon.com', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.8', 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36, LuminadBot/1.0 (Apollo@Luminad.com)', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' ,'Cache-Control': 'max-age=0' }, dont_filter=True)
            #requesturl = scrapy.FormRequest(urlpattern,callback=self.parse1,headers={'Origin': 'https://www.amazon.com', 'Referer':'https://www.amazon.com', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.8', 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36, LuminadBot/1.0 (Apollo@Luminad.com)', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' ,'Cache-Control': 'max-age=0' }, dont_filter=True)
            #requesturl.cookies = {'aws-target-static-id':'1452239187641-159842', 'aws-business-metrics-last-visit':'1460349972900', '__utmv':'194891197.%22QDSe8l%404pyTIl%3FpKm5C24aEFXeBtLGw3BhDIGikRUeXlFGLshyp4Dtw4gLRG%3F9cU%22', 'aws-userInfo':'%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A111320495319%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22rahul%2520bhaskar%22%2C%22keybase%22%3A%22%22%2C%22issuer%22%3A%22https%3A%2F%2Fwww.amazon.com%2Fap%2Fsignin%22%7D', 's_pers':'%20s_vnum%3D1880352564702%2526vn%253D3%7C1880352564702%3B%20s_invisit%3Dtrue%7C1470309348410%3B%20s_nr%3D1470307548416-Repeat%7C1478083548416%3B', '__utma':'194891197.372951375.1452236845.1470290622.1470307550.17', 'aws-ubid-main':'182-7331780-4611541', '_mkto_trk':'id:112-TZM-766&token:_mch-aws.amazon.com-1484112318467-15791', 'aws-target-visitor-id':'1452239187643-451048.20_19', 'aws-target-data':'%7B%22support%22%3A%221%22%7D', 's_fid':'70673D38D5DFE123-1B689FC000FE2EFF', 'regStatus':'registered', 'ubid-main':'156-9680828-0484351', 'ca':'ALAAAAAAEAAAAAQGAAEIAUQ=', 's_vnum':'1926421318258%26vn%3D2', 's_nr':'1514281824850-New', 's_dslv':'1514281824851', 'session-id':'144-3935774-8062208', 'session-id-time':'2082787201l', 'x-amz-captcha-1':'1518768468239967', 'x-amz-captcha-2':'8brJzDGjVr0g6SMt7y51KQ==', 'a-ogbcbff':'1', 'x-main':'"fycgicqnXAG9h3NMiDoGTALK8XmKMT8Y7zmG2J0BNpcL1f@?TcYxcPMWWipZhvof"', 'at-main':'Atza|IwEBIJvW6xlsbiH1hRs9vJ2V_w16jlQhSQjg3ehsg3W76LxrQT-VH9tsIRiHoHcaMXn9pyYCgqS8ncyALBot9Lfa-oHQ9B5haHTZ234l1wd5cjS3lIpoebl3XqE8R13u2oHsAscFbcYZ1OArAxJHSYSkJxFwIlml-M4T3b8VcujEZdeoQEzvAipwwJHDzh7P4QQmNxSFyR7173IySmfados6vrpYc0OdSwLDpR42eLBACHhfFxTrY2EdG0O7vgr2UoDUnvd4o5SOTq54TBh4f2fNkV5OObxldSU1DMPF7E4PJnqBYC0n_gjy2Re3AId4a80qUdi0mQGItumFTtvkVmM_Ha5AXBWKaUL2SLS9RWjbeDoBRIQdaftjGACfgp_USVFfOBWwq_-7HQbM7J_EasxZZjfzA9JdgMGy37DAIGWG9abF-A2XLSehJ3qw9yD6Ce0it8E', 'sess-at-main':'"pXRzY7+0cEA6QAXiw7xtqkVPnlTizA/bSV5Ufn8LWUQ="', 'sst-main':'Sst1|PQFckmUHN5sOVumX4CdB104DCaCzuvSHXylkeh4qpfwQHzhV2em2zJkPumi2szBhhz9iPmGUE6CWI7DPT2W-mOFK_1ffiVN_x7DG-d0D6cM-mLVUboxgRg6LPiCypuwOCA2ORnqALrSSjuRTm8JbkhYlSW1hevw1Va5WGMEvvNpNAg4AtoISvv6jyI79Gsl3-drWQ6lRJ9PSdiUTY2SgCdjGnexsZA_-Rnd9BInaqRJzwMYPOlCHY9p-4QpuybnnbX17HPFzOAJhrhSCUiDFSEt9wYOKaMQw3urk_a2zCjOjBwo', 'lc-main':'en_US', 'x-wl-uid':'1qO28TBan5h3oE1QxU2WGyoczvrC0FTgSurawI1g3sgmWQYwqLKN1zESoN3ANbMEfUc3uWSsKr9FyRbNyggYPQ+zMMdgAVJ2WL/Tf3lZHoYsm3zTt0ornhvjL6gVv6qw2U2rxb397ybM7PcAb7MFQVQ==', 'session-token':'"8oBu2yRmYSRcMko83QPjy+BgTzk9Hoeu/IhZqLO6f9E6sk3RoJ5TYUU+uS72FeKUc/090SieEJSZ4zIMwli8u+wD1adpp/yhZA6tz6CgQs96B6clWL1YtQZuyYMlXLRIxynxTrfIXGxY01cAkMTzFq+Dz2tG/5U194x6UTPT684kVRuSYdXgGsTzDoN/af1mq+m4FjMcoS4q/SJJRMHzDiQUmcKll91lr4Eemcp7bfnd7huqHdUFMgC/i0Jl7w5TA9Vgmcih4vGkWck7b5lAaA=="', 'csm-hit':'GJ6HJMM3CFA43W994KHK+b-ZQ6HYQ744MSFND7T1VVB|1519010944543'}
            #request = Request(url,headers={'Origin': 'https://www.amazon.com', 'Referer':'https://www.amazon.com', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.8', 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36, LuminadBot/1.0 (Apollo@Luminad.com)', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' ,'Cache-Control': 'max-age=0' }, dont_filter=True)
            #request.cookies = {'aws-target-static-id':'1452239187641-159842', 'aws-business-metrics-last-visit':'1460349972900', '__utmv':'194891197.%22QDSe8l%404pyTIl%3FpKm5C24aEFXeBtLGw3BhDIGikRUeXlFGLshyp4Dtw4gLRG%3F9cU%22', 'aws-userInfo':'%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A111320495319%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22rahul%2520bhaskar%22%2C%22keybase%22%3A%22%22%2C%22issuer%22%3A%22https%3A%2F%2Fwww.amazon.com%2Fap%2Fsignin%22%7D', 's_pers':'%20s_vnum%3D1880352564702%2526vn%253D3%7C1880352564702%3B%20s_invisit%3Dtrue%7C1470309348410%3B%20s_nr%3D1470307548416-Repeat%7C1478083548416%3B', '__utma':'194891197.372951375.1452236845.1470290622.1470307550.17', 'aws-ubid-main':'182-7331780-4611541', '_mkto_trk':'id:112-TZM-766&token:_mch-aws.amazon.com-1484112318467-15791', 'aws-target-visitor-id':'1452239187643-451048.20_19', 'aws-target-data':'%7B%22support%22%3A%221%22%7D', 's_fid':'70673D38D5DFE123-1B689FC000FE2EFF', 'regStatus':'registered', 'ubid-main':'156-9680828-0484351', 'ca':'ALAAAAAAEAAAAAQGAAEIAUQ=', 's_vnum':'1926421318258%26vn%3D2', 's_nr':'1514281824850-New', 's_dslv':'1514281824851', 'session-id':'144-3935774-8062208', 'session-id-time':'2082787201l', 'x-amz-captcha-1':'1518768468239967', 'x-amz-captcha-2':'8brJzDGjVr0g6SMt7y51KQ==', 'a-ogbcbff':'1', 'x-main':'"fycgicqnXAG9h3NMiDoGTALK8XmKMT8Y7zmG2J0BNpcL1f@?TcYxcPMWWipZhvof"', 'at-main':'Atza|IwEBIJvW6xlsbiH1hRs9vJ2V_w16jlQhSQjg3ehsg3W76LxrQT-VH9tsIRiHoHcaMXn9pyYCgqS8ncyALBot9Lfa-oHQ9B5haHTZ234l1wd5cjS3lIpoebl3XqE8R13u2oHsAscFbcYZ1OArAxJHSYSkJxFwIlml-M4T3b8VcujEZdeoQEzvAipwwJHDzh7P4QQmNxSFyR7173IySmfados6vrpYc0OdSwLDpR42eLBACHhfFxTrY2EdG0O7vgr2UoDUnvd4o5SOTq54TBh4f2fNkV5OObxldSU1DMPF7E4PJnqBYC0n_gjy2Re3AId4a80qUdi0mQGItumFTtvkVmM_Ha5AXBWKaUL2SLS9RWjbeDoBRIQdaftjGACfgp_USVFfOBWwq_-7HQbM7J_EasxZZjfzA9JdgMGy37DAIGWG9abF-A2XLSehJ3qw9yD6Ce0it8E', 'sess-at-main':'"pXRzY7+0cEA6QAXiw7xtqkVPnlTizA/bSV5Ufn8LWUQ="', 'sst-main':'Sst1|PQFckmUHN5sOVumX4CdB104DCaCzuvSHXylkeh4qpfwQHzhV2em2zJkPumi2szBhhz9iPmGUE6CWI7DPT2W-mOFK_1ffiVN_x7DG-d0D6cM-mLVUboxgRg6LPiCypuwOCA2ORnqALrSSjuRTm8JbkhYlSW1hevw1Va5WGMEvvNpNAg4AtoISvv6jyI79Gsl3-drWQ6lRJ9PSdiUTY2SgCdjGnexsZA_-Rnd9BInaqRJzwMYPOlCHY9p-4QpuybnnbX17HPFzOAJhrhSCUiDFSEt9wYOKaMQw3urk_a2zCjOjBwo', 'lc-main':'en_US', 'x-wl-uid':'1qO28TBan5h3oE1QxU2WGyoczvrC0FTgSurawI1g3sgmWQYwqLKN1zESoN3ANbMEfUc3uWSsKr9FyRbNyggYPQ+zMMdgAVJ2WL/Tf3lZHoYsm3zTt0ornhvjL6gVv6qw2U2rxb397ybM7PcAb7MFQVQ==', 'session-token':'"8oBu2yRmYSRcMko83QPjy+BgTzk9Hoeu/IhZqLO6f9E6sk3RoJ5TYUU+uS72FeKUc/090SieEJSZ4zIMwli8u+wD1adpp/yhZA6tz6CgQs96B6clWL1YtQZuyYMlXLRIxynxTrfIXGxY01cAkMTzFq+Dz2tG/5U194x6UTPT684kVRuSYdXgGsTzDoN/af1mq+m4FjMcoS4q/SJJRMHzDiQUmcKll91lr4Eemcp7bfnd7huqHdUFMgC/i0Jl7w5TA9Vgmcih4vGkWck7b5lAaA=="', 'csm-hit':'GJ6HJMM3CFA43W994KHK+b-ZQ6HYQ744MSFND7T1VVB|1519010944543'}
            requesturl = scrapy.FormRequest(urlpattern,callback=self.parse1, dont_filter=True)

            #requesturl.cookies ={'aws-target-static-id':'1452239187641-159842', 'aws-business-metrics-last-visit':'1460349972900', '__utmv':'194891197.%22QDSe8l%404pyTIl%3FpKm5C24aEFXeBtLGw3BhDIGikRUeXlFGLshyp4Dtw4gLRG%3F9cU%22', 'aws-userInfo':'%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A111320495319%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22rahul%2520bhaskar%22%2C%22keybase%22%3A%22%22%2C%22issuer%22%3A%22https%3A%2F%2Fwww.amazon.com%2Fap%2Fsignin%22%7D; s_pers=%20s_vnum%3D1880352564702%2526vn%253D3%7C1880352564702%3B%20s_invisit%3Dtrue%7C1470309348410%3B%20s_nr%3D1470307548416-Repeat%7C1478083548416%3B', '__utma':'194891197.372951375.1452236845.1470290622.1470307550.17', 'aws-ubid-main':'182-7331780-4611541', '_mkto_trk':'id:112-TZM-766&token:_mch-aws.amazon.com-1484112318467-15791', 'aws-target-visitor-id':'1452239187643-451048.20_19', 'aws-target-data':'%7B%22support%22%3A%221%22%7D', 's_fid':'70673D38D5DFE123-1B689FC000FE2EFF', 'regStatus':'registered', 'ubid-main':'156-9680828-0484351', 'ca':'ALAAAAAAEAAAAAQGAAEIAUQ=', 's_vnum':'1926421318258%26vn%3D2', 's_nr':'1514281824850-New', 's_dslv':'1514281824851', 'session-id':'144-3935774-8062208', 'session-id-time':'2082787201l', 'x-amz-captcha-1':'1518768468239967', 'x-amz-captcha-2':'8brJzDGjVr0g6SMt7y51KQ==', 'x-main':'"fycgicqnXAG9h3NMiDoGTALK8XmKMT8Y7zmG2J0BNpcL1f@?TcYxcPMWWipZhvof"', 'at-main':'Atza|IwEBIJvW6xlsbiH1hRs9vJ2V_w16jlQhSQjg3ehsg3W76LxrQT-VH9tsIRiHoHcaMXn9pyYCgqS8ncyALBot9Lfa-oHQ9B5haHTZ234l1wd5cjS3lIpoebl3XqE8R13u2oHsAscFbcYZ1OArAxJHSYSkJxFwIlml-M4T3b8VcujEZdeoQEzvAipwwJHDzh7P4QQmNxSFyR7173IySmfados6vrpYc0OdSwLDpR42eLBACHhfFxTrY2EdG0O7vgr2UoDUnvd4o5SOTq54TBh4f2fNkV5OObxldSU1DMPF7E4PJnqBYC0n_gjy2Re3AId4a80qUdi0mQGItumFTtvkVmM_Ha5AXBWKaUL2SLS9RWjbeDoBRIQdaftjGACfgp_USVFfOBWwq_-7HQbM7J_EasxZZjfzA9JdgMGy37DAIGWG9abF-A2XLSehJ3qw9yD6Ce0it8E', 'sess-at-main':'"pXRzY7+0cEA6QAXiw7xtqkVPnlTizA/bSV5Ufn8LWUQ="', 'sst-main':'Sst1|PQFckmUHN5sOVumX4CdB104DCaCzuvSHXylkeh4qpfwQHzhV2em2zJkPumi2szBhhz9iPmGUE6CWI7DPT2W-mOFK_1ffiVN_x7DG-d0D6cM-mLVUboxgRg6LPiCypuwOCA2ORnqALrSSjuRTm8JbkhYlSW1hevw1Va5WGMEvvNpNAg4AtoISvv6jyI79Gsl3-drWQ6lRJ9PSdiUTY2SgCdjGnexsZA_-Rnd9BInaqRJzwMYPOlCHY9p-4QpuybnnbX17HPFzOAJhrhSCUiDFSEt9wYOKaMQw3urk_a2zCjOjBwo', 'lc-main':'en_US', 'skin':'noskin', 'x-wl-uid':'1P2s8zV8gxeEeFD0Dn38stQHvpnAB9kKzAfUX70mWSo0oCR8zQo0Ce3ujwaqav3zL/F1TgQbugbMwwDC54cWrZjWF5WwTyi24JvBVR3uC7q3Gz3N7jvQzsBcAhpJ1oOaHzinPOOjXkMs=', 'session-token':'vi6m1V7KbHp+5PQ5TjJhpEuSzmPhxOVkSBlXFcKGXajlz/F5OGhdXKzK/KmtNKXD014wZpCIYsOwWySIiO/8ZE1YghBUDxNuziX/lL1GOG0aM6yT+4F0flwQkjq+YWe/sIezg5ZVCM0EO99qUIS7eagBJZVftS8dqUzeF99VElq2l+N3mqXNVKlvYzj8bna5vMMVRcPBMLK/U33pmVI47i0GV4wqMuAu+Li1gd/4tXdGCFUVjb1KhroBaeZxbGHgmId8egTZy/5GDzqReIbbwg==', 'csm-hit':'tb:Z9P2TYNR9D868FBPRFKQ+s-BX5XTSPM1V76MW5STEB8|1520227993291&adb:adblk_no' } 
            requesturl.meta['product_id']=url[0]
            requesturl.meta['id1']=url[1]
            requesturl.meta['id2']=url[2]
            requesturl.meta['mpn']=url[3]
            time.sleep(.1)
            yield requesturl
        #url='http://www.upcbarcodes.com/wp-admin/admin-ajax.php'        # print input_seller_name
        #zipcodelist=["60629","11385","10025","91911","78572","33012","75228","33157","95111","60453","70072","17602","55337","57701","2895","98125","35216","29841","68701","83815"]
        #for zipcodes in zipcodelist:
        #    requsturl=scrapy.FormRequest('https://www.amazon.com/gp/delivery/ajax/address-change.html', headers= { 'Origin': 'https://www.amazon.com', 'Accept-Encoding': 'gzip, deflate, br' ,'Accept-Language': 'en-US,en;q=0.9' ,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8' ,'Accept': 'text/html,*/*' , 'Referer': 'https://www.amazon.com/' , 'X-Requested-With': 'XMLHttpRequest' , 'Connection': 'keep-alive'  }, formdata={'zipCode': zipcodes,'locationType':'LOCATION_INPUT','deviceType':'web','pageType':'Detail'} ,callback=self.getupc,method="POST", meta={'zipcode':zipcodes}, dont_filter=True)
        #    #print requsturl.body
        #    #requsturl.

        #    #requsturl.cookies = { 'aws-target-static-id':'1452239187641-159842', 'aws-business-metrics-last-visit':'1460349972900', '__utmv':'194891197.%22QDSe8l%404pyTIl%3FpKm5C24aEFXeBtLGw3BhDIGikRUeXlFGLshyp4Dtw4gLRG%3F9cU%22', 'aws-userInfo':'%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A111320495319%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22rahul%2520bhaskar%22%2C%22keybase%22%3A%22%22%2C%22issuer%22%3A%22https%3A%2F%2Fwww.amazon.com%2Fap%2Fsignin%22%7D', 's_pers':'%20s_vnum%3D1880352564702%2526vn%253D3%7C1880352564702%3B%20s_invisit%3Dtrue%7C1470309348410%3B%20s_nr%3D1470307548416-Repeat%7C1478083548416%3B', '__utma':'194891197.372951375.1452236845.1470290622.1470307550.17', 'aws-ubid-main':'182-7331780-4611541', '_mkto_trk':'id:112-TZM-766&token:_mch-aws.amazon.com-1484112318467-15791', 'x-amz-captcha-1':'1494506850389641', 'x-amz-captcha-2':'7TNj5/ZBUiQE8Q7M1TGIGw==', 'aws-target-visitor-id':'1452239187643-451048.20_19', 'aws-target-data':'%7B%22support%22%3A%221%22%7D', 's_fid':'70673D38D5DFE123-1B689FC000FE2EFF', 's_vn':'1515648318007%26vn%3D7', 'regStatus':'registered', 'x-wl-uid':'1YbHUe7z4Q16UzYOKnza7nF0Z8c60AUse7MqEp+CAv+wdJamSRB88EpQjCOb5Xsg9wS/EFz0+hhSbAl3qbMeh7dWiD1jtJRDs/6R5VxAFk6LzV16+6hZ0Cz+uIpt9TzsXS7IGe2aDx3Q=', 'sst-main':'Sst1|PQGX_RwjQAxLFI_BwdTV0Q4UCL8-RIlysfyKrjYoFGe3oqm9lnuttlbX-lGX4weSExupeA7cYB3Zb0CSGU91LcK9xa8Av4IeMWfbcMKAV4AXqvCSM7S-SXJJpEWQhn0AsaJNc4wwxVVQzrZRhD4jVmdocyJewDAfSRGF1SSTgg_cvNGYGZx8-WqW1z-bekrkDEc-ZrMz9f9Ii077rpcz7Q0tBrE5xr2htKXdWZUzmT4ZSBqkJ9NlatkaEU7sYxBuyl0LadTT6wmYRPPfHnJzSQYdUQ', 'ubid-main':'156-9680828-0484351', 'ca':'ALAAAAAAEAAAAAQGAAEIAUQ=', 's_vnum':'1926421318258%26vn%3D2', 's_nr':'1514281824850-New', 's_dslv':'1514281824851', 'session-id':'144-3935774-8062208', 'session-token':'"n2d7o5bJUB480T+okCcD+Qgte5eb6+XVoWrh4WzA8cPLcyI8v4G8hDqqoR2uWyzLBg4ETAaFwIQ6lGxkm9Hx8EmSQMVq4In0q2pXM0KD/1jNBUtqnPJf5WRZb/xRJGL2mIv58UxYLpLX0e1wf6XYjtrHfPcAOONchcbeZIpAXZOil1fCyrFDBgE3AmUSvlFNadxFHlRhG6IUrSJ/W7TAEw=="', 'session-id-time':'2082787201l', 'csm-hit':'%7B%22tb%22%3A%227099AAE54J4R4DQXDH89%2Bs-7099AAE54J4R4DQXDH89%7C1515471521353%22%2C%22adb%22%3A%22adblk_no%22%7D' }
        #    requsturl.cookies = {'x-wl-uid':'1QBgT0TBwoj9RQ+QP7eh8ocBTABgs1739+rzq1e3s1iwjoSRYnMpbAczaaknzT2id2ww9iSyiyXd3OQeaJ9Nm9xZrZOKqXNWIDJihS4V7CV+xlp+PQA7T/ILJyNBZ15so9XvNPTzCBQA=', 'x-amz-captcha-1':'1511784189246059', 'x-amz-captcha-2':'e+dIUFBcjimZCAzt1M7ENg==', 'skin':'noskin', 's_cc':'true', 's_nr':'1514464459649-Repeat', 's_vnum':'1935816974090%26vn%3D2', 's_dslv':'1514464459650', 's_sq':'%5B%5BB%5D%5D', 'amznacsleftnav-74393fbe-66a6-3a52-840b-37b54d8c76ce':'1', 'ubid-main':'151-8001146-5395566', 'session-id':'143-2570392-1761151', 'session-id-time':'2082787201l', 'session-token':'06YC+sJBPQUYica59Tep0SDc/OdZYTQk3nRUXwMQ9ZmJuSTmJrg+RBhaKKMtSTw3JQmmVuO3ivHRybUoZlp/Lb25cUBOQGLD18j18BjmoDMwnAVTFYJCwm/m3y5jPQeB0R+2uhl1LI4U6not78OaHrRqy4mxqRjwgLpf0e2GYbKAHbN0i1BQkXoyX5rlQjM+', 'csm-hit':'HRT1PQHJ2W7REDHGHZ8C+s-HRT1PQHJ2W7REDHGHZ8C|1517381562270' }
        #    #time.sleep(.2)
        #    yield requsturl
		
		
    def parse1(self, response):
        item=AmazonItems()
        item['product_id']=response.meta["product_id"]
        item['id1']=response.meta["id1"]
        item['id2']=response.meta["id2"]
        item['mpn']=response.meta["mpn"]
        item['response_url']=response.url
        try:
            totalcount = response.xpath('//*[@id="s-result-count"]/text()').extract()[0]
        except:
            totalcount = "NA"
			
        item['result_count']=totalcount
        if totalcount is not "NA":
            all_list=response.xpath('//div[@id="atfResults"]/ul[@id="s-results-list-atf"]/li')
            if not all_list: all_list=response.xpath('//*[@id="mainResults"]/ul/li')
            asin_list = all_list.xpath('@data-asin').extract()
            title_list = all_list.xpath('div[@class="s-item-container"]/div[3]/div[1]/a/h2/text()').extract()
            if not title_list: title_list=all_list.xpath('div[@class="s-item-container"]/div/div/div[2]/div[1]/div[1]/a/h2/text()').extract()
            if not title_list: title_list=all_list.xpath('div[@class="s-item-container"]/div[2]/div/div[2]/div[1]/div[1]/a/h2/text()').extract()
            #print "asin_list : ", asin_list
            #print "title_list : ", title_list
			
            if len(asin_list)>= 5:
                #print "asin_list: ", len(asin_list)
                asin_title_dict=dict(zip(asin_list[:5],title_list[:5]))
            else:
                asin_title_dict=dict(zip(asin_list,title_list))
                #print "asin_list: ", len(asin_list)
            item['asin_title_dict']=asin_title_dict
            #print "asin_title_dict : ", asin_title_dict
        else: item['asin_title_dict']="NA"
        yield item