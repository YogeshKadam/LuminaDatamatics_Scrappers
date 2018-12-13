import scrapy
import urllib
#from missouri.items1 import TyreItem,MatchItem,Refurb
import os
import time
import re
from scrapy.http.cookies import CookieJar
from urcourts.items import UrcourtsItem
import ssl
from OpenSSL import SSL
from scrapy.core.downloader.contextfactory import ScrapyClientContextFactory

 
class MyClientContextFactory(ScrapyClientContextFactory):

    def __init__(self):
        self.method = SSL.SSLv23_METHOD  # or SSL.SSLv3_METHOD
 
class amazonSpider(scrapy.Spider):

    name = "ln1"
    allowed_domains = []
    start_urls =["https://www.courts.mo.gov" ]  

    def parse(self,response):
        print  response.url, response.headers['Set-Cookie'][0]
        url = 'https://www.courts.mo.gov/casenet/cases/caseFileSearch.do'
        headers = {'Origin':'https://www.courts.mo.gov', 'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.8,ar;q=0.6,hi;q=0.4', 'Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Cache-Control': 'max-age:0', 'Referer': 'https://www.courts.mo.gov/casenet/cases/searchCases.do?searchType=caseNumber', 'Connection': 'keep-alive' }
        my_data = { 'courtId':'SW','inputVO.caseNo':'09SD-AC00235','findButton':'Find','inputVO.courtId':'SW','inputVO.caseNumber':'','inputVO.errFlag':'N','inputVO.ocnNo':'',}

        req = scrapy.http.FormRequest( url, method='POST',formdata= my_data,headers=headers, callback=self.parse1,)
        req.cookies = {'JSESSIONID':'0000lwuFBd-bsCDALEPwQi5V56h:1avs00urg'}
        print req.body
        yield req
    def parse1(self,response):
    	print response.url, response.body
    	url = 'https://www.courts.mo.gov/casenet/cases/header.do'
    	headers = {'Origin':'https://www.courts.mo.gov', 'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.8,ar;q=0.6,hi;q=0.4', 'Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Cache-Control': 'max-age:0', 'Referer': 'https://www.courts.mo.gov/casenet/cases/searchCases.do?searchType=caseNumber', 'Connection': 'keep-alive' }
        my_data = {'inputVO.caseNumber':'09SD-AC00235-01','inputVO.courtId':'SMPDB0001_CT35'}    	
        req = scrapy.http.FormRequest( url, method='POST',formdata= my_data,headers=headers, callback=self.parse2,)
        req.cookies = {'JSESSIONID':'00001BOCuNP2o_Y2TjLUUmejpA0:1avs01ajv'}
        
        yield req

    def parse2(self,response):
    	items = []
        
        judge1 = ''.join(response.xpath('//table[@class="detailRecordTable"]/tr[1]/td[2]/text()').extract())
        case_type = ''.join(response.xpath('//table[@class="detailRecordTable"]/tr[2]/td[4]/text()').extract())
        date_f1 = ''.join(response.xpath('//table[@class="detailRecordTable"]/tr[3]/td[4]/text()').extract())
        #print(case_type)
        location1 = ''.join(response.xpath('//table[@class="detailRecordTable"]/tr[2]/td[2]/text()').extract())
        disposition1  = ''.join(response.xpath('//table[@class="detailRecordTable"]/tr[3]/td[2]/text()').extract())
        date_of_disposition1 = ''.join(response.xpath('//table[@class="detailRecordTable"]/tr[3]/td[4]/text()').extract())
        judge_at_disposition1 = ''.join(response.xpath('//table[@class="detailRecordTable"]/tr[4]/td[2]/text()').extract())
        

        item = UrcourtsItem()
        item['judge'] = ''.join(str(judge1).strip())
        item['case_type'] = ''.join(str(case_type).strip())
        item['date_filed'] =  ''.join(str(date_f1).strip())
        item["location"] = ''.join(str(location1).strip())
        item["disposition"] = ''.join(str(disposition1).strip())
        item["date_of_disposition"] = ''.join(str(date_of_disposition1).strip())
        item["judge_at_disposition"] = ''.join(str(judge_at_disposition1).strip())
        items.append(item)
#       
        return(items) 
