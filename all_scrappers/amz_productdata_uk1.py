import scrapy
import urllib

import os
import time
import re
import json
class ComapreItem(scrapy.Item):
    product_title = scrapy.Field()
    #article_no = scrapy.Field()
    price = scrapy.Field()
    brand1 = scrapy.Field()
    brand2 = scrapy.Field()
    ean = scrapy.Field()
    mpn = scrapy.Field()
    model_number = scrapy.Field()
    colour = scrapy.Field()
    #description = scrapy.Field()
    url_page = scrapy.Field()
    breadcrumb  = scrapy.Field()
    base_breadcrumb = scrapy.Field()
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
    seller_name = scrapy.Field()
    product_id = scrapy.Field()
    comp = scrapy.Field()



class amazonSpider(scrapy.Spider):
    imgcount = 1
    name = "amz_productdata_uk1"
    allowed_domains = []

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]  

    def parse(self,response):
        urls_done = [



		]
        urls = [
["1","B000122BS6"],
["2","B000SO2IPI"],
["3","B000U3WHQW"],
["4","B000KJKFZQ"],
["5","B000122SC0"],
["6","B0013FB51E"],
["7","B0013DEJ7S"],
["8","B000KJVA46"],
["9","B000KJMIIS"],
["10","B000TK7VK8"],
["11","B000KJKC6S"],
["12","B000KJKAHE"],
["13","B000QB6HGO"],
["13","B000QB6HGO"],
["13","B000QB6HGO"],
["13","B000QB6HGO"],
["13","B000QB6HGO"],
["14","B000QB2ZWO"],
["15","B000I2DSM2"],
["16","B0013MGRG0"],
["17","B0007OEJGK"],
["18","B000KTD058"],
["19","B000SHQW66"],
["20","B000KT8WW4"],
["21","B000JTMC44"],
["22","B000KJMP04"],
["23","B000MPLG8I"],
["24","B000KJMOZU"],
["25","B0007OEJBK"],
["26","B001394HBK"],
["27","B000KJP08I"],
["28","B000KTBD2A"],
["29","B004GTML5S"],
["30","B00IMDR2IA"],
["31","B0041VQ2IS"],
["32","B0041VYYKG"],
["33","B000KJOM46"],
["34","B000J69ED4"],
["35","B000SO2JMK"],
["36","B00X0VNDE6"],
["39","B0755H943T"],
["48","B00BN8IU64"],
["49","B0012T0OWC"],
["51","B003RY7BY4"],
["52","B0012T0OWC"],
["53","B012ZMLLNK"],
["54","B001AS40I4"],
["55","B0046IZ7QY"],
["56","B005OK36N4"],
["57","B002UCTILI"],
["58","B004HWHYUG"],
["59","B074CL1CVD"],
["60","B00EPFWZTK"],
["63","B00C9A0K5Y"],
["64","B00FO188MM"],
["67","B00BY6SHI6"],
["68","B06XQGH9T6"],
["69","B00BY6SHI6"],
["70","B009R0CMNC"],
["72","B005T9CISE"],
["73","B00J8DJOES"],
["81","B000V7JZO4"],
["83","B002R0RDTM"],
["84","B001D5GYG0"],
["85","B00FPICEL0"],
["88","B00OA4LHIG"],
["90","B005MIAIQQ"],
["91","B003AQTI5E"],
["92","B000JTNIIS"],
["93","B004YJLVZ6"],
["94","B002Q4QHOG"],
["95","B000ZEHAFY"],
["96","B000KTBF6Y"],
["97","B00O4X51BC"],
["99","B005R1KX8G"],
["100","B004V7BA84"],
["101","B00OA4L2JA"],
["102","B000094G30"],
["103","B00JF0H3M4"],
["105","B0002BGCMW"],
["106","B0001D9JCQ"],
["107","B00008A92B"],
["108","B001GV232A"],
["109","B01LX12NDX"],
["113","B01G3V51EE"],
["115","B00GKBL4NA"],
["118","B003Y3TZ6K"],
["119","B001G5VII6"],
["120","B001EQADTC"],
["122","B003AXIVMI"],
["123","B00UX9QV42"],
["129","B0007OEE8S"],
["130","B009L1UN9M"],
["131","B000XQ4FIY"],
["132","B00FO188MM"],
["134","B00BNMTPL4"],
["135","B000KTCGBC"],
["137","B005LZTLQ8"],
["139","B019FFFBC2"],
["140","B000VDHYWI"],
["141","B00ANI7HI2"],
["142","B000MPN7T4"],
["143","B000CDSQE2"],
["147","B00VWQA3TY"],
["148","B0114B113S"],
["149","B00HVXP3Y2"],
["150","B000UW12PU"],
["152","B003K157XG"],
["153","B00A2QIOFU"],
["154","B00HVXOGEK"],
["157","B073NQBS89"],
["161","B0028YRE32"],
["164","B006J33DSS"],
["165","B0068QUH1M"],
["166","B00J8DJM0O"],
["169","B00IJRSLVQ"],
["172","B002GH37YG"],
["173","B008ERG1S6"],
["175","B004G6KD56"],
["179","B0082X8JNM"],
["182","B0012QCIUG"],
["183","B00FXY3L1S"],
["190","B000A6DJKW"],
["193","B008F5RX4I"],
["194","B00BFW9QES"],
["196","B005MI6ITW"],
["198","B001DXKGKM"],
["199","B00KBSB24O"],
["200","B0016AM9KM"],
["202","B002ZDFPL4"],
["203","B000GL19FS"],
["205","B00M1UAII6"],
["206","B0090UFNR6"],
["207","B00IHOP6C8"],
["209","B00006BBKN"],
["210","B002652QWC"],
["211","B00OA4LIHQ"],
["213","B00BX9K09S"],
["214","B00MA5OWHU"],
["216","B00BX9K09S"],
["217","B008L5GNUM"],
["219","B00DU5BIU8"],
["222","B00L27OLEG"],
["224","B002ZDFPL4"],
["225","B00JXDTZPQ"],
["226","B017C04RO0"],
["227","B00CPGVE6Q"],
["228","B004UTT422"],
["229","B000O6ISOU"],
["231","B003P7X38Q"],
["232","B00006B8NO"],
["236","B003UL1RGC"],
["240","B00DU5BI8K"],
["241","B0753CPLFJ"],
["242","B00NQGP42Y"],
["243","B00D9IBTPA"],
["244","B00NQFVEKQ"],
["246","B01LSJLQJA"],
["247","B005ORCAMA"],
["248","B00DU5AVDS"],
["249","B00BFXPBQY"],
["251","B0085MPGDG"],
["252","B00LPHBF60"],
["253","B016A509WM"],
["254","B00MGP1YE8"],
["255","B003SUGEG8"],
["256","B00P736UEU"],
["258","B0031SXPJ6"],
["259","B00F3J2ITY"],
["262","B003U8BL8Y"],
["264","B006T02YRM"],
["265","B00ANS5T5K"],
["266","B0028YOKA2"],
["267","B00IJRSLVQ"],
["270","B00096J3TY"],
["271","B019LBHADS"],
["274","B00EV0N62O"],
["277","B00F35N0VI"],
["290","B01N39HOPA"],
["292","B000KJOJAI"],
["294","B00LMXBOP4"],
["296","B00BTK823W"],
["297","B00552K0GM"],
["300","B000KJPBGE"],
["301","B01N39HQ58"],
["303","B000KTBFZ0"],
["305","B00E91Z2W2"],
["307","B017I90LYA"],
["309","B00LELLQZ2"],
["310","B00BY9XXXC"],
["311","B000P5UCEO"],
["312","B007G97D9O"],
["315","B00BLGJJFY"],
["317","B00BUGLFX4"],
["318","B00WB2OXUI"],
["319","B00VKZ35ZQ"],
["320","B000KT7FWM"],
["321","B002LXT852"],
["322","B01GU2P44S"],
["323","B0109ZG1DU"],
["324","B00096J3TY"],
["329","B00NQ0YUKW"],
["330","B01ARRHT4U"],
["331","B003U8BL8Y"],
["332","B00P10SZYC"],
["333","B002KKM5J2"],
["334","B002TVXOP6"],
["335","B071CPZLJP"],
["337","B00RBRWXM8"],
["341","B01M8HV1WL"],
["343","B01L2BGIME"],
["344","B011GVHFB8"],
["345","B0041IQK3I"],
["346","B00TS3KCJO"],
["347","B01N7JFTMV"],
["348","B00312LYWM"],
["349","B00BQC75JU"],
["350","B00ABOBRWU"],
["352","B00138Y9QO"],
["353","B001IMGRAQ"],
["354","B000ONORY8"],
["355","B01N907Z3V"],
["356","B00L9UG5IQ"],
["359","B00FG9UIZ2"],
["360","B00OINUMQW"],
["361","B01B7PL6PE"],
["362","B001JKG4S2"],
["363","B0152JGTPS"],
["365","B00J8MQ032"],
["366","B00AZKNPZC"],
["369","B003KW0TBU"],
["370","B004FQPMYO"],
["371","B00OLEO23C"],
["372","B0013F98JK"],
["374","B00LF10KTO"],
["375","B015DRKQ3U"],
["376","LGXD00033BL"],
["378","B00NDRH6TK"],
["384","B007XDYKE4"],
["385","B00ENAMNKI"],
["386","B00GGNLGDK"],
["387","B00MDG4CY4"],
["388","B00NK332GS"],
["390","B00A6N60I2"],
["393","B001EQADU6"],
["394","B009L1UN9M"],
["396","B00DOPOAUY"],
["397","B00KOUDJYA"],
["398","B011G3WQ1A"],
["399","B00HVXP0GI"],
["405","B004G8ZYQW"],
["407","B000TK3AGC"],
["408","B005ORCAMA"],
["414","B011CTJZ9Y"],
["416","B000KPL8H4"],
["418","B01DZXWVE6"],
["420","B00IL18FOI"],
["422","B000KJR1A8"],
["439","B06XCJN5Y9"],
["474","B008REPG6O"],
["492","B003A5YKLM"],
["493","B072PWLMYX"],
["494","B01N7VVYN0"],
["497","B0030MBZA4"],
["498","B000X2B5MW"],
["1_c","B00PUJLUZU"],
["2_c","B00J9E216Y"],
["3_c","B00VF2CDAC"],
["4_c","B00XPIZS7Y"],
["5_c","B00XPJ16PG"],
["6_c","B00DOVCEWO"],
["7_c","B01N047TPW"],
["9_c","B01ABXS42Q"],
["10_c","B00M6B1140"],
["11_c","B01MRV69M4"],
["13_c","B00BS9AIA4"],
["14_c","B004ODAEDW"],
["15_c","B000WL0Z9I"],
["20_c","B004OHKX6G"],
["21_c","B00E7T166C"],
["26_c","B003A24KW4"],
["31_c","B002K8V7GG"],
["32_c","B000MQHFPK"],
["33_c","B004LXO4M2"],
["34_c","B000JTIAI6"],
["35_c","B00OLTFGP0"],
["48_c","B0195EOP3E"],
["49_c","B007E6GGQU"],
["52_c","B007E6GGQU"],
["55_c","B00UAVJRTE"],
["58_c","B0747PY954"],
["59_c","B007RN9SVA"],
["72_c","B0747PBNJY"],
["88_c","B004VDKYWG"],
["90_c","B007M7W7GY"],
["92_c","B01KO83PBI"],
["94_c","B01CTIOEJS"],
["95_c","B0719K526N"],
["99_c","B019C7BT06"],
["100_c","B00364NNU6"],
["101_c","B015FSLMA8"],
["102_c","B01H2S2M7Q"],
["103_c","B010NMELD6"],
["106_c","B000ZEIEP4"],
["107_c","B00R359OVQ"],
["108_c","B01LGITGY0"],
["109_c","B000O1ATDS"],
["113_c","B003OB925G"],
["115_c","B01JS7U3GQ"],
["118_c","B004C22FQ4"],
["119_c","B00QEFUCI0"],
["120_c","B001552G10"],
["129_c","B0007OEE2O"],
["130_c","B002UUY7PM"],
["147_c","B00IZQBF0A"],
["152_c","B01MRSVRBA"],
["153_c","B00A8BEQPQ"],
["164_c","B0059586MU"],
["173_c","B00B1C4EEY"],
["178_c","B0746D376K"],
["193_c","B00TK0WZ0E"],
["194_c","B00PGWQLPK"],
["203_c","B016DM0IOG"],
["206_c","B06XGNCCSV"],
["210_c","B001OOYS5E"],
["211_c","B06XWSGDHP"],
["216_c","B00HVYBU6Q"],
["217_c","B00BIZ94TY"],
["219_c","B010NMERA8"],
["222_c","B01LXKF64I"],
["225_c","B01EFWG296"],
["226_c","B00H2FLPD2"],
["227_c","B00EXOGH0Q"],
["228_c","B072QC24V2"],
["232_c","B002UUY7PM"],
["240_c","B010NMELD6"],
["243_c","B01ACQX4OU"],
["246_c","B072QC24V2"],
["248_c","B00CQ35HBQ"],
["249_c","B074XC6TD9"],
["252_c","B01BBL6VOU"],
["253_c","B017BACHKC"],
["256_c","B0722C3SRC"],
["258_c","B004FHBTMM"],
["262_c","B01EDDFVC6"],
["263_c","B000O6ISOU"],
["266_c","B000ONQBFQ"],
["270_c","B00EMGEEFA"],
["274_c","B01KO3XSS8"],
["277_c","B00P0UDSN6"],
["292_c","B01DLEOVYM"],
["294_c","B01GLXU1U8"],
["297_c","B01CHZQMY8"],
["300_c","B01EITKQ16"],
["305_c","B01KF4NS2M"],
["309_c","B00JMXQ5SM"],
["311_c","B009ZA6CDU"],
["317_c","B017JE8T70"],
["318_c","B019D0EMSS"],
["319_c","B000SHOQH8"],
["320_c","B00C68W430"],
["321_c","B015YWJTOG"],
["322_c","B000J6F1LS"],
["324_c","B00OLTI6HA"],
["331_c","B01EDDFVC6"],
["332_c","B071G2JQH4"],
["333_c","B0755512NF"],
["334_c","B01G037KI0"],
["341_c","B00NGWLIIM"],
["343_c","B00HCJ98DM"],
["345_c","B01I1AMIZU"],
["348_c","B00FBFI53S"],
["349_c","B06Y4S24TC"],
["352_c","B000WGWRDK"],
["353_c","B00A30FFRK"],
["355_c","B07212NT46"],
["356_c","B00JS545H2"],
["363_c","B00U2ZZX5A"],
["371_c","B01N8QKDNL"],
["372_c","B00GPZO75I"],
["374_c","B01K8A29CS"],
["378_c","B00O0WFFSQ"],
["384_c","B000H9HKH0"],
["385_c","B01IN2MGIA"],
["386_c","B07214QRNZ"],
["387_c","B01MSW58S2"],
["390_c","B00TGPSHI2"],
["393_c","B00861WAR6"],
["394_c","B073TSZDZQ"],
["396_c","B001552G10"],
["407_c","B00387J3EG"],
["420_c","B00MMYVKBA"],
["422_c","B004FQYB50"]
]
        for url in urls:
            try:
                req = scrapy.Request( 'https://www.amazon.co.uk/dp/' +url[1] +'/' , headers={ 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Cache-Control': 'max-age=0' },callback=self.parse6)
                req.meta['item_id']=url[1]
                req.meta['product_id']=url[0]
                req.cookies = { 'x-wl-uid':'1y8ltVLwKU/L4uHVRT4wcyu32QxGmsLap3PS10lHQ8I4lHwvcV3mdItRxlTQQbVCy6hcltYxKLMM=', 's_nr':'1498670542228-New', 's_vnum':'1930670542228%26vn%3D1', 's_dslv':'1498670542232','amznacsleftnav-ac35e287-d67e-4607-a950-5d9ffd0c2ca9':'1', 'x-amz-captcha-1':'1499054178128406', 'x-amz-captcha-2':'f44Jo5PiWFZO/J2o05Otig==', 'session-token':'jmS4MZ+87cNOfytK07tpUCEGti+GXuHdZ0oZyPtYqY7t0jdykH+Ub7kXBm+uyaqfsw9okzU8c7KFuF577LQSOEOVzXGU6Ky1xqdZjaFUDfW6H5HbFByM0YxhwaB/i3TdgWzWRV7hvGo3qygmjkrIJ3ESRIOOM6YB4EJWL65CQUTq+Cp4ORjO1XQaGvfPERmPKJ8tKI4p77AQ0pKocXEOtyFku2Vp9HJzTUI9LN4bZVnXVtkV/ra/ElaVLqz1HqDJ', 'csm-hit':'s-GZBERSD0R10VXC0HBQZ6|1500714195597', 'session-id-time':'2082754801l', 'session-id':'261-2325209-6209161', 'ubid-acbde':'259-4651163-1859124' }

                if url[1] not in urls_done: 
                    yield req
                    time.sleep(.1)
            except: raise


    def parse6(self,response):
        #print response.url
        #print 'https://www.amazon.co.uk/gp/offer-listing/' + response.url.split("dp/")[1] + '/ref=dp_olp_new?ie=UTF8&condition=new'
        #print response.body
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
			
            try: price = "".join(response.xpath('//*[@id="priceblock_ourprice"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            except: raise
            ship_price = "".join(response.xpath('//*[@id="ourprice_shippingmessage"]/span/b/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            if not ship_price :  ship_price =  "".join(response.xpath('//*[@id="price-shipping-message"]/span/b/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            if not ship_price :  ship_price =  "".join(response.xpath('//span[@id="price-shipping-message"]//text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            if not ship_price :  ship_price =  "".join(response.xpath('//*[@id="ourprice_shippingmessage"]//text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
          
			
            seller_name = " ".join(response.xpath('//*[@id="merchant-info"]/a//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not seller_name: seller_name = " ".join(response.xpath('//*[@id="merchant-info"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
			
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
		
                                                        
        try:
            count = "".join(response.xpath('//*[@id="olp_feature_div"]/div/span[1]/a/text()').extract()).strip()
            star_rating  = "".join(response.xpath('//*[@id="acrPopover"]/span[1]/a/i[1]/span/text()').extract()).replace('/n','').strip()
            num_review = "".join(response.xpath('//*[@id="acrCustomerReviewText"]/text()').extract()).replace('/n','').strip()
            question_answered = "".join(response.xpath('//*[@id="askATFLink"]/span/text()').extract()).replace('/n','').strip()
            item = ComapreItem()
            item['star_rating'] = star_rating
            item['num_review'] = num_review
            item['question_answered'] = question_answered
            item['product_title'] = title
            item['mpn'] = "'" +item_no+"'"
            item['attr_dict'] = json.dumps(attr_dict)
            item['brand1'] = brand1
            item['brand2'] = brand2
            item['response_url']=response.url
            item['ASIN']=response.meta['item_id']
            if response.meta['product_id'].find('_') > -1:
                item['comp']='Alt'
                item['product_id']=response.meta['product_id'].split('_')[0]
            else: 
                item['comp']=''
                item['product_id']=response.meta['product_id']

            item['breadcrumb']="/".join(bredcrumb_temp)
            item['seller_count'] = count
            item['ship_price'] = ship_price
            item['price'] = price
            item['seller_name'] = seller_name
            item['ean'] = ean
            #print item
            yield item
        except:
            raise

