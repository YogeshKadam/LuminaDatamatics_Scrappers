import scrapy

from scrapy_splash import SplashRequest

class iSplash(scrapy.Spider):
    name = "gastro"
    start_urls =["https://www.gastro24.de"]

    allowed_domains = []

    def start_requests(self):
        yield SplashRequest("https://www.gastro24.de/Elektro-Kippbratpfanne",
        self.parse,
        endpoint="render.json",
        args={
              'wait': 25.0
             }
        )

    def parse(self, response):
        #print response.body
        f1=open("gastro2256.html","w")
        f1.write(response.body)
        

        #print response.xpath('//*[@class="r"]/a/@href').extract()
        f1.close()
