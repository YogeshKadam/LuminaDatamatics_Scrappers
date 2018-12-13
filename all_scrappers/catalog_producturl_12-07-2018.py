# -*- coding: utf-8 -*-
import scrapy
import urllib

import os
import time
import re
import json


class CatalogItems(scrapy.Item):
    product_url= scrapy.Field()

class CatalogSpider(scrapy.Spider):
    imgcount = 1
    name = "catalog_producturl_12-07-2018"
    allowed_domains = []

    start_urls = ["https://catalog.services.book-fair.com/en/exhibitors-and-directories/exhibitors-a-z-search/action/list/controller/Exhibitors/filterhash/e3cbaeda8ce9da871e3a50ddc6b2c6d0/"]  

    def parse(self,response):
        urllist=response.xpath('//*[@id="div_AusstellerTreffer"]/table/tbody/tr')
        for urls in urllist:
            if urls.xpath('td[@class="col-sm-4 content_company"]/div/div[1]/div[2]/a/@href').extract():
                item=CatalogItems()
                item['product_url']="".join(urls.xpath('td[@class="col-sm-4 content_company"]/div/div[1]/div[2]/a/@href').extract())
                yield item
        i=20
        while i <=4740:
            urlpattern="https://catalog.services.book-fair.com/en/exhibitors-and-directories/exhibitors-a-z-search/action/list/controller/Exhibitors/xoffset/"+str(i)+"/filterhash/"
            req = scrapy.Request( urlpattern , callback=self.parse1)
            i+=20
            yield req
 

    def parse1(self,response):
        urllist=response.xpath('//*[@id="div_AusstellerTreffer"]/table/tbody/tr')
        for urls in urllist:
            if urls.xpath('td[@class="col-sm-4 content_company"]/div/div[1]/div[2]/a/@href').extract():
                item=CatalogItems()
                item['product_url']="".join(urls.xpath('td[@class="col-sm-4 content_company"]/div/div[1]/div[2]/a/@href').extract())
                yield item