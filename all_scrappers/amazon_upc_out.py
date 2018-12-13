# -*- coding: utf-8 -*-
from __future__ import absolute_import
import scrapy
import urllib
from amazon_upc_out.items1 import Amazon_upc_out
import os
import time
from amazon_upc_out.spiders.spiders1 import * 
import json
class AmazonSpider(ListeningKafkaSpider):
    imgcount = 1
    name = "amazon_upc_out_de"
    handle_httpstatus_list = [404]
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.alowed_domains = filter(None, domain.split(','))
        super(AmazonSpider, self).__init__(*args, **kwargs)

    def parse(self,response):
 

        try:
            attr=response.meta['attr']
            json_acceptable_string = attr.replace("'", "\"")
            attr = json.loads(json_acceptable_string)
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
		
            try: price = "".join(response.xpath('//*[@id="priceblock_ourprice"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            except: raise
            if not price: price = "".join(response.xpath('//*[@id="priceblock_businessprice"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not price: price = "".join(response.xpath('//*[@id="priceblock_dealprice"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not price: price = "".join(response.xpath('//*[@id="priceblock_ourprice_row"]/td[2]/span[@class="a-size-base a-color-price priceblock_vat_inc_price"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            if not price: price = "".join(response.xpath('//*[@id="priceblock_saleprice_row"]/td[2]/span[@class="a-size-base a-color-price priceblock_vat_inc_price"]/text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
            price1 =""
            try: 
                price_base = "#".join(response.xpath('//*[@id="priceblock_ourprice_row"]/td[2]/span//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip().lower()
                price_index =  price_base.split('#').index('inkl. ust')
                print price_index, "kjjhhhhhhhhhhhhhhhhhhhhhh",price_base
                if not price : price = "".join(price_base.split('#')[price_index -2: price_index +1])
                price1 = "".join(price_base.split('#')[0: price_index -2])
                if price1 and not price: price=price_base.split('#')[price_index -3:]

            except: 
                price = "".join(response.xpath('//*[@id="priceblock_ourprice_row"]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip()
                
            try:
                if not price:
                    price = "".join(response.xpath('//*[@id="soldByThirdParty"]/span[2]//text()').extract()).replace("  ",'').replace("\n",'').replace('\t','').strip().lower().replace('incl. vat','')
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
            item['ASIN'] = attr.get('DPID')
            item['date_timestamp']= int(time.time())
            item['job_id'] = attr['job_id']
            item['product_id'] = response.meta['id']
            item['UPC']= attr['UPC']
            item['breadcrumb']="/".join(bredcrumb_temp)
            item['seller_count'] = count
            item['ship_price'] = ship_price
            item['ship_price2'] = ship_price2
            item['price'] = price
            item['price1'] = price1
            item['seller_name'] = seller_name
            item['spider'] = self.name
            if attr['UPC'].find('_') > -1:
                item['comp']='Alt'
                item['UPC']=attr['UPC'].split('_')[0]
            else:
                item['comp']=''
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
                    item['ASIN'] = attr.get('DPID')
                    item['response_url']=response.url
                    item['UPC']= attr['UPC']
                    item['date_timestamp']= int(time.time())
                    item['spider'] = self.name
                    item['job_id'] = attr['job_id']
                    item['seller_count'] = 'Not Found'
                    if attr['UPC'].find('_') > -1:
                        item['comp']='Alt'
                        item['UPC']=attr['UPC'].split('_')[0]
                    else:
                        item['comp']=''
                    item['body'] = response.body                              
                    yield item
                result = response.xpath('//title/text()').extract()[0].find('Page Not Found')
                if result>-1:
                    item = Amazon_upc_out()
                    item['product_id'] = response.meta['id']
                    item['ASIN'] = attr.get('DPID')
                    item['response_url']=response.url
                    item['UPC']= attr['UPC']
                    item['date_timestamp']= int(time.time())
                    item['spider'] = self.name
                    item['job_id'] = attr['job_id']
                    item['seller_count'] = 'Not Found'
                    if attr['UPC'].find('_') > -1:
                        item['comp']='Alt'
                        item['UPC']=attr['UPC'].split('_')[0]
                    else:
                        item['comp']=''
                    item['body'] = response.body                              
                    yield item
            except: raise 



