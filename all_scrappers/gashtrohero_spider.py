

#Amazon seller list spider
import time
import scrapy
import json
class GastroHeroItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    articleno = scrapy.Field()
    price = scrapy.Field()
    url=scrapy.Field()
    breadcrumb=scrapy.Field()
    description=scrapy.Field()
    attr_dict=scrapy.Field()
	
    

class Spider(scrapy.Spider):
    
    name = "gashtrohero"
    allowed_domain=[]
    start_urls = ['https://www.gastro-hero.de/']
    

    def parse(self, response):

        urls_done = []
        
        urls= [["1","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChlschr%C3%A4nke/Edelstahl-K%C3%BChlschr%C3%A4nke"],
["2","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChlschr%C3%A4nke/Getr%C3%A4nkek%C3%BChlschr%C3%A4nke"],
["3","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChlschr%C3%A4nke/Bark%C3%BChlschr%C3%A4nke"],
["4","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChlschr%C3%A4nke/Lagerk%C3%BChlschr%C3%A4nke"],
["5","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChlschr%C3%A4nke/Weink%C3%BChlschr%C3%A4nke"],
["6","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChlschr%C3%A4nke/Tiefk%C3%BChlschr%C3%A4nke"],
["7","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChlschr%C3%A4nke/Kombik%C3%BChlschr%C3%A4nke"],
["8","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChlschr%C3%A4nke/Fischk%C3%BChlschr%C3%A4nke"],
["9","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChlschr%C3%A4nke/B%C3%A4ckereik%C3%BChlschr%C3%A4nke"],
["10","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChlschr%C3%A4nke/Minibark%C3%BChlschrank"],
["11","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChltische/K%C3%BChltische"],
["12","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChltische/K%C3%BChltische/K%C3%BChltische-Mini"],
["13","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChltische/K%C3%BChltische/Gastro-K%C3%BChltische-700"],
["14","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChltische/K%C3%BChltische/Gastro-K%C3%BChltische-600"],
["15","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChltische/K%C3%BChltische/Unterbauk%C3%BChltische"],
["16","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChltische/Tiefk%C3%BChltische"],
["17","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChltische/Bark%C3%BChltische"],
["18","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChltische/B%C3%A4ckereik%C3%BChltische"],
["19","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChltische/Pizza-K%C3%BChltische"],
["20","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChltische/Belegstationen"],
["21","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChltische/Durchreichek%C3%BChltische"],
["22","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChltheken/Imbissk%C3%BChltheken"],
["23","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChltheken/Gastroline-K%C3%BChltheken"],
["24","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChltheken/Bartheken"],
["25","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChltheken/Eistheken"],
["26","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChltheken/Fischkuehltheken"],
["27","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChltheken/Kuchentheken"],
["28","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChltheken/Salatbars"],
["29","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChlzellen-und-Aggregate/K%C3%BChlzellen"],
["30","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChlzellen-und-Aggregate/K%C3%BChlaggregate"],
["31","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChlzellen-und-Aggregate/Tiefk%C3%BChlzellen"],
["32","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChlzellen-und-Aggregate/Tiefk%C3%BChlaggregate"],
["33","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChlzellen-und-Aggregate/K%C3%BChlzellenregale"],
["34","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChlvitrinen"],
["35","https://www.gastro-hero.de/K%C3%BChltechnik/Biertheken"],
["36","https://www.gastro-hero.de/K%C3%BChltechnik/Saladetten"],
["37","https://www.gastro-hero.de/K%C3%BChltechnik/Eisw%C3%BCrfelbereiter/Vollw%C3%BCrfelbereiter"],
["38","https://www.gastro-hero.de/K%C3%BChltechnik/Eisw%C3%BCrfelbereiter/Hohlw%C3%BCrfelbereiter"],
["39","https://www.gastro-hero.de/K%C3%BChltechnik/Eisw%C3%BCrfelbereiter/Flockeneisbereiter"],
["40","https://www.gastro-hero.de/K%C3%BChltechnik/Eisw%C3%BCrfelbereiter/Scherbeneisbereiter"],
["41","https://www.gastro-hero.de/K%C3%BChltechnik/Eisw%C3%BCrfelbereiter/Eiscrusher"],
["42","https://www.gastro-hero.de/K%C3%BChltechnik/Eisw%C3%BCrfelbereiter/Zubeh%C3%B6r"],
["43","https://www.gastro-hero.de/K%C3%BChltechnik/Tiefk%C3%BChltruhen"],
["44","https://www.gastro-hero.de/K%C3%BChltechnik/Schockfroster"],
["45","https://www.gastro-hero.de/K%C3%BChltechnik/Flaschenk%C3%BChler"],
["46","https://www.gastro-hero.de/K%C3%BChltechnik/K%C3%BChlaufs%C3%A4tze"],
["47","https://www.gastro-hero.de/K%C3%BChltechnik/Wandk%C3%BChlregale"],
["48","https://www.gastro-hero.de/K%C3%BChltechnik/Sushi-Vitrinen"],
["49","https://www.gastro-hero.de/K%C3%BChltechnik/Fassk%C3%BChler"],
["50","https://www.gastro-hero.de/Kochger%C3%A4te/Herde"],
["51","https://www.gastro-hero.de/Kochger%C3%A4te/Herde/Gasherde"],
["52","https://www.gastro-hero.de/Kochger%C3%A4te/Herde/Elektroherde"],
["53","https://www.gastro-hero.de/Kochger%C3%A4te/Herde/Ceranherde"],
["54","https://www.gastro-hero.de/Kochger%C3%A4te/Herde/Induktionsherde"],
["55","https://www.gastro-hero.de/Kochger%C3%A4te/Fritteusen/Gas-Fritteusen"],
["56","https://www.gastro-hero.de/Kochger%C3%A4te/Fritteusen/Elektro-Fritteusen"],
["57","https://www.gastro-hero.de/Kochger%C3%A4te/Grillplatten/Gas-Grillplatten"],
["58","https://www.gastro-hero.de/Kochger%C3%A4te/Grillplatten/Elektro-Grillplatten"],
["59","https://www.gastro-hero.de/Kochger%C3%A4te/Bain-Maries"],
["60","https://www.gastro-hero.de/Kochger%C3%A4te/Nudelkocher/Gas-Nudelkocher"],
["61","https://www.gastro-hero.de/Kochger%C3%A4te/Nudelkocher/Elektro-Nudelkocher"],
["62","https://www.gastro-hero.de/Kochger%C3%A4te/Lavasteingrills"],
["63","https://www.gastro-hero.de/Kochger%C3%A4te/Kochkessel/Gas-Kochkessel"],
["64","https://www.gastro-hero.de/Kochger%C3%A4te/Kochkessel/Elektro-Kochkessel"],
["65","https://www.gastro-hero.de/Kochger%C3%A4te/Kippbratpfanne/Gas-Kippbratpfannen"],
["66","https://www.gastro-hero.de/Kochger%C3%A4te/Kippbratpfanne/Elektro-Kippbratpfannen"],
["67","https://www.gastro-hero.de/Kochger%C3%A4te/Hei%C3%9Fluft%C3%B6fen-und-Kombid%C3%A4mpfer/Kombid%C3%A4mpfer"],
["68","https://www.gastro-hero.de/Kochger%C3%A4te/Hei%C3%9Fluft%C3%B6fen-und-Kombid%C3%A4mpfer/Hei%C3%9Fluft%C3%B6fen"],
["69","https://www.gastro-hero.de/Kochger%C3%A4te/Hei%C3%9Fluft%C3%B6fen-und-Kombid%C3%A4mpfer/B%C3%A4ckereiback%C3%B6fen"],
["70","https://www.gastro-hero.de/Kochger%C3%A4te/Hei%C3%9Fluft%C3%B6fen-und-Kombid%C3%A4mpfer/Kartoffel%C3%B6fen"],
["71","https://www.gastro-hero.de/Kochger%C3%A4te/Hei%C3%9Fluft%C3%B6fen-und-Kombid%C3%A4mpfer/Kn%C3%B6deld%C3%A4mpfer"],
["72","https://www.gastro-hero.de/Kochger%C3%A4te/Hei%C3%9Fluft%C3%B6fen-und-Kombid%C3%A4mpfer/Zubeh%C3%B6r"],
["73","https://www.gastro-hero.de/Kochger%C3%A4te/Wokherde"],
["74","https://www.gastro-hero.de/Kochger%C3%A4te/Kochkleinger%C3%A4te/Induktionskochfelder"],
["75","https://www.gastro-hero.de/Kochger%C3%A4te/Kochkleinger%C3%A4te/Induktions-Woks"],
["76","https://www.gastro-hero.de/Kochger%C3%A4te/Kochkleinger%C3%A4te/Gaskocher"],
["77","https://www.gastro-hero.de/Kochger%C3%A4te/Kochkleinger%C3%A4te/Reiskocher"],
["78","https://www.gastro-hero.de/Kochger%C3%A4te/Kochkleinger%C3%A4te/Tischfritteusen"],
["79","https://www.gastro-hero.de/Kochger%C3%A4te/Kochkleinger%C3%A4te/Grillplatten"],
["80","https://www.gastro-hero.de/Kochger%C3%A4te/Kochkleinger%C3%A4te/Suppent%C3%B6pfe"],
["81","https://www.gastro-hero.de/Kochger%C3%A4te/Kochkleinger%C3%A4te/Currywurst-Schneider"],
["82","https://www.gastro-hero.de/Kochger%C3%A4te/Kochkleinger%C3%A4te/Mikrowellen"],
["83","https://www.gastro-hero.de/Kochger%C3%A4te/Kochkleinger%C3%A4te/Sous-Vide-Garer"],
["84","https://www.gastro-hero.de/Kochger%C3%A4te/Kochserien/ECO-70"],
["85","https://www.gastro-hero.de/Kochger%C3%A4te/Kochserien/Dexion-66"],
["86","https://www.gastro-hero.de/Kochger%C3%A4te/Kochserien/Dexion-77"],
["87","https://www.gastro-hero.de/Kochger%C3%A4te/Kochserien/Dexion-700"],
["88","https://www.gastro-hero.de/Kochger%C3%A4te/Kochserien/Dexion-980"],
["89","https://www.gastro-hero.de/Kochger%C3%A4te/Kochserien/PROFI-70"],
["90","https://www.gastro-hero.de/Kochger%C3%A4te/Kochserien/PREMIUM-70"],
["91","https://www.gastro-hero.de/Kochger%C3%A4te/Kochserien/Bartscher"],
["92","https://www.gastro-hero.de/Kochger%C3%A4te/Elektro-Kochger%C3%A4te"],
["93","https://www.gastro-hero.de/Kochger%C3%A4te/Gas-Kochger%C3%A4te"],
["94","https://www.gastro-hero.de/Pizzeria-und-Grill/Aufschnittmaschinen"],
["95","https://www.gastro-hero.de/Pizzeria-und-Grill/D%C3%B6nergrills-Gyrosgrills"],
["96","https://www.gastro-hero.de/Pizzeria-und-Grill/Pizza%C3%B6fen/Einkammer-Pizza%C3%B6fen"],
["97","https://www.gastro-hero.de/Pizzeria-und-Grill/Pizza%C3%B6fen/Doppelkammer-Pizza%C3%B6fen"],
["98","https://www.gastro-hero.de/Pizzeria-und-Grill/Pizza%C3%B6fen/Durchlauf%C3%B6fen"],
["99","https://www.gastro-hero.de/Pizzeria-und-Grill/Pizza%C3%B6fen/Zubeh%C3%B6r"],
["100","https://www.gastro-hero.de/Pizzeria-und-Grill/Gas-Kombibr%C3%A4ter"],
["101","https://www.gastro-hero.de/Pizzeria-und-Grill/Gem%C3%BCseschneider"],
["102","https://www.gastro-hero.de/Pizzeria-und-Grill/Kontaktgrills"],
["103","https://www.gastro-hero.de/Pizzeria-und-Grill/Grillplatten"],
["104","https://www.gastro-hero.de/Pizzeria-und-Grill/Pizzatische"],
["105","https://www.gastro-hero.de/Pizzeria-und-Grill/Saladetten"],
["106","https://www.gastro-hero.de/Pizzeria-und-Grill/Teigknetmaschinen/Spiralteigknetmaschinen"],
["107","https://www.gastro-hero.de/Pizzeria-und-Grill/Teigknetmaschinen/Planetenr%C3%BChrwerke"],
["108","https://www.gastro-hero.de/Pizzeria-und-Grill/Teigausrollmaschinen"],
["109","https://www.gastro-hero.de/Pizzeria-und-Grill/Teigpresse"],
["110","https://www.gastro-hero.de/Pizzeria-und-Grill/H%C3%A4hnchengrills"],
["111","https://www.gastro-hero.de/K%C3%BCchenger%C3%A4te/Kaffeemaschinen/Kaffeemaschinen"],
["112","https://www.gastro-hero.de/K%C3%BCchenger%C3%A4te/Kaffeemaschinen/Kaffeem%C3%BChlen"],
["113","https://www.gastro-hero.de/K%C3%BCchenger%C3%A4te/Kaffeemaschinen/Zubeh%C3%B6r"],
["114","https://www.gastro-hero.de/K%C3%BCchenger%C3%A4te/Mikrowellen"],
["115","https://www.gastro-hero.de/K%C3%BCchenger%C3%A4te/Wurstw%C3%A4rmer"],
["116","https://www.gastro-hero.de/K%C3%BCchenger%C3%A4te/Hei%C3%9Fe-Theken"]]

        for url in urls:
            try:
                req = scrapy.Request(url[1] , callback=self.parse3 , meta={'allpagesdict':{}})
                req.meta['item_id'] = url[0]
                req.meta['req'] = url[1]
                if url[0] not in urls_done: 
                    yield req
                    time.sleep(.3)
            except: raise

    def parse3(self,response):
        titleurllist=response.xpath('//*[@id="products-list"]/li')
        #print "LENGTH of titles is : ",len(titlelist)
        for titleurls in titleurllist:
            
            titlesuburl=titleurls.xpath('div[2]/div/h2/a/@href').extract()
            #print title
            if titlesuburl:
                titleurl=titlesuburl[0]
                #print "TITLEURL IS : ",titleurl
                # item = GastroHeroItem()
                # item['url']=titleurl
                # item['breadcrumb']=response.url
                # yield item
                try:
                    req = scrapy.Request(titleurl,callback=self.parse4)
                    yield req
                    #time.sleep(.3)
                except : raise
				
            else:
                pass
        
			
        print "AFTER YIELD STATEMENT"
        allpagesdict1=response.meta['allpagesdict']
        #print "ALLPAGESDICT : ",allpagesdict
        allpageslist=response.xpath('//*[@class="toolbar-bottom"]/div[1]/div[2]/div/ol/li')
 
        for page in allpageslist:
            nextpageurl=page.xpath('a/@href').extract()
            #print "NEXT PAGE URL : ",nextpageurl
            nextpageno=page.xpath('a/text()').extract()
            if not nextpageno: nextpageno=page.xpath('text()').extract()
            nextbutton=page.xpath('@class').extract()
            if nextbutton:
                if nextbutton[0].replace(" ","").upper()=="NEXT" or nextbutton[0].replace(" ","").upper()=="PREVIOUS" :
                    pass
					
                else:
                    #print "NEXT PAGE No. : ",nextpageno
                    if nextpageno[0] in allpagesdict1.keys():
                        pass
                        #continue
                    else:
                        #if nextpageurl[0].replace(" ","")=="":
                        if not nextpageurl:
                            #print "SELECTED URL : "
                            allpagesdict1[nextpageno[0]]="selected"
                        else:
                            allpagesdict1[nextpageno[0]]=nextpageurl[0]
                            #print nextpageurl[0]
                            try:
                                req = scrapy.Request(nextpageurl[0],callback=self.parse3,meta={'allpagesdict':allpagesdict1})
                                yield req
                                #time.sleep(.3)
                            except: raise
            else:
                #print "NEXT PAGE No. : ",nextpageno
                if nextpageno[0] in allpagesdict1.keys():
                    pass
                    #continue
                else:
                    #if nextpageurl[0].replace(" ","")=="":
                    if not nextpageurl:
                        #print "SELECTED URL : "
                        allpagesdict1[nextpageno[0]]="selected"
                    else:
                        allpagesdict1[nextpageno[0]]=nextpageurl[0]
                        #print nextpageurl[0]
                        try:
                            req = scrapy.Request(nextpageurl[0],callback=self.parse3,meta={'allpagesdict':allpagesdict1})
                            yield req
                            #time.sleep(.3)
                        except: raise
					
    def parse4(self,response):
        item=GastroHeroItem()
        title=response.xpath('//*[@id="product_addtocart_form"]/div[2]/h1/text()').extract()
        item['title']=("".join(title)).replace("\t","").replace("\n","")
        articleno=response.xpath('//*[@id="product_addtocart_form"]/div[4]/div[2]/span[2]/text()').extract()
        if not articleno: articleno=response.xpath('//*[@id="product_addtocart_form"]/div[4]/div[3]/span[2]/text()').extract()
		
        #print articleno
        item['articleno']="".join(articleno)
        #cost=response.xpath('//*[@class="gastro_content_box price_box headless"]/li[2]/span[2]/text()').extract()
        cost=response.xpath('//span[@itemprop="offers"]/text()').extract()
        if cost: item['price']=("".join(cost)).encode('ascii','ignore').replace('.','').replace(',','.').replace(" ","").replace("\n","")
        # if not cost: cost=response.xpath('//*[@id="buy_form"]/div/div/div[2]/ul[1]/li[5]/span/text()').extract()
        # if not cost: cost=response.xpath('//*[@id="buy_form"]/div/div/div[3]/ul[1]/li[4]/span/text()').extract()
        # if not cost: cost=response.xpath('//*[@id="buy_form"]/div/div/div[3]/ul[1]/li[4]/span/text()').extract()
        #print cost
        #cost1=cost[0].split(":")[1]
        if not cost : cost= response.xpath('//p[@class="regular-price-block"]/span[2]//text()').extract()[1]
        item['price']="{0:.2f}".format( float(("".join(cost)).encode('ascii','ignore').replace('.','').replace(',','.').replace('*','')) * 1.19)
        #item['price']=("".join(cost)).encode('ascii','ignore').replace('.','').replace(',','.').replace(" ","").replace("\n","")
        
        item['url']=response.url
        desc=response.xpath('//*[@id="product-tabs"]/div/div[2]/div//text()').extract()
        item['description']=(",".join(desc)).replace("\n","").replace("\t","")
        bread=response.xpath('//*[@id="root-wrapper"]/div/div/div[2]/div[2]/div/div[1]/ul/li//text()').extract()
        bread1=filter(lambda x: x != '\n', bread)
        item['breadcrumb']=("/".join(bread1)).replace("\t","")
        attribute_dict={}
        table=response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr')
        for row in table:
            key=row.xpath('th/text()').extract()
            value=row.xpath('td/text()').extract()
            attribute_dict[key[0]]=value[0]
        item['attr_dict']=json.dumps(attribute_dict)
        yield item
		