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
    min_price = scrapy.Field()
    max_price = scrapy.Field()
    buy_box_seller= scrapy.Field()

    ratings= scrapy.Field()
    customer_reviews= scrapy.Field()
    brand= scrapy.Field()
    asin= scrapy.Field()
    title= scrapy.Field()
    category= scrapy.Field()
    category1= scrapy.Field()
    position = scrapy.Field()
    product_url = scrapy.Field()
    timestamp = scrapy.Field()
    best_sellers_rank = scrapy.Field()

    product_id = scrapy.Field()
    upc = scrapy.Field()
    product_rank = scrapy.Field()
    price_per_unit = scrapy.Field()
    prime_eligible = scrapy.Field()
    prime_pantry = scrapy.Field()
    add_on_item = scrapy.Field()
    amazon_fresh = scrapy.Field()
    subscribe_and_save = scrapy.Field()
    one_time_purchase = scrapy.Field()
    min_delivery_days = scrapy.Field()
    max_delivery_days = scrapy.Field()
    pack_size = scrapy.Field()
    quantity = scrapy.Field()
    color = scrapy.Field()
    size = scrapy.Field()
    material = scrapy.Field()
    item_model_number = scrapy.Field()
    flavour = scrapy.Field()
    scent = scrapy.Field()
    style = scrapy.Field()
    department = scrapy.Field()
    delivery_location = scrapy.Field()
    zipcode = scrapy.Field()

