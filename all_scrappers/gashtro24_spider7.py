

#Amazon seller list spider
import time
import scrapy
from scrapy.linkextractors import LinkExtractor

from scrapy_splash import SplashRequest
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
    
    name = "gashtro247"
    allowed_domain=[]
    start_urls = ['http://www.gastro24.de/']
    

    def parse(self, response):

        urls_done = []
        
        urls= [["1","http://www.gastro24.de/Kuehlplatten"],
["2","http://www.gastro24.de/Slush-Ice-Maschinen"],
["3","http://www.gastro24.de/Flaschenkuehlung"],
["4","http://www.gastro24.de/Wandkuehlregale"],
["5","http://www.gastro24.de/Saladetten"],
["6","http://www.gastro24.de/Tiefkuehltruhen"],
["7","http://www.gastro24.de/Schockfroster-Schnellabkuehler"],
["8","http://www.gastro24.de/Kuehlwannen"],
["9","http://www.gastro24.de/Laborkuehlung"],
["10","http://www.gastro24.de/Kuehlelemente"],
["11","http://www.gastro24.de/Kuehlzellen"],
["12","http://www.gastro24.de/Tiefkuehlzellen"],
["13","http://www.gastro24.de/Minikuehlzellen"],
["14","http://www.gastro24.de/Kuehlzellenregale"],
["15","http://www.gastro24.de/Biertheken/Biertheken"],
["16","http://www.gastro24.de/Mobile-Zapfanlagen"],
["17","http://www.gastro24.de/Fasskuehler/Fasskuehler"],
["18","http://www.gastro24.de/Fasskuehler-Zubehoer"],
["19","http://www.gastro24.de/Kuehlinseln-Tiefkuehlinseln"],
["20","http://www.gastro24.de/Einbauvitrinen"],
["21","http://www.gastro24.de/Kuehltonnen"],
["22","http://www.gastro24.de/Imbisstheken"],
["23","http://www.gastro24.de/Fleischereitheken"],
["24","http://www.gastro24.de/Eistheken"],
["25","http://www.gastro24.de/Baeckereitheken"],
["26","http://www.gastro24.de/Fischtheken"],
["27","http://www.gastro24.de/Kuehltheken-Zubehoer"],
["28","http://www.gastro24.de/Tischvitrinen"],
["29","http://www.gastro24.de/Panoramavitrinen"],
["30","http://www.gastro24.de/Eisflockenmaschine"],
["31","http://www.gastro24.de/Eiswuerfelmaschine"],
["32","http://www.gastro24.de/Vorratsbehaelter-fuer-Eiswuerfelmaschinen"],
["33","http://www.gastro24.de/Tapasvitrinen"],
["34","http://www.gastro24.de/Sushivitrinen"],
["35","http://www.gastro24.de/Pizzaaufsatzvitrinen"],
["36","http://www.gastro24.de/Begleitkuehler"],
["37","http://www.gastro24.de/Decken-Kuehlaggregate"],
["38","http://www.gastro24.de/Huckepack-Kuehlaggregate"],
["39","http://www.gastro24.de/Monoblock-Kuehlaggregate"],
["40","http://www.gastro24.de/Split-Kuehlaggregate"],
["41","http://www.gastro24.de/Tiefkuehlaggregate"],
["42","http://www.gastro24.de/Gastro-Kuehltische"],
["43","http://www.gastro24.de/Tiefkuehltische"],
["44","http://www.gastro24.de/Barkuehltische"],
["45","http://www.gastro24.de/Baeckereikuehltische"],
["46","http://www.gastro24.de/Kuehlunterbauten"],
["47","http://www.gastro24.de/Pizzakuehltische"],
["48","http://www.gastro24.de/Fleischreifeschraenke"],
["49","http://www.gastro24.de/Edelstahl-Kuehlschraenke"],
["50","http://www.gastro24.de/Getraenkekuehlschraenke"],
["51","http://www.gastro24.de/Barkuehlschraenke"],
["52","http://www.gastro24.de/Lagerkuehlschraenke"],
["53","http://www.gastro24.de/Weinkuehlschraenke"],
["54","http://www.gastro24.de/Tiefkuehlschraenke"],
["55","http://www.gastro24.de/Kombischraenke"],
["56","http://www.gastro24.de/Fischkuehlschraenke"],
["57","http://www.gastro24.de/Baeckereikuehlschraenke"],
["58","http://www.gastro24.de/Minibarkuehlschraenke"],
["59","http://www.gastro24.de/Aufschnittmaschinen"],
["60","http://www.gastro24.de/Braeter-Rostbraeter"],
["61","http://www.gastro24.de/Crepegeraete-Crepe-Maker"],
["62","http://www.gastro24.de/Currywurstschneider"],
["63","http://www.gastro24.de/Cutter"],
["64","http://www.gastro24.de/Dampfgarer"],
["65","http://www.gastro24.de/Doerrautomaten"],
["66","http://www.gastro24.de/Durchlauftoaster"],
["67","http://www.gastro24.de/Einkochautomaten"],
["68","http://www.gastro24.de/Fettabscheider"],
["69","http://www.gastro24.de/Fleisch-Knochensaegen"],
["70","http://www.gastro24.de/Fleischmischer-Fleischmaschinen"],
["71","http://www.gastro24.de/Fleischwolf-Kaesereibenkombination"],
["72","http://www.gastro24.de/Verpackungsmaschinen-Folienmaschinen"],
["73","http://www.gastro24.de/Hamburgerpresse"],
["74","http://www.gastro24.de/Hockerkocher"],
["75","http://www.gastro24.de/Hotdoggeraete-Wuerstchengeraete"],
["76","http://www.gastro24.de/Kartoffelschaelmaschine"],
["77","http://www.gastro24.de/Kaesereiben-Kaeseschneider"],
["78","http://www.gastro24.de/Kontaktgrills"],
["79","http://www.gastro24.de/Kuechenmaschinen"],
["80","http://www.gastro24.de/Mikrowellen"],
["81","http://www.gastro24.de/Multipfannen"],
["82","http://www.gastro24.de/Pizzateigmaschinen-Ausrollmaschinen"],
["83","http://www.gastro24.de/Pizzateigpressen"],
["84","http://www.gastro24.de/Pommeswannen-Pommeswaermer"],
["85","http://www.gastro24.de/Reiskocher-Reiswaermer"],
["86","http://www.gastro24.de/Salamander"],
["87","http://www.gastro24.de/Sous-Vide-Geraete"],
["88","http://www.gastro24.de/Speiseeismaschinen"],
["89","http://www.gastro24.de/Stabmixer-Ruehrbesen"],
["90","http://www.gastro24.de/Teigausrollmaschine"],
["91","http://www.gastro24.de/Teigballenportionierer"],
["92","http://www.gastro24.de/Thekenkessel-/-Suppenkessel"],
["93","http://www.gastro24.de/Toaster-klassisch"],
["94","http://www.gastro24.de/Waffeleisen"],
["95","http://www.gastro24.de/Waermebruecken-Waermelampen"],
["96","http://www.gastro24.de/Warmhalteplatten"],
["97","http://www.gastro24.de/Wok-Herde-Chinaherde"],
["98","http://www.gastro24.de/Wurstfuellmaschinen"],
["99","http://www.gastro24.de/Bain-Maries-Einbaumodelle"],
["100","http://www.gastro24.de/Bain-Maries-Standmodelle"],
["101","http://www.gastro24.de/Bain-Maries-Tischmodelle"],
["102","http://www.gastro24.de/Bain-Maries-Einsaetze"],
["103","http://www.gastro24.de/Bain-Marie-Thermosystem"],
["104","http://www.gastro24.de/Bain-Marie-Wagen"],
["105","http://www.gastro24.de/Herde/Gasherde"],
["106","http://www.gastro24.de/Herde/Elektroherde"],
["107","http://www.gastro24.de/Herde/Ceranherde"],
["108","http://www.gastro24.de/Herde/Induktionsherde"],
["109","http://www.gastro24.de/Doener-Gyrosgrills-Elektro"],
["110","http://www.gastro24.de/Doener-Gyrosgrills-Gas"],
["111","http://www.gastro24.de/Zubehoer-fuer-Potis-Geraete"],
["112","http://www.gastro24.de/Haehnchengrill-Elektrisch"],
["113","http://www.gastro24.de/Haehnchengrill-Gas"],
["114","http://www.gastro24.de/Gas-Kombibraeter"],
["115","http://www.gastro24.de/Grill-Tischgeraete"],
["116","http://www.gastro24.de/Lavasteingrills"],
["117","http://www.gastro24.de/Holzkohlegrill"],
["118","http://www.gastro24.de/Zubehoer_5"],
["119","http://www.gastro24.de/Teppanyaki-Grills"],
["120","http://www.gastro24.de/Vakuumiergeraete"],
["121","http://www.gastro24.de/Vakuummaschinen-Zubehoer"],
["122","http://www.gastro24.de/Spiralteigkneter"],
["123","http://www.gastro24.de/Planetenruehrmaschinen"],
["124","http://www.gastro24.de/Einkammer-Pizzaoefen"],
["125","http://www.gastro24.de/Doppelkammer-Pizzaoefen"],
["126","http://www.gastro24.de/Durchlaufoefen"],
["127","http://www.gastro24.de/Pizzaoefen-zur-Eckmontage"],
["128","http://www.gastro24.de/Pizzaoefen-Zubehoer"],
["129","http://www.gastro24.de/Kombidaempfer"],
["130","http://www.gastro24.de/Heissluftoefen"],
["131","http://www.gastro24.de/Zubehoer_6"],
["132","http://www.gastro24.de/Nudelkocher-Elektrisch"],
["133","http://www.gastro24.de/Nudelkocher-Gas"],
["134","http://www.gastro24.de/Nudelkocherkoerbe"],
["135","http://www.gastro24.de/Nudelmaschinen"],
["136","http://www.gastro24.de/Kleine-Dunstabzugshauben"],
["137","http://www.gastro24.de/Regler-Schaltkaesten"],
["138","http://www.gastro24.de/Aktivkohle"],
["139","http://www.gastro24.de/Fettfangfilter"],
["140","http://www.gastro24.de/Flammschutzfilter"],
["141","http://www.gastro24.de/Synthetikfilter"],
["142","http://www.gastro24.de/Abluftreinigungsanlagen"],
["143","http://www.gastro24.de/Airboxen"],
["144","http://www.gastro24.de/Radialventilatoren"],
["145","http://www.gastro24.de/Dexion-Serie-77"],
["146","http://www.gastro24.de/EMME-6"],
["147","http://www.gastro24.de/EMME-7"],
["148","http://www.gastro24.de/FUNCTION-650"],
["149","http://www.gastro24.de/FUNCTION-700"],
["150","http://www.gastro24.de/Motoren-fuer-Hauben-/-Lueftermotoren"],
["151","http://www.gastro24.de/Sonstige-Lueftungstechnik"],
["152","http://www.gastro24.de/Kochkessel-Elektrisch"],
["153","http://www.gastro24.de/Kochkessel-Gas"],
["154","http://www.gastro24.de/Wandhauben-Kastenform-ohne-Motor-mit-Licht-Bautiefe-110cm"],
["155","http://www.gastro24.de/Wandhauben-Kastenform-ohne-Motor-mit-Licht-Bautiefe-120cm"],
["156","http://www.gastro24.de/Wandhauben-Kastenform-ohne-Motor-mit-Licht-Bautiefe-140cm"],
["157","http://www.gastro24.de/Wandhauben-Kastenform-ohne-Motor-mit-Licht-Bautiefe-150cm"],
["158","http://www.gastro24.de/Wandhauben-Kastenform-ohne-Motor-mit-Licht-Bautiefe-180cm"],
["159","http://www.gastro24.de/Wandhauben-Kastenform-ohne-Motor-mit-Licht-Bautiefe-220cm"],
["160","http://www.gastro24.de/Wandhauben-Kastenform-ohne-Motor-mit-Licht-Bautiefe-70cm"],
["161","http://www.gastro24.de/Wandhauben-Kastenform-ohne-Motor-mit-Licht-Bautiefe-90cm"],
["162","http://www.gastro24.de/Zentralhauben-ohne-Motor-mit-Licht-Bautiefe-120cm"],
["163","http://www.gastro24.de/Zentralhauben-ohne-Motor-mit-Licht-Bautiefe-130cm"],
["164","http://www.gastro24.de/Zentralhauben-ohne-Motor-mit-Licht-Bautiefe-140cm"],
["165","http://www.gastro24.de/Zentralhauben-ohne-Motor-mit-Licht-Bautiefe-150cm"],
["166","http://www.gastro24.de/Zentralhauben-ohne-Motor-mit-Licht-Bautiefe-180cm"],
["167","http://www.gastro24.de/Zentralhauben-ohne-Motor-mit-Licht-Bautiefe-220cm"],
["168","http://www.gastro24.de/Wandhaube-ohne-Motor-mit-Licht-Bautiefe-110cm"],
["169","http://www.gastro24.de/Wandhaube-ohne-Motor-mit-Licht-Bautiefe-130cm"],
["170","http://www.gastro24.de/Wandhaube-ohne-Motor-mit-Licht-Bautiefe-70cm"],
["171","http://www.gastro24.de/Wandhaube-ohne-Motor-mit-Licht-Bautiefe-80cm"],
["172","http://www.gastro24.de/Wandhaube-ohne-Motor-mit-Licht-Bautiefe-90cm"],
["173","http://www.gastro24.de/Wandhaube-mit-Motor-ohne-Licht-Bautiefe-110cm"],
["174","http://www.gastro24.de/Wandhaube-mit-Motor-ohne-Licht-Bautiefe-90cm"],
["175","http://www.gastro24.de/Wandhaube-mit-Motor-mit-Licht-und-Regler-Bautiefe-110cm"],
["176","http://www.gastro24.de/Wandhaube-mit-Motor-mit-Licht-und-Regler-Bautiefe-70cm"],
["177","http://www.gastro24.de/Wandhaube-mit-Motor-mit-Licht-und-Regler-Bautiefe-90cm"],
["178","http://www.gastro24.de/Wandhaube-mit-Motor-und-Licht-Bautiefe-110cm"],
["179","http://www.gastro24.de/Wandhaube-mit-Motor-und-Licht-Bautiefe-70cm"],
["180","http://www.gastro24.de/Wandhaube-mit-Motor-und-Licht-Bautiefe-80cm"],
["181","http://www.gastro24.de/Wandhaube-mit-Motor-und-Licht-Bautiefe-90cm"],
["182","http://www.gastro24.de/Kippbratpfannen-Elektrisch"],
["183","http://www.gastro24.de/Kippbratpfannen-Gas"],
["184","http://www.gastro24.de/Gas-Grillplatte"],
["185","http://www.gastro24.de/Elektro-Grillplatte"],
["186","http://www.gastro24.de/Grillplatten-Zubehoer"],
["187","http://www.gastro24.de/Gemueseschneidemaschinen"],
["188","http://www.gastro24.de/Gemueseschneider-Zubehoer"],
["189","http://www.gastro24.de/Friteusen-Zubehoer"],
["190","http://www.gastro24.de/Gas-Fritteusen"],
["191","http://www.gastro24.de/Elektro-Fritteusen"],
["192","http://www.gastro24.de/Tischfritteusen"],
["193","http://www.gastro24.de/Aufschaeumkannen"],
["194","http://www.gastro24.de/Dekorationsschablonen-fuer-Milchschaum"],
["195","http://www.gastro24.de/Entkalkung"],
["196","http://www.gastro24.de/Filterpapier"],
["197","http://www.gastro24.de/Gluehweinkocher"],
["198","http://www.gastro24.de/Kaffeemaschinen"],
["199","http://www.gastro24.de/Kaffeemuehlen"],
["200","http://www.gastro24.de/Kaffeeportionierer"],
["201","http://www.gastro24.de/Kaffeesiebe"],
["202","http://www.gastro24.de/Cafetiere-French-Press"],
["203","http://www.gastro24.de/Satzschubladen"],
["204","http://www.gastro24.de/Tassenwaermer"],
["205","http://www.gastro24.de/Warmhalteplatten-fuer-Kaffeekannen"],
["206","http://www.gastro24.de/weitere-Cafeartikel"],
["207","http://www.gastro24.de/Isolierkannen"],
["208","http://www.gastro24.de/Pumpkannen"],
["209","http://www.gastro24.de/Systemkonforme-Kannen"],
["210","http://www.gastro24.de/Eisbecher"],
["211","http://www.gastro24.de/Eisbehaelter-fuer-Eisvitrine"],
["212","http://www.gastro24.de/Eisformen"],
["213","http://www.gastro24.de/Eisportionierer"],
["214","http://www.gastro24.de/Eistuetenhalter"]]

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
        titleurllist=response.xpath('//*[@id="outer_wrapper"]/div/div[2]/div[2]/div/div[7]/div[1]/ul/li["list_item list"]')
        #print "LENGTH of titles is : ",len(titlelist)
        for titleurls in titleurllist:
            
            titlesuburl=titleurls.xpath('div/div[1]/a/@href').extract()
            #print title
            if titlesuburl:
                titleurl="http://www.gastro24.de/"+titlesuburl[0]
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
        allpageslist=response.xpath('//*[@id="outer_wrapper"]/div/div[2]/div[2]/div/div[6]/div[1]/div/span[2]/ul/li')
 
        for page in allpageslist:
            nextpageurl=page.xpath('a/@href').extract()
            #print "NEXT PAGE URL : ",nextpageurl
            nextpageno=page.xpath('a/text()').extract()
            #print "NEXT PAGE No. : ",nextpageno
          
            if nextpageno in allpagesdict1.keys():
                pass
            else:
                if nextpageurl[0].replace(" ","")=="":
                    #print "SELECTED URL : "
                    allpagesdict1[nextpageno[0]]="selected"
                else:
                    allpagesdict1[nextpageno[0]]=nextpageurl[0]
                    try:
                        req = scrapy.Request(nextpageurl[0],callback=self.parse3,meta={'allpagesdict':allpagesdict1})
                        yield req
                        #time.sleep(.3)
                    except: raise
					
    def parse4(self,response):
        item=GastroItem()
        title=response.xpath('//*[@id="buy_form"]/div/div/div[1]/h1/text()').extract()
        item['title']=("".join(title)).replace("\t","").replace("\n","")
        articleno=response.xpath('//*[@class="gastro_content_box price_box headless"]/li[1]/span/text()').extract()
        #print articleno
        item['articleno']="".join(articleno)
        #cost=response.xpath('//*[@class="gastro_content_box price_box headless"]/li[2]/span[2]/text()').extract()
        cost=response.xpath('//*[@id="buy_form"]/div/div/div[2]/ul[1]/li[4]/span/text()').extract()
        if not cost: cost=response.xpath('//*[@id="buy_form"]/div/div/div[2]/ul[1]/li[5]/span/text()').extract()
        if not cost: cost=response.xpath('//*[@id="buy_form"]/div/div/div[3]/ul[1]/li[4]/span/text()').extract()
        if not cost: cost=response.xpath('//*[@id="buy_form"]/div/div/div[3]/ul[1]/li[4]/span/text()').extract()
        #print cost
        cost1=cost[0].split(":")[1]
        
        if "ab" in cost1:

            try:
                yield SplashRequest(
                    response.url,
                    self.parse_link,
                    endpoint='render.json',
                    args={
				        'har': 1,
                        'html': 1,
			            'wait': 2.0
                        }
                    )

            except : raise
        else: 
            item['price'] = cost1.encode('ascii','ignore').replace('.','').replace(',','.').replace(" ","").replace("\n","")
            brand=response.xpath('//*[@id="buy_form"]/div/div/div[1]/div[2]/ul/li[1]/a/@href').extract()
            item['brand']=brand[0]
            item['url']=response.url
            desc=response.xpath('//*[@id="description"]/div//text()').extract()
            item['description']=(",".join(desc)).replace("\n","").replace("\t","")
            breadcrumblist=response.xpath('//*[@id="content"]/div[1]/span/a//text()').extract()
            item['breadcrumb']=">".join(breadcrumblist)
            yield item
		
		
        variants=response.xpath('//*[@id="article_buyfield"]/fieldset/div/ul')
        if len(variants)==2:
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
                        yield FormRequest(ajaxurl, method='POST', formdata=frmdata, callback=self.parse5, meta={'bread':breadcrumb, 'url':response.url})
						
        elif len(variants)==1:
            breadcrumblist=response.xpath('//*[@id="content"]/div[1]/span/a//text()').extract()
            breadcrumb=">".join(breadcrumblist)
            ajaxurl="http://www.gastro24.de/toolsajax.server.php"
            xjxargsarray1="<xjxobj><e><k>inWarenkorb</k><v>S<![CDATA[In den Warenkorb]]></v></e><e><k>a</k><v>S"
            var1=response.xpath('//*[@id="AktuellerkArtikel"]/@value').extract()
            #print "Variable 1: ",var1
            xjxargsarray2="</v></e><e><k>wke</k><v>S1</v></e><e><k>show</k><v>S1</v></e><e><k>kKundengruppe</k><v>S1</v></e><e><k>kSprache</k><v>S1</v></e><e><k>JTLSHOP</k><v>Sqe27afp85au5jbn7kk2irmnc53</v></e><e><k>"
            var2=response.xpath('//*[@id="article_buyfield"]/fieldset/div/ul[1]/li[2]/label/input/@name').extract()
            #print "Variable 2: ",var2
            xjxargsarray3="</k><v>S"
            #value in for loop
            xjxargsarray6="</v></e><e><k>anzahl</k><v>S1</v></e><e><k>Wunschliste</k><v>S</v></e></xjxobj>"
            variantslist= response.xpath('//div[@class="variations section_box"]/ul/li/label/input')
            for variants in variantslist:
                variant=variants.xpath('@value').extract()
                if variant[0]!="0":
                    #print variant[0]
                    xjxargsfunc="tauscheVariationKombi"
                    xjxargs=xjxargsarray1+var1[0]+xjxargsarray2+var2[0]+xjxargsarray3+variant[0]+xjxargsarray6
                    xjxargs1="NO"
                    fourthargs=response.xpath('//*[@id="article_buyfield"]/fieldset/div/ul[1]/li[2]/label/input/@name').extract()
                    fourtharg=(fourthargs[0].split('_'))[1]
                    xjxargs2="S"+fourtharg
                    xjxargs3="S"+variant[0]
                    xjxargs9=[ xjxargs, xjxargs1, xjxargs2, xjxargs3]
                    frmdata={"xjxfun":xjxargsfunc, "xjxargs[]":xjxargs9}
                    yield FormRequest(ajaxurl, method='POST', formdata=frmdata, callback=self.parse5, meta={'bread':breadcrumb, 'url':response.url})
						
    def parse5(self,response):
        item=GastroItem()
        
        parser = html.HTMLParser()
        
        tree = html.parse(StringIO(response.body), parser)
        
        
        cost=tree.xpath('//*[@id="buy_form"]/div/div/div[2]/ul[1]/li[4]/span/text()')
		        
        if not cost: cost=tree.xpath('//*[@id="buy_form"]/div/div/div[2]/ul[1]/li[5]/span/text()')
        if not cost: cost=tree.xpath('//*[@id="buy_form"]/div/div/div[3]/ul[1]/li[4]/span/text()')
        if not cost: cost=tree.xpath('//*[@id="buy_form"]/div/div/div[3]/ul[1]/li[4]/span/text()')
        cost1=(("".join(cost)).encode('ascii','ignore')).split(":")[1]
        if "ab" in cost1:
            cost=tree.xpath('//*[@id="price1"]/text()')
            cost1=(("".join(cost)).encode('ascii','ignore')).replace(" ","")
            cost2="{0:.1f}".format( float(cost1.encode('ascii','ignore').replace('.','').replace(',','.').replace('*','')) * 1.19)
            item['price']=cost2
        else:
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
        item['description']= ",".join(desc).replace("\n","").replace("\t","")
        item['breadcrumb']=response.meta['bread']
        item['url']=response.meta['url']
        yield item
		
		
    def parse_link(self, response):
        item=GastroItem()
        title=response.xpath('//*[@id="buy_form"]/div/div/div[1]/h1/text()').extract()
        item['title']=("".join(title)).replace("\t","").replace("\n","")
        articleno=response.xpath('//*[@class="gastro_content_box price_box headless"]/li[1]/span/text()').extract()
        #print articleno
        item['articleno']="".join(articleno)
        #cost=response.xpath('//*[@class="gastro_content_box price_box headless"]/li[2]/span[2]/text()').extract()
        cost=response.xpath('//div[@class="differential_price section_box well"]/ul/li/div/span//text()').extract()[1]
        #print cost
        cost1=cost[0].split(":")[1]
        
        item['price'] = cost1.encode('ascii','ignore').replace('.','').replace(',','.').replace(" ","").replace("\n","")
        brand=response.xpath('//*[@id="buy_form"]/div/div/div[1]/div[2]/ul/li[1]/a/@href').extract()
        item['brand']=brand[0]
        item['url']=response.url
        desc=response.xpath('//*[@id="description"]/div//text()').extract()
        item['description']=(",".join(desc)).replace("\n","").replace("\t","")
        breadcrumblist=response.xpath('//*[@id="content"]/div[1]/span/a//text()').extract()
        item['breadcrumb']=">".join(breadcrumblist)
        yield item