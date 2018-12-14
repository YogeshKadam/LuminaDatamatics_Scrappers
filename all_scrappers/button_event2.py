# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor

from scrapy_splash import SplashRequest
import time
import demjson

class GastroItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    articleno = scrapy.Field()
    price = scrapy.Field()
    url=scrapy.Field()
    brand=scrapy.Field()
    breadcrumb=scrapy.Field()
    description=scrapy.Field()


class QuotesSpider(scrapy.Spider):
    name = "clickbutton2"
    allowed_domains = ['gastro24.de']
    start_urls = ['http://www.gastro24.de/Eisportionierer-aus-Edelstahl-von-Stoeckel-in-verschiedenen-Groessen']


    def parse(self, response):
        script = """
        function main(splash)
            ids=splash.args.id
            --print(ids)
            local url = splash.args.url
            assert(splash:go(url))
            assert(splash:wait(5))
            --local submitbutton = splash:select('#kEigenschaftWert_3412')
            --submitbutton:mouse_click()
            assert(splash:runjs("$('#kEigenschaftWert_3425').click()"))
            --assert(splash:runjs("document.getElementsById('kEigenschaftWert_3425').click()"))
            assert(splash:wait(5))
            return {
                html = splash:html()
            }
        end
        """
        url="http://www.gastro24.de/Eisportionierer-aus-Edelstahl-von-Stoeckel-in-verschiedenen-Groessen"
        yield scrapy.Request(url,      self.parse_link,       meta={
                             'splash': {
                             'args': {'lua_source': script                     },
                             'endpoint': 'execute'
                            }
                            })
        #le = LinkExtractor()
        
        """yield SplashRequest(
                "http://www.gastro24.de/Eisportionierer-aus-Edelstahl-von-Stoeckel-in-verschiedenen-Groessen",
                self.parse_link,
                endpoint='execute',
                args={
				    'har': 1,
                    'html': 1,
			         'wait': 2.0,
                    'lua_source': script
                }
            )"""

    def parse_link(self,response):
        
        cost=response.xpath('//div[@class="differential_price section_box well"]/ul/li/div/span//text()').extract()[1]
        print "THE COST IS : ",cost
        #baseurl = response.meta["_splash_processed"]["args"]["url"]
        #print baseurl
        #splash_json = demjson.decode(response.body_as_unicode())
        #print response.body_as_unicode()
        #f=open("file2.html","w")
        #f.write(response.body_as_unicode().encode('utf-8'))
        #f.close()
