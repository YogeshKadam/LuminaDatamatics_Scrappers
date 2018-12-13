# -*- coding: utf-8 -*-
import scrapy
#from scrapy.spiders import Spider
import urllib
#from shop.items1 import TyreItem,MatchItem,Refurb
import os
import time
import re
import ssl
from OpenSSL import SSL
from scrapy.core.downloader.contextfactory import ScrapyClientContextFactory


class MyClientContextFactory(ScrapyClientContextFactory):

    def __init__(self):

        self.method = SSL.SSLv23_METHOD  # or SSL.SSLv3_METHOD


class amazonSpider(scrapy.Spider):
    #imgcount = 1
    #handle_httpstatus_list = [404]
    name = "ln2"
    allowed_domains = []
    start_urls = ['https://www.courts.mo.gov/casenet/cases/searchCases.do?searchType=caseNumber']  
    
    def parse(self,response):
        
        cook=   response.headers['Set-Cookie'].split(";")[0]
        url = "https://www.courts.mo.gov/casenet/cases/caseFileSearch.do"
        #headers = {"Host":"https://www.courts.mo.gov", "Accept-Encoding":"gzip, deflate, sdch, br", "Accept-Language":"en-US,en;q=0.8","Upgrade-Insecure-Requests": "1", "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Referer":"http//www.courts.mo.gov/casenet/base/welcome.do", "Connection": "keep-alive"}
        headers = {'Origin': 'https://www.courts.mo.gov' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1' ,'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36' , 'Content-Type': 'application/x-www-form-urlencoded' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' , 'Cache-Control': 'max-age=0' , 'Referer': 'https://www.courts.mo.gov/casenet/cases/searchCases.do?searchType=caseNumber' , 'Connection': 'keep-alive'}
        #my_data = {'courtId':'SW', 'inputVO.caseNo':'09SD-AC00235', 'findButton':'Find', 'inputVO.courtId':'SW', 'inputVO.caseNumber':'', 'inputVO.errFlag':'N', 'inputVO.ocnNo':''}         
        my_data =  {"courtId":"SW","inputVO.caseNo":"09SD-AC00235","findButton":"Find","inputVO.courtId":"SW","inputVO.caseNumber":"","inputVO.errFlag":"N","inputVO.ocnNo":""}
        print cook.split("=")[1], "fsfs"
        req = scrapy.http.FormRequest( url, method='POST',formdata= my_data,headers=headers,callback=self.parse1,)
        req.cookies = {'JSESSIONID': cook.split("=")[1]}
        print req.cookies, req.body
        yield req
    def parse1(self,response):
        print response.url, response.status, response.headers, response.xpath('//td/a/@href').extract()
        url = "https://www.courts.mo.gov/casenet/cases/header.do"
        headers = {'Origin': 'https://www.courts.mo.gov' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1' ,'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36' , 'Content-Type': 'application/x-www-form-urlencoded' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' , 'Cache-Control': 'max-age=0' , 'Referer': 'https://www.courts.mo.gov/casenet/cases/searchCases.do?searchType=caseNumber' , 'Connection': 'keep-alive'}
        my_data = {'inputVO.caseNumber': '09SD-AC00235-01', 'inputVO.courtId': 'SMPDB0001_CT35', }
        req = scrapy.Request(url, method='POST',formdata=my_data, headers=headers,callback=self.parse2,)
        req.cookies = response.meta['cookies'] 
        req.meta['cookie'] = response.meta['cookies']
        yield req 
    
    def parse2(self,response):
        pass
