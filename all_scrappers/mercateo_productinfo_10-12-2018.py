# -*- coding: utf-8 -*-
import scrapy
import urllib
#from shop.items1 import TyreItem,MatchItem,Refurb
import os
import time
import re
import json
from scrapy.http.cookies import CookieJar


class MercateoItems(scrapy.Item):
    product_title = scrapy.Field()
    product_id = scrapy.Field()
    article_no = scrapy.Field()
    #price = scrapy.Field()
    brand = scrapy.Field()
    ean = scrapy.Field()
    mpn = scrapy.Field()
    model_number = scrapy.Field()
    colour = scrapy.Field()
    description = scrapy.Field()
    url_page = scrapy.Field()
    breadcrumb  = scrapy.Field()
    base_breadcrumb = scrapy.Field()
    attr_dict = scrapy.Field()
    quantity = scrapy.Field()
    response_url = scrapy.Field()
    #seller_name = scrapy.Field()
    # desc = scrapy.Field()

class MercateoSpider(scrapy.Spider):
    name = "mercateo_productinfo_10-12-2018"
    allowed_domains = ["mercateo.com"]

    start_urls = ["http://www.mercateo.com" ]  
    result = ''
    


    def parse(self,response):
        url_done = []
        url_list= [
["1","http://www.mercateo.com/kw/wendeplattenbohrer/wendeplattenbohrer.html?ViewName=live~s.20","http://www.mercateo.com/p/1498P-4112911704/Wendeplattenaufbohrer_AW_D_28mm_m_Bilzkegelschaft_f_SCHX09_.html?ViewName=live~s.20"],
["2","http://www.mercateo.com/kw/wendeplattenbohrer/wendeplattenbohrer.html?ViewName=live~s.20","http://www.mercateo.com/p/C3160-4000833664/Werkzg_h_DIN_69880_Form_E1_Spann_D_32mm_VDI30_z_Wendeplattenbohrer_PROMAT.html?ViewName=live~s.20"],
["3","http://www.mercateo.com/kw/wendeplattenbohrer/wendeplattenbohrer.html?ViewName=live~s.20","http://www.mercateo.com/p/1498P-4112911703/Wendeplattenaufbohrer_AW_D_26mm_m_Bilzkegelschaft_f_SCHX06_.html?ViewName=live~s.20"],
["4","http://www.mercateo.com/kw/wendeplattenbohrer/wendeplattenbohrer.html?ViewName=live~s.20","http://www.mercateo.com/p/C3160-4000833663/Werkzg_h_DIN_69880_Form_E1_Spann_D_25mm_VDI30_z_Wendeplattenbohrer_PROMAT.html?ViewName=live~s.20"],
["5","http://www.mercateo.com/kw/wendeplattenbohrer/wendeplattenbohrer.html?ViewName=live~s.20","http://www.mercateo.com/p/C3160-4000833668/Werkzg_h_DIN_69880_Form_E1_Spann_D_25mm_VDI40_z_Wendeplattenbohrer_PROMAT.html?ViewName=live~s.20"],
["6","http://www.mercateo.com/kw/wendeplattenbohrer/wendeplattenbohrer.html?ViewName=live~s.20","http://www.mercateo.com/p/C3160-4000833670/Werkzg_h_DIN_69880_Form_E1_Spann_D_40mm_VDI40_z_Wendeplattenbohrer_PROMAT.html?ViewName=live~s.20"],
["7","http://www.mercateo.com/kw/wendeplattenbohrer/wendeplattenbohrer.html?ViewName=live~s.20","http://www.mercateo.com/p/214-3029995720/Vollbohrer_f_WP_m_IK_27_mm_3_x_D.html?ViewName=live~s.20"],
["8","http://www.mercateo.com/kw/wendeplattenbohrer/wendeplattenbohrer.html?ViewName=live~s.20","http://www.mercateo.com/p/214-3029995785/Vollbohrer_f_WP_m_IK_40_mm_3_x_D.html?ViewName=live~s.20"],
["9","http://www.mercateo.com/kw/wendeplattenbohrer/wendeplattenbohrer.html?ViewName=live~s.20","http://www.mercateo.com/p/356-5031806040/VDI_Halter_fuer_Wendeplattenbohrer_E1_60x40mm.html?ViewName=live~s.20"],
["10","http://www.mercateo.com/kw/wendeplattenbohrer/wendeplattenbohrer.html?ViewName=live~s.20","http://www.mercateo.com/p/214-3029995775/Vollbohrer_f_WP_m_IK_38_mm_3_x_D.html?ViewName=live~s.20"],
]
        for url in url_list:
            if url[0] in url_done:
                continue
            url1 = url[2]
            try:
                req = scrapy.Request(url1,callback=self.parse4)
                req.meta['base_breadcrumb'] = url[1]
                req.meta['product_id'] = url[0]
                yield req
            except: raise
    def parse4(self,response):
        global result
        
        item = MercateoItems()
        artical ="".join(response.xpath('//td[@class="BD02"]/div[1]/span[2]/text()').extract())
        ean1 = "".join(response.xpath('//td[@class="BD02"]/div[4]/span[2]/text()').extract())
        brand = ''.join(response.xpath('//td[@class="BD02"]/div[2]/span/a/text()').extract() )
        if not brand: brand = ''.join(response.xpath('//td[@class="BD02"]/div[2]/span/text()').extract() )
        mpn  = ''.join(response.xpath('//td[@class="BD02"]/div[3]/span[2]/text()').extract() )
    

        if " ".join(response.xpath('//*[@id="productFormID"]/table/tr/td[2]/table/tr[1]/td/div/text()').extract()).find(u'Mind.-Mengeff')>-1:
            index = response.xpath('//*[@id="productFormID"]/table/tr/td[2]/table/tr[1]/td/div/text()').extract().index(u'Mind.-Menge') +4

            for data in response.xpath('//*[@id="productFormID"]/table/tr/td[2]/table/tr'): 
                if ''.join(data.xpath('td['+str(index) +']/div/text()').extract()) =='1':
                    price_index = len(data.xpath('td').extract()) -1
                    price = "",join(data.xpath('td['+str(price_index) +']/div/text()').extract())
                    seller = "".join(data.xpath('td[2]/div/span/text()').extract())
                    if not seller:seller = "".join(data.xpath('td[3]/div/a/text()').extract())
                    if not seller:seller = "".join(data.xpath('td[3]/div/span/text()').extract())
                    break
        else:
            for data in response.xpath('//*[@id="productFormID"]/table/tr/td[2]/table/tr'):

                price_index = len(data.xpath('td').extract()) -1
                price = "".join(data.xpath('td['+str(price_index) +']/div/text()').extract())
                if not price: price = "".join(data.xpath('td['+str(price_index) +']/div/span/text()').extract())
                    #print price
                if price.encode('ascii','ignore').strip():
                    try:
                        re.search(r'\d+' ,price.encode('ascii','ignore')).group()
                        seller = "".join(data.xpath('td[2]/div/span/text()').extract())
                        if not seller:seller = "".join(data.xpath('td[3]/div/a/text()').extract())
                        if not seller:seller = "".join(data.xpath('td[3]/div/span/text()').extract())
                        break
                    except:
                        continue
        #print "#####################################",price.encode('ascii','ignore')
        #price = "{0:.2f}".format( float(price.encode('ascii','ignore').replace('.','').replace(',','.').replace('*','')) * 1.19)
        #item['price'] = price
        #item['seller_name'] = seller                        
        attr_dict={}
        variantslist=response.xpath('//*[@id="productFormID"]/table/tr/td[1]/table/tr[5]/td[2]/table/tr/td/table/tr')
        if len(response.xpath('//*[@id="productFormID"]/table/tr/td[1]/table/tr[5]/td[2]/table/tr/td/table/tr[1]/td'))==2:
            item['attr_dict'] = json.dumps(dict([ ("".join(variants.xpath('td[1]/div/text()').extract()),"".join(variants.xpath('td[2]/div/text()').extract()))for variants in variantslist]))

        elif len(response.xpath('//*[@id="productFormID"]/table/tr/td[1]/table/tr[5]/td[2]/table/tr/td/table/tr[1]/td'))==3:
            item['attr_dict'] =json.dumps(dict([("".join(variants.xpath('td[2]/div/text()').extract()),"".join(variants.xpath('td[3]/div/text()').extract())) for variants in variantslist]))

        else:
            if response.xpath('//*[@id="productFormID"]/table/tr/td[1]/table/tr[5]/td[2]/table/tr/td/div/ul/li//text()').extract():
                key="Description"
                item['attr_dict'] =json.dumps({key:response.xpath('//*[@id="productFormID"]/table/tr/td[1]/table/tr[5]/td[2]/table/tr/td/div/ul/li//text()').extract()})
            else:
                key="Description"
                item['attr_dict']=json.dumps({key:response.xpath('//*[@id="productFormID"]/table/tr/td[1]/table/tr[5]/td[2]/table/tr/td/div//text()').extract()})

        
        breadcrumb= '/'.join(response.xpath('//span[@itemprop="child"]/a/span/text()').extract()) +"/"+ ''.join(response.xpath('//span[@itemprop="child"]/span/text()').extract())
        description=""
        if response.xpath('//*[@id="productFormID"]/table/tr[1]/td[1]/table/tr[5]/td[2]/table/tr/td/div[1]/ul/li/b/text()').extract():
            desc_list=[]
            list1=response.xpath('//*[@id="productFormID"]/table/tr[1]/td[1]/table/tr[5]/td[2]/table/tr/td/div[1]/ul/li')
            for lis in list1:
                try:
                    desc_list.append(lis.xpath('b/text()').extract()[0] + lis.xpath('text()').extract()[0])
                except:
                    desc_list.append(lis.xpath('text()').extract()[0])
            description="||".join(desc_list)
        else: description= '||'.join(response.xpath('//*[@id="productFormID"]/table/tr[1]/td[1]/table/tr[5]/td[2]/table/tr/td/div[1]/ul/li//text()').extract())
        
        item['product_title']= "".join(response.xpath('//*[@id="productFormID"]/div[2]/table/tr[1]/td[1]/h1/text()').extract())
        item['article_no']=artical
        item['ean']=ean1
        item['response_url'] = response.url
        item['base_breadcrumb'] = response.meta['base_breadcrumb']
        item['product_id'] = response.meta['product_id']
        # item['attr_dict'] = attr_dict
        item['mpn'] = mpn
        item['breadcrumb'] = breadcrumb
        item['description'] = description
        item['brand'] = brand
        yield item