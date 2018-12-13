# -*- coding: utf-8 -*-
import scrapy


class YelpItem(scrapy.Item):
    restaurant_name = scrapy.Field()
    address = scrapy.Field()
    contact = scrapy.Field()
    rating = scrapy.Field()
    no_of_reviews = scrapy.Field()
    cuisine = scrapy.Field()
    pricing = scrapy.Field()
    reservations = scrapy.Field()
    page_url = scrapy.Field()



class yelpSpider(scrapy.Spider):
    name = "yelp_hotel_info"
    allowed_domains = ['yelp.com']

    start_urls = ["https://www.yelp.com/"]  

    def parse(self,response):
        i=0
        while i<=990:
            urlpattern="https://www.yelp.com/search?find_loc=New+York,+NY&start="+str(i)
            req = scrapy.Request(urlpattern, callback=self.parse1)
            yield req
            i+=10

    def parse1(self,response):
        hotel_list=response.xpath('//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]/li')
        for hotels in hotel_list:
            item=YelpItem()
            restaurant_name="".join(hotels.xpath('div/div/div/div[2]/div[1]/div[1]/h3/span/a/span/text()').extract())
            rating="".join(hotels.xpath('div/div/div/div[2]/div[1]/div[1]/div[1]/div/@title').extract()).replace('\n','')
            no_of_reviews="".join(hotels.xpath('div/div/div/div[2]/div[1]/div[1]/div[1]/span/text()').extract()).replace('  ','').replace('\n','')
            pricing="".join(hotels.xpath('div/div/div/div[2]/div[1]/div[1]/div[2]/span[1]/span/text()').extract()).replace('\n','').replace('   ','')
            cuisine =" , ".join(hotels.xpath('div/div/div/div[2]/div[1]/div[1]/div[2]/span[2]/a//text()').extract()).replace('\n','').replace('   ','')
            contact ="".join(hotels.xpath('div/div/div/div[2]/div[1]/div[2]/span[@class="biz-phone"]/text()').extract()).replace('  ','').replace('\n','')
            address ="".join(hotels.xpath('div/div/div/div[2]/div[1]/div[2]/address/text()').extract()).replace('  ','').replace('\n','') + " , " + "".join(hotels.xpath('div/div/div/div[2]/div[1]/div[2]/span[@class="neighborhood-str-list"]/text()').extract()).replace('  ','').replace('\n','')
            reservations =''.join(hotels.xpath('div/div/div/div[2]/div[2]/div[2]/div[@class="search-avatar-offset js-reservation"]/div[1]/div/div[@class="arrange_unit--fill arrange_unit cta-text js-cta-text"]/span/text()').extract()).replace('  ','').replace('\n','')
            item['restaurant_name']=restaurant_name
            item['page_url']=response.url
            item['rating']=rating
            item['no_of_reviews']=no_of_reviews
            item['pricing']=pricing
            item['cuisine']=cuisine
            item['contact']=contact
            item['address']=address
            item['reservations']=reservations
            yield item