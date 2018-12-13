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
    thumbnail_name= scrapy.Field()
    breadcrumb= scrapy.Field()
    availability= scrapy.Field()
    delivery_days= scrapy.Field()
    response_url= scrapy.Field()
    brand= scrapy.Field()
    item_id= scrapy.Field()

class ShopcluesSpider(scrapy.Spider):
    imgcount = 1
    name = "shopclues_productinfo_part3"
    allowed_domains = ["shopclues.com"]

    start_urls = ["https://www.shopclues.com/computers-monitors.html"]
			
    def parse1(self, response):
        urlpattern="https://www.shopclues.com/ajaxCall/getDeliveryDetails?itemId="+response.meta['item_id']+"&pincode="+response.meta['zipCode']+"&user_segment=&user_id=&user_email=&price_tbp=&user_mobile="
        form_data={'itemId': response.meta['item_id'],'pincode': response.meta['zipCode'],'user_segment':'', 'user_id':'', 'user_email':'','price_tbp':'', 'user_mobile':''}
        zipcode_request=scrapy.FormRequest(urlpattern, headers= {'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36' , 'Accept': '*/*' , 'Referer': 'https://www.shopclues.com/', 'Connection': 'keep-alive'} ,formdata=form_data, callback=self.parse2, method="POST", meta={'url':response.meta['url'], 'zipCode':response.meta['zipCode'], 'item_id':response.meta['item_id']}, dont_filter=True)
        yield zipcode_request
			
    def parse(self, response):
        url_list=response.xpath('//*[@id="product_list"]/div[@class="row"]/div[@class="column col3"]')
        counter=0
        while counter<10:
            url="https:"+url_list[counter].xpath('a[2]/@href').extract()[0]
            item_id=url_list[counter].xpath('a[1]/@pid').extract()[0]
            #print url
            counter+=1
            zipCodeList=["560070", "575001", "671551"]
            for zipCode in zipCodeList:
                req = scrapy.Request(url, callback=self.parse1, meta={"url":url, "item_id":item_id, "zipCode":zipCode}, dont_filter=True)
                yield req
                time.sleep(.1)

		
    def parse2(self, response):
        del_dict=demjson.decode(response.body)
        req = scrapy.Request(response.meta['url'], callback=self.parse3, meta={"delivery_days":del_dict['fdate']+"-"+del_dict['sdate'], 'zipCode':response.meta['zipCode'], 'item_id':response.meta['item_id']} ,dont_filter=True)
        yield req
				
    def parse3(self, response):
        item=ShopcluesItems()
        item['zipCode']=response.meta["zipCode"]
        item['delivery_days']=response.meta['delivery_days']
        item['item_id']=response.meta['item_id']
        item['response_url']=response.url
        title="".join(response.xpath('//*[@id="main_data"]/div[@class="shd_box"]/div[@class="prd_mid_info"]/h1//text()').extract()).replace('   ','').replace('\r','').replace('\n','').replace('\t','').strip()

        breadcrumb = " > ".join(response.xpath('//*[@id="main_data"]/div[1]/ul/li/a/span//text()').extract()).replace('   ','').replace('\r','').replace('\n','').replace('\t','').strip()+">"+title
        
        brand = response.xpath('//*[@id="main_data"]/div[@class="shd_box"]/div[@class="prd_mid_info"]/span[@class="pID"]/a/text()').extract()

        price = "".join(response.xpath('//*[@id="main_data"]/div[@class="shd_box"]/div[@class="prd_mid_info"]/div[@itemprop="offers"]/span[@itemprop="lowPrice"]/text()').extract()).replace('  ','').replace('\r','').replace('\n','').replace('\t','')
        item['brand']="".join(brand)
        item['title']="".join(title).replace("\n","").replace("\t","").replace("    ","")
        item['breadcrumb']=breadcrumb
        item['price']=price
        image_url="".join(response.xpath('//*[@id="main_data"]/div[@class="shd_box"]/div[@class="prd_mid_info"]/img/@src').extract())
        item['thumbnail']=[image_url]
        item['thumbnail_name']=[response.meta['item_id']]
        if response.xpath('//*[@id="main_data"]/div[4]/div[2]/div[@class="product_ntavailable"]'):
            item['availability']="no"
        else:
            item['availability']="yes"
        yield item
