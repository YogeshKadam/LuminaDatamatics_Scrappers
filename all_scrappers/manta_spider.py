import scrapy

class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    name  = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()

class DmozSpider(scrapy.Spider):
    name = "manta"
    allowed_domains = []
    start_urls = [
        "https://www.manta.com/search?&search=7gifts"
    ]


    def parse(self, response):
        url ="https://www.manta.com/search?&search=7gifts"
        #headers = {"Host":"www.notebooksbilliger.de","User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Referer": "https://www.notebooksbilliger.de/produkte/canon+1300d"}
        headers={'Host':'www.manta.com','Accept-Encoding': 'gzip, deflate, sdch, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' , 'Referer': 'https://www.manta.com/search?&search=7gifts' ,'Connection': 'keep-alive' , 'Cache-Control': 'max-age=0'}  
        result_req = scrapy.Request(url,headers=headers, callback=self.parse1)
        result_req.cookies= {'D_SID':'220.227.52.23:NqidzIzqUsd/H7b8+pxV3sOP/YBHyZHO6C3bg4F5+Kg', 'cust_id':'2b0798c6-7b09-4fbc-9210-63a4597c5f8e', 'refer_id':'0000', 'manta_session':'%7B%22loginIp%22%3A%2210.78.35.12%22%2C%22subId%22%3A%22%22%2C%22touchTimestamp%22%3A%221496810293201%22%2C%22userRole%22%3A%22%22%2C%22notifType%22%3A%22%22%7D', 'city':'Mumbai', 'state':'16', 'lat':'18.975006', 'lon':'72.825806', 'ipCountry':'IN', 'ftoggle-frontend-prod':'%7B%22v%22%3A1496765240293%2C%22e%22%3A1%2C%22trackingNumber%22%3A%7B%22e%22%3A1%7D%2C%22homeyou%22%3A%7B%22e%22%3A1%7D%2C%22avvo%22%3A%7B%22e%22%3A1%2C%22avvo_control%22%3A%7B%22e%22%3A1%7D%7D%2C%22yextInterstitial%22%3A%7B%22e%22%3A1%7D%2C%22abTests%22%3A%7B%22e%22%3A1%2C%22subscriptions%22%3A%7B%22e%22%3A1%2C%22ampads_control%22%3A%7B%22e%22%3A1%7D%7D%7D%2C%22surveys%22%3A%7B%22e%22%3A1%7D%2C%22tracking%22%3A%7B%22e%22%3A1%2C%22mixpanel%22%3A%7B%22e%22%3A1%7D%2C%22ga%22%3A%7B%22e%22%3A1%7D%7D%2C%22ditto%22%3A%7B%22e%22%3A1%2C%22GMBScan%22%3A%7B%22e%22%3A1%7D%7D%2C%22updopt%22%3A%7B%22e%22%3A1%2C%22updoptDossier%22%3A%7B%22e%22%3A1%7D%7D%2C%22intercom%22%3A%7B%22e%22%3A1%7D%2C%22serverSideTracking%22%3A%7B%22e%22%3A1%2C%22subscriptions%22%3A%7B%22e%22%3A1%7D%7D%2C%22paywall%22%3A%7B%22e%22%3A1%2C%22test%22%3A%7B%22e%22%3A1%7D%7D%2C%22primaryContactCapture%22%3A%7B%22e%22%3A1%7D%2C%22subscriberScan%22%3A%7B%22e%22%3A1%7D%2C%22marketingProTasks%22%3A%7B%22e%22%3A1%7D%2C%22homepage%22%3A%7B%22e%22%3A1%2C%22dm%22%3A%7B%22e%22%3A1%7D%7D%7D', 'mp_f6712b90922aca648f9e2307427ca86f_mixpanel':'%7B%22distinct_id%22%3A%20%2215c80d88f1b2d6-0bd0ff5b1d20d5-323f5c0f-100200-15c80d88f1c28a%22%2C%22offHours%22%3A%20true%2C%22treatment%22%3A%20%22subscriptions_ampads_control%22%2C%22altTreatment1%22%3A%20%22paywall-interstitial%22%2C%22altTreatment2%22%3A%20%22%22%2C%22altTreatment3%22%3A%20%22%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.manta.com%2Fsearch%3F%26search%3D7gifts%22%2C%22%24initial_referring_domain%22%3A%20%22www.manta.com%22%7D', '__gads':'ID=f1e4f724932b8fe5:T=1496810295:S=ALNI_MbBHHlhxOBwLEaeDRdsSshF-kr7yw', 'OX_plg':'pm', 'D_IID':'D25D4EFA-2B4B-3D77-B31B-A8311EBEB120', 'D_UID':'C5F300EB-5176-399F-9F50-3ACFB20F556F', 'D_ZID':'D14BA6C2-D7FA-3FC6-AA43-5044B7279753', 'D_ZUID':'4F446478-E6C2-308E-A0D1-49FA8ECA9D34', 'D_HID':'5E32367C-3D90-30D7-B161-3D0D13018013', '_ga':'GA1.2.1334758695.1496810296', '_gid':'GA1.2.56737241.1496810299', '_uetsid':'_uet06eeeee0', 'calltrk_referrer':'https%3A//www.manta.com/search%3F%26search%3D7gifts', 'calltrk_landing':'https%3A//www.manta.com/search%3F%26search%3D7gifts', 'mp_mixpanel__c':'1'} 
        yield result_req


    def parse1(self,response):
        print response.body
        #item =TutorialItem()
        
        #item['title'] = response.xpath('//*[@id="epoq_searchresult"]/div[3]/div[1]/div[1]/div[1]/span/text()').extract()
        #yield item

