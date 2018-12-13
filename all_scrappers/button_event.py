# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor

from scrapy_splash import SplashRequest


class QuotesSpider(scrapy.Spider):
    name = "clickbutton"
    allowed_domains = ['gastro24.de']
    start_urls = ['http://www.gastro24.de/']


    def parse(self, response):
        #le = LinkExtractor()
        
        yield SplashRequest(
                "http://www.gastro24.de/Eisportionierer-aus-Edelstahl-von-Stoeckel-in-verschiedenen-Groessen",
                self.parse_link,
                endpoint='render.json',
                args={
				    'har': 1,
                    'html': 1,
			         'wait': 2.0
                }
            )

    def parse_link(self, response):
        #fd = open('d1.html','w')
        #fd.write(response.body)
        #fd.close()
        print response.xpath('//div[@class="differential_price section_box well"]/ul/li/div/span//text()').extract()[1]