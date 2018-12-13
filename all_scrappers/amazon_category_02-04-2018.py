#Amazon seller list spider
import time
import scrapy
import re
class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    category = scrapy.Field()

class Spider(scrapy.Spider):
    
    name = "amazon_category_02-04-2018"
    allowed_domain=[]
    start_urls = ['http://www.fnwerkzeuge.de/akkugeraete.html']
        
		
    def parse(self, response):
        urls = [
["Electronics", "https://www.amazon.com/s/ref=lp_17608344011_nr_i_0?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Aelectronics&ie=UTF8&qid=1522670094"],
["Office Products","https://www.amazon.com/s/ref=lp_17608344011_nr_i_1?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Aoffice-products&ie=UTF8&qid=1522670094"],
["Home & Kitchen","https://www.amazon.com/s/ref=lp_17608344011_nr_i_2?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Agarden&ie=UTF8&qid=1522670094"],
["Industrial & Scientific","https://www.amazon.com/s/ref=lp_17608344011_nr_i_3?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Aindustrial&ie=UTF8&qid=1522670094"],
["Health, Household & Baby Care","https://www.amazon.com/s/ref=lp_17608344011_nr_i_4?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Ahpc&ie=UTF8&qid=1522670094"],
["Cell Phones & Accessories","https://www.amazon.com/s/ref=lp_17608344011_nr_i_5?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Amobile&ie=UTF8&qid=1522670094"],
["Grocery & Gourmet Food","https://www.amazon.com/s/ref=lp_17608344011_nr_i_6?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Agrocery&ie=UTF8&qid=1522670094"],
["Tools & Home Improvement","https://www.amazon.com/s/ref=lp_17608344011_nr_i_7?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Atools&ie=UTF8&qid=1522670094"],
["Appliances","https://www.amazon.com/s/ref=lp_17608344011_nr_i_8?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Aappliances&ie=UTF8&qid=1522670094"],
["Arts, Crafts & Sewing","https://www.amazon.com/s/ref=lp_17608344011_nr_i_9?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Aarts-crafts&ie=UTF8&qid=1522670094"],
["Beauty & Personal Care","https://www.amazon.com/s/ref=lp_17608344011_nr_i_10?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Abeauty&ie=UTF8&qid=1522670094"],
["Automotive Parts & Accessories","https://www.amazon.com/s/ref=lp_17608344011_nr_i_11?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Aautomotive&ie=UTF8&qid=1522670094"],
["Sports & Outdoors","https://www.amazon.com/s/ref=lp_17608344011_nr_i_12?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Asporting&ie=UTF8&qid=1522670094"],
["Baby","https://www.amazon.com/s/ref=lp_17608344011_nr_i_14?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Ababy-products&ie=UTF8&qid=1522670094"],
["Clothing, Shoes & Jewelry","https://www.amazon.com/s/ref=lp_17608344011_nr_i_13?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Afashion&ie=UTF8&qid=1522670094"],
["Everything Else","https://www.amazon.com/s/ref=lp_17608344011_nr_i_15?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Amisc&ie=UTF8&qid=1522670094"],
["Musical Instruments","https://www.amazon.com/s/ref=lp_17608344011_nr_i_16?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Ami&ie=UTF8&qid=1522670094"],
["Toys & Games","https://www.amazon.com/s/ref=lp_17608344011_nr_i_17?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Atoys-and-games&ie=UTF8&qid=1522670094"],
["Garden & Outdoor","https://www.amazon.com/s/ref=lp_17608344011_nr_i_18?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Alawngarden&ie=UTF8&qid=1522670094"],
["Video Games","https://www.amazon.com/s/ref=lp_17608344011_nr_i_19?srs=17608344011&fst=as%3Aoff&rh=i%3Aspecialty-aps%2Ci%3Avideogames&ie=UTF8&qid=1522670094"],
]
        
        for url in urls:
            req = scrapy.Request(url[1], headers={'Accept-Encoding': 'gzip, deflate, sdch, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' , 'Cache-Control': 'max-age=0' , 'Connection': 'keep-alive'},callback=self.parse1, meta={'categoryname':url[0]})
            item=AmazonItem()
            item['url']=url[1]
            item['category'] =url[0]
            yield item
            yield req
                                
                        
    def parse1(self, response):
        categorylist=response.xpath('//*[@id="leftNavContainer"]/ul[1]/ul/div/li')
        if len(categorylist)>0:
            for categories in categorylist:
                item=AmazonItem()
                categoryurl="https://www.amazon.com" + categories.xpath('span/a/@href').extract()[0]
                categoryname= categories.xpath('span/a/span/text()').extract()[0]
                req=scrapy.Request(categoryurl,callback=self.parse1, meta={'categoryname':categoryname})
                item['url']=categoryurl
                item['category'] =categoryname
                yield item
                yield req