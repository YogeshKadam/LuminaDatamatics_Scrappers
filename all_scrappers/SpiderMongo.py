
#Read write data to mongoDB.

import scrapy
from mongospider.items import MongospiderItem

class Spider(scrapy.Spider):
	#handle_httpstatus_list = [407]
	name = "Mongo"
	allowed_domain=[]
 
	start_urls = ['http://www.amazon.in/Asus-10050mAH-Power-Bank-Gold/dp/B010AKGD64/ref=sr_1_2?ie=UTF8&qid=1490162406&sr=8-2&keywords=asus+power+bank']
	#start_urls = ['http://www.amazon.in']

        def parse(self, response):
            item =MongospiderItem()
 
            item['title'] =  response.xpath('//*[@id="titleSection"]/h1[1]/span[1]/text()').extract()

            item['price']=response.xpath('//*[@class="a-span12"]/span[1]/text()').extract()

            print ("Title : '{0}' and Price : '{1}'")%item['title'],item['price']
			
            yield item
			
			