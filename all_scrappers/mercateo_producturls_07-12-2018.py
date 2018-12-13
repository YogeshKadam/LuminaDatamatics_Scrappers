# -*- coding: utf-8 -*-
import scrapy
import urllib

import os
import time
import re
import json


class MercateoItems(scrapy.Item):
    product_url= scrapy.Field()
    response_url= scrapy.Field()
    product_id= scrapy.Field()

class MercateoSpider(scrapy.Spider):
    name = "mercateo_producturls_07-12-2018"
    allowed_domains = ["mercateo.com"]

    start_urls = ["http://www.londonbookfair.co.uk/en/exhibitor-directory/#"]  

    def parse(self,response):
        urls=[
["1","http://www.mercateo.com/kw/telefonanlage/telefonanlage.html?ViewName=live~s.20"],
["2","http://www.mercateo.com/kw/pilotenkoffer/pilotenkoffer.html?ViewName=live~s.20"],
["3","http://www.mercateo.com/kw/tintenl(f6)scher/tintenloescher.html?ViewName=live~s.20"],
["4","http://www.mercateo.com/kw/kettenr(e4)der/kettenraeder.html?ViewName=live~s.20"],
["5","http://www.mercateo.com/kw/saatgut/saatgut.html?ViewName=live~s.20"],
["6","http://www.mercateo.com/kw/zylinderknopf/zylinderknopf.html?ViewName=live~s.20"],
["7","http://www.mercateo.com/kw/einbauleuchten/einbauleuchten.html?ViewName=live~s.20"],
["8","http://www.mercateo.com/kw/beize/beize.html?ViewName=live~s.20"],
["9","http://www.mercateo.com/kw/spektrumanalysatoren/spektrumanalysatoren.html?ViewName=live~s.20"],
["10","http://www.mercateo.com/kw/vibrationsmessger(e4)te/vibrationsmessgeraete.html?ViewName=live~s.20"],
["11","http://www.mercateo.com/kw/hebelschalter/hebelschalter.html?ViewName=live~s.20"],
["12","http://www.mercateo.com/kw/teller/teller.html?ViewName=live~s.20"],
["13","http://www.mercateo.com/kw/h(e4)hnchengrill/haehnchengrill.html?ViewName=live~s.20"],
["14","http://www.mercateo.com/kw/bettbezug/bettbezug.html?ViewName=live~s.20"],
["15","http://www.mercateo.com/kw/op(2d)kasack/op_kasack.html?ViewName=live~s.20"],
["16","http://www.mercateo.com/kw/mikroskop(2d)objektiv/mikroskop_objektiv.html?ViewName=live~s.20"],
["17","http://www.mercateo.com/kw/frottierwaren/frottierwaren.html?ViewName=live~s.20"],
["18","http://www.mercateo.com/kw/wendeplattenbohrer/wendeplattenbohrer.html?ViewName=live~s.20"],
["19","http://www.mercateo.com/kw/gummischeiben/gummischeiben.html?ViewName=live~s.20"],
["20","http://www.mercateo.com/kw/schwei(df)erausr(fc)stung/schweisserausruestung.html?ViewName=live~s.20"],
["21","http://www.mercateo.com/kw/sackkarre/sackkarre.html?ViewName=live~s.20"],
["22","http://www.mercateo.com/kw/hebeband/hebeband.html?ViewName=live~s.20"],
["23","http://www.mercateo.com/kw/handkreiss(e4)geblatt/handkreissaegeblatt.html?ViewName=live~s.20"],
["24","http://www.mercateo.com/kw/malerpinsel/malerpinsel.html?ViewName=live~s.20"],
["25","http://www.mercateo.com/kw/schraubenset/schraubenset.html?ViewName=live~s.20"],
]
        urls_done=[]
        for url in urls:
            req=scrapy.Request(url[1], callback=self.parse2)
            req.meta['product_id']=url[0]
            yield req
        #form_data={'rpp': '64', 'id': '264317', 'epsLanguage': 'en'}
        #req=scrapy.FormRequest("http://www.londonbookfair.co.uk/en/exhibitor-directory/#search=rpp%3D64" , formdata=form_data, method="POST", headers=header, callback=self.parse2)
        #req.cookies={'ucid':'45415cff-ca0b-4337-928a-423a03a6a11e', 'fsid':'62125eff-8ba0-447a-9ddb-ee4d9a9cb525', '_vwo_uuid_v2':'D1DF4B29EAFD46EDDD8749A74A60D0D9E|7c2579207f4856190fdf2c91741d4eba', '_ga':'GA1.3.2006064913.1543911540', '_gid':'GA1.3.562854177.1543911540', 'voviciSurvey_invitationDateTime':'Tue%20Dec%2004%202018%2013%3A51%3A00%20GMT%2B0530%20(India%20Standard%20Time)', '__gads':'ID=d059ed4ad29e71b3:T=1543911540:S=ALNI_Mbo99PG2urURfkcqVJbj5u_7wQCwg', 'feathr_session_id':'5c06387486977d3f4b6ca864', 'liveagent_oref':'', 'liveagent_sid':'6f9d434c-2821-4e00-b680-f65177a7ddc1', 'liveagent_vc':'2', 'liveagent_ptid':'6f9d434c-2821-4e00-b680-f65177a7ddc1', 'novaState':'/wEymwwAAQAAAP////8BAAAAAAAAAAQBAAAA4gFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5EaWN0aW9uYXJ5YDJbW1N5c3RlbS5PYmplY3QsIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV0sW1N5c3RlbS5PYmplY3QsIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV1dBAAAAAdWZXJzaW9uCENvbXBhcmVyCEhhc2hTaXplDUtleVZhbHVlUGFpcnMAAwADCJEBU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuT2JqZWN0RXF1YWxpdHlDb21wYXJlcmAxW1tTeXN0ZW0uT2JqZWN0LCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQjmAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLktleVZhbHVlUGFpcmAyW1tTeXN0ZW0uT2JqZWN0LCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldLFtTeXN0ZW0uT2JqZWN0LCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXVtdAQAAAAkCAAAAAwAAAAkDAAAABAIAAACRAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLk9iamVjdEVxdWFsaXR5Q29tcGFyZXJgMVtbU3lzdGVtLk9iamVjdCwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0AAAAABwMAAAAAAQAAAAEAAAAD5AFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5LZXlWYWx1ZVBhaXJgMltbU3lzdGVtLk9iamVjdCwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XSxbU3lzdGVtLk9iamVjdCwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0MBQAAAFlSZWVkRXhwby5Ob3ZhLkZyYW1ld29yay5GdW5jdGlvbmFsLCBWZXJzaW9uPTEuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbAT8////5AFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5LZXlWYWx1ZVBhaXJgMltbU3lzdGVtLk9iamVjdCwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XSxbU3lzdGVtLk9iamVjdCwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0CAAAAA2tleQV2YWx1ZQICBgYAAAAWU2l0ZUFjdGl2aXR5RmlsdGVyVHlwZQkHAAAABQcAAAA5UmVlZEV4cG8uTm92YS5GcmFtZXdvcmsuU3RhdGlzdGljcy5TaXRlQWN0aXZpdHlGaWx0ZXJUeXBlAQAAAAd2YWx1ZV9fAAgFAAAAAAAAAAs=', '__atuvc':'4%7C49', '__atuvs':'5c06387328254880003', '_ceg.s':'pj7ea4', '_ceg.u':'pj7ea4', '_dc_gtm_UA-2269150-1':'1' }
        #yield req
		
    def parse2(self,response):
        #f1=open("londonbookfair111.html","w")
        #f1.write(response.body)
        #f1.close()
        list1=response.xpath('//*[@id="pl_l_p_1"]/tr[@class="B2 he"]')
        list2=response.xpath('//*[@id="pl_l_p_1"]/tr[@class="B14 he"]')
        for li in list1:
            link="http://www.mercateo.com"+li.xpath('td/div/a[1]/@href').extract()[0]
            item=MercateoItems()
            item['product_url']=link
            item['product_id']=response.meta['product_id']
            item['response_url']=response.url
            yield item
        for li in list2:
            link="http://www.mercateo.com"+li.xpath('td/div/a[1]/@href').extract()[0]
            item=MercateoItems()
            item['product_url']=link
            item['product_id']=response.meta['product_id']
            item['response_url']=response.url
            yield item