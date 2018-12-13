# -*- coding: utf-8 -*-
import scrapy
import urllib
#from shop.items1 import TyreItem,MatchItem,Refurb
import os
import time
import re
from scrapy.http.cookies import CookieJar
from court.courtitems import CourtItems

class amazonSpider(scrapy.Spider):
    imgcount = 1
    name = "ln"
    allowed_domains = []

    start_urls = ["http://www.courtrecords.alaska.gov/" ]  

    handle_httpstatus_list = [400]
    def parse(self,response):

        url1=str(response.xpath('//*[@id="acknowledgement"]/div[1]/a/@onclick').extract()[0]) .split(",")[1].replace("'","").strip()
        
        print "URL1 : %r"%url1
        cook=response.request.headers['Cookie']
        print cook, "lkkkkkkkkkkk"
       #"Host: "www.courtrecords.alaska.gov" , "Accept": "text/xml" , "Origin": "http://www.courtrecords.alaska.gov" , "Wicket-Ajax": "true" -H "Wicket-FocusedElementId": "id26" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3056.0 Safari/537.36" -H "Referer: http://www.courtrecords.alaska.gov/eservices/home.page.4" -H "Accept-Language: en-US,en;q=0.8" -H "Cookie: JSESSIONID=B89737E1DBAC75270193472ADCAC7D4D; _ga=GA1.2.176920323.1491154107" 
	   #url ="http://www.courtrecords.alaska.gov/eservices/home.page.4?x=LBdlKR9RiEw1AA-N8NnQwAads*HBqwzOmrXqtzsfJi2b*PshQpxiJR-Xdsq70aGvTQOw*3ADrEpru-3xPYosEuH22Ge7xIoZoTdmHasmNcAu4UW3iu-SeXVX*7hq8elkmyK8Fdz*0F*ZRuai*wWZs4gD7IoN8l3ffJJCuXhP0pY&random=0.7920623108833817"
       

        header= {"Host": "www.courtrecords.alaska.gov" ,"Accept":"text/html", "Origin": "http://www.courtrecords.alaska.gov", "Wicket-Ajax": "true" , "Wicket-FocusedElementId": str(response.xpath('//*[@id="acknowledgement"]/div[1]/a/@id').extract()[0]) , "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3056.0 Safari/537.36" , "Referer": str(response.url),"Accept-Language": "en-US,en;q=0.8" }
        my_data={str(response.xpath('//form/@id').extract()[0])+'_hf_0':'','linkFrag:beginButton':'1'}
        url= response.url+url1

        req = scrapy.http.FormRequest( url, method='POST',formdata= my_data,headers=header,  callback=self.parse1)

        req.cookies= {'JSESSIONID':cook.split("=")[1]}
        req.meta['cookie'] = {'JSESSIONID':cook.split("=")[1], '_ga':'GA1.2.519902805.1490944872', '_gat':'1'}
        req.meta['header'] = header
        #url ='http://www.courtrecords.alaska.gov/eservices/search.page.3?x=6xiLc1H40m*h0J0YemLTR8N*73mAgjjX4gEBZdaKyyCtHD2u3aDyrVTi*uzr1PiIHJwiFEIcR8kZn0*bMyVheYXoTpVJ7f8ixWqK1jgrKzE'
        #headers = {  'Origin': 'http://www.courtrecords.alaska.gov' , 'Accept-Encoding': 'gzip, deflate' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1' ,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36' ,'Content-Type': 'application/x-www-form-urlencoded' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' ,'Cache-Control': 'max-age=0' ,'Referer': 'http://www.courtrecords.alaska.gov/eservices/search.page.3?x=9VoDj3vv6TohzWytO1GIvQ' , 'Connection': 'keep-alive'}
        #my_data={'id19_hf_0':'','caseDscr':'4FA-08-01494CI','submitLink':'Search'}
		
        #result_req = scrapy.http.FormRequest(url, callback=self.parse1, headers=headers )

        #req = scrapy.http.FormRequest( url, method='POST',formdata= my_data,headers=headers, callback=self.parse1,)
        #req.cookies= {'JSESSIONID':'27E443576F193954C1F54D0759199670', '_ga':'GA1.2.519902805.1490944872'}
        print header,req.cookies
        print req.body
        yield req



    def parse1(self,response):
        print response.body, response.url
        #print response.url,response.body.split("CDATA[")[1].split("]]")[0], "hhhhhhhhhhhhh" ,response.meta['cookie'],response.meta['header']
        url = "http://www.courtrecords.alaska.gov/eservices/" +response.body.split("CDATA[")[1].split("]]")[0]
        headers = {  'Origin': 'http://www.courtrecords.alaska.gov' , 'Accept-Encoding': 'gzip, deflate' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1' ,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36' ,'Content-Type': 'application/x-www-form-urlencoded' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' ,'Cache-Control': 'max-age=0' ,'Referer': response.meta['header']['Referer'] , 'Connection': 'keep-alive'}
        print response.meta['cookie'],response.meta['header'], "lllllllllllllllllllllll"
        req = scrapy.Request(url,callback=self.parse3, headers=headers )
        req.cookies= response.meta['cookie'] 
        req.meta['cookie'] = response.meta['cookie']
        req.meta['header'] = response.meta['header']
	    
        yield req


    def parse3(self,response):
        print response.url,response.xpath('//form/@action').extract()
        url= response.url.split('?x')[0] + response.xpath('//form/@action').extract()[0]
        headers = {  'Origin': 'http://www.courtrecords.alaska.gov' , 'Accept-Encoding': 'gzip, deflate' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1' ,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36' ,'Content-Type': 'application/x-www-form-urlencoded' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' ,'Cache-Control': 'max-age=0' ,'Referer': response.url , 'Connection': 'keep-alive'}
        my_data={response.xpath('//form/@id').extract()[0]+'_hf_0':'','caseDscr':'4FA-08-01494CI','submitLink':'Search'}
        req = scrapy.http.FormRequest( url, method='POST',formdata= my_data,headers=headers, callback=self.parse11,)        
        req.cookies= response.meta['cookie']
        req.meta['cookie'] = response.meta['cookie']		
        #result_req = scrapy.http.FormRequest(url, callback=self.parse1, headers=headers )
        yield req

    def parse11(self,response):
        print response.url, response.xpath('//*[@id="grid$row:1$cell:2$link"]/@href').extract()[0]
        url= response.url.split('?x')[0] + response.xpath('//*[@id="grid$row:1$cell:2$link"]/@href').extract()[0]
        headers = {  'Origin': 'http://www.courtrecords.alaska.gov' , 'Accept-Encoding': 'gzip, deflate' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1' ,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36' ,'Content-Type': 'application/x-www-form-urlencoded' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' ,'Cache-Control': 'max-age=0' , 'Connection': 'keep-alive'}

        req = scrapy.Request(url,callback=self.parse12, headers=headers )
        req.cookies= response.meta['cookie'] 
        req.meta['cookie'] = response.meta['cookie']
        yield req

    def parse12(self,response):
        JsonDict={'Response':'Found', 'ReqestID':'12345', 'CaseTypeID':'2', 'CourtDescription':'Anchorage', 'CourtID':'AKANCD1', 'Cause of Action':'1', 'Casenumber':'4FA-08-01491CI', 'CaseStatusID':'2', 'FilingDate':'null', 'FeedID':'ANCG', 'CollectorID':'XXX', 'CollectDate':'Mm/dd/yyyy' }
        #print response.url,response.xpath('//*[@id="caseDetail"]').extract()
        sites = response.xpath('//*[@id="caseDetail"]/div["caseDetailHeader"]/div["caseInfo formSec bgClr1"]/div["caseInfo-col1 col"]/dt')
        item =CourtItems()
        item['key']=[]
        for site in sites:
            #print "I is : %r"%i
            item['key'].append("".join(site.xpath('text()').extract()).replace('[','').replace(']',''))
                        

        sites1 = response.xpath('//*[@id="caseDetail"]/div["caseDetailHeader"]/div["caseInfo formSec bgClr1"]/div["caseInfo-col1 col"]/dd')
        
        item['value']=[]
        for site1 in sites1:
            #print "I is : %r"%i
            item['value'].append("".join(site1.xpath('text()').extract()).replace('[','').replace(']',''))

        yield item
        print "KEY : %r"%item['key']
        print "VALUE : %r"%item['value']
        dictionary=dict(zip(item['key'],item['value']))
        
        print "DICTIONARY : %r"%dictionary

        print "JsonDict : %r"%JsonDict

        print "After Updating..."        
        JsonDict['FilingDate']=dictionary['File Date:']
        JsonDict['CaseStatusID']=dictionary['Case Status:']
        JsonDict['CourtDescription']=dictionary['Case Type']
        print "JsonDict : %r"%JsonDict



