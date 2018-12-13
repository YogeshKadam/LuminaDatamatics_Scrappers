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

class BigbasketItems(scrapy.Item):
    product_variants = scrapy.Field()
    price = scrapy.Field()
    title= scrapy.Field()
    thumbnail= scrapy.Field()
    thumbnail_name= scrapy.Field()
    breadcrumb= scrapy.Field()
    location= scrapy.Field()
    delivery_days= scrapy.Field()
    response_url= scrapy.Field()
    brand= scrapy.Field()
    item_id= scrapy.Field()

class BigbasketSpider(scrapy.Spider):
    imgcount = 1
    name = "bigbasket_productinfo_part6"
    allowed_domains = ["shopclues.com"]

    start_urls = ["https://www.shopclues.com/computers-monitors.html"]
			
    def parse(self, response):
        #city_info={'Chennai':['6','85'], 'Coimbatore':['12','99']}
        city_info={'Bangalore':['6','85','94900084'], 'Coimbatore':['12','99','95729826'], 'Gurgaon':['18','99','88779842']}
        for key,value in city_info.iteritems():
            #urlpattern="https://www.bigbasket.com/auth/get_menu/?city_id="+id
            #urlpattern="https://www.bigbasket.com/auth/get_footer/?city_id="+id
            #urlpattern="https://www.bigbasket.com/pd/30007659/elite-rusk-milk-65-gm/"
            #urlpattern="https://www.bigbasket.com/pd/40019371/bournvita-pro-health-drink-chocolate-750-gm-pouch/"
            #urlpattern="https://www.bigbasket.com/"
            urlpattern="https://www.bigbasket.com/custompage/display?url=b01eee88-e6bc-410e-993c-dedd012cf04b&cai="+value[2]+"vs&isB2B=False"
            form_data={'url': 'e483caf9-1259-4c8b-89db-c3b00d0870e2', 'cai':value[2], 'isB2B':'False'}
            #urlpattern="https://www.bigbasket.com/auth/get_page_data/?cai="+value[1]
            #urlpattern="https://www.bigbasket.com/pd/40018400/elina-long-grain-rice-1-kg/?nc=as&q=eli"
            #zipcode_request=scrapy.FormRequest(urlpattern, headers= {'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36' , 'Accept': 'application/json, text/plain, */*' , 'Referer': 'https://www.bigbasket.com/' , 'X-Requested-With': 'XMLHttpRequest' , 'Connection': 'keep-alive' , 'X-CSRFToken': 'w5XXUqsj8RR3PQ5OYDdsHwV6JDc314o7fLYAq8YpupjfhUu5CNpVW0bPho1o6XHU'} ,formdata=form_data, callback=self.parse1, method="POST", dont_filter=True)
            #zipcode_request=scrapy.FormRequest(urlpattern, headers= {'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36' , 'Accept': 'application/json, text/plain, */*' , 'Referer': 'https://www.bigbasket.com/' , 'X-Requested-With': 'XMLHttpRequest' , 'Connection': 'keep-alive' , 'X-CSRFToken': 'ULzSJLnxgUbH08MGao89iUIPc4TxLRXcIuftv9wk5hI9vz1ZYBNEkxnqZj9tv8MW'},formdata=form_data, callback=self.parse1, method="POST", dont_filter=True)
            #zipcode_request=scrapy.Request(urlpattern, headers= {'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36' , 'Accept': 'application/json, text/plain, */*' , 'Referer': 'https://www.bigbasket.com/' , 'X-Requested-With': 'XMLHttpRequest' , 'Connection': 'keep-alive' , 'X-CSRFToken': 'ULzSJLnxgUbH08MGao89iUIPc4TxLRXcIuftv9wk5hI9vz1ZYBNEkxnqZj9tv8MW'}, callback=self.parse1, dont_filter=True)
            #zipcode_request=scrapy.Request(urlpattern, headers= {'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': urlpattern , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' }, callback=self.parse1, dont_filter=True)
            #zipcode_request=scrapy.Request(urlpattern, headers= {'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://www.bigbasket.com' , 'Upgrade-Insecure-Requests': '1' , 'Content-Type': 'application/x-www-form-urlencoded' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://www.bigbasket.com/pd/40019371/bournvita-pro-health-drink-chocolate-750-gm-pouch/?nc=as&q=bour' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' }, callback=self.parse1, dont_filter=True)
            #zipcode_request=scrapy.FormRequest(urlpattern, headers= {'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://www.bigbasket.com' , 'Upgrade-Insecure-Requests': '1' , 'Content-Type': 'application/x-www-form-urlencoded' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://www.bigbasket.com/' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' }, formdata=form_data, callback=self.parse1, method="POST", dont_filter=True)
            #zipcode_request=scrapy.FormRequest(urlpattern, headers= {'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36' , 'Accept': 'application/json, text/plain, */*' , 'Referer': 'https://www.bigbasket.com/' , 'X-Requested-With': 'XMLHttpRequest' , 'Connection': 'keep-alive' , 'X-CSRFToken': 'zNR4KfXSfKCWC3bBhutzUNfIPamya21iQcrIVRckDU732YLMNTiQBYCk3hYS68Om' , 'Cache-Control': 'no-cache'},  meta={'city':value[0], 'hid':value[1]}, formdata=form_data, callback=self.parse1, method="POST", dont_filter=True)
            zipcode_request=scrapy.FormRequest(urlpattern, headers= {'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36' , 'Accept': 'application/json, text/plain, */*' , 'Referer': 'https://www.bigbasket.com/' , 'X-Requested-With': 'XMLHttpRequest' , 'Connection': 'keep-alive' , 'X-CSRFToken': 'TDdPS2mYKPsb24VNxdnY8o4XawYOGtoqaNXiqysXXo8NT2Pts8eZl2li43btOD6c'},  meta={'city':value[0], 'hid':value[1]}, formdata=form_data, callback=self.parse1, method="POST", dont_filter=True)
            #zipcode_request.cookies={'_bb_tc':'0', '_bb_vid':"MjY2OTU2NDI5NQ==", '_bb_rdt':"MzE1MjAwNDU2OA==.0", '_bb_rd':'6', 'sessionid':'l7n936ndbkkyz1r28d79ml90ceah5d0t', '_ga':'GA1.2.1264447924.1530024086', '_gid':'GA1.2.179730791.1530024086', '_vz':'viz_58d0b47048003', 'cto_lwid':'c829fb77-d399-4f01-b0e7-0372384b0c62', '_client_version':'2052', 'Nprd':'20|1530110487085', 'csrftoken':'w5XXUqsj8RR3PQ5OYDdsHwV6JDc314o7fLYAq8YpupjfhUu5CNpVW0bPho1o6XHU', '_bb_cid':id, '_bb_hid':'85', 'ts':"2018-06-27 18:13:36.856", 'bigbasket.com':'2989f2a9-5f1e-4658-93b3-0fb518e86baf'}
            #zipcode_request.cookies={'_bb_tc':'0', '_bb_vid':"MjY2OTU2NDI5NQ==", '_bb_rdt':"MzE1MjAwNDU2OA==.0", '_bb_rd':ids, 'sessionid':'l7n936ndbkkyz1r28d79ml90ceah5d0t', '_ga':'GA1.2.1264447924.1530024086', '_gid':'GA1.2.179730791.1530024086', '_vz':'viz_58d0b47048003', 'cto_lwid':'c829fb77-d399-4f01-b0e7-0372384b0c62', '_client_version':'2052', 'Nprd':'2|1530254703532', 'csrftoken':'ULzSJLnxgUbH08MGao89iUIPc4TxLRXcIuftv9wk5hI9vz1ZYBNEkxnqZj9tv8MW', '_bb_cid':ids, '_bb_hid':'85', 'ts':"2018-06-28 16:55:40.543", 'bigbasket.com':'d08c6536-2f64-4b2e-99e0-5df74460eeef'}
            #zipcode_request.cookies={'_bb_tc':'0', '_bb_vid':"MjY2OTU2NDI5NQ==", '_bb_rdt':"MzE1MjAwNDU2OA==.0", '_bb_rd':'6', 'sessionid':'l7n936ndbkkyz1r28d79ml90ceah5d0t', '_ga':'GA1.2.1264447924.1530024086', '_gid':'GA1.2.179730791.1530024086', '_vz':'viz_58d0b47048003', 'cto_lwid':'c829fb77-d399-4f01-b0e7-0372384b0c62', '_client_version':'2052', 'csrftoken':'ULzSJLnxgUbH08MGao89iUIPc4TxLRXcIuftv9wk5hI9vz1ZYBNEkxnqZj9tv8MW', '_bb_cid':ids, '_bb_hid':'85', 'ts':"2018-06-28 16:55:42.947", 'bigbasket.com':'5ffdafa7-c0a9-47af-9157-2d638df6e7d1'}
            #zipcode_request.cookies={'_bb_tc':'0', '_bb_vid':"MjY2OTU2NDI5NQ==", '_bb_rdt':"MzE1MjAwNDU2OA==.0", '_bb_rd':'6', 'sessionid':'l7n936ndbkkyz1r28d79ml90ceah5d0t', '_ga':'GA1.2.1264447924.1530024086', '_gid':'GA1.2.179730791.1530024086', '_vz':'viz_58d0b47048003', 'cto_lwid':'c829fb77-d399-4f01-b0e7-0372384b0c62', '_client_version':'2052', '_bb_cid':city_info[key]['city_id'], '_bb_hid':'119', 'csrftoken':'V1SS0DEgLm750WCcxmaGJWHZmKvbSlHNtHUVoHp2LsM683516c9rRZPLUbvCXaI8', 'ts':"2018-06-29 15:28:59.289", 'Nprd':'7|1530342220877', '_gat':'1', 'bigbasket.com':'1d656dfb-0597-4cd8-a9c0-996c4cdf1e2e'}
            #zipcode_request.cookies={'_bb_tc':'0', '_bb_vid':"MjY2OTU2NDI5NQ==", '_bb_rdt':"MzE1MjAwNDU2OA==.0", '_bb_rd':'6', 'sessionid':'l7n936ndbkkyz1r28d79ml90ceah5d0t', '_ga':'GA1.2.1264447924.1530024086', '_vz':'viz_58d0b47048003', 'cto_lwid':'c829fb77-d399-4f01-b0e7-0372384b0c62', '_client_version':'2052', '_gid':'GA1.2.188541119.1530381546', '_fls':'true', '_gat':'1', 'Nprd':'8|1530467946902', 'csrftoken':'zNR4KfXSfKCWC3bBhutzUNfIPamya21iQcrIVRckDU732YLMNTiQBYCk3hYS68Om', '_bb_cid':value[0], '_bb_hid':value[1], 'ts':"2018-07-01 00:31:17.046", 'bigbasket.com':'7f9e6856-5e1b-42f7-9db2-146aa7db5c76' }
            zipcode_request.cookies={'_bb_tc':'0', '_bb_vid':"MjY2OTU2NDI5NQ==", '_bb_rdt':"MzE1MjAwNDU2OA==.0", '_bb_rd':'6', 'sessionid':'l7n936ndbkkyz1r28d79ml90ceah5d0t', '_ga':'GA1.2.1264447924.1530024086', '_vz':'viz_58d0b47048003', 'cto_lwid':'c829fb77-d399-4f01-b0e7-0372384b0c62', '_client_version':'2052', '_gid':'GA1.2.456461948.1530768742', 'Nprd':'1|1530855142328', '_gat':'1', 'bigbasket.com':'bb9f1f1a-3cb9-43b7-bbb4-1f3bfcb66b7c', 'csrftoken':'mqHNg8nrWrU5co3rChspA2sr5yAooKeih93D2yHtEnfywjXd0D7LRDcwponoY5by', '_bb_cid':value[0], '_bb_hid':'269', 'ts':"2018-07-05 11:08:54.496"}
            yield zipcode_request

    def parse1(self, response):
        city_data=demjson.decode(response.body)
        print city_data['sectionDetails']['0']['section_data']['excel_data']['0']['City Name']
        if response.meta['city']=="12":
            product_url="https://www.bigbasket.com/pd/40018400/elina-long-grain-rice-1-kg/"
            req = scrapy.Request(product_url, headers= {'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36' , 'Accept': 'application/json, text/plain, */*' , 'Referer': 'https://www.bigbasket.com/' , 'X-Requested-With': 'XMLHttpRequest' , 'Connection': 'keep-alive' , 'X-CSRFToken': 'zNR4KfXSfKCWC3bBhutzUNfIPamya21iQcrIVRckDU732YLMNTiQBYCk3hYS68Om' , 'Cache-Control': 'no-cache'}, callback=self.parse2, dont_filter=True)
            req.cookies={'_bb_tc':'0', '_bb_vid':"MjY2OTU2NDI5NQ==", '_bb_rdt':"MzE1MjAwNDU2OA==.0", '_bb_rd':'6', 'sessionid':'l7n936ndbkkyz1r28d79ml90ceah5d0t', '_ga':'GA1.2.1264447924.1530024086', '_vz':'viz_58d0b47048003', 'cto_lwid':'c829fb77-d399-4f01-b0e7-0372384b0c62', '_client_version':'2052', '_gid':'GA1.2.188541119.1530381546', '_fls':'true', '_gat':'1', 'Nprd':'8|1530467946902', 'csrftoken':'zNR4KfXSfKCWC3bBhutzUNfIPamya21iQcrIVRckDU732YLMNTiQBYCk3hYS68Om', '_bb_cid':response.meta['city'], '_bb_hid':response.meta['hid'], 'ts':"2018-07-01 00:31:17.046", 'bigbasket.com':'7f9e6856-5e1b-42f7-9db2-146aa7db5c76' }
            yield req
        elif response.meta['city']=="6":
            product_url="https://www.bigbasket.com/pd/40018400/elina-long-grain-rice-1-kg/"
            req = scrapy.Request(product_url, headers= {'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36' , 'Accept': 'application/json, text/plain, */*' , 'Referer': 'https://www.bigbasket.com/' , 'X-Requested-With': 'XMLHttpRequest' , 'Connection': 'keep-alive' , 'X-CSRFToken': 'zNR4KfXSfKCWC3bBhutzUNfIPamya21iQcrIVRckDU732YLMNTiQBYCk3hYS68Om' , 'Cache-Control': 'no-cache'}, callback=self.parse2, dont_filter=True)
            req.cookies={'_bb_tc':'0', '_bb_vid':"MjY2OTU2NDI5NQ==", '_bb_rdt':"MzE1MjAwNDU2OA==.0", '_bb_rd':'6', 'sessionid':'l7n936ndbkkyz1r28d79ml90ceah5d0t', '_ga':'GA1.2.1264447924.1530024086', '_vz':'viz_58d0b47048003', 'cto_lwid':'c829fb77-d399-4f01-b0e7-0372384b0c62', '_client_version':'2052', '_gid':'GA1.2.188541119.1530381546', '_fls':'true', '_gat':'1', 'Nprd':'8|1530467946902', 'csrftoken':'zNR4KfXSfKCWC3bBhutzUNfIPamya21iQcrIVRckDU732YLMNTiQBYCk3hYS68Om', '_bb_cid':response.meta['city'], '_bb_hid':response.meta['hid'], 'ts':"2018-07-01 00:31:17.046", 'bigbasket.com':'7f9e6856-5e1b-42f7-9db2-146aa7db5c76' }
            yield req
        elif response.meta['city']=="18":
            product_url="https://www.bigbasket.com/pd/40018400/elina-long-grain-rice-1-kg/"
            req = scrapy.Request(product_url, headers= {'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36' , 'Accept': 'application/json, text/plain, */*' , 'Referer': 'https://www.bigbasket.com/' , 'X-Requested-With': 'XMLHttpRequest' , 'Connection': 'keep-alive' , 'X-CSRFToken': 'zNR4KfXSfKCWC3bBhutzUNfIPamya21iQcrIVRckDU732YLMNTiQBYCk3hYS68Om' , 'Cache-Control': 'no-cache'}, callback=self.parse2, dont_filter=True)
            req.cookies={'_bb_tc':'0', '_bb_vid':"MjY2OTU2NDI5NQ==", '_bb_rdt':"MzE1MjAwNDU2OA==.0", '_bb_rd':'6', 'sessionid':'l7n936ndbkkyz1r28d79ml90ceah5d0t', '_ga':'GA1.2.1264447924.1530024086', '_vz':'viz_58d0b47048003', 'cto_lwid':'c829fb77-d399-4f01-b0e7-0372384b0c62', '_client_version':'2052', '_gid':'GA1.2.188541119.1530381546', '_fls':'true', '_gat':'1', 'Nprd':'8|1530467946902', 'csrftoken':'zNR4KfXSfKCWC3bBhutzUNfIPamya21iQcrIVRckDU732YLMNTiQBYCk3hYS68Om', '_bb_cid':response.meta['city'], '_bb_hid':response.meta['hid'], 'ts':"2018-07-01 00:31:17.046", 'bigbasket.com':'7f9e6856-5e1b-42f7-9db2-146aa7db5c76' }
            yield req

    def parse2(self, response):
        item=BigbasketItems()
        #item['zipCode']=response.meta["zipCode"]
        id=response.url.split('pd/')[1].split('/')[0]
        xpath_pattern="slidingProduct"+id
        xpath_pattern1='//*[@id=\"'+ xpath_pattern +'\"]/div[2]/div[2]/h1/text()'
        #item['delivery_days']=response.meta['delivery_days']
        item['item_id']=id
        item['response_url']=response.url
        title="".join(response.xpath(xpath_pattern1).extract()).replace('   ','').replace('\r','').replace('\n','').replace('\t','').strip()

        breadcrumb = "".join(response.xpath('//*[@id="uiv2-shopping-list"]/div[1]/div//text()').extract()).replace('   ','').replace('\r','').replace('\n','').replace('\t','').strip()
        brand_xpath_pattern='//*[@id=\"'+xpath_pattern+'\"]/div[@class="uiv2-product-detail-content"]/div[@class="uiv2-brand-name"]/a/text()'
        brand = response.xpath(brand_xpath_pattern).extract()

        price_xpath='//*[@id="'+xpath_pattern+'"]/div[@class="uiv2-product-detail-content"]/div[@class="uiv2-product-value"]/div[@class="uiv2-price"]//text()'
        price = "".join(response.xpath(price_xpath).extract()).replace('  ','').replace('\r','').replace('\n','').replace('\t','')
        variants_xpath='//*[@id=\"'+ xpath_pattern + '\"]/div[2]/div[3]/div/label'
        variants_xpath1='//*[@id=\"'+ xpath_pattern + '\"]/div[2]/div[3]/div'
        variants_count=len(response.xpath(variants_xpath))
        #variants_list=[]
        #print "".join(response.xpath('//*[@id="slidingProduct30007659"]/div[2]/div[3]/div/label/text()').extract()).replace('   ','').replace('  ','').replace('\r','').replace('\n','').replace('\t','').strip()
        variants="".join(response.xpath('//*[@id="slidingProduct'+id+'"]/div[2]/div[3]/div/label/text()').extract()).replace('   ','').replace('  ','').replace('\r','').replace('\n','').replace('\t','').strip()
        #if variants_count >0:
            #for i in range(1,variants_count+1):
                #variant="".join(response.xpath(variants_xpath1+'['+str(i)+']/label/text()').extract()).replace('   ','').replace('\r','').replace('\n','').replace('\t','').strip()
                #variants_list.append(variant)
				
        #location="".join(response.xpath('//*[@id="headercontroller"]/section[1]/div/div[2]/div/button/span/span[@class="ng-binding ng-scope"]//text()').extract()).replace('   ','').replace('\r','').replace('\n','').replace('\t','').strip()
        location_dict=demjson.decode("".join(response.xpath('//script[@id="page-data"]/text()').extract()).replace('   ','').replace('\r','').replace('\n','').replace('\t','').strip().split('=')[1].replace(';',''))
        location_info=[location_dict['selected_address']['area'], location_dict['selected_address']['city_name'], str(location_dict['selected_address']['pin'])]
        #print location_info
        item['brand']="".join(brand)
        item['delivery_days']=location_dict['normal_next_slot']
        item['title']="".join(title).replace("\n","").replace("\t","").replace("    ","")
        item['breadcrumb']=breadcrumb
        item['location']=" , ".join(location_info)
        item['product_variants']=variants
        item['price']=price
        image_xpath='//*[@id="pimg_'+id+'"]/@src'
        image_url="https:"+"".join(response.xpath('//*[@id=\"'+ xpath_pattern +'\"]/div[1]/a/@href').extract())
        item['thumbnail']=[image_url]
        item['thumbnail_name']=[id]
        location_info=[]
        yield item