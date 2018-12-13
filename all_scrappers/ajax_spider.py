

#Amazon seller list spider
import time
import scrapy
import json
from scrapy.http import FormRequest
import requests
from lxml import etree, html
from StringIO import StringIO
class GastroItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    articleno = scrapy.Field()
    price = scrapy.Field()
    url=scrapy.Field()
    brand=scrapy.Field()
    breadcrumb=scrapy.Field()
    description=scrapy.Field()

    

class Spider(scrapy.Spider):
    
    name = "gastro24ajax"
    allowed_domain=[]
    start_urls = ['https://www.gastro-hero.de/']
    

    def parse(self, response):

        urls_done = []
        
        #urls= [["1","http://www.gastro24.de/Arbeitsschrank-ECO-offen-verschiedene-Ausfuehrungen"]]
        urls= [["1","http://www.gastro24.de/Arbeitsplatte-Variabel-aus-Edelstahl-160x70cm-wandseitig-aufgekantet"]]

        for url in urls:
            try:
                req = scrapy.Request(url[1] , callback=self.parse3)
                req.meta['item_id'] = url[0]
                req.meta['req'] = url[1]
                if url[0] not in urls_done: 
                    yield req
                    time.sleep(.3)
            except: raise


    """def parse3(self,response):
        #item=GastroItem()
        breadcrumblist=response.xpath('//*[@id="content"]/div[1]/span/a//text()').extract()
        breadcrumb=">".join(breadcrumblist)
        ajaxurl="http://www.gastro24.de/toolsajax.server.php"
        xjxargs1="<xjxobj><e><k>inWarenkorb</k><v>S<![CDATA[In den Warenkorb]]></v></e><e><k>a</k><v>S234831</v></e><e><k>aK</k><v>S108479</v></e><e><k>wke</k><v>S1</v></e><e><k>show</k><v>S1</v></e><e><k>kKundengruppe</k><v>S1</v></e><e><k>kSprache</k><v>S1</v></e><e><k>JTLSHOP</k><v>Sqe27afp85au5jbn7kk2irmnc53</v></e><e><k>eigenschaftwert_1202</k><v>S"
        xjxargs2="</v></e><e><k>eigenschaftwert_1203</k><v>S4717</v></e><e><k>anzahl</k><v>S1</v></e><e><k>Wunschliste</k><v>S</v></e></xjxobj>"
        variantslist= response.xpath('//div[@class="variations section_box"]/ul/li[2]/select/option[2]')
        for variants in variantslist:
            variant=variants.xpath('@value').extract()
            if variant[0]!="0":
                xjxargs=xjxargs1+variant[0]+xjxargs2
                
                #xjxargs3="S"+variant[0]
                xjxargs3="S4660"
                xjxargs4="S1196"
                xjxargs5="NO"
                xjxargs6="tauscheVariationKombi"
                xjxargs7="checkVarkombiDependencies"
                xjxargs8="<xjxobj><e><k>inWarenkorb</k><v>S<![CDATA[In den Warenkorb]]></v></e><e><k>a</k><v>S234773</v></e><e><k>aK</k><v></v></e><e><k>wke</k><v>S1</v></e><e><k>show</k><v>S1</v></e><e><k>kKundengruppe</k><v>S1</v></e><e><k>kSprache</k><v>S1</v></e><e><k>JTLSHOP</k><v>Sqe27afp85au5jbn7kk2irmnc53</v></e><e><k>eigenschaftwert_1195</k><v>S4662</v></e><e><k>eigenschaftwert_1196</k><v>S4660</v></e><e><k>anzahl</k><v>S1</v></e><e><k>Wunschliste</k><v>S</v></e></xjxobj>"
            
                xjxargs9=[xjxargs8, xjxargs5, xjxargs4, xjxargs3]
                frmdata={"xjxfun":xjxargs6, "xjxargs[]":xjxargs9}
            
                yield FormRequest(ajaxurl, method='POST', formdata=frmdata, callback=self.parse4, meta={'bread':breadcrumb, 'url':response.url})"""
				
				
    def parse3(self,response):
        #item=GastroItem()
        breadcrumblist=response.xpath('//*[@id="content"]/div[1]/span/a//text()').extract()
        breadcrumb=">".join(breadcrumblist)
        ajaxurl="http://www.gastro24.de/toolsajax.server.php"
        xjxargsarray1="<xjxobj><e><k>inWarenkorb</k><v>S<![CDATA[In den Warenkorb]]></v></e><e><k>a</k><v>S"
        var1=response.xpath('//*[@id="AktuellerkArtikel"]/@value').extract()
        #print "Variable 1: ",var1
        xjxargsarray2="</v></e><e><k>aK</k><v></v></e><e><k>wke</k><v>S1</v></e><e><k>show</k><v>S1</v></e><e><k>kKundengruppe</k><v>S1</v></e><e><k>kSprache</k><v>S1</v></e><e><k>JTLSHOP</k><v>Sqe27afp85au5jbn7kk2irmnc53</v></e><e><k>"
        var2=response.xpath('//*[@id="article_buyfield"]/fieldset/div/ul[1]/li[2]/select/@name').extract()
        #print "Variable 2: ",var2
        xjxargsarray3="</k><v>S"
        #value in for loop
        xjxargsarray4="</v></e><e><k>"
        secondvariantname=response.xpath('//*[@id="article_buyfield"]/fieldset/div/ul[2]/li[2]/label[1]/input/@name').extract()
        #print "secondvariantname : ",secondvariantname
        xjxargsarray5="</k><v>S"
        #value in first for loop
        xjxargsarray6="</v></e><e><k>anzahl</k><v>S1</v></e><e><k>Wunschliste</k><v>S</v></e></xjxobj>"
        secondvariantlist=response.xpath('//*[@id="article_buyfield"]/fieldset/div/ul[2]/li/label')
        for secondvariants in secondvariantlist:
            secondvariant=secondvariants.xpath('input/@value').extract()
            #print "secondvariant : ",secondvariant
            variantslist= response.xpath('//div[@class="variations section_box"]/ul/li[2]/select/option')
            for variants in variantslist:
                variant=variants.xpath('@value').extract()
                if variant[0]!="0":
                    #print variant[0]
                    xjxargsfunc="tauscheVariationKombi"
                    xjxargs=xjxargsarray1+var1[0]+xjxargsarray2+var2[0]+xjxargsarray3+variant[0]+xjxargsarray4+secondvariantname[0]+xjxargsarray5+secondvariant[0]+xjxargsarray6
                    xjxargs1="NO"
                    fourthargs=response.xpath('//*[@id="article_buyfield"]/fieldset/div/ul[1]/li[2]/select/@name').extract()
                    fourtharg=(fourthargs[0].split('_'))[1]
                    xjxargs2="S"+fourtharg
                    xjxargs3="S"+variant[0]
                    xjxargs9=[ xjxargs, xjxargs1, xjxargs2, xjxargs3]
                    frmdata={"xjxfun":xjxargsfunc, "xjxargs[]":xjxargs9}
                    yield FormRequest(ajaxurl, method='POST', formdata=frmdata, callback=self.parse4, meta={'bread':breadcrumb, 'url':response.url})

            
    def parse4(self,response):
        item=GastroItem()
        #bread=response.meta['bread']
        #print bread
        #f1=open("gastro24.html","w")
        #f1.write(response.body)
        #f1.close()
        #fl= open("amzg3.html",'w')
        #fl.write(response.body)
        #fl.close()
        
        #inputfh=open('amzg3.html', 'r')
        
        #filecontent = inputfh.read()
        
        #inputfh.close()
        #print response.body
        #cost=response.xpath('//*[@id="buy_form"]/div/div/div[2]/ul[1]/li[4]/span/text()').extract()
        #print cost
        parser = html.HTMLParser()
        
        tree = html.parse(StringIO(response.body), parser)
        
        
        cost=tree.xpath('//*[@id="buy_form"]/div/div/div[2]/ul[1]/li[4]/span/text()')
        
        if not cost: cost=tree.xpath('//*[@id="buy_form"]/div/div/div[2]/ul[1]/li[5]/span/text()')
        if not cost: cost=tree.xpath('//*[@id="buy_form"]/div/div/div[3]/ul[1]/li[4]/span/text()')
        if not cost: cost=tree.xpath('//*[@id="buy_form"]/div/div/div[3]/ul[1]/li[4]/span/text()')
        cost1=(("".join(cost)).encode('ascii','ignore')).split(":")[1]
        item['price']=cost1.replace('.','').replace(',','.').replace(" ","").replace("\n","")
        title=tree.xpath('//*[@id="buy_form"]/div/div/div[1]/h1/text()')
        item['title']= ("".join(title)).replace("\t","").replace("\n","")
        articleno=tree.xpath('//*[@class="gastro_content_box price_box headless"]/li[1]/span/text()')
        #print articleno
        item['articleno']= "".join(articleno)
        brand=tree.xpath('//*[@id="buy_form"]/div/div/div[1]/div[2]/ul/li[1]/a/@href')
        item['brand']= "".join(brand)
        #print response.url
        desc=tree.xpath('//*[@id="description"]/div//text()')
        item['description']= (",".join(desc)).replace("\n","").replace("\t","")
        item['breadcrumb']=response.meta['bread']
        item['url']=response.meta['url']
        yield item
        