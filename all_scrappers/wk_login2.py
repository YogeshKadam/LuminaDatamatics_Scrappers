

import scrapy
from scrapy.utils.response import open_in_browser

class LoginSpider(scrapy.Spider):
    name = 'wk_login2'
    allowed_domains = ['digitalassets.wolterskluwer.be']
    #start_urls = ['https://digitalassets.wolterskluwer.be/media/']
    #start_urls = ['https://digitalassets.wolterskluwer.be/login/']
    start_urls = ['https://digitalassets.wolterskluwer.be/user/doLogin/']

    def parse2(self, response):
        token=response.xpath('//*[@id="languageSwitch"]/ul[@class="single"]/li[1]/form/input[@name="csrf"]/@value').extract()[0]
        print "TOKEN : ",token
        return scrapy.FormRequest.from_response(
            response,
            formdata={'csrf':token, 'urlhash':'', 'username': 'Deepali.sawant@luminad.com', 'password': 'luminadatamatics'},
            callback=self.after_login1)
		
    def parse1(self, response):
        req=scrapy.Request('https://digitalassets.wolterskluwer.be/account/dashboard/', headers={'authority': 'digitalassets.wolterskluwer.be' , 'cache-control': 'max-age=0' , 'origin': 'https://digitalassets.wolterskluwer.be' , 'upgrade-insecure-requests': '1' , 'content-type': 'application/x-www-form-urlencoded' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'referer': 'https://digitalassets.wolterskluwer.be/login/' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9' }, callback=self.after_login)
        req.cookies={'DefaultLocale':'en_US', 'bynder':'9A45AE65-7E5B-4341-B16D882656E03AEE'}
        yield req
		
    def parse(self, response):
        token=response.xpath('//*[@id="languageSwitch"]/ul[@class="single"]/li[1]/form/input[@name="csrf"]/@value').extract()[0]
        formdata={'csrf':token, 'urlhash':'', 'username': 'Deepali.sawant@luminad.com', 'password': 'luminadatamatics'}
        req=scrapy.FormRequest('https://digitalassets.wolterskluwer.be/user/doLogin/', meta = {'dont_redirect': True,'handle_httpstatus_list': [302]},formdata= formdata ,headers={'origin': 'https://digitalassets.wolterskluwer.be', 'referer': 'https://digitalassets.wolterskluwer.be/login/', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'cache-control': 'max-age=0', 'accept-language': 'en-US,en;q=0.9', 'accept-encoding': 'gzip, deflate, br', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', 'content-type': 'application/x-www-form-urlencoded', 'authority': 'digitalassets.wolterskluwer.be', 'upgrade-insecure-requests': '1'},callback=self.after_login2,method="POST")
        yield req
    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return

        # continue scraping with authenticated session...
        f1=open('wk_login29.html','w')
        f1.write(response.body)
        f1.close()

    def after_login1(self, response):
        open_in_browser(response)
		
    def after_login2(self, response):
        #open_in_browser(response)
        req=scrapy.Request('https://digitalassets.wolterskluwer.be/account/dashboard/', headers={'authority': 'digitalassets.wolterskluwer.be' , 'cache-control': 'max-age=0' , 'origin': 'https://digitalassets.wolterskluwer.be' , 'upgrade-insecure-requests': '1' , 'content-type': 'application/x-www-form-urlencoded' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'referer': 'https://digitalassets.wolterskluwer.be/login/' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9' }, callback=self.after_login)
        req.cookies={'DefaultLocale':'en_US', 'bynder':'9A45AE65-7E5B-4341-B16D882656E03AEE'}
        yield req