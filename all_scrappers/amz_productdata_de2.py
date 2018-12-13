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
    ship_price1 = scrapy.Field()
    ship_price2 = scrapy.Field()
    seller_name = scrapy.Field()
    product_id = scrapy.Field()
    comp = scrapy.Field()



class amazonSpider(scrapy.Spider):
    imgcount = 1
    name = "amz_productdata_de2"
    allowed_domains = []

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]  

    def parse(self,response):
        urls_done = [

		]
        urls = [
["1","B000122BS6"],
["2","0B000SO2IPI"],
["3","B000U3WHQW"],
["4","B00X0VNDPU"],
["5","B000122SC0"],
["6","B0013FB51E"],
["7","B0013DEJ7S"],
["8","B00IHJZRWC"],
["9","B000KJMIIS"],
["10","B000TK7VK8"],
["11","B000KJKC6S"],
["12","B000KJKAHE"],
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
["36","B000KJMBTY"],
["39","B073W2BJ7X"],
["40","B074N8NK5F"],
["43","B073BJM392"],
["44","B073BJW6KP"],
["45","B073BJM392"],
["46","B073BMR77M"],
["47","B073BKL4WH"],
["48","B00SPC0LZ4"],
["49","B00G6P8Q5Y"],
["50","B00FO4NLXK"],
["51","B003RY7BY4"],
["52","B009KYYG9I"],
["53","B012ZMLLNK"],
["54","B001AS40I4"],
["55","B0046IZ7QY"],
["56","B005OK36N4"],
["57","B002UCTILI"],
["58","B007A0EXAQ"],
["59","B00AS5ZZCA"],
["60","B00EPFWZTK"],
["63","B001IVN0KC"],
["64","B00FO188MM"],
["66","B00AS5ZZCA"],
["67","B0092KVZ1W"],
["68","B000OZU6WS"],
["69","B00BY6SHI6"],
["70","B00ASIOV4A"],
["72","B005T9CISE"],
["73","B00GD6O9AW"],
["75","B002UTBSLY"],
["76","B000V4CQ5W"],
["77","B00MI8L5JC"],
["78","B000V4CQ5W"],
["79","B017K4QMVE"],
["80","B0018NOB12"],
["81","B00WMSLSFY"],
["82","B003A6B0IM"],
["83","B0046YIR56"],
["84","B001D5GYG0"],
["85","B01D2X5LY6"],
["88","B00OA4LHIG"],
["90","B005MIAIQQ"],
["91","B001Z9FDSE"],
["92","B000JTNIIS"],
["93","B004YJLVZ6"],
["94","B0047RYXBE"],
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
["108","B00VXY2HMG"],
["109","B00AEORN8Y"],
["112","B004HPNZ7Y"],
["113","B001ERA0BM"],
["115","B00GKBL4NA"],
["117","B001MS606W"],
["118","B00426UJMW"],
["119","B001G5VII6"],
["120","B0748D7B75"],
["122","B001JK8412"],
["123","B00UX9QV42"],
["124","B01BRKRDG0"],
["125","B00GOY43G8"],
["126","B00CKKOOQE"],
["128","B0046YLEJ2"],
["129","B0007OEE8S"],
["130","B009L1UN9M"],
["131","B000XQ4FIY"],
["132","B00FO188MM"],
["135","B000KT8TIQ"],
["137","B005LZTLQ8"],
["139","B007VGEO6W"],
["140","B000VDHYWI"],
["141","B00ANI7HI2"],
["142","B000MPN7T4"],
["143","B000CDSQE2"],
["144","B003Z7E98O"],
["145","B002UV3EVO"],
["147","B00J3U4DUQ"],
["148","B0114B113S"],
["149","B00HVXP3Y2"],
["150","B000UW12PU"],
["152","B003K157XG"],
["153","B00A2QIOFU"],
["154","B00HVXOGEK"],
["157","B01DPMWT1W"],
["159","B00QVBCT3I"],
["161","B0028YRAK4"],
["164","B006J33DSS"],
["165","B0007M69KQ"],
["166","B00N6ZJCWI"],
["169","B00M26NKUC"],
["171","B0733DYM12"],
["172","B002GH37YG"],
["173","B008ERG1S6"],
["175","B00B7ZBYUM"],
["176","B01G5IUNAW"],
["177","B000R27HQ6"],
["178","B00HZREDTK"],
["179","B0082X8JNM"],
["180","B01J629SS2"],
["182","B0012QCIUG"],
["183","B00FXY3L1S"],
["186","B00JOLG1MW"],
["190","B000A6DJKW"],
["193","6EP13341LB00"],
["194","B00BFW9QES"],
["195","B000UW8YVU"],
["196","B005MI6ITW"],
["197","B016MQ5Q04"],
["198","B00AVYYRZY"],
["199","B007IEDERW"],
["200","B00T7JIJKS"],
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
["222","B00GAS3RU6"],
["224","B002ZDFPL4"],
["225","B00JXDTZPQ"],
["226","B00FC1V61E"],
["227","B00CPGVE6Q"],
["228","B004UTT422"],
["229","B000RAGOQM"],
["231","B003P7X38Q"],
["232","B00006B8NO"],
["236","B003UL1RGC"],
["240","B00DU5BI8K"],
["241","B01F6XO6BE"],
["242","B00NGOCJ74"],
["243","B00D9IBTPA"],
["244","B00NGOCZ3C"],
["246","B01LSJLQJA"],
["247","B005ORCAMA"],
["248","B00DU5AVDS"],
["249","B00BFXPBQY"],
["251","B0085MPGDG"],
["252","B00LPHBF60"],
["253","B00L27SCQE"],
["254","B00LH010L0"],
["255","B00GJU4YKW"],
["256","B00P736UEU"],
["258","B00RD3X676"],
["259","B00F8JHGXM"],
["262","B003U8BL8Y"],
["263","B000QWICZW"],
["264","B006T02YRM"],
["265","B00ANS5T5K"],
["266","B0028YOKA2"],
["267","B00IJRSLVQ"],
["270","B00096J3TY"],
["271","B019LBHADS"],
["272","B00W5EA5EK"],
["274","B06XYPD37T"],
["277","B00F35N0VI"],
["280","B00W5EA5EK"],
["287","B004IO5BMQ"],
["290","B000WL3NIS"],
["292","B000KJOJAI"],
["294","B00LMXBOP4"],
["296","B00BTK823W"],
["297","B0052EH8OA"],
["300","B000KJPBGE"],
["301","B001QPL49E"],
["303","B000KTBFZ0"],
["305","B00E91Z2W2"],
["307","B01N2KJGDS"],
["308","B00W5EA5EK"],
["309","B00LELLQZ2"],
["310","B00CSQFG12"],
["311","B000093OW2"],
["312","B007G97D9O"],
["315","B00BERCLI2"],
["317","B00BUGLFX4"],
["318","B00WB2OXUI"],
["319","B00VKZ35ZQ"],
["320","B000KT7FWM"],
["321","B002MUMF2M"],
["322","B008UQHF0Y"],
["323","B00YOJ9SZ6"],
["324","B00096J3TY"],
["325","B01H36SCQC"],
["326","B01JMW6Z28"],
["329","B00NGOCP64"],
["330","B00UVHMGM2"],
["331","B003U8BL8Y"],
["332","B00W4YMLG6"],
["333","B002KKM5J2"],
["334","B002TVXOP6"],
["335","B01CCYLXUM"],
["337","B013BV5JOQ"],
["341","B01M8HV1WL"],
["343","B00G4R0R8I"],
["344","B00W5EA5EK"],
["345","B0041IQK3I"],
["346","B00OVT2UK4"],
["347","B00H3ZENIU"],
["348","B00312LYWM"],
["349","B00BQC75JU"],
["350","B00ABOBRWU"],
["352","B0076IYLUE"],
["353","B001IMGRAQ"],
["354","B000ONORY8"],
["355","B007NUV7MA"],
["356","B00L9UG5IQ"],
["359","B00F8JHE16"],
["360","B007L3CFRU"],
["361","B00MRH1J6I"],
["362","B016L192U0"],
["363","B00Y37VM94"],
["365","B00JA0ZWOU"],
["366","B00AZKNPZC"],
["369","B003KW0TBU"],
["370","B0050CGYAS"],
["371","B00OLEO23C"],
["372","B0013F98JK"],
["373","B00W5EA5EK"],
["374","B00LF10KTO"],
["375","B015A0THUI"],
["376","B00ODRSN0A"],
["378","B00HWHW05C"],
["379","B0107Y6UMA"],
["384","B007XDYKE4"],
["385","B00ENAMNKI"],
["386","B00GGNLGDK"],
["387","B00MDG4CY4"],
["388","B00NGOD2OI"],
["390","B008968MZW"],
["393","B001EQADTC"],
["394","B009L1UN9M"],
["396","B00DOPOAUY"],
["397","B0045TE0IU"],
["398","B00O1WJ6QW"],
["399","B00HVXP0GI"],
["405","B004G8ZYQW"],
["407","B000TK3AGC"],
["408","B005ORCAMA"],
["414","B01N294KL1"],
["416","B00J3RT1Z6"],
["417","B000TKB9WE"],
["418","B01DZXWVE6"],
["420","B00XWDXR3Y"],
["421","B003NQJXI8"],
["422","B000KJR1A8"],
["439","B06XCJN5Y9"],
["442","B01054IHT6"],
["468","B01BQKFL3I"],
["471","B01MQFU137"],
["474","B008REPG6O"],
["476","B01DC0FV8K"],
["492","B003A5YKLM"],
["493","B072PWLMYX"],
["494","B01N7VVYN0"],
["497","B0030MBZA4"],
["498","B000X2B5MW"],
["1_c","B00304ROY8"],
["2_c","B000I5SAUO"],
["3_c","B0745KTPLP"],
["10_c","B000WL50IO"],
["11_c","B000KJKC6S"],
["12_c","B00MGR181U"],
["13_c","B00NSLBDAY"],
["14_c","B00EZ4O2FG"],
["15_c","B00JQYCIWO"],
["16_c","B002SQE834"],
["17_c","B0007OEJFG"],
["18_c","B000KJRE0K"],
["21_c","B00211U8TY"],
["23_c","B00N5U8ET6"],
["24_c","B000KJMP04"],
["25_c","B00X0VQ17M"],
["26_c","B00TY7CCOM"],
["27_c","B000NM4KRE"],
["30_c","B000SHT4NY"],
["31_c","B000KJMJZ0"],
["32_c","B000KJMJZ0"],
["33_c","B00BXY54T4"],
["35_c","B000YIWL4G"],
["36_c","B00X0VNDE6"],
["48_c","B00AO18M8M"],
["49_c","B0714MLWZH"],
["52_c","B06XQ3KF5N"],
["54_c","B00XVUYWQ4"],
["55_c","B008CK51OA"],
["58_c","B009I6SE4G"],
["60_c","B00BY6SHI6"],
["63_c","B002P8JAM4"],
["64_c","B0719VKRWK"],
["68_c","B009FUZ30S"],
["70_c","B00ASIQLSE"],
["72_c","B008OWBE56"],
["73_c","B008TLWQOK"],
["77_c","B00MI8OV1Q"],
["83_c","B002R0RDTM"],
["84_c","B01LN5EF06"],
["88_c","B00EE3MF48"],
["90_c","B007M7R4FS"],
["91_c","B003Z7FJBA"],
["93_c","B06XBFKFJC"],
["94_c","B00LRYUJQS"],
["95_c","B0743D343S"],
["97_c","B01EWVMWO4"],
["99_c","B01CCS5O94"],
["100_c","B00364NNU6"],
["101_c","B00I1HNKYM"],
["103_c","B00CQ35GYE"],
["106_c","B005I4P4IQ"],
["107_c","B00J09IRY8"],
["108_c","B00OJBEQBA"],
["109_c","B00K1BII34"],
["113_c","B00IIBIX4S"],
["115_c","B01L250IVW"],
["118_c","B06XZNZF1T"],
["119_c","B0072IIRXU"],
["122_c","B0002PQ5F2"],
["125_c","B01IHR6LLE"],
["129_c","B0007OEE2O"],
["130_c","B072V93NG3"],
["135_c","B00D2O2LXU"],
["137_c","B06X9BW1DY"],
["141_c","B01LF5XE4M"],
["164_c","B00SGTIO5K"],
["169_c","B00BQ7H8GK"],
["173_c","B008ERG1P4"],
["175_c","B004G6COGW"],
["177_c","B0020OWP2A"],
["178_c","B073WQ6GHV"],
["179_c","B0082X8JAK"],
["193_c","B073GP4WK6"],
["198_c","B00977G4UC"],
["203_c","B01F7HY4U2"],
["205_c","B00LGDNQDI"],
["206_c","B008FXHKVQ"],
["210_c","B003XDUCAO"],
["211_c","B00HGGLC9O"],
["216_c","B00BB9SHJK"],
["217_c","B00KMNY2Z4"],
["219_c","B010NMERA8"],
["224_c","B0046BGUJY"],
["225_c","B01EFWG296"],
["227_c","B00GT3KCS2"],
["228_c","B01IN2MGIA"],
["229_c","B000WL7K8M"],
["232_c","B003TNWROW"],
["236_c","B0151GJYNQ"],
["240_c","B00F45U21S"],
["243_c","B00OK99LH0"],
["246_c","B00Y85H8Z8"],
["247_c","B0718YWK6S"],
["248_c","B006YG8X9Y"],
["249_c","B06XR21B17"],
["251_c","B0034JWE3U"],
["252_c","B017DH68F8"],
["253_c","B01DNUI758"],
["256_c","B00TIJMF84"],
["258_c","B000H8RXKA"],
["262_c","B01EDDFVC6"],
["263_c","B000O6ISOU"],
["264_c","B004DGJOQ8"],
["265_c","B00BG23GSE"],
["270_c","B002R9J62A"],
["274_c","B00EDB44PO"],
["277_c","B01MU1FZVF"],
["287_c","B01B1QBK78"],
["292_c","B0012SCT4Y"],
["294_c","B0093HMLJ4"],
["296_c","B005HWEYN0"],
["297_c","B00QGTFOZK"],
["300_c","B002TLN51O"],
["303_c","B00G9XNDF6"],
["305_c","B00SKZ87DE"],
["309_c","B00LFNRXTC"],
["311_c","B002LYROL6"],
["312_c","B010CTD5UU"],
["317_c","B008SN3KMQ"],
["318_c","B0081Z2H0W"],
["319_c","B00VKZ36FK"],
["320_c","B000MQHH1C"],
["321_c","B015YWJTOG"],
["322_c","B000J6F1LS"],
["324_c","B003WU6KFO"],
["331_c","B00KGTTA9C"],
["332_c","B071G2JQH4"],
["333_c","B015U51ONG"],
["334_c","B00FJ1B2YI"],
["341_c","B00NGWR6MO"],
["343_c","B01M8GIMZR"],
["345_c","B00UCJ6C7O"],
["346_c","B00TS3KCJO"],
["348_c","B00FBFI53S"],
["349_c","B071V489KH"],
["352_c","B000KTCMDO"],
["353_c","B01BKGKSG8"],
["355_c","B007MHMNFE"],
["356_c","B00PHVDXT2"],
["363_c","B014NH551E"],
["366_c","B001AXN562"],
["370_c","B000KJOAZC"],
["371_c","B015FY325A"],
["372_c","B01CS3XTEK"],
["374_c","B00P73B1E4"],
["376_c","B06XSGJTV3"],
["378_c","B009L1UX9W"],
["384_c","B00DUGZFWY"],
["385_c","B00QN8Z89G"],
["386_c","B0725PSP9N"],
["387_c","B00I8R8YYQ"],
["390_c","B01LYIFQH8"],
["393_c","B00D142QN6"],
["394_c","B071W9FFLB"],
["396_c","B001552G10"],
["417_c","B000NM4KRE"],

]
        for url in urls:
            try:
                req = scrapy.Request( 'https://www.amazon.de/dp/' +url[1] +'/' , headers={ 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Cache-Control': 'max-age=0' },callback=self.parse6)
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
            ship_price1 = "".join(response.xpath('//*[@id="ourprice_shippingmessage"]/span/b/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            if not ship_price1 :  ship_price1 =  "".join(response.xpath('//*[@id="price-shipping-message"]/span/b/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            if not ship_price1 :  ship_price1 =  "".join(response.xpath('//span[@id="price-shipping-message"]//text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            if not ship_price1 :  ship_price1 =  "".join(response.xpath('//*[@id="ourprice_shippingmessage"]//text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
            ship_price2 = "".join(response.xpath('//*[@id="soldByThirdParty"]/span[2]/text()').extract()).replace("   ",'').replace("\n",'').replace('\t','').strip()
			
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
            if not brand2:  brand2 =result_dict.get('Marke','').strip() 

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
            item['ship_price1'] = ship_price1
            item['ship_price2'] = ship_price2
            item['price'] = price
            item['seller_name'] = seller_name
            item['ean'] = ean
            #print item
            yield item
        except:
            raise

