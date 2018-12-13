#Amazon seller list spider

import scrapy
from court.items import CourtItem

class Spider(scrapy.Spider):
	
	name = "court"
	allowed_domain=[]
 
	start_urls = ['http://www.courtrecords.alaska.gov']

	def parse(self, response):
		url ='http://www.courtrecords.alaska.gov/eservices/search.page.14?x=czIs-mFjqdYLnpbCq-obYYAsi*76a78KDcKMV6EM79P4PEc0q1ndj4yjS*1BRO1OpTQFoyc*tWtD8vspJzLgzA'
		headers = {'Accept-Encoding': 'gzip, deflate, sdch' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' , 'Referer': 'http://www.courtrecords.alaska.gov/eservices/search.page.3?x=tdon5wKIyKeqHZYfZKq4gg'}
		result_req = scrapy.Request(url,headers=headers, callback=self.parse1)
		result_req.cookies= {'JSESSIONID':'4DCBA88E9AD0E82ECA22F3A135B29A92', '_ga':'GA1.2.1393740131.1491203566' , 'Connection': 'keep-alive'}
		yield result_req

	def parse1(self,response):
		sites = response.xpath('//*[@id="caseDetail"]/div["caseDetailHeader"]/div["caseHeader"]')
		item =CourtItem()
		for site in sites:
			item['data'] ={}
			key =  site.xpath('div["caseInfo-col1 col"]/dt[1]/text()').extract()
			print "KEY : ",key
			item['data'][key]=site.xpath('div["caseInfo-col1 col"]/dd[1]/text()').extract()
			
			print "Dictionary : ",item['data']
			yield item