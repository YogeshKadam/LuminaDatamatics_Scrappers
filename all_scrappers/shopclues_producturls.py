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

class ShopcluesItems(scrapy.Item):
    zipCode = scrapy.Field()
    price = scrapy.Field()
    title= scrapy.Field()
    thumbnail= scrapy.Field()
    breadcrumb= scrapy.Field()
    availability= scrapy.Field()
    delivery_days= scrapy.Field()
    response_url= scrapy.Field()
    brand= scrapy.Field()

class ShopcluesSpider(scrapy.Spider):
    imgcount = 1
    name = "shopclues_producturls"
    allowed_domains = ["shopclues.com"]

    start_urls = ["https://www.shopclues.com/computers-monitors.html"]

    """def parse1(self, response):
        zipCodeList=["560070", "575001", "671551"]
        for zipCode in zipCodeList:
            zipcode_request=scrapy.FormRequest('https://www.shopclues.com/setUserzone', headers= {'Origin': 'https://www.shopclues.com' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36' , 'Content-Type': 'application/x-www-form-urlencoded', 'charset':'UTF-8' , 'Accept': '*/*' , 'Referer': 'https://www.shopclues.com/' , 'X-Requested-With': 'XMLHttpRequest' , 'Connection': 'keep-alive'}, formdata={'pincode': zipCode,'target':'pincode_form','local':'pincode'} ,callback=self.parse2, method="POST", meta={'list_of_urls':response.meta['list_of_urls'], 'zipCode':zipCode}, dont_filter=True)
            #zipcode_request.cookies={'_ga':'GA1.2.1920399166.1529909650', '_gid':'GA1.2.553001380.1529909650', 'AMCVS_20CC138653C6496B0A490D45%40AdobeOrg':'1', 'sc_loc':'1111', 'sc_loc_source':'ISP', 'sc_loc_variable':'1111%7Cnorth%7CISP', '_uuId':'0:jitwpcbj:77EFpkdiNXm_iZ6pQpucjsVw5YIed9kI', 'ruserd':'slogn', 'zettata_threshold':'0', 'cto_lwid':'e9fa16e0-2602-4c85-8135-d1188cc1f4cc', 'prp25':'456', 's_cc':'true', 'sess_id':'ZjUxYTcyZmE4MzY1M2FlNTUzY2I4NGVhYmQ3YmI1YjlkNDFkOGNkOThmMDBiMjA0ZTk4MDA5OThlY2Y4NDI3ZQ%3D%3D', '__gads':'ID=1350365bb9e6ac57:T=1529909658:S=ALNI_MZpb8tD9fFN2-8_rUvIwMAoJEiDbA', '_sdsat_isLoggedIn-V':'notloggedin', 'mbox':'PC#f8ce343efdf84bc586bf983b2b9d7b19.22_33#1593160192|session#8206daafc3f44d7984cf5f7a0004b68a#1529917260', 'categoryValues':'Computers:Desktops & Monitors:Monitors', 'AMCV_20CC138653C6496B0A490D45%40AdobeOrg':'1406116232%7CMCIDTS%7C17708%7CMCMID%7C91169419825935539312426312498847079987%7CMCAAMLH-1530520250%7C3%7CMCAAMB-1530520250%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1529916850s%7CNONE%7CMCAID%7C2D3C077B052A2DC0-6000012AE04D0B32%7CMCCIDH%7C1318359124%7CMCSYNCSOP%7C411-17715%7CvVersion%7C2.5.0', 's_ptc':'0.01%5E%5E0.00%5E%5E0.00%5E%5E0.15%5E%5E1.82%5E%5E1.07%5E%5E19.96%5E%5E0.06%5E%5E24.07', 'gpv':'Home%3AComputers%3ADesktops%20%26%20Monitors%3AMonitors%3AAOC%2024%20WIDE%20LED%20E2450SWH%20Monitor', 'gpv1':'Product%20View', 'gpv2':'Computers%3ADesktops%20%26%20Monitors%3AMonitors', 'visit_st':'1', 'gpv3':'%3B5578804%3B1%3B12490.00%3B%3BeVar36%3DComputers%7CeVar55%3D12590%3A12490%3A10709', 's_sq':'%5B%5BB%5D%5D', 's_nr':'1529925113856-Repeat', 's_ev85_n':'%5B%5B%273%27%2C%271529925113867%27%5D%5D'}
            yield zipcode_request"""
			
    def parse1(self, response):
        zipCodeList=["560070", "575001", "671551"]
        #for zipCode in zipCodeList:
        zipcode_request=scrapy.FormRequest('https://www.shopclues.com/setUserzone', headers= {'Origin': 'https://www.shopclues.com' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36' , 'Content-Type': 'application/x-www-form-urlencoded', 'charset':'UTF-8' , 'Accept': '*/*' , 'Referer': 'https://www.shopclues.com/' , 'X-Requested-With': 'XMLHttpRequest' , 'Connection': 'keep-alive'}, formdata={'pincode': zipCodeList[0],'target':'pincode_form','local':zipCodeList[0]} ,callback=self.parse2, method="POST", meta={'url':response.meta['url']}, dont_filter=True)
        zipcode_request.cookies={'_ga':'GA1.2.1920399166.1529909650', '_gid':'GA1.2.553001380.1529909650', 'AMCVS_20CC138653C6496B0A490D45%40AdobeOrg':'1', 'sc_loc':'1111', 'sc_loc_source':'ISP', 'sc_loc_variable':'1111%7Cnorth%7CISP', '_uuId':'0:jitwpcbj:77EFpkdiNXm_iZ6pQpucjsVw5YIed9kI', 'ruserd':'slogn', 'zettata_threshold':'0', 'cto_lwid':'e9fa16e0-2602-4c85-8135-d1188cc1f4cc', 'prp25':'456', 's_cc':'true', 'sess_id':'ZjUxYTcyZmE4MzY1M2FlNTUzY2I4NGVhYmQ3YmI1YjlkNDFkOGNkOThmMDBiMjA0ZTk4MDA5OThlY2Y4NDI3ZQ%3D%3D', '__gads':'ID=1350365bb9e6ac57:T=1529909658:S=ALNI_MZpb8tD9fFN2-8_rUvIwMAoJEiDbA', '_sdsat_isLoggedIn-V':'notloggedin', 'mbox':'PC#f8ce343efdf84bc586bf983b2b9d7b19.22_33#1593160192|session#8206daafc3f44d7984cf5f7a0004b68a#1529917260', 'categoryValues':'Computers:Desktops & Monitors:Monitors', 'AMCV_20CC138653C6496B0A490D45%40AdobeOrg':'1406116232%7CMCIDTS%7C17708%7CMCMID%7C91169419825935539312426312498847079987%7CMCAAMLH-1530520250%7C3%7CMCAAMB-1530520250%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1529916850s%7CNONE%7CMCAID%7C2D3C077B052A2DC0-6000012AE04D0B32%7CMCCIDH%7C1318359124%7CMCSYNCSOP%7C411-17715%7CvVersion%7C2.5.0', 's_ptc':'0.01%5E%5E0.00%5E%5E0.00%5E%5E0.15%5E%5E1.82%5E%5E1.07%5E%5E19.96%5E%5E0.06%5E%5E24.07', 'gpv':'Home%3AComputers%3ADesktops%20%26%20Monitors%3AMonitors%3AAOC%2024%20WIDE%20LED%20E2450SWH%20Monitor', 'gpv1':'Product%20View', 'gpv2':'Computers%3ADesktops%20%26%20Monitors%3AMonitors', 'visit_st':'1', 'gpv3':'%3B5578804%3B1%3B12490.00%3B%3BeVar36%3DComputers%7CeVar55%3D12590%3A12490%3A10709', 's_sq':'%5B%5BB%5D%5D', 's_nr':'1529925113856-Repeat', 's_ev85_n':'%5B%5B%273%27%2C%271529925113867%27%5D%5D'}
        yield zipcode_request
			
    def parse(self, response):
        #print response.xpath('//*[@id="product_list"]/div[3]/div[1]/a[2]/h2/text()').extract()
        """zipCodeList=["560070", "575001", "671551"]
        for zipCode in zipCodeList:
            if response.meta['zipCode']==zipCode:
                counter=0
                url_list=response.xpath('//*[@id="product_list"]/div[@class="row"]/div[@class="column col3"]')
                for urls in url_list:
                #while counter<10:
                    url="https:"+urls.xpath('a[2]/@href').extract()[0]
                    #print url
                    #counter+=1
                    req = scrapy.Request(url, callback=self.parse2, meta={"zipCode":zipCode}, dont_filter=True)
                    yield req
                    time.sleep(.1)"""
					
        
        #for zipCode in zipCodeList:
        """url_list=response.xpath('//*[@id="product_list"]/div[@class="row"]/div[@class="column col3"]')
        counter=0
        list_of_urls=[]
        #for urls in url_list:
        while counter<10:
            url="https:"+url_list[counter].xpath('a[2]/@href').extract()[0]
            #print url
            counter+=1
            zipCodeList=["560070", "575001", "671551"]
            for zipCode in zipCodeList:
                #req = scrapy.Request(url, callback=self.parse1, meta={"zipCode":zipCode}, dont_filter=True)
                #yield req
                #time.sleep(.1)
                list_of_urls.append((url,zipCode))"""
				
        #req = scrapy.Request(url, callback=self.parse1, meta={"list_of_urls":list_of_urls}, dont_filter=True)
        #yield req
		
        url=response.xpath('//*[@id="product_list"]/div[3]/div[1]/a[2]/@href').extract()[0]
        req = scrapy.Request("https:"+url, callback=self.parse1, meta={"url":"https:"+url, "zipCode":"560070"}, dont_filter=True)
        yield req
		
    def parse2(self, response):
        #f1=open("amazon_fresh.html","w")
        #f1.write(response.body)
        #f1.close()
        #print " ".join(response.xpath('//*[@id="fast-track-message"]/div//text()').extract())
        #print " ".join(response.xpath('//*[@id="unifiedLocation_feature_div"]/div/div/span[2]/a/span//text()').extract())
        """for tup in response.meta['list_of_urls']:
            if tup[1]==response.meta['zipCode']:
                req = scrapy.Request(tup[0], callback=self.parse3, meta={"zipCode":response.meta['zipCode']}, dont_filter=True)
                yield req"""
				
        req = scrapy.Request(response.meta['url'], headers= {'Origin': 'https://www.shopclues.com' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36' , 'Content-Type': 'application/x-www-form-urlencoded', 'charset':'UTF-8' , 'Accept': '*/*' , 'Referer': 'https://www.shopclues.com/' , 'X-Requested-With': 'XMLHttpRequest' , 'Connection': 'keep-alive'}, callback=self.parse3, dont_filter=True)
        req.cookies={'_ga':'GA1.2.1920399166.1529909650', '_gid':'GA1.2.553001380.1529909650', 'AMCVS_20CC138653C6496B0A490D45%40AdobeOrg':'1', 'sc_loc':'1111', 'sc_loc_source':'ISP', 'sc_loc_variable':'1111%7Cnorth%7CISP', '_uuId':'0:jitwpcbj:77EFpkdiNXm_iZ6pQpucjsVw5YIed9kI', 'ruserd':'slogn', 'zettata_threshold':'0', 'cto_lwid':'e9fa16e0-2602-4c85-8135-d1188cc1f4cc', 'prp25':'456', 's_cc':'true', 'sess_id':'ZjUxYTcyZmE4MzY1M2FlNTUzY2I4NGVhYmQ3YmI1YjlkNDFkOGNkOThmMDBiMjA0ZTk4MDA5OThlY2Y4NDI3ZQ%3D%3D', '__gads':'ID=1350365bb9e6ac57:T=1529909658:S=ALNI_MZpb8tD9fFN2-8_rUvIwMAoJEiDbA', '_sdsat_isLoggedIn-V':'notloggedin', 'mbox':'PC#f8ce343efdf84bc586bf983b2b9d7b19.22_33#1593160192|session#8206daafc3f44d7984cf5f7a0004b68a#1529917260', 'categoryValues':'Computers:Desktops & Monitors:Monitors', 'AMCV_20CC138653C6496B0A490D45%40AdobeOrg':'1406116232%7CMCIDTS%7C17708%7CMCMID%7C91169419825935539312426312498847079987%7CMCAAMLH-1530520250%7C3%7CMCAAMB-1530520250%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1529916850s%7CNONE%7CMCAID%7C2D3C077B052A2DC0-6000012AE04D0B32%7CMCCIDH%7C1318359124%7CMCSYNCSOP%7C411-17715%7CvVersion%7C2.5.0', 's_ptc':'0.01%5E%5E0.00%5E%5E0.00%5E%5E0.15%5E%5E1.82%5E%5E1.07%5E%5E19.96%5E%5E0.06%5E%5E24.07', 'gpv':'Home%3AComputers%3ADesktops%20%26%20Monitors%3AMonitors%3AAOC%2024%20WIDE%20LED%20E2450SWH%20Monitor', 'gpv1':'Product%20View', 'gpv2':'Computers%3ADesktops%20%26%20Monitors%3AMonitors', 'visit_st':'1', 'gpv3':'%3B5578804%3B1%3B12490.00%3B%3BeVar36%3DComputers%7CeVar55%3D12590%3A12490%3A10709', 's_sq':'%5B%5BB%5D%5D', 's_nr':'1529925113856-Repeat', 's_ev85_n':'%5B%5B%273%27%2C%271529925113867%27%5D%5D'}
        yield req
				
				
				
    def parse3(self, response):
        f1=open("shopclues144.html","w")
        f1.write(response.body)
        f1.close()
        item=ShopcluesItems()
        #item['zipCode']=response.meta["zipCode"]
        item['response_url']=response.url
        title="".join(response.xpath('//*[@id="main_data"]/div[2]/div[2]/h1//text()').extract()).replace('   ','').replace('\r','').replace('\n','').replace('\t','').strip()

        breadcrumb = " > ".join(response.xpath('//*[@id="main_data"]/div[1]/ul/li/a/span//text()').extract()).replace('   ','').replace('\r','').replace('\n','').replace('\t','').strip()+">"+title
        
        brand = response.xpath('//*[@id="main_data"]/div[2]/div[2]/span[3]/a/text()').extract()

        price = "".join(response.xpath('//*[@id="main_data"]/div[2]/div[2]/div[2]/span[@itemprop="lowPrice"]/text()').extract()).replace('  ','').replace('\r','').replace('\n','').replace('\t','')
        """if not price: price = "".join(response.xpath('//*[@id="priceblock_saleprice"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
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
            item['max_price']="""
        #item['brand']=brand1
        if response.xpath('//*[@id="main_data"]/div[4]/div[2]/div[@class="product_ntavailable"]'):
            item['availability']="yes"
            delivery_days= "".join(response.xpath('//*[@id="servicable"]/text()').extract()).replace('  ','').replace('\r','').replace('\n','').replace('\t','')
            print delivery_days
		
        """if response.xpath('//*[@id="fast-track-message"]/div//text()').extract():
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
        if title: yield item"""