import scrapy
import urllib
#from shop.items1 import TyreItem

import os
import time

class AmazonItem(scrapy.Item):
    url=scrapy.Field()
    brand=scrapy.Field()
	

class amazonSpider(scrapy.Spider):
    imgcount = 1
    name = "amz_url_brand2"
    allowed_domains = ["amazon.com"]

    start_urls = ["https://www.amazon.com"]
  

    def parse(self,response):
        result = []
        res=[
'/gp/search/other/ref=sr_in_1_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=%23&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_a_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=a&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_b_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=b&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_c_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=c&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_d_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=d&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_e_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=e&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_f_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=f&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_g_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=g&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_h_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=h&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_i_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=i&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_j_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=j&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_k_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=k&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_l_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=l&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_m_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=m&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_n_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=n&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_o_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=o&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_p_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=p&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_q_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=q&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_r_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=r&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_s_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=s&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_t_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=t&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_u_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=u&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_v_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=v&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_w_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=w&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_x_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=x&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_y_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=y&unfiltered=1&ie=UTF8&qid=1502174362',
'/gp/search/other/ref=sr_in_z_-2?sf=fr&rh=i%3Afashion-baby%2Cn%3A7141123011%2Cn%3A7147444011%2Ck%3AChildren+Apparel&bbn=7147444011&keywords=Children+Apparel&pickerToList=lbr_brands_browse-bin&indexField=z&unfiltered=1&ie=UTF8&qid=1502174362',

]
        for re in res:        
            req = scrapy.Request("https://www.amazon.com"+re,callback=self.parse1 ,headers={'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://www.amazon.de/gp/search/other/ref=sr_in_a_1/261-5906571-3749750?rh=i%3Aindustrial%2Cn%3A5866098031%2Cn%3A%215866099031%2Cn%3A6587752031&bbn=6587752031&pickerToList=lbr_brands_browse-bin&indexField=a&ie=UTF8&qid=1501841151' , 'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' })
            #req = scrapy.Request(f_url,callback=self.parse1)
            yield req   
		
    def parse1(self,response):
        result = []
        res=response.xpath('//span[@class="a-list-item"]/a')
        for re in res:
            url = 'https://www.amazon.com' + re.xpath('@href').extract()[0].replace('&page=1','')
            
            count = int(str(re.xpath('span/text()').extract()[1].replace('.','').replace(',','').replace('(','').replace(')','')))
            
            brand= re.xpath('span/text()').extract()[0]
            #print url, count, brand
            #req = scrapy.Request(url,callback=self.parse1)
            #yield req  
            page_number = count/24 +2
            for i in range(1,page_number):
                item=AmazonItem()
                f_url = url+'&page='+ str(i)
                item['url']=f_url
                item['brand']=brand
                yield item
                #req = scrapy.Request(f_url,callback=self.parse2 ,headers={'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://www.amazon.de/gp/search/other/ref=sr_in_a_1/261-5906571-3749750?rh=i%3Aindustrial%2Cn%3A5866098031%2Cn%3A%215866099031%2Cn%3A6587752031&bbn=6587752031&pickerToList=lbr_brands_browse-bin&indexField=a&ie=UTF8&qid=1501841151' , 'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' })
                #req = scrapy.Request(f_url,callback=self.parse1)
                #req.meta['brand']=""
                #yield req"""    
	
    def parse2(self,response):

        res = response.xpath('//div/div[3]/div[1]/a/@href').extract()
        for url in res:
            #req = scrapy.Request(url,callback=self.parse2)
            item = TyreItem()
            item['url'] = url
            item['profile']="".join(response.xpath('//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li/span/a/text()').extract()).replace('\n','').replace('    ','')
            yield item                              