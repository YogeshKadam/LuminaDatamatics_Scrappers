# -*- coding: utf-8 -*-
import scrapy
import urllib

import os
import time
import re
import json


class PacerItems(scrapy.Item):
    list_price= scrapy.Field()
    your_price= scrapy.Field()
    model_number= scrapy.Field()
    number_of_items= scrapy.Field()

class PacerSpider(scrapy.Spider):
    imgcount = 1
    name = "pacer_login_scrapper"
    allowed_domains = []

    start_urls = ['https://pacer.login.uscourts.gov/csologin/login.jsf']

    def parse(self, response):
        formdata = {'login':'login', 'login:loginName':'cc0002', 'login:password':'courts66', 'login:clientCode':'Lumina', 'login:fbtnLogin':'', 'javax.faces.ViewState':'stateless'} 
        #requsturl=scrapy.FormRequest('https://digitalassets.wolterskluwer.be/user/doLogin/', meta = {'dont_redirect': True,'handle_httpstatus_list': [302]},formdata= formdata ,headers={'origin': 'https://digitalassets.wolterskluwer.be', 'referer': 'https://digitalassets.wolterskluwer.be/login/', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'cache-control': 'max-age=0', 'accept-language': 'en-US,en;q=0.9', 'accept-encoding': 'gzip, deflate, br', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', 'content-type': 'application/x-www-form-urlencoded', 'authority': 'digitalassets.wolterskluwer.be', 'upgrade-insecure-requests': '1'},callback=self.parse1,method="POST")
        requsturl=scrapy.FormRequest('https://pacer.login.uscourts.gov/csologin/login.jsf', meta = {'dont_redirect': True,'handle_httpstatus_list': [302]},formdata= formdata ,headers={'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://pacer.login.uscourts.gov' , 'Upgrade-Insecure-Requests': '1' , 'Content-Type': 'application/x-www-form-urlencoded' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://pacer.login.uscourts.gov/csologin/login.jsf' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' }, callback=self.parse1,method="POST")
        #requsturl.cookies ={ 'DefaultLocale':'en_US', 'JSESSIONID':'1C3FDBF21A509C6AB55379F6A8C449A5', 'bynder':'716DCA54-C9D5-4486-981523FB5D28B0F2' }
        yield requsturl
    def parse1(self, response):
        requsturl=scrapy.http.Request("https://www.pacer.gov/psco/cgi-bin/links.pl",headers={'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://pacer.login.uscourts.gov' , 'Upgrade-Insecure-Requests': '1' , 'Content-Type': 'application/x-www-form-urlencoded' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://pacer.login.uscourts.gov/csologin/login.jsf' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' }, callback=self.parse2)
        yield requsturl
        #print response.headers
    def parse2(self, response):
        with open("pacer_data12.html",'w') as fd:
                   fd.write(response.body)