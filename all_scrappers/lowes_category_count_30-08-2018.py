#Amazon seller list spider
import time
import scrapy
import re
class LowesItem(scrapy.Item):
    # define the fields for your item here like:
    response_url = scrapy.Field()
    category = scrapy.Field()
    item_id = scrapy.Field()
    product_count = scrapy.Field()
    breadcrumb = scrapy.Field()

class Spider(scrapy.Spider):
    
    name = "lowes_category_count_30-08-2018"
    allowed_domain=[]
    start_urls = ['http://www.fnwerkzeuge.de/akkugeraete.html']
        
		
    def parse(self, response):
        urls_done=[
"item_id",
"10",
"6",
"5",
]
        urls = [
["1","Bedside Assistance","https://www.lowes.com/pl/Bedside-assistance-Accessible-home/4294644781"],
["2","Dining & Dressing Aids","https://www.lowes.com/pl/Dining-dressing-aids-Accessible-home/4294644797"],
["3","Emergency Alert Devices","https://www.lowes.com/pl/Emergency-alert-devices-Accessible-home/4294644783"],
["4","Injury Relief & Physical Therapy","https://www.lowes.com/pl/Injury-relief-physical-therapy-Accessible-home/4294644776"],
["5","Reading Magnifiers","https://www.lowes.com/pl/Reading-magnifiers-Accessible-home/4294644782"],
["6","Shopping Carts","https://www.lowes.com/pl/Shopping-carts-Accessible-home/4294644798"],
["7","Wheelchairs & Mobility Aids","https://www.lowes.com/pl/Wheelchairs-mobility-aids-Accessible-home/4294644793"],
["8","Barriers & Dig Protection","https://www.lowes.com/pl/Barriers-dig-protection-Animal-pet-care/4125235027"],
["9","Cat Trees","https://www.lowes.com/pl/Cat-trees-Animal-pet-care/4294506791"],
["10","Chicken Coops & Rabbit Hutches","https://www.lowes.com/pl/Chicken-coops-rabbit-hutches-Animal-pet-care/4294610501"],
]
        
        for url in urls:
            req = scrapy.Request(url[2], headers={'authority': 'www.lowes.com' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9' }, callback=self.parse1, meta={'categoryname':url[1], 'item_id':url[0]})
            req.cookies={'check':'true', 'AMCVS_5E00123F5245B2780A490D45%40AdobeOrg':'1', 'user':'%7B%22zipPrompt%22%3Atrue%7D', 'sn':'1738', '_abck':'9F6AB22FF6AD9089D59BDEE03BE4403973F8EE15C5300000D2A17F5B05E0F27D~0~yJnDH+xEDJ2LHtm2tdpUzGFXd303MMdGyb5BW5H9QnU=~-1~-1', 's_visit':'1', 'LPVID':'JlM2Y3Y2ViZjA2YTA5MmUx', 'feature':'0|0', 'stop_mobi':'yes', 'AKA_A2':'A', 'bm_sz':'7FDAA8399ED7ACE241876BCA5ADE79A9~QAAQMnxBF+6h+lplAQAAJlZjiUtrOGxPEfcO9ITDBvwqSf455A+xRWteSY7Askm/M73aLEed+N9npCp9Zbm7xUkg3uUA0H9AAWl9V1Cwwil9MPC4MyTghtS2OxXF3xaJm8UQ7HILEoYbXARE0VzGkuTJNBdy6p0RVs+MRu5vF2uxeaCJ7E4JashYIYWrVg==', 'AMCV_5E00123F5245B2780A490D45%40AdobeOrg':'-1176276602%7CMCIDTS%7C17774%7CMCMID%7C85006305325023271133086745164214912881%7CMCAAMLH-1536054889%7C3%7CMCAAMB-1536213114%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1535615514s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.3.0', 'JSESSIONID':'0000DsO0F3uAATAzD0L3k3ycpJ7:1bgtuseld', 'ak_bmsc':'B05C1063AC2326C118B440856A0B223517417C3288650000F985875B227D0168~plZxW8ySswvKC0m65VJvLhPaPU+0n2zy4cZYnUP8+BSsJi/SGlLiVVBbNP9r4FSq1OM/RRnI+DktA7/1CF1PtrLtpOR2CLZrz1LCH+P6yGOETVf9XpiQgHIgEzgC436UKdJmy3Kmr8XsiG0XgaQj0AmYBqcPltXzov5mqPUPwyv7hXzuoOo7g4tw1EEqFU7MQuwiHga2vRuq2K5coVS+1NpRXA2wJWmtrA00wT+r40kse3cvRpq5Xsi72xZkZ0FuE4', 'LPSID-22554410':'YqPS3eTgSkqaVszpP4YfrA', 'akavpau_default':'1535609060~id=43523eac1c8cdc8173484a2fcee1dfc7', 'bm_sv':'F76E5744459F799420648B5AC3C38E58~lwn/+TOUeSmkJcey7+/SC92fVoE4VYroh0d3fMesNh71O5XaMzktxvKEztPYeKS3ueAFAeuiS30Hyvv3W4N9SO8T1ZCLitOYtnokvWNVlMtRkGtwRvScoSa8bHNSITw3C9a0c84QA0o9vDfin35+dNDPPYmNUfmBYBS0qZpHn18=', 'catSearchResult':'|/pl/Jack-posts-Building-supplies/4294515331', 's_sess':'%20s_visit%3D1%3B%20s_sq%3D%3B%20s_cc%3Dtrue%3B', 'mbox':'PC#1cb40fa4a5d74bd48eba10f69b7ce1d6.22_22#1598335957|session#f2be0d6f372d476d8e7f8db2d80a8ed2#1535610623', 'fsr.s':'%7B%22v2%22%3A-2%2C%22v1%22%3A-2%2C%22rid%22%3A%22d489c26-86157607-3bcb-acda-032eb%22%2C%22to%22%3A5%2C%22c%22%3A%22https%3A%2F%2Fwww.lowes.com%2Fpl%2FJack-posts-Building-supplies%2F4294515331%22%2C%22pv%22%3A153%2C%22lc%22%3A%7B%22d1%22%3A%7B%22v%22%3A153%2C%22s%22%3Atrue%7D%7D%2C%22cd%22%3A1%2C%22cp%22%3A%7B%22campaign_name%22%3A%22PPR%20-%20DT%20-%20List%20Pages%20-%20Top%20Trending%20in%20Your%20Store%22%2C%22campaign_recipe_name%22%3A%227787-14579-2%22%7D%2C%22f%22%3A1535550480632%2C%22sd%22%3A1%7D', 'sc_length':'1342', 'productnum':'202', 's_pers':'%20s_vnum%3D1566627158672%2526vn%253D12%7C1566627158672%3B%20gpv_page%3Dlowes%253Adt%253Abuilding_supplies%253Ajack_posts%7C1535610564421%3B%20gpv_pgtype%3Dproduct-list%7C1535610564424%3B%20gpv_sec%3Dbuilding_supplies%7C1535610564426%3B%20s_invisit%3Dtrue%7C1535610564428%3B%20s_lv%3D1535608764431%7C1630216764431%3B%20s_lv_s%3DLess%2520than%25207%2520days%7C1535610564431%3B', 'RT':"sl=5&ss=1535608303734&tt=38482&obo=0&sh=1535608764241%3D5%3A0%3A38482%2C1535608450294%3D4%3A0%3A32916%2C1535608365447%3D3%3A0%3A28754%2C1535608346251%3D2%3A0%3A24892%2C1535608324974%3D1%3A0%3A21220&dm=lowes.com&si=74f27d58-3809-4dd1-83a8-22496e7bac78&bcn=%2F%2F36fb6d10.akstat.io%2F&nu=https%3A%2F%2Fwww.lowes.com%2Fpl%2FJack-posts-Building-supplies%2F4294515331&cl=1535608807457&r=https%3A%2F%2Fwww.lowes.com%2Fpl%2FJack-posts-Building-supplies%2F4294515331&ul=1535608876102"}
            if url[0] not in urls_done:
                yield req
                                
                        
    def parse1(self, response):
        productlist=response.xpath('//ul[@class="product-cards-grid"]/li/div[@class="product-wrapper-right"]/div[@class="product-details"]/a/@href').extract()
        breadcrumb= " > ".join(response.xpath('//ul[@class="breadcrumb"]/li/a/span/text()').extract())
        if response.xpath('//ul[@class="pagination js-pagination met-pagination art-pl-pagination"]/@data-pages').extract():
            pagelist=response.xpath('//ul[@class="pagination js-pagination met-pagination art-pl-pagination"]/@data-pages').extract()[0]
            pattern="?offset="+str(36*(int(pagelist)-1))
            urlpattern=response.url+pattern
            req=scrapy.Request(urlpattern, headers={'authority': 'www.lowes.com' , 'cache-control': 'max-age=0' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9' }, callback=self.parse2)
            req.cookies={'check':'true', 'AMCVS_5E00123F5245B2780A490D45%40AdobeOrg':'1', 'user':'%7B%22zipPrompt%22%3Atrue%7D', 'sn':'1738', '_abck':'9F6AB22FF6AD9089D59BDEE03BE4403973F8EE15C5300000D2A17F5B05E0F27D~0~yJnDH+xEDJ2LHtm2tdpUzGFXd303MMdGyb5BW5H9QnU=~-1~-1', 's_visit':'1', 'LPVID':'JlM2Y3Y2ViZjA2YTA5MmUx', 'feature':'0|0', 'stop_mobi':'yes', 'AKA_A2':'A', 'bm_sz':'7FDAA8399ED7ACE241876BCA5ADE79A9~QAAQMnxBF+6h+lplAQAAJlZjiUtrOGxPEfcO9ITDBvwqSf455A+xRWteSY7Askm/M73aLEed+N9npCp9Zbm7xUkg3uUA0H9AAWl9V1Cwwil9MPC4MyTghtS2OxXF3xaJm8UQ7HILEoYbXARE0VzGkuTJNBdy6p0RVs+MRu5vF2uxeaCJ7E4JashYIYWrVg==', 'AMCV_5E00123F5245B2780A490D45%40AdobeOrg':'-1176276602%7CMCIDTS%7C17774%7CMCMID%7C85006305325023271133086745164214912881%7CMCAAMLH-1536054889%7C3%7CMCAAMB-1536213114%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1535615514s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.3.0', 'JSESSIONID':'0000DsO0F3uAATAzD0L3k3ycpJ7:1bgtuseld', 'ak_bmsc':'B05C1063AC2326C118B440856A0B223517417C3288650000F985875B227D0168~plZxW8ySswvKC0m65VJvLhPaPU+0n2zy4cZYnUP8+BSsJi/SGlLiVVBbNP9r4FSq1OM/RRnI+DktA7/1CF1PtrLtpOR2CLZrz1LCH+P6yGOETVf9XpiQgHIgEzgC436UKdJmy3Kmr8XsiG0XgaQj0AmYBqcPltXzov5mqPUPwyv7hXzuoOo7g4tw1EEqFU7MQuwiHga2vRuq2K5coVS+1NpRXA2wJWmtrA00wT+r40kse3cvRpq5Xsi72xZkZ0FuE4', 'LPSID-22554410':'YqPS3eTgSkqaVszpP4YfrA', 'akavpau_default':'1535609060~id=43523eac1c8cdc8173484a2fcee1dfc7', 'bm_sv':'F76E5744459F799420648B5AC3C38E58~lwn/+TOUeSmkJcey7+/SC92fVoE4VYroh0d3fMesNh71O5XaMzktxvKEztPYeKS3ueAFAeuiS30Hyvv3W4N9SO8T1ZCLitOYtnokvWNVlMtRkGtwRvScoSa8bHNSITw3C9a0c84QA0o9vDfin35+dNDPPYmNUfmBYBS0qZpHn18=', 'catSearchResult':'|/pl/Jack-posts-Building-supplies/4294515331', 's_sess':'%20s_visit%3D1%3B%20s_sq%3D%3B%20s_cc%3Dtrue%3B', 'mbox':'PC#1cb40fa4a5d74bd48eba10f69b7ce1d6.22_22#1598335957|session#f2be0d6f372d476d8e7f8db2d80a8ed2#1535610623', 'fsr.s':'%7B%22v2%22%3A-2%2C%22v1%22%3A-2%2C%22rid%22%3A%22d489c26-86157607-3bcb-acda-032eb%22%2C%22to%22%3A5%2C%22c%22%3A%22https%3A%2F%2Fwww.lowes.com%2Fpl%2FJack-posts-Building-supplies%2F4294515331%22%2C%22pv%22%3A153%2C%22lc%22%3A%7B%22d1%22%3A%7B%22v%22%3A153%2C%22s%22%3Atrue%7D%7D%2C%22cd%22%3A1%2C%22cp%22%3A%7B%22campaign_name%22%3A%22PPR%20-%20DT%20-%20List%20Pages%20-%20Top%20Trending%20in%20Your%20Store%22%2C%22campaign_recipe_name%22%3A%227787-14579-2%22%7D%2C%22f%22%3A1535550480632%2C%22sd%22%3A1%7D', 'sc_length':'1342', 'productnum':'202', 's_pers':'%20s_vnum%3D1566627158672%2526vn%253D12%7C1566627158672%3B%20gpv_page%3Dlowes%253Adt%253Abuilding_supplies%253Ajack_posts%7C1535610564421%3B%20gpv_pgtype%3Dproduct-list%7C1535610564424%3B%20gpv_sec%3Dbuilding_supplies%7C1535610564426%3B%20s_invisit%3Dtrue%7C1535610564428%3B%20s_lv%3D1535608764431%7C1630216764431%3B%20s_lv_s%3DLess%2520than%25207%2520days%7C1535610564431%3B', 'RT':"sl=5&ss=1535608303734&tt=38482&obo=0&sh=1535608764241%3D5%3A0%3A38482%2C1535608450294%3D4%3A0%3A32916%2C1535608365447%3D3%3A0%3A28754%2C1535608346251%3D2%3A0%3A24892%2C1535608324974%3D1%3A0%3A21220&dm=lowes.com&si=74f27d58-3809-4dd1-83a8-22496e7bac78&bcn=%2F%2F36fb6d10.akstat.io%2F&nu=https%3A%2F%2Fwww.lowes.com%2Fpl%2FJack-posts-Building-supplies%2F4294515331&cl=1535608807457&r=https%3A%2F%2Fwww.lowes.com%2Fpl%2FJack-posts-Building-supplies%2F4294515331&ul=1535608876102"}
            req.meta['page_count']=36*(int(pagelist)-1)
            req.meta['item_id']=response.meta['item_id']
            req.meta['categoryname']=response.meta['categoryname']
            req.meta['response_url']=response.url
            yield req
        else:
            item=LowesItem()
            item['response_url'] =response.url
            item['category'] =response.meta['categoryname']
            item['item_id'] =response.meta['item_id']
            item['product_count'] =len(productlist)
            item['breadcrumb'] =breadcrumb
            yield item
			
    def parse2(self, response):
        productlist=response.xpath('//ul[@class="product-cards-grid"]/li/div[@class="product-wrapper-right"]/div[@class="product-details"]/a/@href').extract()
        breadcrumb= " > ".join(response.xpath('//ul[@class="breadcrumb"]/li/a/span/text()').extract())
        item=LowesItem()
        item['response_url'] =response.meta['response_url']
        item['category'] =response.meta['categoryname']
        item['item_id'] =response.meta['item_id']
        item['product_count'] =response.meta['page_count']+len(productlist)
        item['breadcrumb'] =breadcrumb
        yield item