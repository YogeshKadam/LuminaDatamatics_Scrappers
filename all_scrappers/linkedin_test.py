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
    name = "linkedin_test"
    allowed_domains = []

    #start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    start_urls = ["https://www.linkedin.com/"]

    def parse(self, response):
        
        req = scrapy.Request("https://www.linkedin.com/in/yogesh-kadam-31b863100/", headers={'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'cache-control': 'max-age=0' , 'authority': 'www.linkedin.com' , 'referer': 'https://www.linkedin.com/'} ,callback=self.parse1)
        #req = scrapy.Request("https://www.linkedin.com/in/yogesh-kadam-31b863100/", callback=self.parse1)
        req.cookies = {'bcookie': 'v=2&c7adf5c0-071e-4100-8f15-fcc29cdb9ff2', 'bscookie':'v=1&20170320095536cafa59f2-6c46-4d41-8c8c-532486cf735dAQEngkVi9fWYXyUI-qVF7EERpmU5fIlg', 'visit':'v=1&M', '_chartbeat2':'DNoI1RB8-KIuCF80M4.1500966876379.1504264415172.0000000000000001', '_ga':'GA1.2.314132270.1490338107', 'lang':'v=2&lang=en-us', 'sdsc':'22%3A1%2C1517986701157%7ECONN%2C0DZbOMOu5WN1h8RGJQPNiHjnU4y8%3D', 'JSESSIONID':'ajax:3099466848599524778', '_gat':'1', 'leo_auth_token':'GST:Z9LpEMKEsVfgCJPQoaLP0JkxFD3ZZnv0wTzh6UTgDhUZJOGQr8eN1T:1517987172:c3d811bc499cc31978e90701d32cd297ab9c648b', 'sl':'v=1&AF8Rt', 'liap':'true', 'li_at':'AQEDARnBXAcE01UrAAABYW8WD_UAAAFhkyKT9U0AAdXq7SQov1NXhF_suI3QXOygi670hSeInjPYrFpsXEAw60gbqKBSzOYi5u01RDHzu4aITFmrmhqwb1YgVABrlZoupjU0WqeG2mg4EpoehZoppD2k', 'RT':'s=1517987094373&r=https%3A%2F%2Fwww.linkedin.com%2F', '_lipt':'CwEAAAFhbxYiDXrAwLmyW6Adno00w8u8qAzy5zn_tU14qtbrOSbOOce_1XTkCfvfEBK_i3x3DvmulAsOgUej8TTLn9hEa_k5F_LGV5bbFMt_DnPsNqaxU3Sy0BWpIqePwnA8hCP_7L9L9SwVb7nb_KaqI97QrSDsyLJVwJBYQ1HJOzPayZ4kg2H0rSoWdmAe52SmNiXV5rBt1dtU8iUSd3eJbPbHPCxOfmscb8cWslERimFQkZ1nF4e_6TeHx6QdiomjTioonCoItlGjFtKubd6JZhnc7tTMlwYyn1-3D3sL0PaL7Unqf7x0c7sXgCsDOgUbZbHNsywq', 'lidc':'b=VGST03:g=668:u=1:i=1517987160:t=1518073560:s=AQFSlfSJb2v5EtlLRHSVdckHuBQV-Rlm'}
        time.sleep(.5)
        yield req

    def parse1(self, response):
        #f1=open("linkedin.html","w")
        #f1.write(response.body)
        #f1.close()
        #print response.body
        #print " ".join(response.xpath('//*[@id="fast-track-message"]/div//text()').extract())
        #print " ".join(response.xpath('//*[@id="unifiedLocation_feature_div"]/div/div/span[2]/a/span//text()').extract())
        item=LinkedinItems()
        name=response.xpath('//*[@id="ember4528"]/div[1]/h1//text()').extract()
        print "Name : ",name
        college = response.xpath('//*[@id="ember4528"]/div[2]/h3[2]//text()').extract()
        print "college : ",college
        company = response.xpath('//*[@id="ember4528"]/div[2]/h3[1]//text()').extract()
        print "company : ",company

        #item['name']=name[0]
        #item['college']=college[0]
        #item['company']=company[0]
        #yield item
