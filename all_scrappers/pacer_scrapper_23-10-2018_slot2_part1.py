# -*- coding: utf-8 -*-
import scrapy
import urllib
from requests_toolbelt import MultipartEncoder
import os
import time
import re
import json


class PacerItems(scrapy.Item):
    pdflink= scrapy.Field()
    case_number= scrapy.Field()
    base_url= scrapy.Field()
    case_name= scrapy.Field()
    description= scrapy.Field()
    date_filed= scrapy.Field()
    initial_url= scrapy.Field()

class PacerSpider(scrapy.Spider):
    imgcount = 1
    name = "pacer_scrapper_23-10-2018_slot2_part1"
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
        urls_done=[]
        list1=[
#["10","https://ecf.ilsb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
#["6","https://ecf.wvsb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
#["7","https://ecf.rib.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["8","https://ecf.wiwb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
#["25","https://ecf.vaeb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
"""["1","https://ecf.mdb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["2","https://ecf.alsb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["3","https://ecf.kywb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["4","https://ecf.laeb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["5","https://ecf.idb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["6","https://ecf.vtb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["7","https://ecf.orb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["8","https://ecf.gasb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["9","https://ecf.neb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["10","https://ecf.ilnb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["11","https://ecf.kyeb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["12","https://ecf.paeb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["13","https://ecf.mab.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["14","https://ecf.ksb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["15","https://ecf.mssb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["16","https://ecf.flmb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["17","https://ecf.tneb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["18","https://ecf.utb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["19","https://ecf.wieb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["20","https://ecf.waeb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["21","https://ecf.prb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["22","https://ecf.cacb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["23","https://ecf.txnb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["24","https://ecf.canb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["25","https://ecf.vaeb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["26","https://ecf.caeb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["27","https://ecf.pamb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["28","https://ecf.txeb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["29","https://ecf.ohnb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["30","https://ecf.txsb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["31","https://ecf.ncmb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["32","https://ecf.txwb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["33","https://ecf.nceb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["34","https://ecf.nyeb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["35","https://ecf.nhb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["36","https://ecf.mowb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["37","https://ecf.mnb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["38","https://ecf.moeb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["39","https://ecf.nysb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["40","https://ecf.nynb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["41","https://ecf.tnmb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["42","https://ecf.vawb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["43","https://ecf.wawb.uscourts.gov/cgi-bin/WrtOpRpt.pl"],"""
]
        #print "Total US District courts : ",len(list1)
        for link in list1:
            #link=li.xpath('@href').extract()[0]
            #name=li.xpath('text()').extract()[0].replace('\n','').replace('\t','').replace('\r','')
            req=scrapy.http.Request(link[1],headers={'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://pacer.login.uscourts.gov' , 'Upgrade-Insecure-Requests': '1' , 'Content-Type': 'application/x-www-form-urlencoded' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://pacer.login.uscourts.gov/csologin/login.jsf' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' }, callback=self.parse6)
            req.meta['base_url']=link[1].split('cgi-bin')[0]
            req.meta['initial_url']=link[1]
            if link[1] not in urls_done:
                yield req
        #req=scrapy.http.Request(list1,headers={'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://pacer.login.uscourts.gov' , 'Upgrade-Insecure-Requests': '1' , 'Content-Type': 'application/x-www-form-urlencoded' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://pacer.login.uscourts.gov/csologin/login.jsf' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' }, callback=self.parse3)
        #req.meta['base_url']=list1
        #yield req
			
    def parse6(self, response):
        #with open("pacer_html4444.html",'w') as f1:
        #    f1.write(response.body)
        form_data={'all_case_ids':'0', 'case_num':'', 'last_name':'', 'first_name':'', 'middle_name':'', 'office':'', 'nsuit':'', 'case_type':'', 'cause':'', 'case_flags':'', 'filed_from':'1/12/2018', 'filed_to':'10/12/2018', 'ShowFull':'1', 'Key1':'cs_sort_case_numb', 'UserType':''}
        me = MultipartEncoder(fields=form_data)
        me_boundary = me.boundary[2:]  #need this in headers
        me_length = me.len             #need this in headers
        me_body = me.to_string()
        header={'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://ecf.almd.uscourts.gov' , 'Upgrade-Insecure-Requests': '1' , 'Content-Type': 'multipart/form-data; charset=utf-8; boundary=' + me_boundary,  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://ecf.almd.uscourts.gov/' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9'}
        #bodydata='------WebKitFormBoundarylLLtL7XgUBaPnHEp\r\nContent-Disposition: form-data; name="all_case_ids"\r\n\r\n0\r\n------WebKitFormBoundarylLLtL7XgUBaPnHEp\r\nContent-Disposition: form-data; name="case_num"\r\n\r\n\r\n------WebKitFormBoundarylLLtL7XgUBaPnHEp\r\nContent-Disposition: form-data; name="last_name"\r\n\r\n\r\n------WebKitFormBoundarylLLtL7XgUBaPnHEp\r\nContent-Disposition: form-data; name="first_name"\r\n\r\n\r\n------WebKitFormBoundarylLLtL7XgUBaPnHEp\r\nContent-Disposition: form-data; name="middle_name"\r\n\r\n\r\n------WebKitFormBoundarylLLtL7XgUBaPnHEp\r\nContent-Disposition: form-data; name="office"\r\n\r\n\r\n------WebKitFormBoundarylLLtL7XgUBaPnHEp\r\nContent-Disposition: form-data; name="nsuit"\r\n\r\n\r\n------WebKitFormBoundarylLLtL7XgUBaPnHEp\r\nContent-Disposition: form-data; name="case_type"\r\n\r\n\r\n------WebKitFormBoundarylLLtL7XgUBaPnHEp\r\nContent-Disposition: form-data; name="cause"\r\n\r\n\r\n------WebKitFormBoundarylLLtL7XgUBaPnHEp\r\nContent-Disposition: form-data; name="case_flags"\r\n\r\n\r\n------WebKitFormBoundarylLLtL7XgUBaPnHEp\r\nContent-Disposition: form-data; name="filed_from"\r\n\r\n9/1/2018\r\n------WebKitFormBoundarylLLtL7XgUBaPnHEp\r\nContent-Disposition: form-data; name="filed_to"\r\n\r\n9/21/2018\r\n------WebKitFormBoundarylLLtL7XgUBaPnHEp\r\nContent-Disposition: form-data; name="ShowFull"\r\n\r\n1\r\n------WebKitFormBoundarylLLtL7XgUBaPnHEp\r\nContent-Disposition: form-data; name="Key1"\r\n\r\ncs_sort_case_numb\r\n------WebKitFormBoundarylLLtL7XgUBaPnHEp\r\nContent-Disposition: form-data; name="UserType"\r\n\r\n\r\n------WebKitFormBoundarylLLtL7XgUBaPnHEp--\r\n'
        urlcode=response.xpath('//*[@id="cmecfMainContent"]/form/@action').extract()[0]
        #print urlcode
        link=response.meta['base_url'].rstrip('/')+urlcode.replace('..','')
        #print link
        #req=scrapy.FormRequest(link, meta = {'dont_redirect': True,'handle_httpstatus_list': [500,302]}, body=bodydata, headers={'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://pacer.login.uscourts.gov' , 'Upgrade-Insecure-Requests': '1' , 'Content-Type': 'application/x-www-form-urlencoded' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://pacer.login.uscourts.gov/csologin/login.jsf' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' }, callback=self.parse7, method="POST")
        req=scrapy.Request(link, meta = {'dont_redirect': True,'handle_httpstatus_list': [500,302]}, body=me_body, headers=header, callback=self.parse7, method="POST")
        req.cookies={'_ga':'GA1.2.1437274789.1534401822', 'ClientValidation':"", 'ClientCodeDescription':"", 'MENU':'slow', 'PacerSession':'0oxdQUxn4oxv1KlUJAvfr4kkFQEROH2k0tiDHGNeUEdE2oO5N3NeEJmy5AsVBQiPvefaUJSXI9DSOfshoFpoY94Bgv4EJaiC2mt7Zv2ecmzRpIT4nBqY2COBdjf3YQ0Q', 'NextGenCSO':'0oxdQUxn4oxv1KlUJAvfr4kkFQEROH2k0tiDHGNeUEdE2oO5N3NeEJmy5AsVBQiPvefaUJSXI9DSOfshoFpoY94Bgv4EJaiC2mt7Zv2ecmzRpIT4nBqY2COBdjf3YQ0Q', 'PacerClientCode':'Lumina', 'PacerClient':"", 'ClientDesc':"", 'PacerPref':"receipt=Y"}
        req.meta['base_url']=response.meta['base_url']
        req.meta['initial_url']=response.meta['initial_url']
        #req.meta['base_court_name']=response.meta['base_court_name']
        yield req
		
    def parse7(self, response):
        #link=response.xpath('//*[@id="cmecfMainContent"]/center[1]/table/tr[@valign="top"]')
        #link=response.xpath('//*[@id="cmecfMainContent"]/center[1]/table/tbody/tr[2]/td[@align="center"]/a/@href').extract()[0]
        #with open("pacer_html5555.html",'w') as f1:
        #    f1.write(response.body)valign="top"
        list1=response.xpath('//*[@id="cmecfMainContent"]/center[1]/table/tr[@valign="top"]')
        #list1=response.xpath('//*[@id="cmecfMainContent"]/center[1]/table/tr[2]')
        for li in list1:
            try: 
                case_number=li.xpath('td[1]/a/text()').extract()[0].split(' ',1)[0]
                case_name=li.xpath('td[1]/a/text()').extract()[0].split(' ',1)[1]
            except:
                case_number=""
                case_name=""
            link=li.xpath('td[@align="center"]/a/@href').extract()[0]
            #codes=li.xpath('td[1]/a/@href').extract()[0]
            #print "PARSE7 : ",codes
            description=", ".join(li.xpath('td[4]//text()').extract())
            date_filed=li.xpath('td[2]/text()').extract()[0]
            #print "PARSE 7 : ",case_number,case_name,link,codes,description,date_filed
            #link=response.xpath('//*[@id="cmecfMainContent"]/center[1]/table/tr[2]/td[3]/a/@href').extract()[0]
            #codes=response.xpath('//*[@id="cmecfMainContent"]/center[1]/table/tr[2]/td[3]/a/@onclick').extract()[0]
            #print link, codes
            #code1=codes.split('?')[1]
            #code2=codes.split('(')[1].split(',')[2].strip("'")
            #code3=codes.split('(')[1].split(',')[5].strip("'")
            header={'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://ecf.almd.uscourts.gov' , 'Upgrade-Insecure-Requests': '1' ,  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://ecf.almd.uscourts.gov/' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9'}
            req=scrapy.Request(response.meta['base_url'].rstrip('/')+link, meta = {'dont_redirect': True,'handle_httpstatus_list': [500,302]}, headers=header, callback=self.parse8)
            req.cookies={'_ga':'GA1.2.1437274789.1534401822', 'ClientValidation':"", 'ClientCodeDescription':"", 'MENU':'slow', 'PacerSession':'0oxdQUxn4oxv1KlUJAvfr4kkFQEROH2k0tiDHGNeUEdE2oO5N3NeEJmy5AsVBQiPvefaUJSXI9DSOfshoFpoY94Bgv4EJaiC2mt7Zv2ecmzRpIT4nBqY2COBdjf3YQ0Q', 'NextGenCSO':'0oxdQUxn4oxv1KlUJAvfr4kkFQEROH2k0tiDHGNeUEdE2oO5N3NeEJmy5AsVBQiPvefaUJSXI9DSOfshoFpoY94Bgv4EJaiC2mt7Zv2ecmzRpIT4nBqY2COBdjf3YQ0Q', 'PacerClientCode':'Lumina', 'PacerClient':"", 'ClientDesc':"", 'PacerPref':"receipt=Y"}
            req.meta['pdfname']=response.meta['base_url'].split('/')[2].replace('.','_')+"_"+link.split('/')[-1]+".pdf"
            req.meta['base_url']=response.meta['base_url']
            req.meta['case_number']=case_number
            req.meta['case_name']=case_name
            req.meta['description']=description
            req.meta['date_filed']=date_filed
            #req.meta['code_number']=code1
            req.meta['initial_url']=response.meta['initial_url']
            yield req
			
    def parse8(self, response):
        #with open("pacer_html101010102.html",'w') as f1:
        #    f1.write(response.body)
        #print response.xpath('//*[@id="cmecfMainContent"]/form/center/table/input/@value').extract()
        if "".join(response.xpath('//*[@id="cmecfMainContent"]/p[1]/text()').extract()).replace(' ','').replace('\n','').replace('\t','').replace('\r','').lower().find('documentselectionmenu')>-1:
            url=response.xpath('//*[@id="cmecfMainContent"]/table/tr[2]/td[1]/a/@href').extract()[0]
            header={'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://ecf.almd.uscourts.gov' , 'Upgrade-Insecure-Requests': '1' ,  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://ecf.almd.uscourts.gov/' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9'}
            req=scrapy.Request(response.meta['base_url'].rstrip('/')+url, meta = {'dont_redirect': True,'handle_httpstatus_list': [500,302]}, headers=header, callback=self.parse9)
            req.cookies={'_ga':'GA1.2.1437274789.1534401822', 'ClientValidation':"", 'ClientCodeDescription':"", 'MENU':'slow', 'PacerSession':'0oxdQUxn4oxv1KlUJAvfr4kkFQEROH2k0tiDHGNeUEdE2oO5N3NeEJmy5AsVBQiPvefaUJSXI9DSOfshoFpoY94Bgv4EJaiC2mt7Zv2ecmzRpIT4nBqY2COBdjf3YQ0Q', 'NextGenCSO':'0oxdQUxn4oxv1KlUJAvfr4kkFQEROH2k0tiDHGNeUEdE2oO5N3NeEJmy5AsVBQiPvefaUJSXI9DSOfshoFpoY94Bgv4EJaiC2mt7Zv2ecmzRpIT4nBqY2COBdjf3YQ0Q', 'PacerClientCode':'Lumina', 'PacerClient':"", 'ClientDesc':"", 'PacerPref':"receipt=Y"}
            req.meta['pdfname']=response.meta['pdfname']
            req.meta['base_url']=response.meta['base_url']
            req.meta['case_number']=response.meta['case_number']
            req.meta['case_name']=response.meta['case_name']
            req.meta['description']=response.meta['description']
            req.meta['date_filed']=response.meta['date_filed']
            #req.meta['code_number']=response.meta['code_number']
            req.meta['initial_url']=response.meta['initial_url']
            yield req
        if "".join(response.xpath('//*[@id="cmecfMainContent"]/form/input/@value').extract()).replace(' ','').replace('\n','').replace('\t','').replace('\r','').lower().find('viewdocument')>-1:
            #print "FOUND 2nd IF"
            new_url=response.xpath('//form/@action').extract()[0]
            codes=response.xpath('//form/@onsubmit').extract()[0]
            code1=codes.split('(')[1].split(',')[1].replace("'","").replace('"','').replace(" ","")
            #print "new url : ",new_url
            form_data={'caseid':code1, 'got_receipt':'1'}
            #print "form-data : ",form_data
            #header={'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://ecf.almd.uscourts.gov' , 'Upgrade-Insecure-Requests': '1' ,  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://ecf.almd.uscourts.gov/' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9'}
            header={'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://ecf.alsb.uscourts.gov' , 'Upgrade-Insecure-Requests': '1' , 'Content-Type': 'application/x-www-form-urlencoded' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://ecf.alsb.uscourts.gov/' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' }
            #req=scrapy.FormRequest(new_url, meta = {'dont_redirect': True,'handle_httpstatus_list': [500,302]}, formdata=form_data, headers=header, callback=self.parse10, method="POST")
            req=scrapy.FormRequest(new_url, formdata=form_data, headers=header, callback=self.parse10, method="POST")
            #req.cookies={'_ga':'GA1.2.1437274789.1534401822', 'ClientValidation':"", 'ClientCodeDescription':"", 'MENU':'slow', 'PacerSession':'0oxdQUxn4oxv1KlUJAvfr4kkFQEROH2k0tiDHGNeUEdE2oO5N3NeEJmy5AsVBQiPvefaUJSXI9DSOfshoFpoY94Bgv4EJaiC2mt7Zv2ecmzRpIT4nBqY2COBdjf3YQ0Q', 'NextGenCSO':'0oxdQUxn4oxv1KlUJAvfr4kkFQEROH2k0tiDHGNeUEdE2oO5N3NeEJmy5AsVBQiPvefaUJSXI9DSOfshoFpoY94Bgv4EJaiC2mt7Zv2ecmzRpIT4nBqY2COBdjf3YQ0Q', 'PacerClientCode':'Lumina', 'PacerClient':"", 'ClientDesc':"", 'PacerPref':"receipt=Y"}
            req.cookies={'_ga':'GA1.2.1437274789.1534401822', 'ClientValidation':"", 'ClientCodeDescription':"", 'PacerSession':'7wvtfCNmaGnxZ7RQJ3UOzKLJNEqsHEottcOOePvY7CCLydweD9xPWcmf2XLrwHee09jaipsA51y2egn1UG5ogEK2gQ5xCZk2lXwTKL8jfjyJaZkQ5Bcuj9LqUKvUJmP7', 'NextGenCSO':'7wvtfCNmaGnxZ7RQJ3UOzKLJNEqsHEottcOOePvY7CCLydweD9xPWcmf2XLrwHee09jaipsA51y2egn1UG5ogEK2gQ5xCZk2lXwTKL8jfjyJaZkQ5Bcuj9LqUKvUJmP7', 'PacerClientCode':'Lumina', 'PacerClient':"", 'ClientDesc':"", 'PacerPref':"receipt=Y"}
            req.meta['pdfname']=response.meta['pdfname']
            req.meta['base_url']=response.meta['base_url']
            req.meta['case_number']=response.meta['case_number']
            req.meta['case_name']=response.meta['case_name']
            req.meta['description']=response.meta['description']
            req.meta['date_filed']=response.meta['date_filed']
            req.meta['code_number']=code1
            req.meta['initial_url']=response.meta['initial_url']
            yield req
        if "".join(response.xpath('//*[@id="cmecfMainContent"]/form/center/table/input/@value').extract()).replace(' ','').replace('\n','').replace('\t','').replace('\r','').lower().find('viewdocument')>-1:
            #print "FOUND 3rd IF"
            new_url=response.xpath('//form/@action').extract()[0]
            codes=response.xpath('//form/@onsubmit').extract()[0]
            code1=codes.split('(')[1].split(',')[1].replace("'","").replace('"','').replace(" ","")
            #print "new url : ",new_url
            form_data={'caseid':code1, 'got_receipt':'1'}
            #print "form-data : ",form_data
            #header={'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://ecf.almd.uscourts.gov' , 'Upgrade-Insecure-Requests': '1' ,  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://ecf.almd.uscourts.gov/' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9'}
            header={'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://ecf.alsb.uscourts.gov' , 'Upgrade-Insecure-Requests': '1' , 'Content-Type': 'application/x-www-form-urlencoded' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://ecf.alsb.uscourts.gov/' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' }
            #req=scrapy.FormRequest(new_url, meta = {'dont_redirect': True,'handle_httpstatus_list': [500,302]}, formdata=form_data, headers=header, callback=self.parse10, method="POST")
            req=scrapy.FormRequest(new_url, formdata=form_data, headers=header, callback=self.parse10, method="POST")
            #req.cookies={'_ga':'GA1.2.1437274789.1534401822', 'ClientValidation':"", 'ClientCodeDescription':"", 'MENU':'slow', 'PacerSession':'0oxdQUxn4oxv1KlUJAvfr4kkFQEROH2k0tiDHGNeUEdE2oO5N3NeEJmy5AsVBQiPvefaUJSXI9DSOfshoFpoY94Bgv4EJaiC2mt7Zv2ecmzRpIT4nBqY2COBdjf3YQ0Q', 'NextGenCSO':'0oxdQUxn4oxv1KlUJAvfr4kkFQEROH2k0tiDHGNeUEdE2oO5N3NeEJmy5AsVBQiPvefaUJSXI9DSOfshoFpoY94Bgv4EJaiC2mt7Zv2ecmzRpIT4nBqY2COBdjf3YQ0Q', 'PacerClientCode':'Lumina', 'PacerClient':"", 'ClientDesc':"", 'PacerPref':"receipt=Y"}
            req.cookies={'_ga':'GA1.2.1437274789.1534401822', 'ClientValidation':"", 'ClientCodeDescription':"", 'PacerSession':'7wvtfCNmaGnxZ7RQJ3UOzKLJNEqsHEottcOOePvY7CCLydweD9xPWcmf2XLrwHee09jaipsA51y2egn1UG5ogEK2gQ5xCZk2lXwTKL8jfjyJaZkQ5Bcuj9LqUKvUJmP7', 'NextGenCSO':'7wvtfCNmaGnxZ7RQJ3UOzKLJNEqsHEottcOOePvY7CCLydweD9xPWcmf2XLrwHee09jaipsA51y2egn1UG5ogEK2gQ5xCZk2lXwTKL8jfjyJaZkQ5Bcuj9LqUKvUJmP7', 'PacerClientCode':'Lumina', 'PacerClient':"", 'ClientDesc':"", 'PacerPref':"receipt=Y"}
            req.meta['pdfname']=response.meta['pdfname']
            req.meta['base_url']=response.meta['base_url']
            req.meta['case_number']=response.meta['case_number']
            req.meta['case_name']=response.meta['case_name']
            req.meta['description']=response.meta['description']
            req.meta['date_filed']=response.meta['date_filed']
            req.meta['code_number']=code1
            req.meta['initial_url']=response.meta['initial_url']
            yield req

    def parse9(self,response):
        new_url=response.xpath('//form/@action').extract()[0]
        codes=response.xpath('//form/@onsubmit').extract()[0]
        code1=codes.split('(')[1].split(',')[1].replace("'","").replace('"','').replace(" ","")
        form_data={'caseid':code1, 'got_receipt':'1'}
        header={'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://ecf.almd.uscourts.gov' , 'Upgrade-Insecure-Requests': '1' ,  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://ecf.almd.uscourts.gov/' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9'}
        req=scrapy.FormRequest(new_url, meta = {'dont_redirect': True,'handle_httpstatus_list': [500,302]}, headers=header, formdata=form_data, callback=self.parse10, method="POST")
        req.cookies={'_ga':'GA1.2.1437274789.1534401822', 'ClientValidation':"", 'ClientCodeDescription':"", 'MENU':'slow', 'PacerSession':'0oxdQUxn4oxv1KlUJAvfr4kkFQEROH2k0tiDHGNeUEdE2oO5N3NeEJmy5AsVBQiPvefaUJSXI9DSOfshoFpoY94Bgv4EJaiC2mt7Zv2ecmzRpIT4nBqY2COBdjf3YQ0Q', 'NextGenCSO':'0oxdQUxn4oxv1KlUJAvfr4kkFQEROH2k0tiDHGNeUEdE2oO5N3NeEJmy5AsVBQiPvefaUJSXI9DSOfshoFpoY94Bgv4EJaiC2mt7Zv2ecmzRpIT4nBqY2COBdjf3YQ0Q', 'PacerClientCode':'Lumina', 'PacerClient':"", 'ClientDesc':"", 'PacerPref':"receipt=Y"}
        req.meta['pdfname']=response.meta['pdfname']
        req.meta['base_url']=response.meta['base_url']
        req.meta['case_number']=response.meta['case_number']
        req.meta['case_name']=response.meta['case_name']
        req.meta['description']=response.meta['description']
        req.meta['date_filed']=response.meta['date_filed']
        req.meta['code_number']=code1
        req.meta['initial_url']=response.meta['initial_url']
        yield req

    def parse10(self, response):
        #with open("pacer_html101010101.html",'w') as f1:
        #    f1.write(response.body)
        try:
            pdflink=response.meta['base_url'].rstrip('/')+response.xpath('//iframe/@src').extract()[0]
            #print "ppppppppppp ", response.xpath('//iframe/@src').extract()
            #print "parse10 : try block"
            requsturl=scrapy.Request(pdflink,headers={'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://ecf.almd.uscourts.gov' , 'Upgrade-Insecure-Requests': '1' ,  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://ecf.almd.uscourts.gov/' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9'}, callback=self.parse11)
            requsturl.meta['pdfname']=response.meta['pdfname']
            requsturl.meta['base_url']=response.meta['base_url']
            requsturl.meta['case_number']=response.meta['case_number']
            requsturl.meta['case_name']=response.meta['case_name']
            requsturl.meta['description']=response.meta['description']
            requsturl.meta['date_filed']=response.meta['date_filed']
            requsturl.meta['initial_url']=response.meta['initial_url']
            yield requsturl
            #print pdflink
        except: 
            #print err
            #print "parse10 : except block"
            #print response.meta['initial_url']
            with open(response.meta['pdfname'],'wb') as f1:
                f1.write(response.body)
            item=PacerItems()
            item['pdflink']="Saved_pdf"
            item['base_url']=response.meta['base_url']
            item['case_number']=response.meta['case_number']
            item['case_name']=response.meta['case_name']
            item['description']=response.meta['description']
            item['date_filed']=str(response.meta['date_filed'].replace('-','/')) if response.meta['date_filed'].find('-')>-1 else str(response.meta['date_filed'])
            item['initial_url']=response.meta['initial_url']
            #item['base_court_name']=response.meta['base_court_name']
            yield item

    def parse11(self, response):
        with open(response.meta['pdfname'],'wb') as f1:
            f1.write(response.body)
        item=PacerItems()
        item['pdflink']="Saved_pdf"
        item['base_url']=response.meta['base_url']
        item['case_number']=response.meta['case_number']
        item['case_name']=response.meta['case_name']
        item['description']=response.meta['description']
        item['date_filed']=str(response.meta['date_filed'].replace('-','/')) if response.meta['date_filed'].find('-')>-1 else str(response.meta['date_filed'])
        item['initial_url']=response.meta['initial_url']
        #item['base_court_name']=response.meta['base_court_name']
        yield item