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
from scrapy_splash import SplashRequest
import os


class LinkedinItems(scrapy.Item):
    name = scrapy.Field()
    company = scrapy.Field()
    college = scrapy.Field()


class LinkedinSpider(scrapy.Spider):
    name = "linkedin_search_keyword_splash"
    allowed_domains = ["linkedin.com"]
    #allowed_domains = ["flipkart.com"]

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ["https://www.linkedin.com/"]
    #start_urls = ["https://www.linkedin.com/pub/dir/Yogesh/Kadam"]

    def parse(self, response):
        #url="https://www.linkedin.com/pub/dir/Yogesh/Kadam"
        url="https://www.linkedin.com/search/results/index/?keywords=general%20counsel&origin=GLOBAL_SEARCH_HEADER"
        #req=scrapy.Request(url , headers={'authority': 'www.linkedin.com' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'referer': 'https://www.google.co.in/' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9'}, callback=self.parse1)
        req=scrapy.Request(url , headers={'authority': 'www.linkedin.com' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'referer': 'https://www.linkedin.com/' , 'accept-encoding':'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9' }, callback=self.parse1)
        #req=scrapy.Request(url , headers={'authority': 'www.linkedin.com' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'referer': 'https://www.linkedin.com/' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9'}, callback=self.parse1)
        #req=scrapy.Request(url ,callback=self.parse1)
        req.cookies={'visit':"v=1&M", '_chartbeat2':'DNoI1RB8-KIuCF80M4.1500966876379.1504264415172.0000000000000001', '_ga':'GA1.2.314132270.1490338107', 'bcookie':"v=2&cd36f31a-9c90-4dde-8f5c-882ea9ea0ad7", 'bscookie':"v=1&2018040907420239ce131b-e3bb-40f8-807b-165fea2f4e98AQGGTIxfino3WrcF-GtVPU6r7L4pZv38", '_guid':'bc4b62e0-201e-4a09-8533-63c7614be2dc', 'JSESSIONID':"ajax:7257142032599256502", '__utmc':'226841088', 'lang':"v=2&lang=en-us", '__utma':'226841088.314132270.1490338107.1526384861.1526446575.15', '__utmz':'226841088.1526446575.15.13.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)', 'leo_auth_token':"GST:Z9ztoYz_uYCEJ4t745RSNpzxLWaKrMVj_1zG-7kEDV1k0rt9rlmBvT:1526447233:c61c16272449110a3441f657060c05e28d3f4091", 'sl':"v=1&mlC-9", 'li_at':'AQEDARnBXAcFJCVhAAABY2dYWfQAAAFji2Td9FEApnE-RCl2x_axvTtiT_Z7kjBxyElNtjGAObvisoAN457k-W6y8vFi9b1LEf-vMMqG8OlD5XPWNnPiAPDQEktm24bWKh7ZvCA6cBMwPBDHwZXldNLz', 'liap':'true', 'RT':'s=1526448321391&r=https%3A%2F%2Fwww.linkedin.com%2Fgroups%2F4136932%2Fprofile', 'lidc':"b=SB07:g=52:u=22:i=1526448451:t=1526533634:s=AQGsq4NkYg69C_-WhnCgBjTDKCTUnVij", '_lipt':'CwEAAAFjZ2rv_TSPcoRLlm6zGpf1x2vW0Y4_qBCFDfO49kxSvp8j7AEv_vDh7cV5_BuYPqVkzNX2EBkjIYoj-IGJLt91CWxgzjy7OwOxwHUdhc9zo7eKLLczYIo4F_qOCyMTIaQz0r6OKnumtPXmUwmtSdl0QVO88Hx82CtbNIwjB6ptbmwdTsSoZ5NvNY52INEJ3M4Ep4oiX477ra2vvIZ2h49UhMTsyx1LTibOE60kGtAYZbu3UHGMuuJhkwXMOWupSqmF76X4Jycx9SHAGAgQJienntnUT1JsFCJyWVMoJC0M4S9mePk_9s3HwaoG9Rt8UAovHTp3xQ'}
        yield req


    def parse1(self, response):
        #url="https://www.linkedin.com/pub/dir/Yogesh/Kadam"
        #url="https://www.flipkart.com/asus-zenfone-max-pro-m1-5259-6434-store"
        url="https://www.linkedin.com/search/results/index/?keywords=general%20counsel&origin=GLOBAL_SEARCH_HEADER"
        req = SplashRequest(url,
                self.parse_link,
                endpoint='render.html',
                args={
                    'html': 1,
                    'wait':10.0,
                   
                },
                headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'},
            )
        yield req
        #yield scrapy.Request(url, self.parse_link, meta={'splash': {'args':{'lua_source': script},'endpoint':'execute',}})
        #yield scrapy.Request(url, self.parse_link, meta={'splash': {'args': {'html': 1,'lua_source': script}, 'endpoint': 'execute',
        #'splash_headers':{'authority': 'www.linkedin.com' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'referer': 'https://www.google.co.in/' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9'}, }})


    def parse_link(self,response):
        f=open("linkedin_file11111.html","w")
        f.write(response.body_as_unicode().encode('utf-8'))
        f.close()
