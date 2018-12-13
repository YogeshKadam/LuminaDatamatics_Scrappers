# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor

from scrapy_splash import SplashRequest


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ['gastro24.de']
    start_urls = ['http://gastro24.de/']


    def parse(self, response):
        #le = LinkExtractor()
        
        yield SplashRequest(
                "http://www.gastro24.de/Rundfilter-Kaffeemaschine-Regina-Plus-90T",
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

    """
    # http_user = 'splash-user'
    # http_pass = 'splash-password'

    def parse(self, response):
        le = LinkExtractor()
        for link in le.extract_links(response):
            yield SplashRequest(
                link.url,
                self.parse_link,
                endpoint='render.json',
                args={
                    'har': 1,
                    'html': 1,
                }
            )

    def parse_link(self, response):
        print("PARSED", response.real_url, response.url)
        print(response.css("title").extract())
        print(response.data["har"]["log"]["pages"])
        print(response.headers.get('Content-Type'))
    """
