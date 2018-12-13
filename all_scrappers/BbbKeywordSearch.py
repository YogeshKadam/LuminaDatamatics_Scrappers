# -*- coding: utf-8 -*-
import scrapy
#from ScrapyProjectv1.items import Bbbkeyword
items=[]
#line=""
class Bbbkeyword(scrapy.Item):
    seller_name=scrapy.Field()
    seller_url=scrapy.Field()
    hit_url=scrapy.Field()
    url_from_parse=scrapy.Field()

	
	
	
class BbbkeywordsearchSpider(scrapy.Spider):
    name = 'BbbKeywordSearch'
    allowed_domains = ['bbb.org']
    start_urls = ['https://www.bbb.org/']
    #line=""
	
    def parse(self,response):

        f=open('D:\\YK Python\\fnwer\\domains.txt','r')
        while 1:
            #global line
            line=f.readline()
            if not line:
                break
            else:
                print line
                start_urls = 'https://www.bbb.org/search/?splashPage=true&type=name&input='+ line
                req=scrapy.Request(start_urls,callback=self.parse1,meta={'returns_line': line})
                yield req
        f.close()
        # input_seller_name=[url.strip() for url in f.readlines()]
        #print "#########################################"
        # print input_seller_name
    # start_urls = ['https://www.bbb.org/search/?splashPage=true&type=name&input=']

    def parse1(self, response):

        # print input_seller_name
        print "RESPONSE URL : ",response.url
        print "@@@@@@@@@@@@@@@",response.meta.get('returns_line')
        seller_url=response.xpath('//h4[@class="hcolor"]/a/@href').extract()
        seller_name=response.xpath('//h4[@class="hcolor"]/a/text()').extract()
        # print seller_url
        # print seller_name
        for seller_info in range(0,len(seller_url)):
            item = Bbbkeyword()
            # print "seller info##################"
            # print seller_url[seller_info]
            # print seller_name[seller_info]
            item['seller_name'] = seller_name[seller_info]
            item['seller_url']= seller_url[seller_info]
            item['hit_url']=response.url
            #item['url_from_parse']=self.line
            #items.append(item)
            yield item
        #     item['product_count_on_pagination'] = total_products
