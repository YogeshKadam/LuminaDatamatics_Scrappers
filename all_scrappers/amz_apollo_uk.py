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
    price = scrapy.Field()
    price1 = scrapy.Field()
    ship_price = scrapy.Field()
    asin= scrapy.Field()
    seller_name = scrapy.Field()
    url = scrapy.Field()

class amazonSpider(scrapy.Spider):
    imgcount = 1
    name = "amz_apollo_uk"
    allowed_domains = []

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]

    def parse(self, response):
        urls_done=[]
        urls=[
"B077Z23ZXJ",
"B004NJZ8S8",
"B000VOCQPW",
"B01B51Z1J2",
"B004I655NY",
]
        for url in urls:
            #requesturl = scrapy.FormRequest("https://www.amazon.de/dp/"+url,callback=self.parse1,headers={'Origin': 'https://www.amazon.com', 'Referer':'https://www.amazon.com', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.8', 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36, LuminadBot/1.0 (Apollo@Luminad.com)', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' ,'Cache-Control': 'max-age=0' }, dont_filter=True)
            #requesturl.cookies = {'aws-target-static-id':'1452239187641-159842', 'aws-business-metrics-last-visit':'1460349972900', '__utmv':'194891197.%22QDSe8l%404pyTIl%3FpKm5C24aEFXeBtLGw3BhDIGikRUeXlFGLshyp4Dtw4gLRG%3F9cU%22', 'aws-userInfo':'%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A111320495319%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22rahul%2520bhaskar%22%2C%22keybase%22%3A%22%22%2C%22issuer%22%3A%22https%3A%2F%2Fwww.amazon.com%2Fap%2Fsignin%22%7D', 's_pers':'%20s_vnum%3D1880352564702%2526vn%253D3%7C1880352564702%3B%20s_invisit%3Dtrue%7C1470309348410%3B%20s_nr%3D1470307548416-Repeat%7C1478083548416%3B', '__utma':'194891197.372951375.1452236845.1470290622.1470307550.17', 'aws-ubid-main':'182-7331780-4611541', '_mkto_trk':'id:112-TZM-766&token:_mch-aws.amazon.com-1484112318467-15791', 'aws-target-visitor-id':'1452239187643-451048.20_19', 'aws-target-data':'%7B%22support%22%3A%221%22%7D', 's_fid':'70673D38D5DFE123-1B689FC000FE2EFF', 'regStatus':'registered', 'ubid-main':'156-9680828-0484351', 'ca':'ALAAAAAAEAAAAAQGAAEIAUQ=', 's_vnum':'1926421318258%26vn%3D2', 's_nr':'1514281824850-New', 's_dslv':'1514281824851', 'session-id':'144-3935774-8062208', 'session-id-time':'2082787201l', 'x-amz-captcha-1':'1518768468239967', 'x-amz-captcha-2':'8brJzDGjVr0g6SMt7y51KQ==', 'a-ogbcbff':'1', 'x-main':'"fycgicqnXAG9h3NMiDoGTALK8XmKMT8Y7zmG2J0BNpcL1f@?TcYxcPMWWipZhvof"', 'at-main':'Atza|IwEBIJvW6xlsbiH1hRs9vJ2V_w16jlQhSQjg3ehsg3W76LxrQT-VH9tsIRiHoHcaMXn9pyYCgqS8ncyALBot9Lfa-oHQ9B5haHTZ234l1wd5cjS3lIpoebl3XqE8R13u2oHsAscFbcYZ1OArAxJHSYSkJxFwIlml-M4T3b8VcujEZdeoQEzvAipwwJHDzh7P4QQmNxSFyR7173IySmfados6vrpYc0OdSwLDpR42eLBACHhfFxTrY2EdG0O7vgr2UoDUnvd4o5SOTq54TBh4f2fNkV5OObxldSU1DMPF7E4PJnqBYC0n_gjy2Re3AId4a80qUdi0mQGItumFTtvkVmM_Ha5AXBWKaUL2SLS9RWjbeDoBRIQdaftjGACfgp_USVFfOBWwq_-7HQbM7J_EasxZZjfzA9JdgMGy37DAIGWG9abF-A2XLSehJ3qw9yD6Ce0it8E', 'sess-at-main':'"pXRzY7+0cEA6QAXiw7xtqkVPnlTizA/bSV5Ufn8LWUQ="', 'sst-main':'Sst1|PQFckmUHN5sOVumX4CdB104DCaCzuvSHXylkeh4qpfwQHzhV2em2zJkPumi2szBhhz9iPmGUE6CWI7DPT2W-mOFK_1ffiVN_x7DG-d0D6cM-mLVUboxgRg6LPiCypuwOCA2ORnqALrSSjuRTm8JbkhYlSW1hevw1Va5WGMEvvNpNAg4AtoISvv6jyI79Gsl3-drWQ6lRJ9PSdiUTY2SgCdjGnexsZA_-Rnd9BInaqRJzwMYPOlCHY9p-4QpuybnnbX17HPFzOAJhrhSCUiDFSEt9wYOKaMQw3urk_a2zCjOjBwo', 'lc-main':'en_US', 'x-wl-uid':'1qO28TBan5h3oE1QxU2WGyoczvrC0FTgSurawI1g3sgmWQYwqLKN1zESoN3ANbMEfUc3uWSsKr9FyRbNyggYPQ+zMMdgAVJ2WL/Tf3lZHoYsm3zTt0ornhvjL6gVv6qw2U2rxb397ybM7PcAb7MFQVQ==', 'session-token':'"8oBu2yRmYSRcMko83QPjy+BgTzk9Hoeu/IhZqLO6f9E6sk3RoJ5TYUU+uS72FeKUc/090SieEJSZ4zIMwli8u+wD1adpp/yhZA6tz6CgQs96B6clWL1YtQZuyYMlXLRIxynxTrfIXGxY01cAkMTzFq+Dz2tG/5U194x6UTPT684kVRuSYdXgGsTzDoN/af1mq+m4FjMcoS4q/SJJRMHzDiQUmcKll91lr4Eemcp7bfnd7huqHdUFMgC/i0Jl7w5TA9Vgmcih4vGkWck7b5lAaA=="', 'csm-hit':'GJ6HJMM3CFA43W994KHK+b-ZQ6HYQ744MSFND7T1VVB|1519010944543'}
            #requesturl = scrapy.FormRequest( "https://www.amazon.de/dp/"+ url,callback=self.parse1, headers={'Origin': 'https://www.amazon.de', 'Referer':'https://www.amazon.de', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.8', 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36, LuminadBot/1.0 (Apollo@Luminad.com)', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' ,'Cache-Control': 'max-age=0' }, dont_filter=True)
        
            #requesturl.cookies ={'s_pers':'%20s_fid%3D300B8810F7CDBDE1-10092DE00A8359D7%7C1558680220920%3B%20s_dl%3D1%7C1495610020921%3B%20gpv_page%3DDE%253AAZ%253ASOA-Landing%7C1495610020924%3B%20s_ev15%3D%255B%255B%2527AZDEGNOSellC%2527%252C%25271495608209183%2527%255D%252C%255B%2527AZDEGNOSellC%2527%252C%25271495608216403%2527%255D%252C%255B%2527AZDEGNOSellC%2527%252C%25271495608220916%2527%255D%252C%255B%2527AZDEGNOSellC%2527%252C%25271495608220925%2527%255D%255D%7C1653374620925%3B%20s_eVar26%3DAmazon%2520Services%2520DE%7C1498200220927%3B', 'amznacsleftnav-656eac4a-695b-3a6a-946f-db61e4deb392':'1', 'amznacsleftnav-fdfd699f-c863-3b78-85b2-8a649c6b58f6':'1', 'x-amz-captcha-1':'1508482986892769', 'x-amz-captcha-2':'hw3RhTh0tvhX81cdMFkFgQ==', 'lc-acbde':'de_DE', 'session-id':'261-5677163-4561642', 'ubid-acbde':'259-8821950-7904223', 'a-ogbcbff':'1', 'x-acbde':'"V0z3CSC5jraR2B7OY6OiPR3wrDO7GbRjA9fTg2AJTorXXbAPToPEDvMAo8KTh@7M"', 'at-acbde':'Atza|IwEBIHwqc3CD45BqlJs_5aa-V8dGYqRemzUHaOJhdARXf-o6rlAp0DANlQO8ZPGB23Uek573IjBb2qkX4mlZWKna1Xn3pOzTpiUd0SQO7gh-uTZnxF5r2p22mMsR4_clEZvBBlZBMJYXD6HPxW7_sEYtklqCkY-Br197rDnz9KPza3y5u7XzgezJIBdXCaeq4vAqo9Wrl0uG0RGKSr41-4rKK9hpnGK1nN4UbO_qWxnLSwzA6LwgXczqe0C5EyH1HIp12IlKFB7OgxIEsH0QZAiT0eh0D7sFwlVG6eHfqPNWfix03SZ7apAC7C7jQ-vw1lmICAeJciD9QmumuCNEDDCT-GGWCkrAh-gxMRhKpm7Q5_gOtJijbqoLi3VfPO9QrCA7hYW8Atc-kFRIW3Y6vtRc8OZzZipCneewy-Rj_xYUMFVWMCmHs_ljfe2W6vxWgiRfmyw', 'sess-at-acbde':'"NbwPRqfG4oPuznYLUmFM5Y5JSvyizaA9ZJz6vTkNQL4="', 'sst-acbde':'Sst1|PQEs5smXCO43G8WIotdsANHyCEBZ9TkcZ_OdLYTgnk2mCfAy4Z5W77Y7zX74BQuxS7UKtfnUM6KkKhmcu01A2Fq7xshyjesDvnQDYp9QYcrFDvlceaVvpWqQfpEt2Q9XIM0VQFdd2EMpXc4C9QlehgHT0URfOlUmC47BkfeJr5dpb4Pv_dbnFASQli0k7Cln9sN_Vf4Wqz4km-6UTpsNlVJxJE48_RK6Zsk7bklH_cpJE8tfltiPzdhyhY2oDh7SieUx6CNKphxtIezjzr-0SbD8cg', 'x-wl-uid':'11PAl+O2T6FeY67SmgtWeMBtyZ538YMsy2Zcpov67B4kL2DVIv3Nx7rEprTLBkI4W3ZZ954YAADFuG1oAMSt9uIgNhk3yQfBCY6pDMJUcXUzK6rFTPF4tPnrWr3utKPzHqJATwvQOHKE=', 'session-token':'"tzfdQwuhV4SLJ9/PfV3QSfg2b3LxOcRlqovsFb3AsrqZSnkxHCjhgMsO3d7NbIS7rOee9CPoh7Lxo8LF7EdVopNDFYLMzzOtDGVhnY4czMEVNS5VHAxjtdaDvRNDJC0OloD0EvRMDfHeXG70D93/wWVNfqU0c6nKEv0yTLU7pFpIbTicUYQQFeDZYf9tPQEepQxbZ1pBOU+0FjTwWUj3SnNdDf/SVmmk+feDLRuqn+WcP6w6CPQ1G03W/TACUuIHBz9mSMRFPU0il4m+s0KyzA=="', 'csm-hit':'s-F8Q4HD9WHE8M6GMQKQT4|1519186540551', 'session-id-time':'2082754801l' }
            requesturl = scrapy.FormRequest("https://www.amazon.co.uk/dp/"+ url+"/", callback=self.parse1, headers={'Origin': 'https://www.amazon.co.uk', 'Referer':'https://www.amazon.co.uk', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.8', 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36, LuminadBot/1.0 (Apollo@Luminad.com)', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' ,'Cache-Control': 'max-age=0' }, dont_filter=True)
        
            requesturl.cookies ={'lc-acbuk':'en_GB', 'ubid-acbuk':'255-8382042-2981010', 'session-id':'254-2692518-4950132', 'a-ogbcbff':'1', 'x-acbuk':'"A7XPzcqQrZk3LW9WzTvINrapg@pv0RKLj0QMGoi7H3MOtG@OpJMrmLTWLCCNrP1A"', 'at-acbuk':'Atza|IwEBIChoOQUjuiDD1Ndqg7D90QC9oues6wvtBq9KyxkUO0PeHA_AQG5EQ2Rf1zM5eB4Wd4KmLt6nOjL73sAX2J4nyfiHltnKQ0XvZdYxbEHP9lsAZzMABc0WRV8pYLqsFmC7sTE3IHgTjdX6ExgHv0kKXWn_lh-OcoX23-ilS4czVB_KbZ4tghDVv1ujRihcsyn-7KFmoywM9w7TPRHjqfReHRMbxAiPWsqcXtXHEoFthSYiFEIyooD7fXwNIV1zJMbGBGXWKghw1vOOL3Wsc8jey7k0SydED-QUX0eKWxl3dAJyLa--yJi8-cjl91pVJQy0IZK5vAyI9QYa5cT8-gT4lbitAdJDoqdE2npc3EGSwqNOBfZuqJrnzGp2AfB7Tbjy9hrDZj2VYKhlRwLOt8OEF9oN_1qTWDXLqQiBGbWa3LvsDfM2mf_9DJU85YB9xjCAB5I', 'sess-at-acbuk':'"W0if1uWrGfFaig4NvDN8PESXjswV4em4R3Tx93mFktU="', 'sst-acbuk':'Sst1|PQHz2nPNiFW8ynMzAKfPn4JGCBHaW2z9k1K64ImaTLG1Aqmihve2uaMY-fRCKucfo-3zQUTjQjH8f3Ch8rBnWi04PwTHpbvRdQef5RGG1w834pBD8ng4IlB4YYH9uaucXWJbFZkN3ev7Ig67CFlLwY7kCjFOeZUqa4JZSQ_nR_jV_ZqrktpggrYmEZ4UeW_O5RiDbaQ5f7e2bTqEhc-cTbrDmIYjtI-SdcNOPJQ2oVmAb1i_Z9f3lJorsLkEtZNupBqfvTL_TyEQpBPCmFdABJ7dIQ', 'x-wl-uid':'1CR2os7XFO86l5kPQdlOMqaU/uBkZa0U2l746D2gCHyFzkV2WqtAky0cXRUWgRMvy51BL+xXD1aN4W779JABhJFO3Y+sw9D+bv02XYjAkoSpqtmCJMT0ltpLayiQtsUgnjeacTekELdc=', 'session-token':'"Zz6pHdoE7SGmJCPKNMHUn7bBQ5UPQoRmq/qHabFhbB5F0jvTkWJ3y8uZPf7dHfgZrsc83z/cge0xzvE0APIF1vni7lMBHKWgnLmkmpvmn8PTGYxfpM6gke1RwFjQp/Z8dG2fgaFXJP6K3ZDyja78Lc0OMhGzvFtECXfFnvvfVsyx81lCOmPaQMy0OxbVFUpWgFJhEIW3diF2ct3dtkKDuSWiqMax730uNchE28x+fYCsdNnM27qv83kmJE/yVM12MppRyJXemSLj7IgwDs3JZQ=="', 'csm-hit':'%7B%22tb%22%3A%22s-9RH9B8K1JPN4AF7DSH63%7C1519185777561%22%2C%22adb%22%3A%22adblk_no%22%7D', 'session-id-time':'2082758401l' }
            requesturl.meta['asin']=url
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
        item['asin']=response.meta["asin"]
        item['url']=response.url

        price1 = "".join(response.xpath('//*[@id="priceblock_saleprice_row"]/td[2]/span[@class="a-size-base a-color-price priceblock_vat_excl_label"]/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
        if not price1 : price1 = "".join(response.xpath('//*[@id="priceblock_ourprice_row"]/td[2]/span[@class="a-size-base a-color-price priceblock_vat_excl_label"]/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
        if not price1 : price1 = "".join(response.xpath('//*[@id="priceblock_ourprice_row"]/td[2]/span[@class="a-size-medium a-color-price priceblock_vat_excl_price"]/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
        if not price1 : price1 = "".join(response.xpath('//*[@id="soldByThirdParty"]/span[1]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip().lower()
        if price1!= "":
            item['price1']=price1
        #print "kkkkkkkkkkkkkkkkkkkkkkkkk", ",".join(response.xpath('//*[@id="priceblock_ourprice_row"]/td[2]/span//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip().lower()

        try: price = "".join(response.xpath('//*[@id="priceblock_ourprice"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        except: pass
        if not price: price = "".join(response.xpath('//*[@id="priceblock_ourprice_row"]/td[2]/span[@class="a-size-base a-color-price priceblock_vat_inc_price"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        if not price: price = "".join(response.xpath('//*[@id="priceblock_saleprice_row"]/td[2]/span[@class="a-size-base a-color-price priceblock_vat_inc_price"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        if not price: price = "".join(response.xpath('//*[@id="priceblock_businessprice"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        if not price: price = "".join(response.xpath('//*[@id="priceblock_dealprice"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        if not price: price = "".join(response.xpath('//*[@id="priceblock_ourprice_row"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        if not price: price = "".join(response.xpath('//*[@id="soldByThirdParty"]/span[2]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip().lower().replace('incl. vat','')
        if not price and "".join(response.xpath('//*[@id="buyNewSection"]/a/h5/div/div[1]/span//text()').extract()).find('New')>-1:
            price = ''.join(response.xpath('//*[@id="buyNewSection"]/a/h5/div/div[2]/div/span//text()').extract())
        if not price and "".join(response.xpath('//*[@id="buyNewSection"]/h5/div/div[1]/span//text()').extract()).find('New')>-1:
            if not price: price = ''.join(response.xpath('//*[@id="buyNewSection"]/h5/div/div[2]/div/span//text()').extract())
        if not price and "".join(response.xpath('//*[@id="mediaNoAccordion"]/div[1]/div[1]/span//text()').extract()).find('new')>-1:
            if not price: price = ''.join(response.xpath('//*[@id="mediaNoAccordion"]/div[1]/div[2]/span//text()').extract()).replace("\n",'').replace('\t','').strip()
        if not price and "".join(response.xpath('//*[@id="newOfferAccordionRow"]/div/div[1]/a/h5/div/div[1]/span//text()').extract()).find('new')>-1:
            if not price: price = ''.join(response.xpath('//*[@id="newOfferAccordionRow"]/div/div[1]/a/h5/div/div[2]/span[2]//text()').extract()).replace("\n",'').replace('\t','').strip()
        if price!= "":
            item['price']=price
            
        ship_price =  " ".join(response.xpath('//span[@id="price-shipping-message"]//text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
        if not ship_price :  ship_price =  " ".join(response.xpath('//*[@id="ourprice_shippingmessage"]//text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
        if not ship_price :  ship_price =  " ".join(response.xpath('//*[@id="businessprice_shippingmessage"]//text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
        if not ship_price :  ship_price = " ".join(response.xpath('//*[@id="ourprice_shippingmessage"]/span/b/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
        if not ship_price :  ship_price =  " ".join(response.xpath('//*[@id="price-shipping-message"]/span/b/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
        if ship_price!= "":
            item['ship_price']=ship_price

       
			
        seller_name = "".join(response.xpath('//*[@id="merchant-info"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        if not seller_name: seller_name = "".join(response.xpath('//*[@id="merchant-info"]/a//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        if seller_name!= "":
            item['seller_name']=seller_name
        yield item