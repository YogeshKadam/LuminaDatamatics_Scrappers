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

class PacerSpider(scrapy.Spider):
    imgcount = 1
    name = "pacer_scrapper_19-10-2018_slot1_part1"
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
["1","https://ecf.ohnd.uscourts.gov/cgi-bin/OHND_WrtOpRpt.pl"],
["2","https://ecf.nywd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["3","https://ecf.ncmd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["4","https://ecf.ndd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["5","https://ecf.ohsd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["6","https://ecf.okwd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["7","https://ecf.okwd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["8","https://ecf.oked.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["9","https://ecf.oknd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["10","https://ecf.vaed.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["11","https://ecf.pamd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["12","https://ecf.txwd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["13","https://ecf.pawd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["14","https://ecf.sdd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["15","https://ecf.scd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["16","https://ecf.tned.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["17","https://ecf.txed.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["18","https://ecf.rid.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["19","https://ecf.tnmd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["20","https://ecf.tnwd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["21","https://ecf.caed.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["22","https://ecf.caed.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["23","https://ecf.utd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["24","https://ecf.vid.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["25","https://ecf.azd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["26","https://ecf.cacd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["27","https://ecf.vtd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["28","https://ecf.casd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["29","https://ecf.wawd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["30","https://ecf.waed.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["31","https://ecf.wvsd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["32","https://ecf.ared.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["33","https://ecf.cod.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["34","https://ecf.hid.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["35","https://ecf.arwd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["36","https://ecf.wiwd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["37","https://ecf.gud.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["38","https://ecf.akd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["39","https://ecf.alnd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["40","https://ecf.almd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["41","https://ecf.wvnd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["42","https://ecf.gand.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["43","https://ecf.gasd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["44","https://ecf.alsd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["45","https://ecf.wyd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["46","https://ecf.wied.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["47","https://ecf.txnd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["48","https://ecf.prd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["49","https://ecf.paed.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["50","https://ecf.nmid.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["51","https://ecf.ned.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["52","https://ecf.mad.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["53","https://ecf.mdd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["54","https://ecf.kyed.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["55","https://ecf.ded.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["56","https://ecf.cand.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["57","https://ecf.cand.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["58","https://ecf.mied.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["59","https://ecf.flnd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["60","https://ecf.dcd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["61","https://ecf.flmd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["62","https://ecf.nhd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["63","https://ecf.ctd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["64","https://ecf.njd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["65","https://ecf.flsd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["66","https://ecf.ilnd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["67","https://ecf.ilcd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["68","https://ecf.ilsd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["69","https://ecf.gamd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["70","https://ecf.idd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["71","https://ecf.innd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["72","https://ecf.insd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["73","https://ecf.lawd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["74","https://ecf.laed.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["75","https://ecf.iand.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["76","https://ecf.iasd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["77","https://ecf.ksd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["78","https://ecf.lamd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["79","https://ecf.kywd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["80","https://ecf.miwd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["81","https://ecf.med.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["82","https://ecf.moed.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["83","https://ecf.nvd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["84","https://ecf.msnd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["85","https://ecf.mnd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["86","https://ecf.mssd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["87","https://ecf.mowd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["88","https://ecf.nyed.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["89","https://ecf.mtd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["90","https://ecf.txsd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["91","https://ecf.nysd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["92","https://ecf.nysd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["93","https://ecf.nynd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
["94","https://ecf.ncwd.uscourts.gov/cgi-bin/WrtOpRpt.pl"],
]
        #print "Total US District courts : ",len(list1)
        for link in list1:
            #link=li.xpath('@href').extract()[0]
            #name=li.xpath('text()').extract()[0].replace('\n','').replace('\t','').replace('\r','')
            req=scrapy.http.Request(link[1],headers={'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://pacer.login.uscourts.gov' , 'Upgrade-Insecure-Requests': '1' , 'Content-Type': 'application/x-www-form-urlencoded' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://pacer.login.uscourts.gov/csologin/login.jsf' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' }, callback=self.parse6)
            req.meta['base_url']=link[1].split('cgi-bin')[0]
            #req.meta['base_court_name']=name
            if link[0] not in urls_done:
                yield req
        #req=scrapy.http.Request(list1,headers={'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://pacer.login.uscourts.gov' , 'Upgrade-Insecure-Requests': '1' , 'Content-Type': 'application/x-www-form-urlencoded' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://pacer.login.uscourts.gov/csologin/login.jsf' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' }, callback=self.parse3)
        #req.meta['base_url']=list1
        #yield req
			
    def parse6(self, response):
        #with open("pacer_html4444.html",'w') as f1:
        #    f1.write(response.body)
        form_data={'all_case_ids':'0', 'case_num':'', 'last_name':'', 'first_name':'', 'middle_name':'', 'office':'', 'nsuit':'', 'case_type':'', 'cause':'', 'case_flags':'', 'filed_from':'9/19/2018', 'filed_to':'10/19/2018', 'ShowFull':'1', 'Key1':'cs_sort_case_numb', 'UserType':''}
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
        #req.meta['base_court_name']=response.meta['base_court_name']
        yield req
		
    def parse7(self, response):
        #with open("pacer_html5555.html",'w') as f1:
        #    f1.write(response.body)valign="top"
        #list1=response.xpath('//*[@id="cmecfMainContent"]/center[1]/table/tr[@valign="top"]')
        list1=response.xpath('//*[@id="cmecfMainContent"]/center[1]/table/tr[2]')
        for li in list1:
            case_number=li.xpath('td[1]/a/text()').extract()[0]
            case_name=li.xpath('td[1]/b/text()').extract()[0]
            link=li.xpath('td[@align="center"]/a/@href').extract()[0]
            codes=li.xpath('td[@align="center"]/a/@onclick').extract()[0]
            description=", ".join(li.xpath('td[4]//text()').extract())
            date_filed=li.xpath('td[2]/text()').extract()[0]
            #print case_number,case_name,link,codes,description,date_filed
            #link=response.xpath('//*[@id="cmecfMainContent"]/center[1]/table/tr[2]/td[3]/a/@href').extract()[0]
            #codes=response.xpath('//*[@id="cmecfMainContent"]/center[1]/table/tr[2]/td[3]/a/@onclick').extract()[0]
            #print link, codes
            code1=codes.split('(')[1].split(',')[1].replace("'","").replace('"','').replace(" ","")
            code2=codes.split('(')[1].split(',')[2].replace("'","").replace('"','').replace(" ","")
            code3=codes.split('(')[1].split(',')[5].replace("'","").replace('"','').replace(" ","")
            form_data={'caseid':code1, 'de_seq_num':code2, 'got_receipt':'1', 'pdf_toggle_possible':code3}
            me = MultipartEncoder(fields=form_data)
            me_boundary = me.boundary[2:]  #need this in headers
            me_length = me.len             #need this in headers
            me_body = me.to_string()
            header={'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://ecf.almd.uscourts.gov' , 'Upgrade-Insecure-Requests': '1' , 'Content-Type': 'multipart/form-data; charset=utf-8; boundary=' + me_boundary,  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://ecf.almd.uscourts.gov/' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9'}
            req=scrapy.Request(link, meta = {'dont_redirect': True,'handle_httpstatus_list': [500,302]}, body=me_body, headers=header, callback=self.parse8, method="POST")
            req.cookies={'_ga':'GA1.2.1437274789.1534401822', 'ClientValidation':"", 'ClientCodeDescription':"", 'MENU':'slow', 'PacerSession':'0oxdQUxn4oxv1KlUJAvfr4kkFQEROH2k0tiDHGNeUEdE2oO5N3NeEJmy5AsVBQiPvefaUJSXI9DSOfshoFpoY94Bgv4EJaiC2mt7Zv2ecmzRpIT4nBqY2COBdjf3YQ0Q', 'NextGenCSO':'0oxdQUxn4oxv1KlUJAvfr4kkFQEROH2k0tiDHGNeUEdE2oO5N3NeEJmy5AsVBQiPvefaUJSXI9DSOfshoFpoY94Bgv4EJaiC2mt7Zv2ecmzRpIT4nBqY2COBdjf3YQ0Q', 'PacerClientCode':'Lumina', 'PacerClient':"", 'ClientDesc':"", 'PacerPref':"receipt=Y"}
            req.meta['pdfname']=response.meta['base_url'].split('/')[2].replace('.','_')+"_"+code1+"_"+code2+"_"+code3+".pdf"
            req.meta['base_url']=response.meta['base_url']
            req.meta['case_number']=case_number
            req.meta['case_name']=case_name
            req.meta['description']=description
            req.meta['date_filed']=date_filed
            #req.meta['base_court_name']=response.meta['base_court_name']
            yield req
		
    def parse8(self, response):
        #with open("pacer_html6666.html",'w') as f1:
        #    f1.write(response.body)
        try:
            pdflink=response.meta['base_url'].rstrip('/')+response.xpath('//iframe/@src').extract()[0]
            requsturl=scrapy.http.Request(pdflink,headers={'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0' , 'Origin': 'https://ecf.almd.uscourts.gov' , 'Upgrade-Insecure-Requests': '1' ,  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Referer': 'https://ecf.almd.uscourts.gov/' , 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9'}, callback=self.parse9)
            requsturl.meta['pdfname']=response.meta['pdfname']
            requsturl.meta['base_url']=response.meta['base_url']
            requsturl.meta['case_number']=response.meta['case_number']
            requsturl.meta['case_name']=response.meta['case_name']
            requsturl.meta['description']=response.meta['description']
            requsturl.meta['date_filed']=response.meta['date_filed']
            yield requsturl
            #print pdflink
        except:
            with open(response.meta['pdfname'],'wb') as f1:
                f1.write(response.body)
            item=PacerItems()
            item['pdflink']="Saved_pdf"
            item['base_url']=response.meta['base_url']
            item['case_number']=response.meta['case_number']
            item['case_name']=response.meta['case_name']
            item['description']=response.meta['description']
            item['date_filed']=response.meta['date_filed']
            #item['base_court_name']=response.meta['base_court_name']
            yield item

    def parse9(self, response):
        with open(response.meta['pdfname'],'wb') as f1:
            f1.write(response.body)
        item=PacerItems()
        item['pdflink']="Saved_pdf"
        item['base_url']=response.meta['base_url']
        item['case_number']=response.meta['case_number']
        item['case_name']=response.meta['case_name']
        item['description']=response.meta['description']
        item['date_filed']=response.meta['date_filed']
        #item['base_court_name']=response.meta['base_court_name']
        yield item