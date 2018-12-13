# -*- coding: utf-8 -*-
import scrapy
import urllib

import os
import time
import re
import json
import re
import datetime
import demjson
from scrapy.http.cookies import CookieJar
import scrapy
import urllib
#from shop.items1 import TyreItem,MatchItem,Refurb
import os


class LinkedinItems(scrapy.Item):
    name = scrapy.Field()
    company = scrapy.Field()
    college = scrapy.Field()


class LinkedinSpider(scrapy.Spider):
    imgcount = 1
    name = "linkedin_splash"
    allowed_domains = ["linkedin.com"]
    #allowed_domains = ["https://www.linkedin.com/"]

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ["https://www.linkedin.com/"]
    #start_urls = ["https://www.linkedin.com/pub/dir/Yogesh/Kadam"]




    def parse(self, response):
        url="https://www.linkedin.com/pub/dir/Yogesh/Kadam"
        req=scrapy.Request(url , headers={'authority': 'www.linkedin.com' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'referer': 'https://www.google.co.in/' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9'}, callback=self.parse1)
        #req=scrapy.Request(url ,callback=self.parse1)
        req.cookies={'visit':'v=1&M', '_chartbeat2':'DNoI1RB8-KIuCF80M4.1500966876379.1504264415172.0000000000000001', '_ga':'GA1.2.314132270.1490338107', 'bcookie':'v=2&cd36f31a-9c90-4dde-8f5c-882ea9ea0ad7', 'bscookie':'v=1&2018040907420239ce131b-e3bb-40f8-807b-165fea2f4e98AQGGTIxfino3WrcF-GtVPU6r7L4pZv38', '_guid':'bc4b62e0-201e-4a09-8533-63c7614be2dc', '__utma':'226841088.314132270.1490338107.1525435525.1525435525.1', '__utmc':'226841088', '__utmz':'226841088.1525435525.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)', 'lang':'v=2&lang=en-us', 'sdsc':'22%3A1%2C1525677272300%7ECONN%2C0KoGLfHRG8S7m9nYwhy3eYpzWv2A%3D', '_lipt':'CwEAAAFjOXuQDVj6kRUiJrioDPq0PqBQV24rNGKy9jC1cf3Je64Xabjcn2zsBf-dexE0RztlHUg-v8R1O61bSXHMzVGtw1eefJ3clHafZHJfaPU86jBheXl1o4o61kHlmEDKYxiaT4Y1ixkI1e1XsV4keYpJNjNqlVuMSDWCEeG3fSp0HpaS9ZERIH0owYvodWwVGMb0oAJNTL9FlG6Y5Y76X7idQ3XILl4xpNiprzY1xJs-Javwppi8DwvWojkqhCT2Ctw5c-GTjeazDhH3lpVQrdhKJoUFjkBOk6Jyr05a8-YpgAdv7X0rHqYjdjulbHnz5f_gmen4yQ', 'JSESSIONID':'ajax:4744771991265787761', 'lidc':'b=OGST08:g=556:u=1:i=1525677815:t=1525764215:s=AQGGRNli4lGigJchMempb2ulMe7sHlDP'}
        yield req

    def parse1(self,response):
        #f=open("linkedin_file1.html","w")
        #f.write(response.body)
        #f.close()
        namelist=response.xpath('//*[@id="wrapper"]/div[2]/div[2]/ul/li')
        for names in namelist:
            name=names.xpath('div/div/h3/a/text()').extract()[0].encode('utf-8')
            headline=names.xpath('div/div/p/text()').extract()[0].encode('utf-8')
            print name, " -> ",headline