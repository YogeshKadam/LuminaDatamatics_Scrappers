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
    name = "denodo_splash"
    allowed_domains = ['la4th.org']
    start_urls = ['http://www.gastro24.de/Eisportionierer-aus-Edelstahl-von-Stoeckel-in-verschiedenen-Groessen']


    def parse(self, response):
        script = """
        function main(splash)
            ids=splash.args.id
            #print(ids)
            local url = splash.args.url
            assert(splash:go(url))
            assert(splash:wait(10))
            
            #assert(splash:runjs("$(".."'"..ids.."'"..").click()"))
            
            #assert(splash:wait(10))
            return {
                html = splash:html()
            }
        end
        """
        url="http://www.la4th.org/OpinionsByLodgedYear.aspx"
        yield scrapy.Request(url,      self.parse_link,       meta={
                             'splash': {
                             'args': {'lua_source': script                     },
                             'endpoint': 'execute'
                            }
                            })
        
                
    def parse_link(self,response):
        #print response.meta['splash']['args']['id']
        #cost=response.xpath('//div[@class="differential_price section_box well"]/ul/li/div/span//text()').extract()[1]
        #print "THE COST IS : ",cost
        f1=open('sample_denodo.html','w')
        f1.write(response.body)
        f1.close()
        print response.body