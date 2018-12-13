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
    ship_price = scrapy.Field()
    #asin= scrapy.Field()
    seller_name = scrapy.Field()
    url = scrapy.Field()


class Amazon_upc_out(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    spider = scrapy.Field()
    dpid = scrapy.Field()
    date_timestamp = scrapy.Field()
    job_id = scrapy.Field()
    upc = scrapy.Field()
    title = scrapy.Field()
    product_title = scrapy.Field()
    #article_no = scrapy.Field()
    price = scrapy.Field()
    price1 = scrapy.Field()

    brand1 = scrapy.Field()
    brand2 = scrapy.Field()
    ean = scrapy.Field()
    mpn = scrapy.Field()
    model_number = scrapy.Field()
    colour = scrapy.Field()
    #description = scrapy.Field()
    url_page = scrapy.Field()
    breadcrumb  = scrapy.Field()
    attr_dict = scrapy.Field()
    quantity = scrapy.Field()
    response_url = scrapy.Field()
    seller_count =  scrapy.Field()
    ASIN = scrapy.Field()
    star_rating  = scrapy.Field()
    num_review = scrapy.Field()
    question_answered = scrapy.Field()
    price = scrapy.Field()
    ship_price = scrapy.Field()
    ship_price2 = scrapy.Field()
    seller_name = scrapy.Field()
    product_id = scrapy.Field()
    comp = scrapy.Field()
    UPC = scrapy.Field()
    body = scrapy.Field()

	
class amazonSpider(scrapy.Spider):
    imgcount = 1
    name = "amazon_french"
    allowed_domains = []

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]

    def parse(self, response):
        urls_done=[]
        urls=[
"https://www.amazon.fr/gp/product/B077XBNRYF/ref=s9u_ri_gw_i3?ie=UTF8&pd_rd_i=B077XBNRYF&pd_rd_r=006557ed-6889-11e8-ad28-014ae5dc2f42&pd_rd_w=NLE2O&pd_rd_wg=EH2Zp&pf_rd_m=A1X6FK5RDHNB96&pf_rd_s=&pf_rd_r=A1QE9588X28W8AH3XAEJ&pf_rd_t=36701&pf_rd_p=846f0bb3-dc02-4792-892e-456cc9f34a34&pf_rd_i=desktop",
]
        for url in urls:
            #requesturl = scrapy.FormRequest("https://www.amazon.de/dp/"+url,callback=self.parse1,headers={'Origin': 'https://www.amazon.com', 'Referer':'https://www.amazon.com', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.8', 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36, LuminadBot/1.0 (Apollo@Luminad.com)', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' ,'Cache-Control': 'max-age=0' }, dont_filter=True)
            #requesturl.cookies = {'aws-target-static-id':'1452239187641-159842', 'aws-business-metrics-last-visit':'1460349972900', '__utmv':'194891197.%22QDSe8l%404pyTIl%3FpKm5C24aEFXeBtLGw3BhDIGikRUeXlFGLshyp4Dtw4gLRG%3F9cU%22', 'aws-userInfo':'%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A111320495319%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22rahul%2520bhaskar%22%2C%22keybase%22%3A%22%22%2C%22issuer%22%3A%22https%3A%2F%2Fwww.amazon.com%2Fap%2Fsignin%22%7D', 's_pers':'%20s_vnum%3D1880352564702%2526vn%253D3%7C1880352564702%3B%20s_invisit%3Dtrue%7C1470309348410%3B%20s_nr%3D1470307548416-Repeat%7C1478083548416%3B', '__utma':'194891197.372951375.1452236845.1470290622.1470307550.17', 'aws-ubid-main':'182-7331780-4611541', '_mkto_trk':'id:112-TZM-766&token:_mch-aws.amazon.com-1484112318467-15791', 'aws-target-visitor-id':'1452239187643-451048.20_19', 'aws-target-data':'%7B%22support%22%3A%221%22%7D', 's_fid':'70673D38D5DFE123-1B689FC000FE2EFF', 'regStatus':'registered', 'ubid-main':'156-9680828-0484351', 'ca':'ALAAAAAAEAAAAAQGAAEIAUQ=', 's_vnum':'1926421318258%26vn%3D2', 's_nr':'1514281824850-New', 's_dslv':'1514281824851', 'session-id':'144-3935774-8062208', 'session-id-time':'2082787201l', 'x-amz-captcha-1':'1518768468239967', 'x-amz-captcha-2':'8brJzDGjVr0g6SMt7y51KQ==', 'a-ogbcbff':'1', 'x-main':'"fycgicqnXAG9h3NMiDoGTALK8XmKMT8Y7zmG2J0BNpcL1f@?TcYxcPMWWipZhvof"', 'at-main':'Atza|IwEBIJvW6xlsbiH1hRs9vJ2V_w16jlQhSQjg3ehsg3W76LxrQT-VH9tsIRiHoHcaMXn9pyYCgqS8ncyALBot9Lfa-oHQ9B5haHTZ234l1wd5cjS3lIpoebl3XqE8R13u2oHsAscFbcYZ1OArAxJHSYSkJxFwIlml-M4T3b8VcujEZdeoQEzvAipwwJHDzh7P4QQmNxSFyR7173IySmfados6vrpYc0OdSwLDpR42eLBACHhfFxTrY2EdG0O7vgr2UoDUnvd4o5SOTq54TBh4f2fNkV5OObxldSU1DMPF7E4PJnqBYC0n_gjy2Re3AId4a80qUdi0mQGItumFTtvkVmM_Ha5AXBWKaUL2SLS9RWjbeDoBRIQdaftjGACfgp_USVFfOBWwq_-7HQbM7J_EasxZZjfzA9JdgMGy37DAIGWG9abF-A2XLSehJ3qw9yD6Ce0it8E', 'sess-at-main':'"pXRzY7+0cEA6QAXiw7xtqkVPnlTizA/bSV5Ufn8LWUQ="', 'sst-main':'Sst1|PQFckmUHN5sOVumX4CdB104DCaCzuvSHXylkeh4qpfwQHzhV2em2zJkPumi2szBhhz9iPmGUE6CWI7DPT2W-mOFK_1ffiVN_x7DG-d0D6cM-mLVUboxgRg6LPiCypuwOCA2ORnqALrSSjuRTm8JbkhYlSW1hevw1Va5WGMEvvNpNAg4AtoISvv6jyI79Gsl3-drWQ6lRJ9PSdiUTY2SgCdjGnexsZA_-Rnd9BInaqRJzwMYPOlCHY9p-4QpuybnnbX17HPFzOAJhrhSCUiDFSEt9wYOKaMQw3urk_a2zCjOjBwo', 'lc-main':'en_US', 'x-wl-uid':'1qO28TBan5h3oE1QxU2WGyoczvrC0FTgSurawI1g3sgmWQYwqLKN1zESoN3ANbMEfUc3uWSsKr9FyRbNyggYPQ+zMMdgAVJ2WL/Tf3lZHoYsm3zTt0ornhvjL6gVv6qw2U2rxb397ybM7PcAb7MFQVQ==', 'session-token':'"8oBu2yRmYSRcMko83QPjy+BgTzk9Hoeu/IhZqLO6f9E6sk3RoJ5TYUU+uS72FeKUc/090SieEJSZ4zIMwli8u+wD1adpp/yhZA6tz6CgQs96B6clWL1YtQZuyYMlXLRIxynxTrfIXGxY01cAkMTzFq+Dz2tG/5U194x6UTPT684kVRuSYdXgGsTzDoN/af1mq+m4FjMcoS4q/SJJRMHzDiQUmcKll91lr4Eemcp7bfnd7huqHdUFMgC/i0Jl7w5TA9Vgmcih4vGkWck7b5lAaA=="', 'csm-hit':'GJ6HJMM3CFA43W994KHK+b-ZQ6HYQ744MSFND7T1VVB|1519010944543'}
            #requesturl = scrapy.FormRequest( url,callback=self.parse1, headers={'Origin': 'https://www.amazon.de', 'Referer':'https://www.amazon.de', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.8', 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36, LuminadBot/1.0 (Apollo@Luminad.com)', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' ,'Cache-Control': 'max-age=0' }, dont_filter=True)
            requesturl = scrapy.FormRequest( url,callback=self.parse1, headers={'authority': 'www.amazon.fr' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'referer': 'https://www.amazon.fr/ref=nav_logo' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9'})
            #requesturl.cookies ={'s_pers':'%20s_fid%3D300B8810F7CDBDE1-10092DE00A8359D7%7C1558680220920%3B%20s_dl%3D1%7C1495610020921%3B%20gpv_page%3DDE%253AAZ%253ASOA-Landing%7C1495610020924%3B%20s_ev15%3D%255B%255B%2527AZDEGNOSellC%2527%252C%25271495608209183%2527%255D%252C%255B%2527AZDEGNOSellC%2527%252C%25271495608216403%2527%255D%252C%255B%2527AZDEGNOSellC%2527%252C%25271495608220916%2527%255D%252C%255B%2527AZDEGNOSellC%2527%252C%25271495608220925%2527%255D%255D%7C1653374620925%3B%20s_eVar26%3DAmazon%2520Services%2520DE%7C1498200220927%3B', 'amznacsleftnav-656eac4a-695b-3a6a-946f-db61e4deb392':'1', 'amznacsleftnav-fdfd699f-c863-3b78-85b2-8a649c6b58f6':'1', 'x-amz-captcha-1':'1508482986892769', 'x-amz-captcha-2':'hw3RhTh0tvhX81cdMFkFgQ==', 'lc-acbde':'de_DE', 'session-id':'261-5677163-4561642', 'ubid-acbde':'259-8821950-7904223', 'a-ogbcbff':'1', 'x-acbde':'"V0z3CSC5jraR2B7OY6OiPR3wrDO7GbRjA9fTg2AJTorXXbAPToPEDvMAo8KTh@7M"', 'at-acbde':'Atza|IwEBIHwqc3CD45BqlJs_5aa-V8dGYqRemzUHaOJhdARXf-o6rlAp0DANlQO8ZPGB23Uek573IjBb2qkX4mlZWKna1Xn3pOzTpiUd0SQO7gh-uTZnxF5r2p22mMsR4_clEZvBBlZBMJYXD6HPxW7_sEYtklqCkY-Br197rDnz9KPza3y5u7XzgezJIBdXCaeq4vAqo9Wrl0uG0RGKSr41-4rKK9hpnGK1nN4UbO_qWxnLSwzA6LwgXczqe0C5EyH1HIp12IlKFB7OgxIEsH0QZAiT0eh0D7sFwlVG6eHfqPNWfix03SZ7apAC7C7jQ-vw1lmICAeJciD9QmumuCNEDDCT-GGWCkrAh-gxMRhKpm7Q5_gOtJijbqoLi3VfPO9QrCA7hYW8Atc-kFRIW3Y6vtRc8OZzZipCneewy-Rj_xYUMFVWMCmHs_ljfe2W6vxWgiRfmyw', 'sess-at-acbde':'"NbwPRqfG4oPuznYLUmFM5Y5JSvyizaA9ZJz6vTkNQL4="', 'sst-acbde':'Sst1|PQEs5smXCO43G8WIotdsANHyCEBZ9TkcZ_OdLYTgnk2mCfAy4Z5W77Y7zX74BQuxS7UKtfnUM6KkKhmcu01A2Fq7xshyjesDvnQDYp9QYcrFDvlceaVvpWqQfpEt2Q9XIM0VQFdd2EMpXc4C9QlehgHT0URfOlUmC47BkfeJr5dpb4Pv_dbnFASQli0k7Cln9sN_Vf4Wqz4km-6UTpsNlVJxJE48_RK6Zsk7bklH_cpJE8tfltiPzdhyhY2oDh7SieUx6CNKphxtIezjzr-0SbD8cg', 'x-wl-uid':'11PAl+O2T6FeY67SmgtWeMBtyZ538YMsy2Zcpov67B4kL2DVIv3Nx7rEprTLBkI4W3ZZ954YAADFuG1oAMSt9uIgNhk3yQfBCY6pDMJUcXUzK6rFTPF4tPnrWr3utKPzHqJATwvQOHKE=', 'session-token':'"tzfdQwuhV4SLJ9/PfV3QSfg2b3LxOcRlqovsFb3AsrqZSnkxHCjhgMsO3d7NbIS7rOee9CPoh7Lxo8LF7EdVopNDFYLMzzOtDGVhnY4czMEVNS5VHAxjtdaDvRNDJC0OloD0EvRMDfHeXG70D93/wWVNfqU0c6nKEv0yTLU7pFpIbTicUYQQFeDZYf9tPQEepQxbZ1pBOU+0FjTwWUj3SnNdDf/SVmmk+feDLRuqn+WcP6w6CPQ1G03W/TACUuIHBz9mSMRFPU0il4m+s0KyzA=="', 'csm-hit':'s-F8Q4HD9WHE8M6GMQKQT4|1519186540551', 'session-id-time':'2082754801l' }
            requesturl.cookies ={'session-id':'259-1253251-0267152', 'ubid-acbfr':'259-4521620-4228701', 'x-wl-uid':'1gDsZFy7+3PsNBhiyAnEYd7Bntn9YTxQqtFiVGMUjpnNgWIVCFBwx/j8AT7oXb9ZjVLhW6gKrw/Q=', 'session-token':'p0zvBy0viybpkwY1qo3raLD9z7QYBlPWISuE2XyYtcYhq+5mQibNwWyeiRrMQjxzAqNr+BzW6m0WK9u2sEgwfpgygNSzn2j/B5ddHIGExxn8DQt4P9UDtKbIMFM4eGqtTm2a3aTl6FboxfYiTVhqnGoUO8gYfIwDDWXIeLW+tJy3JwtPfHgYp7f+L73I36uTRotB+GlfWuynyvwB/diYRnqpQejO4dtfRV7dA9aw/0773BbEVJIBZK2W0EQZvl4G', 'lc-acbfr':'fr_FR', 's_cc':'true', 's_nr':'1528177386696-New', 's_vnum':'1960177386696%26vn%3D1', 's_dslv':'1528177386697', 's_sq':'%5B%5BB%5D%5D', 'session-id-time':'2082754801l', 'csm-hit':'tb:KAWM42GX88KY1QTMH4QV+s-HPSGQ8EE7HC885F2A0NG|1528182150863&adb:adblk_no'}
            #requesturl.meta['asin']=url
            time.sleep(.1)
            yield requesturl
		

		
    def parse1(self,response):
 

        try:
            #attr=response.meta['attr']
            attr = {}
            attr['job_id']='12345'
            try:title=response.xpath('//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li/span/a/text()').extract()[-1].replace('\n','').strip()
            except: title=''
            bredcrumb_temp = []
            try:
                for part in response.xpath('//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li/span/a/text()').extract():
                    bredcrumb_temp.append(part.replace('\n','').strip())
            except: pass
            #print title
            try: brand1 = response.xpath('//*[@id="brand"]/text()').extract()[0].replace("  ",'').replace("\n",'').replace('\t','').strip()
            except: brand1=""
            if not brand1:
                try:
                    brand1=response.xpath('//*[@id="bylineInfo"]/text()').extract()[0].replace("  ",'').replace("\n",'').replace('\t','').strip()
                except: 
                    try:
                        brand1=response.xpath('//*[@id="brand"]/@href').extract()[0].replace("  ",'').replace("\n",'').replace('\t','').strip().split('/')[1]
                    except: brand1=""

            ship_price2 = "".join(response.xpath('//*[@id="soldByThirdParty"]/span[2]/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            if ship_price2.find("+")==-1:
                ship_price2 = "".join(response.xpath('//*[@id="soldByThirdParty"]/span[3]/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            price = ''
            price1 = ''
            if not price: price = "".join(response.xpath('//*[@id="priceblock_businessprice"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not price: price = "".join(response.xpath('//*[@id="priceblock_saleprice"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()

            if not price: price = "".join(response.xpath('//*[@id="priceblock_ourprice_row"]/td[2]/span[@class="a-size-base a-color-price priceblock_vat_inc_price"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not price: price = "".join(response.xpath('//*[@id="priceblock_saleprice_row"]/td[2]/span[@class="a-size-base a-color-price priceblock_vat_inc_price"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not price: price = "".join(response.xpath('//*[@id="priceblock_dealprice"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not price: price = "".join(response.xpath('//*[@id="priceblock_dealprice_row"]/td[2]/span[@class="a-size-base a-color-price priceblock_vat_inc_price"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not price and "".join(response.xpath('//*[@id="buyNewSection"]/a/h5/div/div[1]/span//text()').extract()).find('New')>-1:
                price = ''.join(response.xpath('//*[@id="buyNewSection"]/a/h5/div/div[2]/div/span//text()').extract())
            if not price and "".join(response.xpath('//*[@id="buyNewSection"]/h5/div/div[1]/span//text()').extract()).find('New')>-1:
                if not price: price = ''.join(response.xpath('//*[@id="buyNewSection"]/h5/div/div[2]/div/span//text()').extract())
            if not price and "".join(response.xpath('//*[@id="mediaNoAccordion"]/div[1]/div[1]/span//text()').extract()).find('new')>-1:
                if not price: price = ''.join(response.xpath('//*[@id="mediaNoAccordion"]/div[1]/div[2]/span//text()').extract()).replace("\n",'').replace('\t','').strip()
            if not price and "".join(response.xpath('//*[@id="newOfferAccordionRow"]/div/div[1]/a/h5/div/div[1]/span//text()').extract()).find('new')>-1:
                if not price: price = ''.join(response.xpath('//*[@id="newOfferAccordionRow"]/div/div[1]/a/h5/div/div[2]/span[2]//text()').extract()).replace("\n",'').replace('\t','').strip()





            """
            try: 
                if not price: price = "".join(response.xpath('//*[@id="priceblock_ourprice"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            except: raise
            if not price: price = "".join(response.xpath('//*[@id="priceblock_ourprice_row"]/td[2]/span[@class="a-size-base a-color-price priceblock_vat_inc_price"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not price: price = "".join(response.xpath('//*[@id="priceblock_saleprice_row"]/td[2]/span[@class="a-size-base a-color-price priceblock_vat_inc_price"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not price: price = "".join(response.xpath('//*[@id="priceblock_dealprice_row"]/td[2]/span[@class="a-size-base a-color-price priceblock_vat_inc_price"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not price: price = "".join(response.xpath('//*[@id="priceblock_dealprice"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            """
            try: 
                price_base = "#".join(response.xpath('//*[@id="priceblock_ourprice_row"]/td[2]/span//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip().lower()
                price_index =  price_base.split('#').index('inkl. ust')
                print price_index, "kjjhhhhhhhhhhhhhhhhhhhhhh",price_base
                if not price : price = "".join(price_base.split('#')[price_index -2: price_index +1])
                price1 = "".join(price_base.split('#')[0: price_index -2])
                if price1 and not price: price=price_base.split('#')[price_index -3:]

            except: 
                pass
                            
            try:
                if not price:
                    if not price: price = "".join(response.xpath('//*[@id="soldByThirdParty"]/span[2]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip().lower().replace('incl. vat','')
                    price1 = "".join(response.xpath('//*[@id="soldByThirdParty"]/span[1]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip().lower()
            except: price=""
            #ship_price = "".join(response.xpath('//*[@id="ourprice_shippingmessage"]/span/b/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            #if not ship_price :  ship_price =  "".join(response.xpath('//*[@id="price-shipping-message"]/span/b/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            #if not ship_price :  ship_price =  "".join(response.xpath('//span[@id="price-shipping-message"]//text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            #if not ship_price :  ship_price =  "".join(response.xpath('//*[@id="ourprice_shippingmessage"]//text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()

            ship_price =  "".join(response.xpath('//span[@id="price-shipping-message"]//text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            if not ship_price :  ship_price =  "".join(response.xpath('//*[@id="ourprice_shippingmessage"]//text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            if not ship_price :  ship_price =  "".join(response.xpath('//*[@id="businessprice_shippingmessage"]//text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            if not ship_price :  ship_price = "".join(response.xpath('//*[@id="ourprice_shippingmessage"]/span/b/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            if not ship_price :  ship_price =  "".join(response.xpath('//*[@id="price-shipping-message"]/span/b/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
          
			
            #seller_name = " ".join(response.xpath('//*[@id="merchant-info"]/a//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            #if not seller_name: seller_name = " ".join(response.xpath('//*[@id="merchant-info"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()

            seller_name = " ".join(response.xpath('//*[@id="merchant-info"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not seller_name: seller_name = " ".join(response.xpath('//*[@id="merchant-info"]/a//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
			
            #print brand,image
            title=';'.join(response.xpath('//*[@id="productTitle"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            result=[]
            final_dict=[]
            brand_match_type = ''
            product_attr_key1 = '$#'.join(response.xpath('//*[@id="product-specification-table"]/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value1 = response.xpath('//*[@id="product-specification-table"]/tr/td')
            product_attr_key2 = '$#'.join(response.xpath('//*[@id="product-specification-table"]/tbody/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value2 = response.xpath('//*[@id="product-specification-table"]/tbody/tr/td')
            product_attr_key3 = '$#'.join(response.xpath('//*[@id="productDetails_techSpec_section_1"]/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value3 = response.xpath('//*[@id="productDetails_techSpec_section_1"]/tr/td')
            product_attr_key4 =  '$#'.join(response.xpath('//*[@id="productDetails_techSpec_section_2"]/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value4 = response.xpath('//*[@id="productDetails_techSpec_section_2"]/tr/td')
            product_attr_key5 = '$#'.join(response.xpath('//*[@id="productDetails_detailBullets_sections1"]/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value5 = response.xpath('//*[@id="productDetails_detailBullets_sections1"]/tr/td')
            product_attr_key6 = '$#'.join(response.xpath('//*[@id="productDetails_detailBullets_sections2"]/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value6 = response.xpath('//*[@id="productDetails_detailBullets_sections2"]/tr/td')
            product_attr_key7 = '$#'.join(response.xpath('//*[@id="detail-bullets"]/table/tr/td/div/ul/li/b/text()').extract()).replace("\n",'').replace('\t','').strip()
            product_attr_value7 = response.xpath('//*[@id="detail-bullets"]/table/tr/td/div/ul/li')
            product_attr_key8= '$#'.join(response.xpath('//*[@id="feature-bullets"]/ul/li/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value8 = response.xpath('//*[@id="feature-bullets"]/ul/li/span')
            product_attr_key31 = '$#'.join(response.xpath('//*[@id="productDetails_techSpec_section_1"]/tbody/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value31 = response.xpath('//*[@id="productDetails_techSpec_section_1"]/tbody/tr/td')
            product_attr_key41 =  '$#'.join(response.xpath('//*[@id="productDetails_techSpec_section_2"]/tbody/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value41 = response.xpath('//*[@id="productDetails_techSpec_section_2"]/tbody/tr/td')
            product_attr_key51 = '$#'.join(response.xpath('//*[@id="productDetails_detailBullets_sections1"]/tbody/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value51 = response.xpath('//*[@id="productDetails_detailBullets_sections1"]/tbody/tr/td')
            product_attr_key61 = '$#'.join(response.xpath('//*[@id="productDetails_detailBullets_sections2"]/tbody/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value61 = response.xpath('//*[@id="productDetails_detailBullets_sections2"]/tbody/tr/td')
            product_attr_key71 = '$#'.join(response.xpath('//*[@id="detail-bullets"]/table/tbody/tr/td/div/ul/li/b/text()').extract()).replace("\n",'').replace('\t','').strip()
            product_attr_value71 = response.xpath('//*[@id="detail-bullets"]/table/tbody/tr/td/div/ul/li')
            product_attr_value9 =response.xpath('//*[@id="prodDetails"]/span')
            if not product_attr_key7: product_attr_key7 = '$#'.join(response.xpath('//*[@id="detailBullets_feature_div"]/ul/li/span/span[1]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not product_attr_value7: product_attr_value7 = response.xpath('//*[@id="detailBullets_feature_div"]/ul/li/span/span[2]')
            result_dict = {}
            key= None
            if product_attr_key3 and (product_attr_value3  or product_attr_value31)  :
                try:
                    value = product_attr_value3
                    if not value: value = product_attr_value31
                except: value = product_attr_value31
                key = product_attr_key3.split("$#")

                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result =zip(key,value[0:len(key)-1])

            #print result       
            for i,j in result:
                result_dict[i.replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()           
            match_type = ''
            brand_match_type = ''
            item_no =''
            match_dim = ''
            mpn_match =''
            if result_dict:final_dict.append(result_dict)
            if result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip() :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()

            brand2 = result_dict.get('Brand','').strip()
            
            result_dict = {}
            key= None
            if product_attr_key1 and product_attr_value1   :
                try:
                    value = product_attr_value1
                    key = product_attr_key1.split("$#")

                    if  key and len(key) == len(value):
                        result = zip(key,value)
                    else:
			            result = zip(key,value[0:len(key)-1])
                except: pass

            #print result       
            for i,j in result:
                result_dict[i.replace(":",'').strip()] =  "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()

            if result_dict:final_dict.append(result_dict)
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip() 

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 
            result_dict = {}
            key= None
            if product_attr_key4  and product_attr_value4    :
                try:
                    value = product_attr_value4
                    key = product_attr_key4.split("$#")

                    if  key and len(key) == len(value):
                        result =zip(key,value)
                    else:
                        result = zip(key,value[0:len(key)-1])
                except: pass
            
            #print result       
            for i,j in result:
                result_dict[i.replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 
            
            result_dict = {}
            key= None
            value = response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div[2]/ul/li')
            if not value:value = response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div/ul/li')
            if product_attr_key5  and (product_attr_value5  or product_attr_value51 )  :
                try:
                    value = product_attr_value5
                    if not value: value = product_attr_value51                
                except: value = product_attr_value51
                key = product_attr_key5.split("$#")
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[:len(key)-1])

            for i,j in result:
                result_dict[i.replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()

            if result_dict:final_dict.append(result_dict)
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 

            result_dict = {}
            key= None
            if product_attr_key7  and (product_attr_value7  or product_attr_value71 )  :
                try:
                    value = product_attr_value7
                    if not value: value = product_attr_value71
                except: value = product_attr_value71
                key = product_attr_key7.split("$#")

                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

            for i,j in result:
                result_dict[i.replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()

            if result_dict:final_dict.append(result_dict)
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 


            #print brand,item_no



            product_attr_value7 = '$#'.join([i.strip() for i in response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div[2]/ul/li/text()').extract()]).replace("\n",'').replace('\t','').strip()
            product_attr_key7 = '$#'.join(response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div[2]/ul/li/b/text()').extract()).replace("\n",'').replace('\t','').strip()
            result_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                 product_attr_value7 = '$#'.join([i.strip() for i in response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div/ul/li/text()').extract()]).replace("\n",'').replace('\t','').strip()
                 product_attr_key7 = '$#'.join([i.strip() for i in response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div/ul/li/b/text()').extract()]).replace("\n",'').replace('\t','').strip()

            
            if product_attr_key7  and product_attr_value7    :
                try:
                    value = product_attr_value7
                except: value = ""
                key = product_attr_key7.split("$#")
                value = response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div[2]/ul/li')
                if not value:value = response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div/ul/li')

                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for key, val in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()

                    result_dict[key.strip()] = "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                #print result_dict
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 

            result_dict = {}
            key= None
            if result_dict:final_dict.append(result_dict)

            product_attr_value7 = response.xpath('//*[@id="technicalSpecifications_feature_div"]/div[2]/div/div[1]/div/table/tbody/tr/td')
            product_attr_key7 = '$#'.join(response.xpath('//*[@id="technicalSpecifications_feature_div"]/div[2]/div/div[1]/div/table/tbody/tr/th/text()').extract()).replace("\n",'').replace('\t','').strip()
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 = response.xpath('//*[@id="technicalSpecifications_feature_div"]/div[2]/div/div[1]/div/table/tr/td')
                product_attr_key7 = '$#'.join(response.xpath('//*[@id="technicalSpecifications_feature_div"]/div[2]/div/div[1]/div/table/tr/th/text()').extract()).replace("\n",'').replace('\t','').strip()

            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7.split("$#")

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[i.replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()

            if result_dict:final_dict.append(result_dict)
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 



            result_dict = {}
            key= None
		  

            product_attr_value7 = response.xpath('//*[@id="productDetailsTable"]/tbody/tr/td/div/ul/li')
            product_attr_key7 = response.xpath('//*[@id="productDetailsTable"]/tbody/tr/td/div/ul/li/b')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 = response.xpath('//*[@id="productDetailsTable"]/tr/td/div/ul/li')
                product_attr_key7 = response.xpath('//*[@id="productDetailsTable"]/tr/td/div/ul/li/b')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()

            if result_dict:final_dict.append(result_dict)
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 

            product_attr_value7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr/td[2]')
            product_attr_key7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr/td[1]')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tr/td[2]')
                product_attr_key7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tr/td[1]')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            #print result_dict, "1"
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 


            product_attr_value7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr/td[2]')
            product_attr_key7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr/td[1]')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tr/td[2]')
                product_attr_key7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tr/td[1]')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            #print result_dict, "2"
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 

   
            product_attr_value7 = response.xpath('//*[@id="technicalSpecifications_section_1"]/tbody/tr/td')
            product_attr_key7 = response.xpath('//*[@id="technicalSpecifications_section_1"]/tbody/tr/th')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 = response.xpath('//*[@id="technicalSpecifications_section_1"]/tr/td')
                product_attr_key7 = response.xpath('//*[@id="technicalSpecifications_section_1"]/tr/th')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            #print result_dict, "3"
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 



            product_attr_value7 = response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div[2]/div/div/table/tbody/tr/td[2]')
            product_attr_key7 = response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div[2]/div/div/table/tbody/tr/td[1]')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 =  response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div[2]/div/div/table/tr/td[2]')
                product_attr_key7 =  response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div[2]/div/div/table/tr/td[1]')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            #print result_dict, "3"
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 





            product_attr_value7 = response.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li')
            product_attr_key7 = response.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li/b')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 =  response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div/ul/li')
                product_attr_key7 =  response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div/ul/li/b')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            #print result_dict, "3"
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 




            product_attr_value7 = response.xpath('//*[@id="prodDetails"]/div/div[2]/div[1]/div[2]/div/div/table/tbody/tr/td[2]')
            product_attr_key7 = response.xpath('//*[@id="prodDetails"]/div/div[2]/div[1]/div[2]/div/div/table/tbody/tr/td[1]')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 =  response.xpath('//*[@id="prodDetails"]/div/div[2]/div[1]/div[2]/div/div/table/tr/td[2]')
                product_attr_key7 =  response.xpath('//*[@id="prodDetails"]/div/div[2]/div[1]/div[2]/div/div/table/tr/td[1]')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            #print result_dict, "3"
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 


        except:
            raise
		  
        ean = ""
        variation_ASIN = ""
        variation_ASIN = ",".join(response.xpath('//*[@id="variation_color_name"]/ul/li/@data-defaultasin').extract())
      
        variation_dp_url = response.xpath('//*[@id="variation_color_name"]/ul/li/@data-dp-url').extract()
        if len(variation_dp_url )>0:
            variation_dp_url_list = [ i[3:].split("/ref")[0] for i in variation_dp_url]
            variation_ASIN = variation_ASIN + ","+ ",".join(variation_dp_url_list)
        variation_ASIN = variation_ASIN +","+ ",".join(response.xpath('//*[@id="variation_platform_for_display"]/ul/li/@data-defaultasin').extract())

        variation_ASIN = variation_ASIN +","+ ",".join(response.xpath('//*[@id="variation_service_plan_term"]/ul/li/@data-defaultasin').extract())
        if variation_ASIN: variation_ASIN = variation_ASIN +","
        variation_ASIN  = variation_ASIN + ",".join(response.xpath('//*[@id="variation_size_name"]/ul/li/@data-defaultasin').extract())
        variation_size = response.xpath('//*[@id="native_dropdown_selected_size_name"]/option/@value').extract()
        if len(variation_size )>0:
            variation_size_list = [ i.split(",")[1] for i in variation_size[1:]]
            variation_ASIN = variation_ASIN + "," + ",".join(variation_size_list)
        variation_size = response.xpath('//*[@id="native_dropdown_selected_initial_character"]/option/@value').extract()
        #print variation_size
        if len(variation_size )>0:
            variation_size_list = [ i.split(",")[1] for i in variation_size[1:]]
            variation_ASIN = variation_ASIN + "," + ",".join(variation_size_list)
        attr_dict = dict([ (k,v)  for d in final_dict for k,v in d.items() ])
        if not item_no and( attr_dict.get('Modellnummer','').strip() or attr_dict.get('Teilenummer','').strip() ) :
            item_no = attr_dict.get('Modellnummer','').strip() or attr_dict.get('Teilenummer','').strip()
        if not ean and( attr_dict.get('EAN/UPC','').strip() or attr_dict.get('EAN / Artikelnummer','').strip() ) :
            ean =  attr_dict.get('EAN/UPC','').strip() or attr_dict.get('EAN / Artikelnummer','').strip() 
        if not brand2 and( attr_dict.get('Manufacturer','').strip() or attr_dict.get('Brand Name','').strip() ) :
            brand2 =  attr_dict.get('Manufacturer','').strip() or attr_dict.get('Brand Name','').strip() 
            #if not brand2:  brand2 =result_dict.get('Manufacturer','').strip()
		
                                                        
        if title:
            count = "".join(response.xpath('//*[@id="olp_feature_div"]/div/span[1]/a/text()').extract()).strip()
            if not count: count = ''.join(response.xpath('//*[@id="outOfStock"]/div/span//text()').extract()).replace('/t','').replace('/n','').strip()
            if not count: count = ''.join(response.xpath('//*[@id="availability"]/span/text()').extract()).replace('/t','').replace('/n','').strip()
            star_rating  = "".join(response.xpath('//*[@id="acrPopover"]/span[1]/a/i[1]/span/text()').extract()).replace('/n','').strip()
            num_review = "".join(response.xpath('//*[@id="acrCustomerReviewText"]/text()').extract()).replace('/n','').strip()
            question_answered = "".join(response.xpath('//*[@id="askATFLink"]/span/text()').extract()).replace('/n','').strip()
            item = Amazon_upc_out()
            item['star_rating'] = star_rating
            item['num_review'] = num_review
            item['question_answered'] = question_answered
            item['product_title'] = title
            item['mpn'] = "'" +item_no+"'"
            item['attr_dict'] = json.dumps(attr_dict)
            item['brand1'] = brand1
            item['brand2'] = brand2
            item['response_url']=response.url

            item['date_timestamp']= int(time.time())
            item['job_id'] = attr['job_id']
            item['product_id'] = '111111'
            item['UPC']= '112233'
            item['breadcrumb']="/".join(bredcrumb_temp)
            item['seller_count'] = count
            item['ship_price'] = ship_price
            item['ship_price2'] = ship_price2
            item['price'] = price
            item['price1'] = price1
            item['seller_name'] = seller_name
            item['spider'] = self.name


            item['ean'] = ean
            #print item
            yield item
        else:
            try:
                try:result = response.xpath('//meta[2]/@content').extract()[0].find('404.html')
                except: result =-1
                if result>-1 or response.status== 404:
                    item = Amazon_upc_out()
                    item['product_id'] = response.meta['id']

                    item['response_url']=response.url

                    item['date_timestamp']= int(time.time())
                    item['spider'] = self.name
                    item['job_id'] = attr['job_id']
                    item['seller_count'] = 'Not Found'
                            
                    yield item
                result = response.xpath('//title/text()').extract()[0].find('Page Not Found')
                if result>-1:
                    item = Amazon_upc_out()
                    item['product_id'] = response.meta['id']

                    item['response_url']=response.url

                    item['date_timestamp']= int(time.time())
                    item['spider'] = self.name
                    item['job_id'] = attr['job_id']
                    item['seller_count'] = 'Not Found'
                           
                    yield item
            except: raise 


		
		
    def parse11(self, response):
        item=AmazonItems()
        try:
            try:title=response.xpath('//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li/span/a/text()').extract()[-1].replace('\n','').strip()
            except: title=''
            bredcrumb_temp = []
            try:
                for part in response.xpath('//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li/span/a/text()').extract():
                    bredcrumb_temp.append(part.replace('\n','').strip())
            except: pass
            #print title
            try: brand1 = response.xpath('//*[@id="brand"]/text()').extract()[0].replace("  ",'').replace("\n",'').replace('\t','').strip()
            except: brand1=""
            if not brand1:
                try:
                    brand1=response.xpath('//*[@id="bylineInfo"]/text()').extract()[0].replace("  ",'').replace("\n",'').replace('\t','').strip()
                except: 
                    try:
                        brand1=response.xpath('//*[@id="brand"]/@href').extract()[0].replace("  ",'').replace("\n",'').replace('\t','').strip().split('/')[1]
                    except: brand1=""

            ship_price2 = "".join(response.xpath('//*[@id="soldByThirdParty"]/span[2]/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            if ship_price2.find("+")==-1:
                ship_price2 = "".join(response.xpath('//*[@id="soldByThirdParty"]/span[3]/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            price = ''
            price1 = ''
            if not price: price = "".join(response.xpath('//*[@id="priceblock_saleprice"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not price: price = "".join(response.xpath('//*[@id="priceblock_businessprice"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()

            if not price: price = "".join(response.xpath('//*[@id="priceblock_ourprice_row"]/td[2]/span[@class="a-size-base a-color-price priceblock_vat_inc_price"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not price: price = "".join(response.xpath('//*[@id="priceblock_saleprice_row"]/td[2]/span[@class="a-size-base a-color-price priceblock_vat_inc_price"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not price: price = "".join(response.xpath('//*[@id="priceblock_dealprice"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not price: price = "".join(response.xpath('//*[@id="priceblock_dealprice_row"]/td[2]/span[@class="a-size-base a-color-price priceblock_vat_inc_price"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not price and "".join(response.xpath('//*[@id="buyNewSection"]/a/h5/div/div[1]/span//text()').extract()).find('New')>-1:
                price = ''.join(response.xpath('//*[@id="buyNewSection"]/a/h5/div/div[2]/div/span//text()').extract())
            if not price and "".join(response.xpath('//*[@id="buyNewSection"]/h5/div/div[1]/span//text()').extract()).find('New')>-1:
                if not price: price = ''.join(response.xpath('//*[@id="buyNewSection"]/h5/div/div[2]/div/span//text()').extract())
            if not price and "".join(response.xpath('//*[@id="mediaNoAccordion"]/div[1]/div[1]/span//text()').extract()).find('new')>-1:
                if not price: price = ''.join(response.xpath('//*[@id="mediaNoAccordion"]/div[1]/div[2]/span//text()').extract()).replace("\n",'').replace('\t','').strip()
            if not price and "".join(response.xpath('//*[@id="newOfferAccordionRow"]/div/div[1]/a/h5/div/div[1]/span//text()').extract()).find('new')>-1:
                if not price: price = ''.join(response.xpath('//*[@id="newOfferAccordionRow"]/div/div[1]/a/h5/div/div[2]/span[2]//text()').extract()).replace("\n",'').replace('\t','').strip()





            """
            try: 
                if not price: price = "".join(response.xpath('//*[@id="priceblock_ourprice"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            except: raise
            if not price: price = "".join(response.xpath('//*[@id="priceblock_ourprice_row"]/td[2]/span[@class="a-size-base a-color-price priceblock_vat_inc_price"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not price: price = "".join(response.xpath('//*[@id="priceblock_saleprice_row"]/td[2]/span[@class="a-size-base a-color-price priceblock_vat_inc_price"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not price: price = "".join(response.xpath('//*[@id="priceblock_dealprice_row"]/td[2]/span[@class="a-size-base a-color-price priceblock_vat_inc_price"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not price: price = "".join(response.xpath('//*[@id="priceblock_dealprice"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            """
            try: 
                price_base = "#".join(response.xpath('//*[@id="priceblock_ourprice_row"]/td[2]/span//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip().lower()
                price_index =  price_base.split('#').index('inkl. ust')
                print price_index, "kjjhhhhhhhhhhhhhhhhhhhhhh",price_base
                if not price : price = "".join(price_base.split('#')[price_index -2: price_index +1])
                price1 = "".join(price_base.split('#')[0: price_index -2])
                if price1 and not price: price=price_base.split('#')[price_index -3:]

            except: 
                pass
                            
            try:
                if not price:
                    if not price: price = "".join(response.xpath('//*[@id="soldByThirdParty"]/span[2]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip().lower().replace('incl. vat','')
                    price1 = "".join(response.xpath('//*[@id="soldByThirdParty"]/span[1]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip().lower()
            except: price=""
            #ship_price = "".join(response.xpath('//*[@id="ourprice_shippingmessage"]/span/b/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            #if not ship_price :  ship_price =  "".join(response.xpath('//*[@id="price-shipping-message"]/span/b/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            #if not ship_price :  ship_price =  "".join(response.xpath('//span[@id="price-shipping-message"]//text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            #if not ship_price :  ship_price =  "".join(response.xpath('//*[@id="ourprice_shippingmessage"]//text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()

            ship_price =  "".join(response.xpath('//span[@id="price-shipping-message"]//text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            if not ship_price :  ship_price =  "".join(response.xpath('//*[@id="ourprice_shippingmessage"]//text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            if not ship_price :  ship_price =  "".join(response.xpath('//*[@id="businessprice_shippingmessage"]//text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            if not ship_price :  ship_price = "".join(response.xpath('//*[@id="ourprice_shippingmessage"]/span/b/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            if not ship_price :  ship_price =  "".join(response.xpath('//*[@id="price-shipping-message"]/span/b/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
          
			
            #seller_name = " ".join(response.xpath('//*[@id="merchant-info"]/a//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            #if not seller_name: seller_name = " ".join(response.xpath('//*[@id="merchant-info"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()

            seller_name = " ".join(response.xpath('//*[@id="merchant-info"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not seller_name: seller_name = " ".join(response.xpath('//*[@id="merchant-info"]/a//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
			
            #print brand,image
            title=';'.join(response.xpath('//*[@id="productTitle"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            result=[]
            final_dict=[]
            brand_match_type = ''
            product_attr_key1 = '$#'.join(response.xpath('//*[@id="product-specification-table"]/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value1 = response.xpath('//*[@id="product-specification-table"]/tr/td')
            product_attr_key2 = '$#'.join(response.xpath('//*[@id="product-specification-table"]/tbody/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value2 = response.xpath('//*[@id="product-specification-table"]/tbody/tr/td')
            product_attr_key3 = '$#'.join(response.xpath('//*[@id="productDetails_techSpec_section_1"]/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value3 = response.xpath('//*[@id="productDetails_techSpec_section_1"]/tr/td')
            product_attr_key4 =  '$#'.join(response.xpath('//*[@id="productDetails_techSpec_section_2"]/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value4 = response.xpath('//*[@id="productDetails_techSpec_section_2"]/tr/td')
            product_attr_key5 = '$#'.join(response.xpath('//*[@id="productDetails_detailBullets_sections1"]/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value5 = response.xpath('//*[@id="productDetails_detailBullets_sections1"]/tr/td')
            product_attr_key6 = '$#'.join(response.xpath('//*[@id="productDetails_detailBullets_sections2"]/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value6 = response.xpath('//*[@id="productDetails_detailBullets_sections2"]/tr/td')
            product_attr_key7 = '$#'.join(response.xpath('//*[@id="detail-bullets"]/table/tr/td/div/ul/li/b/text()').extract()).replace("\n",'').replace('\t','').strip()
            product_attr_value7 = response.xpath('//*[@id="detail-bullets"]/table/tr/td/div/ul/li')
            product_attr_key8= '$#'.join(response.xpath('//*[@id="feature-bullets"]/ul/li/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value8 = response.xpath('//*[@id="feature-bullets"]/ul/li/span')
            product_attr_key31 = '$#'.join(response.xpath('//*[@id="productDetails_techSpec_section_1"]/tbody/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value31 = response.xpath('//*[@id="productDetails_techSpec_section_1"]/tbody/tr/td')
            product_attr_key41 =  '$#'.join(response.xpath('//*[@id="productDetails_techSpec_section_2"]/tbody/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value41 = response.xpath('//*[@id="productDetails_techSpec_section_2"]/tbody/tr/td')
            product_attr_key51 = '$#'.join(response.xpath('//*[@id="productDetails_detailBullets_sections1"]/tbody/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value51 = response.xpath('//*[@id="productDetails_detailBullets_sections1"]/tbody/tr/td')
            product_attr_key61 = '$#'.join(response.xpath('//*[@id="productDetails_detailBullets_sections2"]/tbody/tr/th/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            product_attr_value61 = response.xpath('//*[@id="productDetails_detailBullets_sections2"]/tbody/tr/td')
            product_attr_key71 = '$#'.join(response.xpath('//*[@id="detail-bullets"]/table/tbody/tr/td/div/ul/li/b/text()').extract()).replace("\n",'').replace('\t','').strip()
            product_attr_value71 = response.xpath('//*[@id="detail-bullets"]/table/tbody/tr/td/div/ul/li')
            product_attr_value9 =response.xpath('//*[@id="prodDetails"]/span')
            if not product_attr_key7: product_attr_key7 = '$#'.join(response.xpath('//*[@id="detailBullets_feature_div"]/ul/li/span/span[1]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not product_attr_value7: product_attr_value7 = response.xpath('//*[@id="detailBullets_feature_div"]/ul/li/span/span[2]')
            result_dict = {}
            key= None
            if product_attr_key3 and (product_attr_value3  or product_attr_value31)  :
                try:
                    value = product_attr_value3
                    if not value: value = product_attr_value31
                except: value = product_attr_value31
                key = product_attr_key3.split("$#")

                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result =zip(key,value[0:len(key)-1])

            #print result       
            for i,j in result:
                result_dict[i.replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()           
            match_type = ''
            brand_match_type = ''
            item_no =''
            match_dim = ''
            mpn_match =''
            if result_dict:final_dict.append(result_dict)
            if result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip() :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()

            brand2 = result_dict.get('Brand','').strip()
            
            result_dict = {}
            key= None
            if product_attr_key1 and product_attr_value1   :
                try:
                    value = product_attr_value1
                    key = product_attr_key1.split("$#")

                    if  key and len(key) == len(value):
                        result = zip(key,value)
                    else:
			            result = zip(key,value[0:len(key)-1])
                except: pass

            #print result       
            for i,j in result:
                result_dict[i.replace(":",'').strip()] =  "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()

            if result_dict:final_dict.append(result_dict)
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip() 

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 
            result_dict = {}
            key= None
            if product_attr_key4  and product_attr_value4    :
                try:
                    value = product_attr_value4
                    key = product_attr_key4.split("$#")

                    if  key and len(key) == len(value):
                        result =zip(key,value)
                    else:
                        result = zip(key,value[0:len(key)-1])
                except: pass
            
            #print result       
            for i,j in result:
                result_dict[i.replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 
            
            result_dict = {}
            key= None
            value = response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div[2]/ul/li')
            if not value:value = response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div/ul/li')
            if product_attr_key5  and (product_attr_value5  or product_attr_value51 )  :
                try:
                    value = product_attr_value5
                    if not value: value = product_attr_value51                
                except: value = product_attr_value51
                key = product_attr_key5.split("$#")
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[:len(key)-1])

            for i,j in result:
                result_dict[i.replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()

            if result_dict:final_dict.append(result_dict)
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 

            result_dict = {}
            key= None
            if product_attr_key7  and (product_attr_value7  or product_attr_value71 )  :
                try:
                    value = product_attr_value7
                    if not value: value = product_attr_value71
                except: value = product_attr_value71
                key = product_attr_key7.split("$#")

                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

            for i,j in result:
                result_dict[i.replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()

            if result_dict:final_dict.append(result_dict)
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 


            #print brand,item_no



            product_attr_value7 = '$#'.join([i.strip() for i in response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div[2]/ul/li/text()').extract()]).replace("\n",'').replace('\t','').strip()
            product_attr_key7 = '$#'.join(response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div[2]/ul/li/b/text()').extract()).replace("\n",'').replace('\t','').strip()
            result_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                 product_attr_value7 = '$#'.join([i.strip() for i in response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div/ul/li/text()').extract()]).replace("\n",'').replace('\t','').strip()
                 product_attr_key7 = '$#'.join([i.strip() for i in response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div/ul/li/b/text()').extract()]).replace("\n",'').replace('\t','').strip()

            
            if product_attr_key7  and product_attr_value7    :
                try:
                    value = product_attr_value7
                except: value = ""
                key = product_attr_key7.split("$#")
                value = response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div[2]/ul/li')
                if not value:value = response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div/ul/li')

                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for key, val in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()

                    result_dict[key.strip()] = "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                #print result_dict
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 

            result_dict = {}
            key= None
            if result_dict:final_dict.append(result_dict)

            product_attr_value7 = response.xpath('//*[@id="technicalSpecifications_feature_div"]/div[2]/div/div[1]/div/table/tbody/tr/td')
            product_attr_key7 = '$#'.join(response.xpath('//*[@id="technicalSpecifications_feature_div"]/div[2]/div/div[1]/div/table/tbody/tr/th/text()').extract()).replace("\n",'').replace('\t','').strip()
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 = response.xpath('//*[@id="technicalSpecifications_feature_div"]/div[2]/div/div[1]/div/table/tr/td')
                product_attr_key7 = '$#'.join(response.xpath('//*[@id="technicalSpecifications_feature_div"]/div[2]/div/div[1]/div/table/tr/th/text()').extract()).replace("\n",'').replace('\t','').strip()

            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7.split("$#")

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[i.replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()

            if result_dict:final_dict.append(result_dict)
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 



            result_dict = {}
            key= None
		  

            product_attr_value7 = response.xpath('//*[@id="productDetailsTable"]/tbody/tr/td/div/ul/li')
            product_attr_key7 = response.xpath('//*[@id="productDetailsTable"]/tbody/tr/td/div/ul/li/b')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 = response.xpath('//*[@id="productDetailsTable"]/tr/td/div/ul/li')
                product_attr_key7 = response.xpath('//*[@id="productDetailsTable"]/tr/td/div/ul/li/b')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()

            if result_dict:final_dict.append(result_dict)
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get('Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 

            product_attr_value7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr/td[2]')
            product_attr_key7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr/td[1]')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tr/td[2]')
                product_attr_key7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tr/td[1]')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            #print result_dict, "1"
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 


            product_attr_value7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr/td[2]')
            product_attr_key7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tbody/tr/td[1]')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tr/td[2]')
                product_attr_key7 = response.xpath('//*[@id="prodDetails"]/div[2]/div[1]/div/div[2]/div/div/table/tr/td[1]')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            #print result_dict, "2"
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model Number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model Number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 

   
            product_attr_value7 = response.xpath('//*[@id="technicalSpecifications_section_1"]/tbody/tr/td')
            product_attr_key7 = response.xpath('//*[@id="technicalSpecifications_section_1"]/tbody/tr/th')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 = response.xpath('//*[@id="technicalSpecifications_section_1"]/tr/td')
                product_attr_key7 = response.xpath('//*[@id="technicalSpecifications_section_1"]/tr/th')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            #print result_dict, "3"
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 



            product_attr_value7 = response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div[2]/div/div/table/tbody/tr/td[2]')
            product_attr_key7 = response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div[2]/div/div/table/tbody/tr/td[1]')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 =  response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div[2]/div/div/table/tr/td[2]')
                product_attr_key7 =  response.xpath('//*[@id="prodDetails"]/div/div[1]/div/div[2]/div/div/table/tr/td[1]')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            #print result_dict, "3"
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 





            product_attr_value7 = response.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li')
            product_attr_key7 = response.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li/b')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 =  response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div/ul/li')
                product_attr_key7 =  response.xpath('//*[@id="detail_bullets_id"]/table/tr/td/div/ul/li/b')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            #print result_dict, "3"
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 




            product_attr_value7 = response.xpath('//*[@id="prodDetails"]/div/div[2]/div[1]/div[2]/div/div/table/tbody/tr/td[2]')
            product_attr_key7 = response.xpath('//*[@id="prodDetails"]/div/div[2]/div[1]/div[2]/div/div/table/tbody/tr/td[1]')
            attr_dict = {}	
            if not (product_attr_key7  and product_attr_value7 ):
                product_attr_value7 =  response.xpath('//*[@id="prodDetails"]/div/div[2]/div[1]/div[2]/div/div/table/tr/td[2]')
                product_attr_key7 =  response.xpath('//*[@id="prodDetails"]/div/div[2]/div[1]/div[2]/div/div/table/tr/td[1]')
            
            if product_attr_key7  and product_attr_value7    :

                key = product_attr_key7

                value= product_attr_value7
                if  key and len(key) == len(value):
                    result = zip(key,value)
                else:
			        result = zip(key,value[0:len(key)-1])

                for i, j in result:
                    #print key, "".join(val.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
                    result_dict[ "".join(i.xpath('text()').extract()).replace("\n",'').replace('\t','').strip().replace(":",'').strip()] = "".join(j.xpath('text()').extract()).replace("\n",'').replace('\t','').strip()
            if result_dict:final_dict.append(result_dict)
            #print result_dict, "3"
            if not item_no and( result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()) :
                item_no = result_dict.get('Manufacturer Part Number','').strip() or result_dict.get('Part Number','').strip() or result_dict.get('Item model number','').strip() or result_dict.get(u'Model number','').strip()

            if not brand2:  brand2 =result_dict.get('Brand','').strip() 


        except:
            raise
		  
        ean = ""
        variation_ASIN = ""
        variation_ASIN = ",".join(response.xpath('//*[@id="variation_color_name"]/ul/li/@data-defaultasin').extract())
      
        variation_dp_url = response.xpath('//*[@id="variation_color_name"]/ul/li/@data-dp-url').extract()
        if len(variation_dp_url )>0:
            variation_dp_url_list = [ i[3:].split("/ref")[0] for i in variation_dp_url]
            variation_ASIN = variation_ASIN + ","+ ",".join(variation_dp_url_list)
        variation_ASIN = variation_ASIN +","+ ",".join(response.xpath('//*[@id="variation_platform_for_display"]/ul/li/@data-defaultasin').extract())

        variation_ASIN = variation_ASIN +","+ ",".join(response.xpath('//*[@id="variation_service_plan_term"]/ul/li/@data-defaultasin').extract())
        if variation_ASIN: variation_ASIN = variation_ASIN +","
        variation_ASIN  = variation_ASIN + ",".join(response.xpath('//*[@id="variation_size_name"]/ul/li/@data-defaultasin').extract())
        variation_size = response.xpath('//*[@id="native_dropdown_selected_size_name"]/option/@value').extract()
        if len(variation_size )>0:
            variation_size_list = [ i.split(",")[1] for i in variation_size[1:]]
            variation_ASIN = variation_ASIN + "," + ",".join(variation_size_list)
        variation_size = response.xpath('//*[@id="native_dropdown_selected_initial_character"]/option/@value').extract()
        #print variation_size
        if len(variation_size )>0:
            variation_size_list = [ i.split(",")[1] for i in variation_size[1:]]
            variation_ASIN = variation_ASIN + "," + ",".join(variation_size_list)
        attr_dict = dict([ (k,v)  for d in final_dict for k,v in d.items() ])
        if not item_no and( attr_dict.get('Modellnummer','').strip() or attr_dict.get('Teilenummer','').strip() ) :
            item_no = attr_dict.get('Modellnummer','').strip() or attr_dict.get('Teilenummer','').strip()
        if not ean and( attr_dict.get('EAN/UPC','').strip() or attr_dict.get('EAN / Artikelnummer','').strip() ) :
            ean =  attr_dict.get('EAN/UPC','').strip() or attr_dict.get('EAN / Artikelnummer','').strip() 
        if not brand2 and( attr_dict.get('Manufacturer','').strip() or attr_dict.get('Brand Name','').strip() ) :
            brand2 =  attr_dict.get('Manufacturer','').strip() or attr_dict.get('Brand Name','').strip() 
            #if not brand2:  brand2 =result_dict.get('Manufacturer','').strip()
		
                                                        
        if title:
            count = "".join(response.xpath('//*[@id="olp_feature_div"]/div/span[1]/a/text()').extract()).strip()
            if not count: count = ''.join(response.xpath('//*[@id="outOfStock"]/div/span//text()').extract()).replace('/t','').replace('/n','').strip()
            if not count: count = ''.join(response.xpath('//*[@id="availability"]/span/text()').extract()).replace('/t','').replace('/n','').strip()
            star_rating  = "".join(response.xpath('//*[@id="acrPopover"]/span[1]/a/i[1]/span/text()').extract()).replace('/n','').strip()
            num_review = "".join(response.xpath('//*[@id="acrCustomerReviewText"]/text()').extract()).replace('/n','').strip()
            question_answered = "".join(response.xpath('//*[@id="askATFLink"]/span/text()').extract()).replace('/n','').strip()
            item = Amazon_upc_out()
            item['star_rating'] = star_rating
            item['num_review'] = num_review
            item['question_answered'] = question_answered
            item['product_title'] = title
            item['mpn'] = "'" +item_no+"'"
            item['attr_dict'] = json.dumps(attr_dict)
            item['brand1'] = brand1
            item['brand2'] = brand2
            item['response_url']=response.url
            #item['ASIN'] = attr.get('DPID')
            item['date_timestamp']= int(time.time())
            #item['UPC']= attr['UPC']
            item['breadcrumb']="/".join(bredcrumb_temp)
            item['seller_count'] = count
            item['ship_price'] = ship_price
            item['ship_price2'] = ship_price2
            item['price'] = price
            item['price1'] = price1
            item['seller_name'] = seller_name
            item['spider'] = self.name
            #if attr['UPC'].find('_') > -1:
            #    item['comp']='Alt'
            #    item['UPC']=attr['UPC'].split('_')[0]
            #else:
            #    item['comp']=''
            item['body'] = response.body
            item['ean'] = ean
            #print item
            yield item
        else:
            try:
                try:result = response.xpath('//meta[2]/@content').extract()[0].find('404.html')
                except: result =-1
                if result>-1 or response.status== 404:
                    item = Amazon_upc_out()
                    item['product_id'] = response.meta['id']
                    #item['ASIN'] = attr.get('DPID')
                    item['response_url']=response.url
                    #item['UPC']= attr['UPC']
                    item['date_timestamp']= int(time.time())
                    item['spider'] = self.name
                    #item['job_id'] = attr['job_id']
                    item['seller_count'] = 'Not Found'
                    #if attr['UPC'].find('_') > -1:
                    #    item['comp']='Alt'
                    #    item['UPC']=attr['UPC'].split('_')[0]
                    #else:
                    #    item['comp']=''
                    item['body'] = response.body                              
                    yield item
                result = response.xpath('//title/text()').extract()[0].find('Page Not Found')
                if result>-1:
                    item = Amazon_upc_out()
                    item['product_id'] = response.meta['id']
                    #item['ASIN'] = attr.get('DPID')
                    item['response_url']=response.url
                    #item['UPC']= attr['UPC']
                    item['date_timestamp']= int(time.time())
                    item['spider'] = self.name
                    #item['job_id'] = attr['job_id']
                    item['seller_count'] = 'Not Found'
                    #if attr['UPC'].find('_') > -1:
                    #    item['comp']='Alt'
                    #    item['UPC']=attr['UPC'].split('_')[0]
                    #else:
                    #    item['comp']=''
                    item['body'] = response.body                              
                    yield item
            except: raise 