class amazonSpider(scrapy.Spider):
    imgcount = 1
    name = "amz_bestsellers_productinfo_23-03-2018_50k_part2"
    allowed_domains = []

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]

    def parse(self, response):
        #url='http://www.upcbarcodes.com/wp-admin/admin-ajax.php'        # print input_seller_name
        zipcodelist=["60629","11385","10025","91911","78572","33012","75228","33157","95111","60453","70072","17602","55337","57701","2895","98125","35216","29841","68701","83815"]
        for zipcodes in zipcodelist:
            requsturl=scrapy.FormRequest('https://www.amazon.com/gp/delivery/ajax/address-change.html', headers= { 'Origin': 'https://www.amazon.com', 'Accept-Encoding': 'gzip, deflate, br' ,'Accept-Language': 'en-US,en;q=0.9' ,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8' ,'Accept': 'text/html,*/*' , 'Referer': 'https://www.amazon.com/' , 'X-Requested-With': 'XMLHttpRequest' , 'Connection': 'keep-alive'  }, formdata={'zipCode': zipcodes,'locationType':'LOCATION_INPUT','deviceType':'web','pageType':'Detail'} ,callback=self.getupc,method="POST", meta={'zipcode':zipcodes}, dont_filter=True)
            #print requsturl.body
            #requsturl.

            #requsturl.cookies = { 'aws-target-static-id':'1452239187641-159842', 'aws-business-metrics-last-visit':'1460349972900', '__utmv':'194891197.%22QDSe8l%404pyTIl%3FpKm5C24aEFXeBtLGw3BhDIGikRUeXlFGLshyp4Dtw4gLRG%3F9cU%22', 'aws-userInfo':'%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A111320495319%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22rahul%2520bhaskar%22%2C%22keybase%22%3A%22%22%2C%22issuer%22%3A%22https%3A%2F%2Fwww.amazon.com%2Fap%2Fsignin%22%7D', 's_pers':'%20s_vnum%3D1880352564702%2526vn%253D3%7C1880352564702%3B%20s_invisit%3Dtrue%7C1470309348410%3B%20s_nr%3D1470307548416-Repeat%7C1478083548416%3B', '__utma':'194891197.372951375.1452236845.1470290622.1470307550.17', 'aws-ubid-main':'182-7331780-4611541', '_mkto_trk':'id:112-TZM-766&token:_mch-aws.amazon.com-1484112318467-15791', 'x-amz-captcha-1':'1494506850389641', 'x-amz-captcha-2':'7TNj5/ZBUiQE8Q7M1TGIGw==', 'aws-target-visitor-id':'1452239187643-451048.20_19', 'aws-target-data':'%7B%22support%22%3A%221%22%7D', 's_fid':'70673D38D5DFE123-1B689FC000FE2EFF', 's_vn':'1515648318007%26vn%3D7', 'regStatus':'registered', 'x-wl-uid':'1YbHUe7z4Q16UzYOKnza7nF0Z8c60AUse7MqEp+CAv+wdJamSRB88EpQjCOb5Xsg9wS/EFz0+hhSbAl3qbMeh7dWiD1jtJRDs/6R5VxAFk6LzV16+6hZ0Cz+uIpt9TzsXS7IGe2aDx3Q=', 'sst-main':'Sst1|PQGX_RwjQAxLFI_BwdTV0Q4UCL8-RIlysfyKrjYoFGe3oqm9lnuttlbX-lGX4weSExupeA7cYB3Zb0CSGU91LcK9xa8Av4IeMWfbcMKAV4AXqvCSM7S-SXJJpEWQhn0AsaJNc4wwxVVQzrZRhD4jVmdocyJewDAfSRGF1SSTgg_cvNGYGZx8-WqW1z-bekrkDEc-ZrMz9f9Ii077rpcz7Q0tBrE5xr2htKXdWZUzmT4ZSBqkJ9NlatkaEU7sYxBuyl0LadTT6wmYRPPfHnJzSQYdUQ', 'ubid-main':'156-9680828-0484351', 'ca':'ALAAAAAAEAAAAAQGAAEIAUQ=', 's_vnum':'1926421318258%26vn%3D2', 's_nr':'1514281824850-New', 's_dslv':'1514281824851', 'session-id':'144-3935774-8062208', 'session-token':'"n2d7o5bJUB480T+okCcD+Qgte5eb6+XVoWrh4WzA8cPLcyI8v4G8hDqqoR2uWyzLBg4ETAaFwIQ6lGxkm9Hx8EmSQMVq4In0q2pXM0KD/1jNBUtqnPJf5WRZb/xRJGL2mIv58UxYLpLX0e1wf6XYjtrHfPcAOONchcbeZIpAXZOil1fCyrFDBgE3AmUSvlFNadxFHlRhG6IUrSJ/W7TAEw=="', 'session-id-time':'2082787201l', 'csm-hit':'%7B%22tb%22%3A%227099AAE54J4R4DQXDH89%2Bs-7099AAE54J4R4DQXDH89%7C1515471521353%22%2C%22adb%22%3A%22adblk_no%22%7D' }
            requsturl.cookies = {'x-wl-uid':'1QBgT0TBwoj9RQ+QP7eh8ocBTABgs1739+rzq1e3s1iwjoSRYnMpbAczaaknzT2id2ww9iSyiyXd3OQeaJ9Nm9xZrZOKqXNWIDJihS4V7CV+xlp+PQA7T/ILJyNBZ15so9XvNPTzCBQA=', 'x-amz-captcha-1':'1511784189246059', 'x-amz-captcha-2':'e+dIUFBcjimZCAzt1M7ENg==', 'skin':'noskin', 's_cc':'true', 's_nr':'1514464459649-Repeat', 's_vnum':'1935816974090%26vn%3D2', 's_dslv':'1514464459650', 's_sq':'%5B%5BB%5D%5D', 'amznacsleftnav-74393fbe-66a6-3a52-840b-37b54d8c76ce':'1', 'ubid-main':'151-8001146-5395566', 'session-id':'143-2570392-1761151', 'session-id-time':'2082787201l', 'session-token':'06YC+sJBPQUYica59Tep0SDc/OdZYTQk3nRUXwMQ9ZmJuSTmJrg+RBhaKKMtSTw3JQmmVuO3ivHRybUoZlp/Lb25cUBOQGLD18j18BjmoDMwnAVTFYJCwm/m3y5jPQeB0R+2uhl1LI4U6not78OaHrRqy4mxqRjwgLpf0e2GYbKAHbN0i1BQkXoyX5rlQjM+', 'csm-hit':'HRT1PQHJ2W7REDHGHZ8C+s-HRT1PQHJ2W7REDHGHZ8C|1517381562270' }
            #time.sleep(.2)
            yield requsturl
    def getupc(self, response):
        url_done =[
]
        urls = [
["50001","Biometrics","https://www.amazon.com/Antner-Fingerprint-Attendance-Directly-Download/dp/B075V41YBC?_encoding=UTF8&psc=1","Electronics","85","10025"],
["50002","Video Glasses","https://www.amazon.com/Aerb-Cardboard-Virtual-Smartphone-Headband/dp/B0199VSE5I?_encoding=UTF8&psc=1","Electronics","83","33157"],
["50003","TV-DVD Combos","https://www.amazon.com/DECK13DR-13-3-TV-DVD-Combo/dp/B005GNR9G4?_encoding=UTF8&psc=1","Electronics","33","11385"],
["50004","TV-DVD Combos","https://www.amazon.com/Player-Package-display-Native-mounted/dp/B014LW16ZA?_encoding=UTF8&psc=1","Electronics","34","75228"],
["50005","VCRs","https://www.amazon.com/Panasonic-PV-9451-Hi-Fi-Stereo-Plus/dp/B009W8FSV2?_encoding=UTF8&psc=1","Electronics","82","33157"],
["50006","PlayStation Vita","https://www.amazon.com/PlayStation-Vita-Memory-Card-PCH-Z641J/dp/B00F27JGVA?_encoding=UTF8&psc=1","Electronics","3","60629"],
["94621","Tabletop Lighting","https://www.amazon.com/TDLTEK-Waterproof-Submersible-Wedding-Decoration/dp/B01N4NPKVV?_encoding=UTF8&psc=1","Patio, Lawn & Garden","96","57701"],
["94622","Tabletop Lighting","https://www.amazon.com/Luminara-Flameless-Candle-Degree-Unscented/dp/B01N4CT0AJ?_encoding=UTF8&psc=1","Patio, Lawn & Garden","97","78572"],
["94623","Tabletop Lighting","https://www.amazon.com/Tapered-Timer-Candlesticks-Flameless-Candles/dp/B07622V1PN?_encoding=UTF8&psc=1","Patio, Lawn & Garden","98","35216"],
]
        for url in urls:
            if response.meta["zipcode"]==url[5]:
                #urls = 'https://www.amazon.com/dp/B00K5SH7LM/?th=1'
                req = scrapy.Request(url[2], headers={'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'} ,callback=self.parse1, meta={"category":url[1], "department":url[3], "position":url[4], "product_id":url[0], "zipcode":url[5]}, dont_filter=True)
                #req.cookies = {'aws-target-static-id':'1452239187641-159842', 'aws-business-metrics-last-visit':'1460349972900', '__utmv':'194891197.%22QDSe8l%404pyTIl%3FpKm5C24aEFXeBtLGw3BhDIGikRUeXlFGLshyp4Dtw4gLRG%3F9cU%22', 'aws-userInfo':'%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A111320495319%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22rahul%2520bhaskar%22%2C%22keybase%22%3A%22%22%2C%22issuer%22%3A%22https%3A%2F%2Fwww.amazon.com%2Fap%2Fsignin%22%7D', 's_pers':'%20s_vnum%3D1880352564702%2526vn%253D3%7C1880352564702%3B%20s_invisit%3Dtrue%7C1470309348410%3B%20s_nr%3D1470307548416-Repeat%7C1478083548416%3B', '__utma':'194891197.372951375.1452236845.1470290622.1470307550.17', 'aws-ubid-main':'182-7331780-4611541', '_mkto_trk':'id:112-TZM-766&token:_mch-aws.amazon.com-1484112318467-15791', 'x-amz-captcha-1':'1494506850389641', 'x-amz-captcha-2':'7TNj5/ZBUiQE8Q7M1TGIGw==', 'aws-target-visitor-id':'1452239187643-451048.20_19', 'aws-target-data':'%7B%22support%22%3A%221%22%7D', 's_fid':'70673D38D5DFE123-1B689FC000FE2EFF', 's_vn':'1515648318007%26vn%3D7', 'regStatus':'registered', 'x-wl-uid':'1YbHUe7z4Q16UzYOKnza7nF0Z8c60AUse7MqEp+CAv+wdJamSRB88EpQjCOb5Xsg9wS/EFz0+hhSbAl3qbMeh7dWiD1jtJRDs/6R5VxAFk6LzV16+6hZ0Cz+uIpt9TzsXS7IGe2aDx3Q=', 'sst-main':'Sst1|PQGX_RwjQAxLFI_BwdTV0Q4UCL8-RIlysfyKrjYoFGe3oqm9lnuttlbX-lGX4weSExupeA7cYB3Zb0CSGU91LcK9xa8Av4IeMWfbcMKAV4AXqvCSM7S-SXJJpEWQhn0AsaJNc4wwxVVQzrZRhD4jVmdocyJewDAfSRGF1SSTgg_cvNGYGZx8-WqW1z-bekrkDEc-ZrMz9f9Ii077rpcz7Q0tBrE5xr2htKXdWZUzmT4ZSBqkJ9NlatkaEU7sYxBuyl0LadTT6wmYRPPfHnJzSQYdUQ', 'ubid-main':'156-9680828-0484351', 'ca':'ALAAAAAAEAAAAAQGAAEIAUQ=', 's_cc':'true', 's_vnum':'1926421318258%26vn%3D2', 's_sq':'%5B%5BB%5D%5D', 's_nr':'1514281824850-New', 's_dslv':'1514281824851', 's_ppv':'0', 'session-id':'144-3935774-8062208', 'session-token':'"n2d7o5bJUB480T+okCcD+Qgte5eb6+XVoWrh4WzA8cPLcyI8v4G8hDqqoR2uWyzLBg4ETAaFwIQ6lGxkm9Hx8EmSQMVq4In0q2pXM0KD/1jNBUtqnPJf5WRZb/xRJGL2mIv58UxYLpLX0e1wf6XYjtrHfPcAOONchcbeZIpAXZOil1fCyrFDBgE3AmUSvlFNadxFHlRhG6IUrSJ/W7TAEw=="', 'session-id-time':'2082787201l', 'csm-hit':'237TD3TWV27YA7YCZ1EQ+sa-2VH3X3ZB5ZYQ580QJTZC-ZWXKG81WSQ9073MYC2G6|1514283786315'}
                #time.sleep(.1)
                if url[0] not in url_done:
                    time.sleep(.1)
                    yield req
		
		
    def parse1(self, response):
        #f1=open("amazon_fresh.html","w")
        #f1.write(response.body)
        #f1.close()
        #print " ".join(response.xpath('//*[@id="fast-track-message"]/div//text()').extract())
        #print " ".join(response.xpath('//*[@id="unifiedLocation_feature_div"]/div/div/span[2]/a/span//text()').extract())
        item=AmazonItems()
        item['product_id']=response.meta["product_id"]
        title=response.xpath('//*[@id="productTitle"]//text()').extract()
        if not title: title=response.xpath('//*[@id="ebooksProductTitle"]/text()').extract()
        asin=response.url
        bredcrumb_temp = []
        item['delivery_location']=" ".join(response.xpath('//*[@id="unifiedLocation_feature_div"]/div/div/span[2]/a/span//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        try:
            for part in response.xpath('//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li/span/a/text()').extract():
                bredcrumb_temp.append(part.replace('\n','').strip())
        except: pass
        #image_url=response.xpath('//*[@id="landingImage"]/@src').extract()
        #image_url=response.xpath('//*[@id="landingImage"]/@data-old-hires').extract()[0]
        #if not image_url: image_url=":".join(response.xpath('//*[@id="landingImage"]/@data-a-dynamic-image').extract()[0].split(":")[:2]).replace("{",'').replace('"','')
        #if not image_url: image_url="".join(response.xpath('//*[@id="js-masrw-main-image"]/@src').extract())
			
        #image_url1=[]
        #image_url1.append(image_url)
        try: brand1 = response.xpath('//*[@id="brand"]/text()').extract()[0].replace("  ",'').replace("\n",'').replace('\t','').strip()
        except: brand1=""
        if not brand1:
            try:
                brand1=response.xpath('//*[@id="bylineInfo"]/text()').extract()[0].replace("  ",'').replace("\n",'').replace('\t','').strip()
            except: 
                try:
                    brand1=response.xpath('//*[@id="brand"]/@href').extract()[0].replace("  ",'').replace("\n",'').replace('\t','').strip().split('/')[1]
                except: brand1=""
        customer_reviews=response.xpath('//*[@id="acrCustomerReviewText"]/text()').extract()
        try:
            ratings=response.xpath('//*[@id="a-popover-content-7"]/div/div/div/div[1]/span[@class="a-size-base a-color-secondary"]/text()').extract()
            #if not ratings: ratings="".join(response.xpath('//*[@id="acrPopover"]/span[1]/a/i[1]/span/text()').extract()).replace('/n','').strip()
            if not ratings: ratings=response.xpath('//*[@id="acrPopover"]/span[1]/a/i[1]/span/text()').extract()[0].replace('/n','').strip()
        except :
            ratings=""
        price = "".join(response.xpath('//*[@id="priceblock_ourprice"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        if not price: price = "".join(response.xpath('//*[@id="priceblock_saleprice"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        if not price: price ="".join(response.xpath('//*[@id="price-quantity-container"]/div[2]/div[1]/span[@class="a-size-large a-color-price guild_priceblock_ourprice"]//text()').extract()).replace("\n","").replace(" ","").strip()
        if not price: price ="".join(response.xpath('//*[@id="price-quantity-container"]/div/div[1]/span[@class="a-size-large a-color-price guild_priceblock_ourprice"]//text()').extract()).replace("\n","").replace(" ","").strip()
        if not price: price ="".join(response.xpath('//*[@id="snsPrice"]/div[@class="a-section a-spacing-none snsPriceBlock"]/span[@class="a-size-large a-color-price"]//text()').extract()).replace("\n","").replace(" ","").strip()
        if not price: price ="".join(response.xpath('//*[@id="buyNewSection"]/h5/div/div[2]/div/span[@class="a-size-medium a-color-price offer-price a-text-normal"]//text()').extract()).replace("\n","").replace(" ","").strip()
        if not price: price ="".join(response.xpath('//*[@id="priceblock_usedprice"]//text()').extract()).replace("\n","").replace(" ","").strip()
        if not price: price ="".join(response.xpath('//*[@id="buybox"]/div/table/tr[@class="kindle-price"]/td[@class="a-color-price a-size-medium a-align-bottom"]//text()').extract()).replace("\n","").replace(" ","").replace('\t','').strip()
        if not price: price ="".join(response.xpath('//*[@id="mediaNoAccordion"]/div[1]/div[2]/span[@class="a-size-medium a-color-price header-price"]//text()').extract()).replace("\n","").replace(" ","").replace('\t','').strip()
        if not price: price ="".join(response.xpath('//*[@id="buyNewSection"]/a/h5/div/div[2]/div/span[@class="a-size-medium a-color-price offer-price a-text-normal"]//text()').extract()).replace("\n","").replace(" ","").replace('\t','').strip()
        if not price: price ="".join(response.xpath('//*[@id="usedBuySection"]/h5/div/div[2]/div/span[@class="a-size-medium a-color-price offer-price a-text-normal"]//text()').extract()).replace("\n","").replace(" ","").replace('\t','').strip()
        if price: 
            if price.find('-') > -1:
                item['min_price']=price.split('-')[0]
                item['max_price']=price.split('-')[1]
            else:
                item['min_price']=price
                item['max_price']=price
        else: 
            item['min_price']=""
            item['max_price']=""
        seller_name = " ".join(response.xpath('//*[@id="merchant-info"]/a//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        if not seller_name: seller_name = " ".join(response.xpath('//*[@id="merchant-info"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
        if not seller_name: seller_name ="".join(response.xpath('//*[@id="buybox_feature_div"]/jsp/div[2]/div/p[@class="a-spacing-micro a-color-base"]//text()').extract()).replace("\n","").replace("    ","").replace('\t','').strip()
        if seller_name: item['buy_box_seller']=seller_name
        else: item['buy_box_seller']=""
		
        #try:
        #    priceperunit=response.xpath('//*[@id="snsPrice"]/div[@class="a-section a-spacing-none snsPriceBlock"]/span[@class="a-size-small a-color-price snsPricePerUnit"]/text()').extract()
        #except: priceperunit=""
        priceperunit="".join(response.xpath('//*[@id="snsPrice"]/div[@class="a-section a-spacing-none snsPriceBlock"]/span[@class="a-size-small a-color-price snsPricePerUnit"]/text()').extract())
        if not priceperunit: priceperunit="".join(response.xpath('//*[@id="pantry_priceblock_ppu"]/text()').extract())
        if not priceperunit: priceperunit="".join(response.xpath('//*[@id="priceblock_ourprice_row"]/td[@class="a-span12"]/span[class="a-size-small a-color-price"]/text()').extract())
        upc=""
        table1=response.xpath('//div[@class="section techD"]/div[@class="content pdClearfix"]/div[@class="attrG"]/div[@class="pdTab"]/table/tbody/tr')
        for tr in table1:
            if "".join(tr.xpath('td[1]/text()').extract()).find('UPC') > -1:
                upc=tr.xpath('td[2]/text()').extract()[0]

        if upc=="":
            table2=response.xpath('//div[@id="detail-bullets_feature_div"]/div[@id="detail-bullets"]/table/tr/td/div[@class="content"]/ul/li')
            for tr in table2:
                if "".join(tr.xpath('b/text()').extract()).find('UPC') > -1:
                    upc=tr.xpath('text()').extract()[0]
					
        if upc=="":
            table2=response.xpath('//div[@id="detail-bullets"]/table/tr/td/div[@class="content"]/ul/li')
            for tr in table2:
                if "".join(tr.xpath('b/text()').extract()).find('UPC') > -1:
                    upc=tr.xpath('text()').extract()[0]
					
        if upc=="":
            tabledatalist=response.xpath('//*[@id="productDetails_detailBullets_sections1"]/tr')
            for tabledatas in tabledatalist:
                if "".join(tabledatas.xpath('th/text()').extract()).replace(" ","").lower().find("UPC") > -1:
                    upc=tabledatas.xpath('td/span//text()').extract()
					
        if upc=="":
            tabledatalist=response.xpath('//*[@id="productDetails_detailBullets_sections1"]/tr')
            for tabledatas in tabledatalist:
                if "".join(tabledatas.xpath('th/text()').extract()).replace(" ","").lower().find("UPC") > -1:
                    upc=tabledatas.xpath('td//text()').extract()
        if upc != "":
            item['upc']=str("|".join(upc.split(' ')).strip('|'))
        tabledatalist=response.xpath('//*[@id="productDetails_detailBullets_sections1"]/tr')
        for tabledatas in tabledatalist:
            if "".join(tabledatas.xpath('th/text()').extract()).replace(" ","").lower().find("bestsellersrank") > -1:
                best_sellers_rank=tabledatas.xpath('td/span//text()').extract()
                item['best_sellers_rank']="".join(best_sellers_rank).replace("\n","").replace("\t","").replace("    ","")
				
        modelno=""
        table1=response.xpath('//div[@class="section techD"]/div[@class="content pdClearfix"]/div[@class="attrG"]/div[@class="pdTab"]/table/tbody/tr')
        for tr in table1:
            if "".join(tr.xpath('td[1]/text()').extract()).replace(' ','').replace('\n','').replace('\r','').replace('\t','').lower().find('modelnumber') > -1:
                modelno=tr.xpath('td[2]/text()').extract()[0]

        if modelno=="":
            table2=response.xpath('//div[@id="detail-bullets_feature_div"]/div[@id="detail-bullets"]/table/tr/td/div[@class="content"]/ul/li')
            for tr in table2:
                if "".join(tr.xpath('b/text()').extract()).replace(' ','').replace('\n','').replace('\r','').replace('\t','').lower().find('modelnumber') > -1:
                    modelno=tr.xpath('text()').extract()[0]
					
        if modelno=="":
            table2=response.xpath('//div[@id="detail-bullets"]/table/tr/td/div[@class="content"]/ul/li')
            for tr in table2:
                if "".join(tr.xpath('b/text()').extract()).replace(' ','').replace('\n','').replace('\r','').replace('\t','').lower().find('modelnumber') > -1:
                    modelno=tr.xpath('text()').extract()[0]
					
        if modelno=="":
            tabledatalist=response.xpath('//*[@id="productDetails_detailBullets_sections1"]/tr')
            for tabledatas in tabledatalist:
                if "".join(tabledatas.xpath('th/text()').extract()).replace(' ','').replace('\n','').replace('\r','').replace('\t','').lower().find('modelnumber') > -1:
                    modelno="".join(tabledatas.xpath('td/span//text()').extract()).replace(' ','').replace('\n','').replace('\r','').replace('\t','')
                    #item['best_sellers_rank']="".join(best_sellers_rank).replace("\n","").replace("\t","").replace("    ","")
        if modelno=="":
            tabledatalist=response.xpath('//*[@id="productDetails_detailBullets_sections1"]/tr')
            for tabledatas in tabledatalist:
                if "".join(tabledatas.xpath('th/text()').extract()).replace(' ','').replace('\n','').replace('\r','').replace('\t','').lower().find('modelnumber') > -1:
                    modelno="".join(tabledatas.xpath('td//text()').extract()).replace(' ','').replace('\n','').replace('\r','').replace('\t','')
                    #item['best_sellers_rank']="".join(best_sellers_rank).replace("\n","").replace("\t","").replace("    ","")
        if modelno != "":
            item['item_model_number']=modelno

				
        material=""
        table1=response.xpath('//div[@class="section techD"]/div[@class="content pdClearfix"]/div[@class="attrG"]/div[@class="pdTab"]/table/tbody/tr')
        for tr in table1:
            if "".join(tr.xpath('td[1]/text()').extract()).replace(' ','').replace('\n','').replace('\r','').replace('\t','').lower().find('material') > -1 :
                material=tr.xpath('td[2]/text()').extract()[0]

        #if size=="":
        #    table2=response.xpath('//div[@id="detail-bullets_feature_div"]/div[@id="detail-bullets"]/table/tr/td/div[@class="content"]/ul/li')
        #    for tr in table2:
        #        if "".join(tr.xpath('b/text()').extract()).replace(' ','').replace('\n','').replace('\r','').replace('\t','').lower().find('productdimensions') > -1 or "".join(tr.xpath('b/text()').extract()).replace(' ','').replace('\n','').replace('\r','').replace('\t','').lower().find('packagedimensions') > -1:
        #            size=tr.xpath('text()').extract()[0]
        if material=="":
            table2=response.xpath('//div[@id="detail-bullets_feature_div"]/div[@id="detail-bullets"]/table/tr/td/div[@class="content"]/ul/li')
            for tr in table2:
                if "".join(tr.xpath('b/text()').extract()).replace(' ','').replace('\n','').replace('\r','').replace('\t','').lower().find('material') > -1 :
                    material="".join(tr.xpath('text()').extract()).replace(' ','').replace('\n','').replace('\r','').replace('\t','')
					
        if material=="":
            table2=response.xpath('//div[@id="detail-bullets"]/table/tr/td/div[@class="content"]/ul/li')
            for tr in table2:
                if "".join(tr.xpath('b/text()').extract()).replace(' ','').replace('\n','').replace('\r','').replace('\t','').lower().find('material') > -1 :
                    material="".join(tr.xpath('text()').extract()).replace(' ','').replace('\n','').replace('\r','').replace('\t','')
		
        if material=="":
            tabledatalist=response.xpath('//*[@id="productDetails_detailBullets_sections1"]/tr')
            for tabledatas in tabledatalist:
                if "".join(tabledatas.xpath('th/text()').extract()).replace(' ','').replace('\n','').replace('\r','').replace('\t','').lower().find('material') > -1 :
                    material="".join(tabledatas.xpath('td/span//text()').extract()).replace('    ','').replace('\n','').replace('\r','').replace('\t','')
                    #item['best_sellers_rank']="".join(best_sellers_rank).replace("\n","").replace("\t","").replace("    ","")
        if material=="":
            tabledatalist=response.xpath('//*[@id="productDetails_detailBullets_sections1"]/tr')
            for tabledatas in tabledatalist:
                if "".join(tabledatas.xpath('th/text()').extract()).replace(' ','').replace('\n','').replace('\r','').replace('\t','').lower().find('material') > -1 :
                    material="".join(tabledatas.xpath('td//text()').extract()).replace('    ','').replace('\n','').replace('\r','').replace('\t','')
                    #item['best_sellers_rank']="".join(best_sellers_rank).replace("\n","").replace("\t","").replace("    ","")
        if material=="":
            tabledatalist=response.xpath('//*[@id="productDetails_techSpec_section_1"]/tr')
            for tabledatas in tabledatalist:
                if "".join(tabledatas.xpath('th/text()').extract()).replace(' ','').replace('\n','').replace('\r','').replace('\t','').lower().find('material') > -1 :
                    material="".join(tabledatas.xpath('td//text()').extract()).replace('    ','').replace('\n','').replace('\r','').replace('\t','')
                    #item['best_sellers_rank']="".join(best_sellers_rank).replace("\n","").replace("\t","").replace("    ","")
        if material != "":
            item['material']=material
				
        quantity=""
        if "".join(response.xpath('//select[@id="quantity"]/option/@selected').extract()).replace(" ","").replace("\n","").replace("\t","") == "selected":
            quantity = "".join(response.xpath('//select[@id="quantity"]/option[@selected="selected"]/text()').extract()).replace(" ","").replace("\n","").replace("\t","")
        if quantity == "":
            if "".join(response.xpath('//select[@id="rcxsubsQuan"]/option/@selected').extract()).replace(" ","").replace("\n","").replace("\t","") == "selected":
                quantity = "".join(response.xpath('//select[@id="rcxsubsQuan"]/option[@selected="selected"]/text()').extract()).replace(" ","").replace("\n","").replace("\t","")
        if quantity!= "":
            item['quantity']=quantity
        else:
            item['quantity']=""
        #item['image_url']=image_url1
        item['ratings']=ratings
        if customer_reviews: item['customer_reviews']=customer_reviews[0]
        else: item['customer_reviews']=""
        item['brand']=brand1
		
        #material="".join(response.xpath('//*[@id="featurebullets_feature_div"]//text()').extract()).replace('\n','').replace('\t','').replace('    ','').replace(',','').replace('"','').replace("'","")
        #if material.replace(' ','').lower().find('fabric') > -1 or material.replace(' ','').lower().find('material') > -1 or material.replace(' ','').lower().find('cotton') > -1 or material.replace(' ','').lower().find('acrylic') > -1 or material.replace(' ','').lower().find('spandex') > -1:
        #    item['material']=material
        #else:
        #    item['material']=""
        #try:Fabric ,Material,cotton,acrylic,spandex
        #    item['image_name'] = [asin.split('/')[5].replace("?_encoding=UTF8&psc=1","")]
        #except:
        #    item['image_name'] = [asin.split('/')[4].replace("?_encoding=UTF8&psc=1","")]
        try:
            item['asin']=asin.split('/')[5].replace("?_encoding=UTF8&psc=1","")
        except:
            item['asin']=asin.split('/')[4].replace("?_encoding=UTF8&psc=1","")
			
        if response.xpath('//*[@id="price-shipping-message"]/i[@class="a-icon a-icon-prime"]').extract():
            item['prime_eligible']="1"
        else:
            item['prime_eligible']="0"
			
        if response.xpath('//img[@id="pantry-badge"]').extract():
            item['prime_pantry']="1"
        else:
            item['prime_pantry']="0"
			
        if response.xpath('//*[@id="addToCart"]/div/div[1]/div/span').extract():
            if "".join(response.xpath('//*[@id="addToCart"]/div/div[1]/div/span/text()').extract()).replace(" ","").lower().find("add-on") > -1:
                item['add_on_item']="1"
            else:
                item['add_on_item']="0"
        else:
            item['add_on_item']="0"
				
        if response.xpath('//*[@id="fresh-merchant-info"]').extract():
            if "".join(response.xpath('//*[@id="fresh-merchant-info"]//text()').extract()).replace(" ","").replace("\n","").replace("\t","").lower().find("amazonfresh") > -1:
                item['amazon_fresh']="1"
            else:
                item['amazon_fresh']="0"
        else:
            item['amazon_fresh']="0"
			
        if response.xpath('//*[@id="snsOption"]/label/span/span[@class="a-size-small a-color-price buybox-price"]//text()').extract():
            item['subscribe_and_save']="".join(response.xpath('//*[@id="snsOption"]/label/span/span[@class="a-size-small a-color-price buybox-price"]//text()').extract()).replace("  ","").replace("\n","").replace("\t","")
        else:
            item['subscribe_and_save']="NA"
				
        if response.xpath('//*[@id="buyNew_dpv2"]/span[@class="a-size-small a-color-price"]//text()').extract():
            item['one_time_purchase']="".join(response.xpath('//*[@id="buyNew_dpv2"]/span[@class="a-size-small a-color-price"]//text()').extract()).replace("  ","").replace("\n","").replace("\t","")
        else:
            item['one_time_purchase']="NA"
				

        #if response.xpath('//*[@id="fast-track-message"]/div//text()').extract():
        #    item['delivery_days']="".join(response.xpath('//*[@id="fast-track-message"]/div//text()').extract()).replace('    ','').replace('\n','').replace('\r','').replace('\t','')
        #else:
        #    item['delivery_days']="NA"
			
        if response.xpath('//*[@id="fast-track-message"]/div//text()').extract():
            delivery_days ="".join(response.xpath('//*[@id="fast-track-message"]/div//text()').extract()).replace('    ','').replace('\n','').replace('\r','').replace('\t','')
            if delivery_days.lower().replace(' ','').find('wantit') > -1:
                item['max_delivery_days']= delivery_days.split('?')[0].split(',')[1]
                item['min_delivery_days']= delivery_days.split('?')[0].split(',')[1]
            elif delivery_days.lower().replace(' ','').find('getit') > -1:
                try:
                    item['min_delivery_days']= delivery_days.split('when')[0].replace('as soon as','assoonas').split('assoonas')[1].split('-')[0]
                    item['max_delivery_days']= delivery_days.split('when')[0].replace('as soon as','assoonas').split('assoonas')[1].split('-')[1]
                except:
                    item['min_delivery_days']="NA"
                    item['max_delivery_days']="NA"
        else:
            item['min_delivery_days']="NA"
            item['max_delivery_days']="NA"
        try:
            pattern = re.compile(r"var dataToReturn = ({.*?});", re.MULTILINE | re.DOTALL)
            locations = response.xpath('//script[contains(., "var dataToReturn")]/text()').re(pattern)[0]
            locations=demjson.decode(locations)
            for key,value in locations["selected_variations"].iteritems():
                if key=="size_name":
                    item['size']=value
                if key=="number_of_items":
                    item['pack_size']=value
                if key=="color_name":
                    item['color']=value
                    if value.lower().replace(" ","").find('pack') > -1 or value.lower().replace(" ","").find('pair') > -1:
                        item['pack_size']=value
                if key=="style_name":
                    item['style']=value
                if key=="flavor_name":
                    item['flavour']=value
                if key=="scent_name":
                    item['scent']=value
        except:
            item['pack_size']=""
            item['size']=""
            item['color']=""
            item['style']=""
            item['flavour']=""
            item['scent']=""
				
        item['title']="".join(title).replace("\n","").replace("\t","").replace("    ","")
        item['category']=">".join(bredcrumb_temp)
        item['category1']=response.meta["category"]
        item['department']=response.meta["department"]
        item['position']=response.meta["position"]
        item['zipcode']=response.meta["zipcode"]
        item['product_rank']=response.meta["position"]
        item['product_url']=response.url
        item['price_per_unit']=priceperunit.replace("\n","").replace("  ","")
        item['timestamp']=str("{:%d/%m/%Y|%H:%M:%S}".format(datetime.datetime.now()))
        #if response.xpath('//div[@id="alternativeOfferEligibilityMessaging_feature_div"]/div'):
        #    print "FOUND PRIME"
        if title: yield item