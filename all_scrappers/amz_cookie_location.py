# -*- coding: utf-8 -*-
import scrapy
import json
import time
#from shop.items import AmazonItems

class UpcbarcodesSpider(scrapy.Spider):
    name = 'amz_cookie'
    allowed_domains = []
    start_urls = ['http://www.flipkart.com/search?q=9780005996218']

    def parse(self, response):
        url_done =[]
        urls = ['https://www.amazon.com/Haier-HC17SF15RB-Refrigerator-Freezer-Qualified/dp/B00N142GLI?_encoding=UTF8&psc=1']


        #url='http://www.upcbarcodes.com/wp-admin/admin-ajax.php'        # print input_seller_name
        for seller_url in urls:
            if seller_url not in url_done:

                requsturl=scrapy.FormRequest('https://www.amazon.com/gp/delivery/ajax/address-change.html', headers= { 'Origin': 'https://www.amazon.com', 'Accept-Encoding': 'gzip, deflate, br' ,'Accept-Language': 'en-US,en;q=0.9' ,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8' ,'Accept': 'text/html,*/*' , 'Referer': 'https://www.amazon.com/' , 'X-Requested-With': 'XMLHttpRequest' , 'Connection': 'keep-alive'  }, formdata={'zipCode':'60629','locationType':'LOCATION_INPUT','deviceType':'web','pageType':'Detail'} ,callback=self.getupc,method="POST")
                #print requsturl.body

                requsturl.cookies = { 'aws-target-static-id':'1452239187641-159842', 'aws-business-metrics-last-visit':'1460349972900', '__utmv':'194891197.%22QDSe8l%404pyTIl%3FpKm5C24aEFXeBtLGw3BhDIGikRUeXlFGLshyp4Dtw4gLRG%3F9cU%22', 'aws-userInfo':'%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A111320495319%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22rahul%2520bhaskar%22%2C%22keybase%22%3A%22%22%2C%22issuer%22%3A%22https%3A%2F%2Fwww.amazon.com%2Fap%2Fsignin%22%7D', 's_pers':'%20s_vnum%3D1880352564702%2526vn%253D3%7C1880352564702%3B%20s_invisit%3Dtrue%7C1470309348410%3B%20s_nr%3D1470307548416-Repeat%7C1478083548416%3B', '__utma':'194891197.372951375.1452236845.1470290622.1470307550.17', 'aws-ubid-main':'182-7331780-4611541', '_mkto_trk':'id:112-TZM-766&token:_mch-aws.amazon.com-1484112318467-15791', 'x-amz-captcha-1':'1494506850389641', 'x-amz-captcha-2':'7TNj5/ZBUiQE8Q7M1TGIGw==', 'aws-target-visitor-id':'1452239187643-451048.20_19', 'aws-target-data':'%7B%22support%22%3A%221%22%7D', 's_fid':'70673D38D5DFE123-1B689FC000FE2EFF', 's_vn':'1515648318007%26vn%3D7', 'regStatus':'registered', 'x-wl-uid':'1YbHUe7z4Q16UzYOKnza7nF0Z8c60AUse7MqEp+CAv+wdJamSRB88EpQjCOb5Xsg9wS/EFz0+hhSbAl3qbMeh7dWiD1jtJRDs/6R5VxAFk6LzV16+6hZ0Cz+uIpt9TzsXS7IGe2aDx3Q=', 'sst-main':'Sst1|PQGX_RwjQAxLFI_BwdTV0Q4UCL8-RIlysfyKrjYoFGe3oqm9lnuttlbX-lGX4weSExupeA7cYB3Zb0CSGU91LcK9xa8Av4IeMWfbcMKAV4AXqvCSM7S-SXJJpEWQhn0AsaJNc4wwxVVQzrZRhD4jVmdocyJewDAfSRGF1SSTgg_cvNGYGZx8-WqW1z-bekrkDEc-ZrMz9f9Ii077rpcz7Q0tBrE5xr2htKXdWZUzmT4ZSBqkJ9NlatkaEU7sYxBuyl0LadTT6wmYRPPfHnJzSQYdUQ', 'ubid-main':'156-9680828-0484351', 'ca':'ALAAAAAAEAAAAAQGAAEIAUQ=', 's_vnum':'1926421318258%26vn%3D2', 's_nr':'1514281824850-New', 's_dslv':'1514281824851', 'session-id':'144-3935774-8062208', 'session-token':'"n2d7o5bJUB480T+okCcD+Qgte5eb6+XVoWrh4WzA8cPLcyI8v4G8hDqqoR2uWyzLBg4ETAaFwIQ6lGxkm9Hx8EmSQMVq4In0q2pXM0KD/1jNBUtqnPJf5WRZb/xRJGL2mIv58UxYLpLX0e1wf6XYjtrHfPcAOONchcbeZIpAXZOil1fCyrFDBgE3AmUSvlFNadxFHlRhG6IUrSJ/W7TAEw=="', 'session-id-time':'2082787201l', 'csm-hit':'%7B%22tb%22%3A%227099AAE54J4R4DQXDH89%2Bs-7099AAE54J4R4DQXDH89%7C1515471521353%22%2C%22adb%22%3A%22adblk_no%22%7D' }
                time.sleep(1)
                yield requsturl
    def getupc(self, response):
        urls = 'https://www.amazon.com/Haier-HC17SF15RB-Refrigerator-Freezer-Qualified/dp/B00N142GLI?_encoding=UTF8&psc=1'
        req = scrapy.Request(urls, headers={'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'} ,callback=self.parse1)
        #req.cookies = {'aws-target-static-id':'1452239187641-159842', 'aws-business-metrics-last-visit':'1460349972900', '__utmv':'194891197.%22QDSe8l%404pyTIl%3FpKm5C24aEFXeBtLGw3BhDIGikRUeXlFGLshyp4Dtw4gLRG%3F9cU%22', 'aws-userInfo':'%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A111320495319%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22rahul%2520bhaskar%22%2C%22keybase%22%3A%22%22%2C%22issuer%22%3A%22https%3A%2F%2Fwww.amazon.com%2Fap%2Fsignin%22%7D', 's_pers':'%20s_vnum%3D1880352564702%2526vn%253D3%7C1880352564702%3B%20s_invisit%3Dtrue%7C1470309348410%3B%20s_nr%3D1470307548416-Repeat%7C1478083548416%3B', '__utma':'194891197.372951375.1452236845.1470290622.1470307550.17', 'aws-ubid-main':'182-7331780-4611541', '_mkto_trk':'id:112-TZM-766&token:_mch-aws.amazon.com-1484112318467-15791', 'x-amz-captcha-1':'1494506850389641', 'x-amz-captcha-2':'7TNj5/ZBUiQE8Q7M1TGIGw==', 'aws-target-visitor-id':'1452239187643-451048.20_19', 'aws-target-data':'%7B%22support%22%3A%221%22%7D', 's_fid':'70673D38D5DFE123-1B689FC000FE2EFF', 's_vn':'1515648318007%26vn%3D7', 'regStatus':'registered', 'x-wl-uid':'1YbHUe7z4Q16UzYOKnza7nF0Z8c60AUse7MqEp+CAv+wdJamSRB88EpQjCOb5Xsg9wS/EFz0+hhSbAl3qbMeh7dWiD1jtJRDs/6R5VxAFk6LzV16+6hZ0Cz+uIpt9TzsXS7IGe2aDx3Q=', 'sst-main':'Sst1|PQGX_RwjQAxLFI_BwdTV0Q4UCL8-RIlysfyKrjYoFGe3oqm9lnuttlbX-lGX4weSExupeA7cYB3Zb0CSGU91LcK9xa8Av4IeMWfbcMKAV4AXqvCSM7S-SXJJpEWQhn0AsaJNc4wwxVVQzrZRhD4jVmdocyJewDAfSRGF1SSTgg_cvNGYGZx8-WqW1z-bekrkDEc-ZrMz9f9Ii077rpcz7Q0tBrE5xr2htKXdWZUzmT4ZSBqkJ9NlatkaEU7sYxBuyl0LadTT6wmYRPPfHnJzSQYdUQ', 'ubid-main':'156-9680828-0484351', 'ca':'ALAAAAAAEAAAAAQGAAEIAUQ=', 's_cc':'true', 's_vnum':'1926421318258%26vn%3D2', 's_sq':'%5B%5BB%5D%5D', 's_nr':'1514281824850-New', 's_dslv':'1514281824851', 's_ppv':'0', 'session-id':'144-3935774-8062208', 'session-token':'"n2d7o5bJUB480T+okCcD+Qgte5eb6+XVoWrh4WzA8cPLcyI8v4G8hDqqoR2uWyzLBg4ETAaFwIQ6lGxkm9Hx8EmSQMVq4In0q2pXM0KD/1jNBUtqnPJf5WRZb/xRJGL2mIv58UxYLpLX0e1wf6XYjtrHfPcAOONchcbeZIpAXZOil1fCyrFDBgE3AmUSvlFNadxFHlRhG6IUrSJ/W7TAEw=="', 'session-id-time':'2082787201l', 'csm-hit':'237TD3TWV27YA7YCZ1EQ+sa-2VH3X3ZB5ZYQ580QJTZC-ZWXKG81WSQ9073MYC2G6|1514283786315'}
        yield req
		
		
    def parse1(self, response):
        print " ".join(response.xpath('//*[@id="fast-track-message"]/div//text()').extract())
        print " ".join(response.xpath('//*[@id="unifiedLocation_feature_div"]/div/div/span[2]/a/span//text()').extract())
        #locations = response.xpath('//script[contains(., "var dataToReturn")]/text()').re(pattern)[0]
        #locations=demjson.decode(locations)
        #item['asins'] = locations["asinVariationValues"].keys()
        #item["dimensionValuesData"] = locations["dimensionValuesData"]

    def getupc1(self,response):
        print response.body
        """
        asin=''
        url=''
        try:
            asin=response.meta['asin']
            url=response.meta['url']
        except:
            pass
        # print("*****************response url ************************")
        # print(response.url)
        # # print("*****************response body ***********************
        # body=response.body
        jsonparsear=json.loads(response.body)
        if jsonparsear['status']=='success':
            item =AmazonItems()
            print(jsonparsear)
            upc=jsonparsear['upc']
            if not upc: upc = jsonparsear['code']
            asin=asin
            item['asin']=asin
            item['input_url']=upc
            yield item

        else:
            print("IN Else*****************")
            print(url)
            print(asin)
            requsturla=scrapy.FormRequest(url,headers={'Accept':'application/json, text/javascript, */*; q=0.01','Accept-Encoding':'gzip, deflate','Accept-Language':'en-IN,en-GB;q=0.8,en-US;q=0.6,en;q=0.4','Cache-Control':'no-cache','Connection':'keep-alive','Content-Length':'51','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Host':'www.upcbarcodes.com','Origin':'http://www.upcbarcodes.com','Pragma':'no-cache','Referer':'http://www.upcbarcodes.com/dashboard/asin-gtin-converter/','User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.32 Safari/537.36','X-Requested-With':'XMLHttpRequest'},formdata={'action':'convert_asin2gtin','code':asin,'country':'us'},dont_filter=True,callback=self.getupc,method="POST",meta={'url':url,'asin':asin})
        # headers={'Accept':'application/json, text/javascript, */*; q=0.01','Accept-Encoding':'gzip, deflate','Accept-Language':'en-IN,en-GB;q=0.8,en-US;q=0.6,en;q=0.4','Cache-Control':'no-cache','Connection':'keep-alive','Content-Length':'51','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Host':'www.upcbarcodes.com','Origin':'http://www.upcbarcodes.com','Pragma':'no-cache','Referer':'http://www.upcbarcodes.com/dashboard/asin-gtin-converter/','User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.32 Safari/537.36','X-Requested-With':'XMLHttpRequest',}
            time.sleep(1)
            yield requsturla
	    """

        # print (body)