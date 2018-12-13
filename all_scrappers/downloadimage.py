

#Download image scrapper.

import scrapy
from spider2.items import Spider2Item

class ImageSpider(scrapy.Spider):
	#handle_httpstatus_list = [407]
	name = "downloadimage"
	allowed_domain=[]
 
	start_urls = ['http://www.amazon.in/Asus-10050mAH-Power-Bank-Gold/dp/B010AKGD64/ref=sr_1_2?ie=UTF8&qid=1490162406&sr=8-2&keywords=asus+power+bank']
	#start_urls = ['http://www.amazon.in']

        def parse(self, response):
            item =Spider2Item()
 
            item['image_urls'] =  response.xpath('//*[@class="a-list-item"]/span[1]/div[1]/img[1]/@src').extract()

            yield item