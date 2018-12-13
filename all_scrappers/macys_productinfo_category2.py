# -*- coding: utf-8 -*-
import scrapy
import json
import re
import demjson
import codecs
import time
#import JSON
#import 
#import pprint
#from sellerspider.items import SellerspiderItem


class MacysItems(scrapy.Item):
    pageurl = scrapy.Field()
    title = scrapy.Field()
    listprice = scrapy.Field()
    finalprice = scrapy.Field()
    url = scrapy.Field()
	
class MacysSpider(scrapy.Spider):
	
    name = "macys_productinfo_category2"
    allowed_domain=[]
    start_urls = ['https://www.macys.com']
    def parse(self, response):
        #urls = 'https://www.kohls.com/catalog/mens-jeans-bottoms-clothing.jsp?CN=Gender:Mens+Product:Jeans+Category:Bottoms+Department:Clothing&cc=mens-TN3.0-S-jeans'
        #urls = "https://www.kohls.com/catalog/womens-coats-jackets-outerwear-clothing.jsp?CN=Gender:Womens+Product:Coats%20%26%20Jackets+Category:Outerwear+Department:Clothing&cc=wms-TN3.0-S-coatsjackets"
        urls = "https://www.macys.com/shop/womens-clothing/womens-jackets?id=120&cm_sp=us_hdr-_-women-_-120_jackets_COL1"
        #req = scrapy.Request(urls, headers={"Accept-Encoding": "gzip,deflate,sdch","Accept-Language": "en-US,en;q=0.8" , "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36" , "Accept": "*/*" ,"Referer": "https://www.amazon.com" , "Connection": "keep-alive" },callback=self.parse1)
        req = scrapy.Request(urls,  callback=self.parse1)
        #req.cookies= {'akacd_www_mosaic=2177452799~rv=90~id':'35602cf2b253070532df8ba1c0b84344', 'klsbrwcki|2254043621655205':'klsbrwcki|2254043621655205', 'AMCVS_F0EF5E09512D2CD20A490D4D%40AdobeOrg':'1', 'btpdb.QF4SXwN.c2lnbmFsIDFzdCBwYXJ0eSBpZA':'NzE0Mjg5NzgwOTU1NzM3NzE5Mg', 's_vi':'[CS]v1|2D17E6A9852A367C-4000010860000479[CE]', 'SignalSpring2016':'A', '__gads':'ID=d985bf1e7e42015f:T=1513082197:S=ALNI_Ma9pohA9T6aayRuQaJwBOmxFa8QFg', 'btpdb.4DPyaxM.dGZjLjU0OTg2OTI':'U0VTU0lPTg', 'btpdb.4DPyaxM.Y3VzdG9tZXIgfCBzaWduYWwgMXN0IHBhcnR5IGlkIC0gc2Vzc2lvbg':'OTAzNzg3MTEzMzI0MDYzMDYzNQ', 'btpdb.4DPyaxM.Y3VzdG9tZXIgfCBzaWduYWwgMXN0IHBhcnR5IGlkIC0gMzY1IGRheXM':'NjI2ODAzMDU0MzYzNjc4NTkzOA', 'IR_gbd':'kohls.com', 'BTT_Collect':'on', '_abck':'332DF9C2A930B7C9CD0038578D4028C217D4328AF86300004ECD2F5AC5C6F855~0~4CMcMlgpRPKyX63BthR/taFb+YRncd2NtgmHzYT20ZA=~-1~-1', 'testVersion':'versionA', 'tfc-l':'%7B%22a%22%3A%7B%22v%22%3A%22c3bb521b-c9fc-4b53-b65d-6f65d3c4d0d4%22%2C%22e%22%3A1513228164%7D%2C%22u%22%3A%7B%22v%22%3A%22V5%7Cunk_82a5c161-23c4-444b-bb84-c884d8a1c37b%7C1575981698%22%2C%22e%22%3A1575981699%7D%2C%22s%22%3A%7B%22v%22%3A%22session.params%3Dadvice%253Dtrue%2526tfpp%253Dkoh%2525252FGeneralSizeAdvice%25253Dtrue%257C1575981698%22%2C%22e%22%3A1575981698%7D%7D', 'tfc-s':'%7B%22v%22%3A%22tfc-fitrec-product%3D6%22%7D', 'CRTOABE':'0', 'AMCV_F0EF5E09512D2CD20A490D4D%40AdobeOrg':'1099438348%7CMCIDTS%7C17515%7CMCMID%7C86211339732481344212921278825520858413%7CMCAAMLH-1513686994%7C3%7CMCAAMB-1513834468%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1513236868s%7CNONE%7CMCAID%7C2D17E6A9852A367C-4000010860000479%7CMCSYNCSOP%7C411-17520%7CvVersion%7C2.1.0', 'kls_p':'false', 's_sq':'%5B%5BB%5D%5D', 'JSESSIONID':'e3JTo47jMBsjjiBV1w7ovcyXk0fuIFN9dUPWMptrZpc_tWIt1iM-!-792164756!-381084835', 'kohls_klbc_cookie':'2575616522.22811.0000', 'kohls_klbd_cookie':'195900076.20480.0000', 'mosaic':'gcpg', 'VisitorId':'2254043621655205', 'CavNV':'4614040071217110251-11127-124697507450-0-9-0-31375-1-3-3', 'TS01ada7dd':'01874bf07ecafc8ae00a2268d798fbfd8895c1c9c351574e1baf988ef1c9e0da60224261fb28a3bf0b793ed1821e5d02ccdbfa5e810a298cf09f6612b0b11784244a83b2aef2b92353293f5c14864b17d6f89d5d6fa8ad78f9a9567839ce872714334800f1', 'TS01105364':'01874bf07ec0589fecb841025ac8429503d38617df51574e1baf988ef1c9e0da60224261fb8135e87148326ee36cba0e82f3a85b4174b33f3309ba5e9e9806945dfc3772bd', 'DCRouteS':'scsp-1513231921', 'productnum':'16', 's_cc':'true', 'staleStorage':'%7B%22count%22%3A1%2C%22persistent_bar_components_json%22%3Anull%2C%22who%22%3A%22https%22%7D', 'mbox':'PC#3dff8d549b4441c8b488a614c970c3c2.28_2#1576476722|session#775acff2f00044b4bc56df830b1217c1#1513233785', 'akavpau_www':'1513232225~id=e2ccdd2d2dd00c445f216aecd740d990', '_ga':'GA1.2.1240642658.1513082196', '_gid':'GA1.2.538153939.1513082199', 'BTT_X0siD':'882904640273488716', 'IR_PI':'1513082199168.ms6pnycg7p', 'IR_5349':'1513231925254%7C385561%7C1513231720588', 'rr_rcs':'eF4FwbERgCAMBdCGyl2-l4QEcAPXgEDuLOzU-X0vpdfPVryPOgg614K6VEwKhS9rLD0sYmz391xzVyawcZbMh5iUDCGAf7jDEl8', 'BTT_WCD_Collect':'off', 'SignalUniversalID':'SrDWSxh0sQ6AobZ0CxuXbJ96l%2BNGQrzwIcnTGBm%2BrCk%3D', 's_stv':'non-search', 'btpdb.4DPyaxM.X2J0X2djbXNfaWQ':'YjU0NmFiY2YtMGMxYy00NDZlLTlkNjItOTJhZGZlNzU4ZDZh', 'RT':'sl=0&ss=1513231920516&tt=0&obo=0&bcn=%2F%2F36fb68c2.akstat.io%2F&sh=&dm=kohls.com&si=24997cab-bd5e-485e-8d10-e4774ba0a047&r=https%3A%2F%2Fwww.kohls.com%2Fcatalog%2Fmens-jeans-bottoms-clothing.jsp%3F304291668d787708a4cbd5b75f2b067f&ul=1513314141080', 'CavSF':',,,,,,,,,0' }
        yield req
        i=2
        while i <=19:
            urlpart="https://www.macys.com/shop/womens-clothing/womens-jackets/Pageindex/"+str(i)+"?id=120"
            #urlpart="&PPP=60&WS="+str(i)
            req = scrapy.Request( urlpart , callback=self.parse1)
            yield req
            time.sleep(.1)
            i += 1

    def parse1(self, response):
        itemlist=response.xpath('//ul[@class="items large-block-grid-3"]/li[@class="productThumbnailItem"]')
        for items in itemlist:
            item=MacysItems()
            titleurl= "https://www.macys.com" + items.xpath('div[@class="productThumbnail"]/div[@class="productDetail"]/div[@class="productDescription"]/a/@href').extract()[0]
            title=items.xpath('div[@class="productThumbnail"]/div[@class="productDetail"]/div[@class="productDescription"]/a/@title').extract()
            finalprice="".join(items.xpath('div[@class="productThumbnail"]/div[@class="productDetail"]/div[@class="productDescription"]/div[@class="priceInfo"]/div[@class="prices"]/div[2]/span[@class="discount"]/text()').extract()).replace(" ","").replace("\n","").replace("\t","").replace("SaleUSD","Sale USD ").replace("NowUSD","Now USD ")
            listprice="".join(items.xpath('div[@class="productThumbnail"]/div[@class="productDetail"]/div[@class="productDescription"]/div[@class="priceInfo"]/div[@class="prices"]/div/span[@class="regular"]/text()').extract()).replace(" ","").replace("\n","").replace("\t","").replace("USD","USD ")
            item['listprice']=listprice
            item['finalprice']= finalprice
            item['url']=titleurl
            item['pageurl']=response.url
            item['title']=" ".join(title)
            yield item