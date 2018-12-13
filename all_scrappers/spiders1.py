# -*- coding: utf-8 -*-
from __future__ import absolute_import
from scrapy import signals
from scrapy.exceptions import DontCloseSpider
from scrapy.spider import Spider
import csv
from kafka import KafkaProducer
from kafka.common import KafkaError
from kafka import KafkaConsumer,SimpleConsumer,KafkaClient
#from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer
from kafka import KafkaConsumer
from scrapy.http import Request
import time
from pymongo import MongoClient
client = MongoClient()
import json
class KafkaSpiderMixin1(object):

    """
    Mixin class to implement reading urls from a kafka queue.

    :type kafka_topic: str
    """
    kafka_topic = None

    def process_kafka_message(self, message):
        """"
        Tell this spider how to extract urls from a kafka message

        :param message: A Kafka message object
        :type message: kafka.common.OffsetAndMessage
        :rtype: str or None
        """
        if not message:
            return None

        return message.value


    # override method
    def make_requests_from_url(self, url, id=None, attr=None):
        #request = Request(url,headers={"Accept-Encoding": "gzip,deflate,sdch","Accept-Language": "en-US,en;q=0.8" , "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36" , "Accept": "*/*" ,"Referer": "https://www.amazon.de" , "Connection": "keep-alive" }, dont_filter=True)
        request = Request(url,headers={'Origin': 'https://www.amazon.de', 'Referer':'https://www.amazon.de', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.8', 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36, LuminadBot/1.0 (Apollo@Luminad.com)', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' ,'Cache-Control': 'max-age=0' }, dont_filter=True)
        request.cookies ={'s_pers':'%20s_fid%3D300B8810F7CDBDE1-10092DE00A8359D7%7C1558680220920%3B%20s_dl%3D1%7C1495610020921%3B%20gpv_page%3DDE%253AAZ%253ASOA-Landing%7C1495610020924%3B%20s_ev15%3D%255B%255B%2527AZDEGNOSellC%2527%252C%25271495608209183%2527%255D%252C%255B%2527AZDEGNOSellC%2527%252C%25271495608216403%2527%255D%252C%255B%2527AZDEGNOSellC%2527%252C%25271495608220916%2527%255D%252C%255B%2527AZDEGNOSellC%2527%252C%25271495608220925%2527%255D%255D%7C1653374620925%3B%20s_eVar26%3DAmazon%2520Services%2520DE%7C1498200220927%3B', 'amznacsleftnav-656eac4a-695b-3a6a-946f-db61e4deb392':'1', 'amznacsleftnav-fdfd699f-c863-3b78-85b2-8a649c6b58f6':'1', 'x-amz-captcha-1':'1508482986892769', 'x-amz-captcha-2':'hw3RhTh0tvhX81cdMFkFgQ==', 'lc-acbde':'de_DE', 'session-id':'261-5677163-4561642', 'ubid-acbde':'259-8821950-7904223', 'a-ogbcbff':'1', 'x-acbde':'"V0z3CSC5jraR2B7OY6OiPR3wrDO7GbRjA9fTg2AJTorXXbAPToPEDvMAo8KTh@7M"', 'at-acbde':'Atza|IwEBIHwqc3CD45BqlJs_5aa-V8dGYqRemzUHaOJhdARXf-o6rlAp0DANlQO8ZPGB23Uek573IjBb2qkX4mlZWKna1Xn3pOzTpiUd0SQO7gh-uTZnxF5r2p22mMsR4_clEZvBBlZBMJYXD6HPxW7_sEYtklqCkY-Br197rDnz9KPza3y5u7XzgezJIBdXCaeq4vAqo9Wrl0uG0RGKSr41-4rKK9hpnGK1nN4UbO_qWxnLSwzA6LwgXczqe0C5EyH1HIp12IlKFB7OgxIEsH0QZAiT0eh0D7sFwlVG6eHfqPNWfix03SZ7apAC7C7jQ-vw1lmICAeJciD9QmumuCNEDDCT-GGWCkrAh-gxMRhKpm7Q5_gOtJijbqoLi3VfPO9QrCA7hYW8Atc-kFRIW3Y6vtRc8OZzZipCneewy-Rj_xYUMFVWMCmHs_ljfe2W6vxWgiRfmyw', 'sess-at-acbde':'"NbwPRqfG4oPuznYLUmFM5Y5JSvyizaA9ZJz6vTkNQL4="', 'sst-acbde':'Sst1|PQEs5smXCO43G8WIotdsANHyCEBZ9TkcZ_OdLYTgnk2mCfAy4Z5W77Y7zX74BQuxS7UKtfnUM6KkKhmcu01A2Fq7xshyjesDvnQDYp9QYcrFDvlceaVvpWqQfpEt2Q9XIM0VQFdd2EMpXc4C9QlehgHT0URfOlUmC47BkfeJr5dpb4Pv_dbnFASQli0k7Cln9sN_Vf4Wqz4km-6UTpsNlVJxJE48_RK6Zsk7bklH_cpJE8tfltiPzdhyhY2oDh7SieUx6CNKphxtIezjzr-0SbD8cg', 'x-wl-uid':'11PAl+O2T6FeY67SmgtWeMBtyZ538YMsy2Zcpov67B4kL2DVIv3Nx7rEprTLBkI4W3ZZ954YAADFuG1oAMSt9uIgNhk3yQfBCY6pDMJUcXUzK6rFTPF4tPnrWr3utKPzHqJATwvQOHKE=', 'session-token':'"tzfdQwuhV4SLJ9/PfV3QSfg2b3LxOcRlqovsFb3AsrqZSnkxHCjhgMsO3d7NbIS7rOee9CPoh7Lxo8LF7EdVopNDFYLMzzOtDGVhnY4czMEVNS5VHAxjtdaDvRNDJC0OloD0EvRMDfHeXG70D93/wWVNfqU0c6nKEv0yTLU7pFpIbTicUYQQFeDZYf9tPQEepQxbZ1pBOU+0FjTwWUj3SnNdDf/SVmmk+feDLRuqn+WcP6w6CPQ1G03W/TACUuIHBz9mSMRFPU0il4m+s0KyzA=="', 'csm-hit':'s-F8Q4HD9WHE8M6GMQKQT4|1519186540551', 'session-id-time':'2082754801l' }
        #request.cookies ={ 'x-wl-uid':'1yOwLjX2WnY9mLM7WsqYh6e6V1fXMd1ZMNtSL2K4PXEdSmASj6jCPPBezf56CZBu8dNd+B0dbGk6FSb6sv3/5Z2bObc/d7RBUn4jelvgzhpzxeiQQPCByKtKt+rFfaF6lordo7OBLv6I=', 's_vn':'1538041742354%26vn%3D1','s_fid':'7FA70D7094115718-2F7725F9CDA62241', 'regStatus':'pre-register', 's_nr':'1506673939908-Repeat', 's_vnum':'1938673939908%26vn%3D1', 's_dslv':'1506673939908', 'JSESSIONID':'7D8C49FEC5F5D74FBFB8C44B4582E920', 'skin':'noskin','session-token':'fMF7GsLbD9OFUtBEffIAbQYQ+k+oGY4qtqc4L+jpdCrQuiLu4c9Hm8YSsbtiO5c9mfQ3IRuuQojX/N/SOZ1vcQVF58RRX0RpMeXLEPvV50aTQq+f/s/rV8yGoETGydD/29yEVxxEqc4cWCblz5+V28+sOHeSSoUiYwysN7+jUIC+ICgHh8EJAM1aQiONRz31', 'ubid-main':'131-1502033-8002851', 'session-id-time':'2082787201l', 'session-id':'143-4281452-3926723', 'csm-hit':'%7B%22tb%22%3A%223FYTGMTG10SZNP3AYFTN%2Bs-TWA04Y4WMDA93A0N8PZQ%7C1507802966608%22%7D' }

        if id:request.meta['id']=id
        if attr:request.meta['attr']=attr
        # set the meta['item'] to use the item in the next call back
        return request

    def setup_kafka(self):
        """Setup redis connection and idle signal.

        This should be called after the spider has set its crawler object.

        :param settings: The current Scrapy settings being used
        :type settings: scrapy.settings.Settings
        """
        if not hasattr(self, 'topic') or not self.topic:
            self.topic = '%s-starturls' % self.name
            self.topic ='general-starturls'

        _server=self.settings.get("KAFKA_LOCATION", 'localhost:9092')
        _partition_id = int(self.settings.get('SPIDER_PARTITION_ID', 0))
        _group = self.settings.get("GROUP","scrapy-crawler")
        _conn = KafkaClient(_server)
        self.topic1 = self.settings.get('TOPIC', 'frontier-todo')
        mongo_server = self.settings.get("MONGODB_SERVER", 'localhost')
        mongo_port = self.settings.get("MONGODB_PORT", 'MONGODB_PORT')
        self.mng_client = MongoClient(mongo_server, mongo_port)
        
        self.consumer = SimpleConsumer(_conn,_group,self.topic1, partitions=[_partition_id], buffer_size=131072, max_buffer_size=1048576) 
        self.producer = KafkaProducer(bootstrap_servers=[_server])
        self.MONGODB_DB = self.settings.get("MONGODB_DB")
        self.MONGODB_COLLECTION = "shop"
        self.SPIDER_NAME = self.settings.get("SPIDER_NAME")
        self.JOB_NAME = self.settings.get("JOB_NAME")
        self.LOCALE = self.settings.get("LOCALE",'us')
        self.MONGODB_DB_INPUT = self.settings.get("MONGODB_DB_INPUT", "scr")
        self.NUM_REPETE = self.settings.get("NUMBER_REPETE_SCRAPE", 7)
        self.JOB_INPUT_COLLECTION =  self.settings.get("JOB_INPUT_COLLECTION", "job_input3")
        self.ITEM_INPUT_COLLECTION =  self.settings.get("ITEM_INPUT_COLLECTION" ,'scrap_input4')
        self.crawler.signals.connect(self.spider_idle, signal=signals.spider_idle)
        self.crawler.signals.connect(self.item_scraped, signal=signals.item_scraped)
        self.log("Reading URLs from kafka topic '%s'" % self.kafka_topic)

    def next_request(self):
        """
        Returns a request to be scheduled.

        :rtype: str or None
        """
        message = self.consumer.get_messages(1)
        print "messsssssssssssssssssss",message 
        if message :
            url = self.process_kafka_message(message[0].message).split(",")[0].replace(",",' ').replace("#", ' ').replace("&", ' ').replace('"','').replace("'",'').replace("(",' ').replace(")",' ')
            #url = 'https://www.amazon.de/gp/offer-listing/' + url + '/ref=dp_olp_new?ie=UTF8&condition=new'
            url = 'https://www.amazon.de/dp/' + url +'/?th=1&psc=1'
            id = self.process_kafka_message(message[0].message).split(",")[1]
            attr =",".join( self.process_kafka_message(message[0].message).split(",")[2:])
            db = self.mng_client['shop_url_out']
            result1 = db.shop.find_one({'product_id':id ,'spider':self.SPIDER_NAME})
            print "asfdsdfasdfafsdfsdf",result1
            if  result1: return None

        else: url=None

        if not url:
            time_data =int(time.time())-98000            
            mng_db = self.mng_client[self.MONGODB_DB_INPUT] 
            db_cm = mng_db[self.JOB_INPUT_COLLECTION]
            try:result = list(db_cm.find({"spider_name":self.JOB_NAME, 'locale': self.LOCALE}).sort('start_time', -1))[0]
            except:result = list(db_cm.find({"repeate": {"$lt": self.NUM_REPETE}}).sort('start_time', -1))[0]
            result = list(db_cm.find({"spider_name":self.JOB_NAME ,'locale': self.LOCALE }).sort('start_time', -1))[0]
            print result
            
            if result:
                job_id = result['job_id']
                db = self.mng_client[self.MONGODB_DB] 
                #result1 = db.shop_url_out.find({'job_id':job_id,'seller_info':[]})
                result2 = db.scrap_input_mapping.find({'job_id':job_id, 'price': {"$ne": '' }  })
                #result2 = db.scrap_input_mapping.find({'job_id':job_id})
                time_data =int(time.time())-3600
                #print db.scrap_input_mapping.find({'job_id':job_id,'spider':self.SPIDER_NAME, 'price': {"$ne": '' }  }).count(),"ggggggggg"
                #return
                scraped_data = []  
                #scraped_data = [res["product_id"] for res in result1 ]
                scraped_data.extend([res.get("product_id",'') for res in result2  ])
                
                #print scraped_data, "rassssssssssssssssssssss"
                collection_name = self.ITEM_INPUT_COLLECTION
                db_cm = mng_db['scrap_input']
                #print db_cm,  list(db_cm.find({'job_id':job_id, "title": { "$exists": False}})), "ddddddddddddddddddddddd"
                #print "ddddddddddddddddddddddddddddddddd",list(db_cm.find({'job_id':job_id}))
                count = 0
                for document in list(db_cm.find({'job_id':job_id})):
                    try:
                        product_id = str(document[u'_id'])
                        #print product_id
                        if product_id not in scraped_data:
                            product_name = str(document[u'DPID'])
                            if product_name == '': continue                            
                            upc = str(document[u'UPC']).replace("'","").replace('"','')
                            msg = json.dumps({'job_id':str(job_id), 'DPID':product_name, 'UPC':upc})
                            future = self.producer.send(self.topic1 , product_name+ "," +product_id+ "," + msg)
                            record_metadata = future.get(timeout=10)
                            count = count+1
                            print record_metadata, count
                    except:
                        pass
            return None
        return self.make_requests_from_url(url,id,attr)

    def schedule_next_request(self):
        """Schedules a request if available"""
        req = self.next_request()
        if req:
            print dir(self)
            #req.headers={"Accept-Encoding": "gzip,deflate,sdch","Accept-Language": "en-US,en;q=0.8" , "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36" , "Accept": "*/*" ,"Referer": "https://www.amazon.de" , "Connection": "keep-alive" }
            self.crawler.engine.crawl(req, spider=self)
        else:
            print "Rahulllllllllllllllll"

    def spider_idle(self):
        """Schedules a request if available, otherwise waits."""
        try:
            self.schedule_next_request()
        except:
            pass
        raise DontCloseSpider

    def item_scraped(self, *args, **kwargs):
        """Avoids waiting for the spider to  idle before scheduling the next request"""
        self.schedule_next_request()


class ListeningKafkaSpider(KafkaSpiderMixin1, Spider):

    """
    Spider that reads urls from a kafka topic when idle.

    This spider will exit only if stopped, otherwise it keeps
    listening to messages on the given topic

    Specify the topic to listen to by setting the spider's `kafka_topic`.

    Messages are assumed to be URLS, one by message. To do custom
    processing of kafka messages, override the spider's `process_kafka_message`
    method
    """
    def _set_crawler(self, crawler):
        """
        :type crawler: scrapy.crawler.Crawler
        """
        super(ListeningKafkaSpider, self)._set_crawler(crawler)
        self.setup_kafka()
