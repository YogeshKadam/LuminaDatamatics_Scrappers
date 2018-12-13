# -*- coding: utf-8 -*-
import scrapy
import urllib

import os
import time
import re
import json


class LondonItems(scrapy.Item):
    product_url= scrapy.Field()

class CatalogSpider(scrapy.Spider):
    imgcount = 1
    name = "london_producturls_04-12-2018"
    allowed_domains = ["londonbookfair.co.uk"]

    start_urls = ["http://www.londonbookfair.co.uk/en/exhibitor-directory/#"]  

    def parse(self,response):
        #f1=open("londonbookfair.html","w")
        #f1.write(response.body)
        #f1.close()
        #handle_httpstatus_list = [304]
        #header={ 'Accept-Encoding': 'gzip, deflate' , 'Accept-Language': 'en-US,en;q=0.9' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36' , 'Accept': 'text/plain, */*; q=0.01' , 'Referer': 'http://www.londonbookfair.co.uk/' , 'X-Requested-With': 'XMLHttpRequest' , 'Proxy-Connection': 'keep-alive' , 'If-Modified-Since': 'Fri, 16 Nov 2018 10:24:49 GMT'}
        #req=scrapy.Request("http://www.londonbookfair.co.uk/en/exhibitor-directory/#search=rpp%3D64" ,meta={'dont_redirect': True}, headers=header, callback=self.parse2)
        #req=scrapy.Request("http://www.londonbookfair.co.uk/en/exhibitor-directory/#search=rpp%3D64" , headers=header, callback=self.parse2)
        i=1
        while i<=700:
            urlpattern="http://www.londonbookfair.co.uk/en/exhibitor-directory/?rpp=64&startRecord="+str(i)
            req=scrapy.Request(urlpattern , callback=self.parse2)
            i+=64
            yield req
        #form_data={'rpp': '64', 'id': '264317', 'epsLanguage': 'en'}
        #req=scrapy.FormRequest("http://www.londonbookfair.co.uk/en/exhibitor-directory/#search=rpp%3D64" , formdata=form_data, method="POST", headers=header, callback=self.parse2)
        #req.cookies={'ucid':'45415cff-ca0b-4337-928a-423a03a6a11e', 'fsid':'62125eff-8ba0-447a-9ddb-ee4d9a9cb525', '_vwo_uuid_v2':'D1DF4B29EAFD46EDDD8749A74A60D0D9E|7c2579207f4856190fdf2c91741d4eba', '_ga':'GA1.3.2006064913.1543911540', '_gid':'GA1.3.562854177.1543911540', 'voviciSurvey_invitationDateTime':'Tue%20Dec%2004%202018%2013%3A51%3A00%20GMT%2B0530%20(India%20Standard%20Time)', '__gads':'ID=d059ed4ad29e71b3:T=1543911540:S=ALNI_Mbo99PG2urURfkcqVJbj5u_7wQCwg', 'feathr_session_id':'5c06387486977d3f4b6ca864', 'liveagent_oref':'', 'liveagent_sid':'6f9d434c-2821-4e00-b680-f65177a7ddc1', 'liveagent_vc':'2', 'liveagent_ptid':'6f9d434c-2821-4e00-b680-f65177a7ddc1', 'novaState':'/wEymwwAAQAAAP////8BAAAAAAAAAAQBAAAA4gFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5EaWN0aW9uYXJ5YDJbW1N5c3RlbS5PYmplY3QsIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV0sW1N5c3RlbS5PYmplY3QsIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV1dBAAAAAdWZXJzaW9uCENvbXBhcmVyCEhhc2hTaXplDUtleVZhbHVlUGFpcnMAAwADCJEBU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuT2JqZWN0RXF1YWxpdHlDb21wYXJlcmAxW1tTeXN0ZW0uT2JqZWN0LCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQjmAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLktleVZhbHVlUGFpcmAyW1tTeXN0ZW0uT2JqZWN0LCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldLFtTeXN0ZW0uT2JqZWN0LCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXVtdAQAAAAkCAAAAAwAAAAkDAAAABAIAAACRAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLk9iamVjdEVxdWFsaXR5Q29tcGFyZXJgMVtbU3lzdGVtLk9iamVjdCwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0AAAAABwMAAAAAAQAAAAEAAAAD5AFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5LZXlWYWx1ZVBhaXJgMltbU3lzdGVtLk9iamVjdCwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XSxbU3lzdGVtLk9iamVjdCwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0MBQAAAFlSZWVkRXhwby5Ob3ZhLkZyYW1ld29yay5GdW5jdGlvbmFsLCBWZXJzaW9uPTEuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbAT8////5AFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5LZXlWYWx1ZVBhaXJgMltbU3lzdGVtLk9iamVjdCwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XSxbU3lzdGVtLk9iamVjdCwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0CAAAAA2tleQV2YWx1ZQICBgYAAAAWU2l0ZUFjdGl2aXR5RmlsdGVyVHlwZQkHAAAABQcAAAA5UmVlZEV4cG8uTm92YS5GcmFtZXdvcmsuU3RhdGlzdGljcy5TaXRlQWN0aXZpdHlGaWx0ZXJUeXBlAQAAAAd2YWx1ZV9fAAgFAAAAAAAAAAs=', '__atuvc':'4%7C49', '__atuvs':'5c06387328254880003', '_ceg.s':'pj7ea4', '_ceg.u':'pj7ea4', '_dc_gtm_UA-2269150-1':'1' }
        #yield req
		
    def parse2(self,response):
        #f1=open("londonbookfair111.html","w")
        #f1.write(response.body)
        #f1.close()
        list1=response.xpath('//*[@id="searchResultsList"]/li')
        for li in list1:
            link="http://www.londonbookfair.co.uk"+li.xpath('div/h3/a/@href').extract()[0]
            item=LondonItems()
            item['product_url']=link
            yield item