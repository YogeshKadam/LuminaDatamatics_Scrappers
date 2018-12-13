



#Amazon seller list spider
import time
import scrapy
import json
    
	
	
class ImdbItem(scrapy.Item):
    year=scrapy.Field()
    pageurl=scrapy.Field()
    mainurl=scrapy.Field()


class ImdbSpider(scrapy.Spider):
    
    name = "imdb_pageurls_all_years"
    allowed_domain=[]
    start_urls = ['http://www.imdb.com/year/']
    #start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ['https://www.amazon.com/musical-instruments-accessories-sound-recording/b/ref=nav_shopall_mi_ce?ie=UTF8&node=11091801']
    
 	

    def parse(self, response):
        urls_done=[]
        urls=[
["1874","1","http://www.imdb.com/search/title?release_date=1874&ref_=rlm_yr"],
["1875","0","http://www.imdb.com/search/title?release_date=1875&ref_=rlm_yr"],
["1876","0","http://www.imdb.com/search/title?release_date=1876&ref_=rlm_yr"],
["1877","0","http://www.imdb.com/search/title?release_date=1877&ref_=rlm_yr"],
["1878","1","http://www.imdb.com/search/title?release_date=1878&ref_=rlm_yr"],
["1879","0","http://www.imdb.com/search/title?release_date=1879&ref_=rlm_yr"],
["1880","0","http://www.imdb.com/search/title?release_date=1880&ref_=rlm_yr"],
["1881","0","http://www.imdb.com/search/title?release_date=1881&ref_=rlm_yr"],
["1882","0","http://www.imdb.com/search/title?release_date=1882&ref_=rlm_yr"],
["1883","1","http://www.imdb.com/search/title?release_date=1883&ref_=rlm_yr"],
["1884","0","http://www.imdb.com/search/title?release_date=1884&ref_=rlm_yr"],
["1885","0","http://www.imdb.com/search/title?release_date=1885&ref_=rlm_yr"],
["1886","0","http://www.imdb.com/search/title?release_date=1886&ref_=rlm_yr"],
["1887","3","http://www.imdb.com/search/title?release_date=1887&ref_=rlm_yr"],
["1888","5","http://www.imdb.com/search/title?release_date=1888&ref_=rlm_yr"],
["1889","2","http://www.imdb.com/search/title?release_date=1889&ref_=rlm_yr"],
["1890","6","http://www.imdb.com/search/title?release_date=1890&ref_=rlm_yr"],
["1891","10","http://www.imdb.com/search/title?release_date=1891&ref_=rlm_yr"],
["1892","9","http://www.imdb.com/search/title?release_date=1892&ref_=rlm_yr"],
["1893","2","http://www.imdb.com/search/title?release_date=1893&ref_=rlm_yr"],
["1894","95","http://www.imdb.com/search/title?release_date=1894&ref_=rlm_yr"],
["1895","115","http://www.imdb.com/search/title?release_date=1895&ref_=rlm_yr"],
["1896","832","http://www.imdb.com/search/title?release_date=1896&ref_=rlm_yr"],
["1897","1344","http://www.imdb.com/search/title?release_date=1897&ref_=rlm_yr"],
["1898","1769","http://www.imdb.com/search/title?release_date=1898&ref_=rlm_yr"],
["1899","1804","http://www.imdb.com/search/title?release_date=1899&ref_=rlm_yr"],
["1900","1839","http://www.imdb.com/search/title?release_date=1900&ref_=rlm_yr"],
["1901","1759","http://www.imdb.com/search/title?release_date=1901&ref_=rlm_yr"],
["1902","1815","http://www.imdb.com/search/title?release_date=1902&ref_=rlm_yr"],
["1903","2673","http://www.imdb.com/search/title?release_date=1903&ref_=rlm_yr"],
["1904","1824","http://www.imdb.com/search/title?release_date=1904&ref_=rlm_yr"],
["1905","1705","http://www.imdb.com/search/title?release_date=1905&ref_=rlm_yr"],
["1906","1863","http://www.imdb.com/search/title?release_date=1906&ref_=rlm_yr"],
["1907","2477","http://www.imdb.com/search/title?release_date=1907&ref_=rlm_yr"],
["1908","4270","http://www.imdb.com/search/title?release_date=1908&ref_=rlm_yr"],
["1909","5418","http://www.imdb.com/search/title?release_date=1909&ref_=rlm_yr"],
["1910","6408","http://www.imdb.com/search/title?release_date=1910&ref_=rlm_yr"],
["1911","6438","http://www.imdb.com/search/title?release_date=1911&ref_=rlm_yr"],
["1912","8463","http://www.imdb.com/search/title?release_date=1912&ref_=rlm_yr"],
["1913","9570","http://www.imdb.com/search/title?release_date=1913&ref_=rlm_yr"],
["1914","9002","http://www.imdb.com/search/title?release_date=1914&ref_=rlm_yr"],
["1915","8430","http://www.imdb.com/search/title?release_date=1915&ref_=rlm_yr"],
["1916","6973","http://www.imdb.com/search/title?release_date=1916&ref_=rlm_yr"],
["1917","5508","http://www.imdb.com/search/title?release_date=1917&ref_=rlm_yr"],
["1918","4615","http://www.imdb.com/search/title?release_date=1918&ref_=rlm_yr"],
["1919","3985","http://www.imdb.com/search/title?release_date=1919&ref_=rlm_yr"],
["1920","4426","http://www.imdb.com/search/title?release_date=1920&ref_=rlm_yr"],
["1921","4181","http://www.imdb.com/search/title?release_date=1921&ref_=rlm_yr"],
["1922","3567","http://www.imdb.com/search/title?release_date=1922&ref_=rlm_yr"],
["1923","2999","http://www.imdb.com/search/title?release_date=1923&ref_=rlm_yr"],
["1924","3055","http://www.imdb.com/search/title?release_date=1924&ref_=rlm_yr"],
["1925","3282","http://www.imdb.com/search/title?release_date=1925&ref_=rlm_yr"],
["1926","3016","http://www.imdb.com/search/title?release_date=1926&ref_=rlm_yr"],
["1927","3105","http://www.imdb.com/search/title?release_date=1927&ref_=rlm_yr"],
["1928","3066","http://www.imdb.com/search/title?release_date=1928&ref_=rlm_yr"],
["1929","3146","http://www.imdb.com/search/title?release_date=1929&ref_=rlm_yr"],
["1930","2772","http://www.imdb.com/search/title?release_date=1930&ref_=rlm_yr"],
["1931","2780","http://www.imdb.com/search/title?release_date=1931&ref_=rlm_yr"],
["1932","2784","http://www.imdb.com/search/title?release_date=1932&ref_=rlm_yr"],
["1933","2638","http://www.imdb.com/search/title?release_date=1933&ref_=rlm_yr"],
["1934","2698","http://www.imdb.com/search/title?release_date=1934&ref_=rlm_yr"],
["1935","2649","http://www.imdb.com/search/title?release_date=1935&ref_=rlm_yr"],
["1936","3084","http://www.imdb.com/search/title?release_date=1936&ref_=rlm_yr"],
["1937","3346","http://www.imdb.com/search/title?release_date=1937&ref_=rlm_yr"],
["1938","3189","http://www.imdb.com/search/title?release_date=1938&ref_=rlm_yr"],
["1939","2833","http://www.imdb.com/search/title?release_date=1939&ref_=rlm_yr"],
["1940","2399","http://www.imdb.com/search/title?release_date=1940&ref_=rlm_yr"],
["1941","2380","http://www.imdb.com/search/title?release_date=1941&ref_=rlm_yr"],
["1942","2280","http://www.imdb.com/search/title?release_date=1942&ref_=rlm_yr"],
["1943","2067","http://www.imdb.com/search/title?release_date=1943&ref_=rlm_yr"],
["1944","1899","http://www.imdb.com/search/title?release_date=1944&ref_=rlm_yr"],
["1945","1859","http://www.imdb.com/search/title?release_date=1945&ref_=rlm_yr"],
["1946","2258","http://www.imdb.com/search/title?release_date=1946&ref_=rlm_yr"],
["1947","2720","http://www.imdb.com/search/title?release_date=1947&ref_=rlm_yr"],
["1948","3296","http://www.imdb.com/search/title?release_date=1948&ref_=rlm_yr"],
["1949","4321","http://www.imdb.com/search/title?release_date=1949&ref_=rlm_yr"],
["1950","5386","http://www.imdb.com/search/title?release_date=1950&ref_=rlm_yr"],
["1951","6355","http://www.imdb.com/search/title?release_date=1951&ref_=rlm_yr"],
["1952","7127","http://www.imdb.com/search/title?release_date=1952&ref_=rlm_yr"],
["1953","7839","http://www.imdb.com/search/title?release_date=1953&ref_=rlm_yr"],
["1954","8336","http://www.imdb.com/search/title?release_date=1954&ref_=rlm_yr"],
["1955","9556","http://www.imdb.com/search/title?release_date=1955&ref_=rlm_yr"],
["1956","10750","http://www.imdb.com/search/title?release_date=1956&ref_=rlm_yr"],
["1957","12145","http://www.imdb.com/search/title?release_date=1957&ref_=rlm_yr"],
["1958","12584","http://www.imdb.com/search/title?release_date=1958&ref_=rlm_yr"],
["1959","13294","http://www.imdb.com/search/title?release_date=1959&ref_=rlm_yr"],
["1960","14608","http://www.imdb.com/search/title?release_date=1960&ref_=rlm_yr"],
["1961","14725","http://www.imdb.com/search/title?release_date=1961&ref_=rlm_yr"],
["1962","13810","http://www.imdb.com/search/title?release_date=1962&ref_=rlm_yr"],
["1963","15172","http://www.imdb.com/search/title?release_date=1963&ref_=rlm_yr"],
["1964","16634","http://www.imdb.com/search/title?release_date=1964&ref_=rlm_yr"],
["1965","18509","http://www.imdb.com/search/title?release_date=1965&ref_=rlm_yr"],
["1966","19258","http://www.imdb.com/search/title?release_date=1966&ref_=rlm_yr"],
["1967","20102","http://www.imdb.com/search/title?release_date=1967&ref_=rlm_yr"],
["1968","18340","http://www.imdb.com/search/title?release_date=1968&ref_=rlm_yr"],
["1969","19443","http://www.imdb.com/search/title?release_date=1969&ref_=rlm_yr"],
["1970","19313","http://www.imdb.com/search/title?release_date=1970&ref_=rlm_yr"],
["1971","19554","http://www.imdb.com/search/title?release_date=1971&ref_=rlm_yr"],
["1972","18944","http://www.imdb.com/search/title?release_date=1972&ref_=rlm_yr"],
["1973","19987","http://www.imdb.com/search/title?release_date=1973&ref_=rlm_yr"],
["1974","19662","http://www.imdb.com/search/title?release_date=1974&ref_=rlm_yr"],
["1975","19977","http://www.imdb.com/search/title?release_date=1975&ref_=rlm_yr"],
["1976","19110","http://www.imdb.com/search/title?release_date=1976&ref_=rlm_yr"],
["1977","19308","http://www.imdb.com/search/title?release_date=1977&ref_=rlm_yr"],
["1978","19797","http://www.imdb.com/search/title?release_date=1978&ref_=rlm_yr"],
["1979","20644","http://www.imdb.com/search/title?release_date=1979&ref_=rlm_yr"],
["1980","21585","http://www.imdb.com/search/title?release_date=1980&ref_=rlm_yr"],
["1981","20188","http://www.imdb.com/search/title?release_date=1981&ref_=rlm_yr"],
["1982","20769","http://www.imdb.com/search/title?release_date=1982&ref_=rlm_yr"],
["1983","21621","http://www.imdb.com/search/title?release_date=1983&ref_=rlm_yr"],
["1984","23285","http://www.imdb.com/search/title?release_date=1984&ref_=rlm_yr"],
["1985","24267","http://www.imdb.com/search/title?release_date=1985&ref_=rlm_yr"],
["1986","24529","http://www.imdb.com/search/title?release_date=1986&ref_=rlm_yr"],
["1987","26744","http://www.imdb.com/search/title?release_date=1987&ref_=rlm_yr"],
["1988","25752","http://www.imdb.com/search/title?release_date=1988&ref_=rlm_yr"],
["1989","27767","http://www.imdb.com/search/title?release_date=1989&ref_=rlm_yr"],
["1990","29516","http://www.imdb.com/search/title?release_date=1990&ref_=rlm_yr"],
["1991","31097","http://www.imdb.com/search/title?release_date=1991&ref_=rlm_yr"],
["1992","32140","http://www.imdb.com/search/title?release_date=1992&ref_=rlm_yr"],
["1993","34946","http://www.imdb.com/search/title?release_date=1993&ref_=rlm_yr"],
["1994","39391","http://www.imdb.com/search/title?release_date=1994&ref_=rlm_yr"],
["1995","45976","http://www.imdb.com/search/title?release_date=1995&ref_=rlm_yr"],
["1996","46874","http://www.imdb.com/search/title?release_date=1996&ref_=rlm_yr"],
["1997","51664","http://www.imdb.com/search/title?release_date=1997&ref_=rlm_yr"],
["1998","57705","http://www.imdb.com/search/title?release_date=1998&ref_=rlm_yr"],
["1999","62054","http://www.imdb.com/search/title?release_date=1999&ref_=rlm_yr"],
["2000","66017","http://www.imdb.com/search/title?release_date=2000&ref_=rlm_yr"],
["2001","72806","http://www.imdb.com/search/title?release_date=2001&ref_=rlm_yr"],
["2002","75693","http://www.imdb.com/search/title?release_date=2002&ref_=rlm_yr"],
["2003","84457","http://www.imdb.com/search/title?release_date=2003&ref_=rlm_yr"],
["2004","98834","http://www.imdb.com/search/title?release_date=2004&ref_=rlm_yr"],
["2005","111725","http://www.imdb.com/search/title?release_date=2005&ref_=rlm_yr"],
["2006","124829","http://www.imdb.com/search/title?release_date=2006&ref_=rlm_yr"],
["2007","138817","http://www.imdb.com/search/title?release_date=2007&ref_=rlm_yr"],
["2008","147155","http://www.imdb.com/search/title?release_date=2008&ref_=rlm_yr"],
["2009","156523","http://www.imdb.com/search/title?release_date=2009&ref_=rlm_yr"],
["2010","174981","http://www.imdb.com/search/title?release_date=2010&ref_=rlm_yr"],
["2011","204024","http://www.imdb.com/search/title?release_date=2011&ref_=rlm_yr"],
["2012","226067","http://www.imdb.com/search/title?release_date=2012&ref_=rlm_yr"],
["2013","238871","http://www.imdb.com/search/title?release_date=2013&ref_=rlm_yr"],
["2014","244647","http://www.imdb.com/search/title?release_date=2014&ref_=rlm_yr"],
["2015","249098","http://www.imdb.com/search/title?release_date=2015&ref_=rlm_yr"],
["2016","253981","http://www.imdb.com/search/title?release_date=2016&ref_=rlm_yr"],
]

        for url in urls:
            try:
                req = scrapy.Request( url[2] , callback=self.parse1, meta={'year':url[0], 'totalpages':url[1]})
                #req.meta['item_id']=url
                #req.cookies = { 'lc-main':'en_US', 'x-wl-uid':'1yE71wxptnrPGpU96MVpeAljDAxEwlHAMNmRkGH3kTDbQNlw65AKYm8JBd2Nm33DfONRPH48N1DRE/phePYv7b8VzqI5P36U503gVSzRJSBmwDQKne/e/xfe/X3r9TLt9Mq2dGxVnAVsmo8PkOTlUOw==', 'skin':'noskin', 'x-main':'X2Uw?4D0ZsoVUNTB1ND?IqOhj4jrdt3SQM?nwPoWs2Vra8r9I13YbE1V8fqOmIli', 'at-main':'Atza|IwEBIM6arSMDjanfYsyURnaqmNeb87cZy6ift3_Ewd6ai-VCWQxN1VU8u-feDM43rwF2oZopky98QowPRIgSVmpR_qWGQgSAAMl_YsBf2E0nGom_GkU0Vl5JNLdIaGZ9g-Je-Uld-_qAa3onwe2Q_rUKPCN6j5PAu_78gARA9l5GI48so08VSR_tDyWO8p_WHTqj2dJMXqKZ-6YuhyOYGPbSFgupS_O-PofP6d9lqKlLtruDVDv98__UgkmhRmUXWTt3X3G_2ALthXr4_8tBnT4VpdNEWYqZKsJF0xej6dixrNlFNWoKyK-jojctn-E95wf1GmItDzSmmwM-fzp8LRptCncE_vJEfXTPknNoUcz2qoYx2kBsuYOviBUZSAONWCXII68hZD4SILOFPKAMmAXRBswx', 'sess-at-main':'hTCj4tFy0geBzyuGIGBYRUfOmwxbmm3iJjvmeMi/emE=', 'JSESSIONID':'C70160F1BC7EC0B9D5E1BD946AA543DF', 'csm-hit':'J1CK3EMBJCQHNYC6PB4P+s-CB6DMAQSAGGJC2C8H354|1503728162175', 'session-token':'n2Bkr05TMvQYIlxStLEPDDdd8KmwvXszRPl41nyUA+1+hlViB/+whjJG3jQjbUov8lRYLkN78KFEgYKt3ZQZjLd8PKw5Sp8DO2anI7lIo5iA5ZlBkkhTAAEz6qxH9pejQawVHIgLmQ0WLVWeZup/JQGwjoNITTENdcZ9A+C55Nfj0eEwqpNI661A1pvmaG9Y2hCGn0xf/zWQnGeus1aGeF6u3GdgzUTVEoqoashearQ8cngRhV/i0uxZoqRJly4ivJIy43Khphvj7Z++9vFB3w==', 'ubid-main':'131-1502033-8002851', 'session-id-time':'2082787201l', 'session-id':'130-6537552-1339612'}
                #req.cookies = {'__csrf_token-1':'xKVo4VZJqkyblSjFlWzEehgUFyHAQg', 'nocache':'detail-1', 'x-ua-device':'tablet', '_ga':'GA1.2.2072088434.1505733636', '_gid':'GA1.2.1081983427.1506316742', 'session-1':'8e46a0f8054191632d15e31849c5862d483ca54447ec216fce4403cd7e3c21de' }
                if url not in urls_done:
                    yield req
            
            except: raise
    def parse1(self, response):
        """     year=response.meta['year']
        totalpages=response.meta['totalpages']
        if totalpages=="0" or int(totalpages)<=50:
            item=ImdbItem()
            item['year']=year
            item['pageurl']=response.url
            item['mainurl']=response.url
            yield item
        elif int(totalpages)>=50:
            item=ImdbItem()
            item['year']=year
            item['pageurl']=response.url
            item['mainurl']=response.url
            yield item
            urlpart1="http://www.imdb.com/search/title?release_date="
            urlpart2="&page="
            urlpart3="&ref_=adv_nxt"
            noofpages=int(totalpages)/50
            for i in range(2,noofpages+2):
                pageurl=urlpart1+year+urlpart2+str(i)+urlpart3
                item=ImdbItem()
                item['year']=year
                item['pageurl']=pageurl
                item['mainurl']=response.url
                yield item"""
        year=response.meta['year']
        totaltitles=response.meta['totalpages']
        #genre=response.meta['genre']
        if totaltitles=="NA":
            yield
        elif totaltitles=="0" or int(totaltitles)<=50:
            item=ImdbItem()
            item['year']=year
            item['pageurl']=response.url
            item['mainurl']=response.url
            yield item
            #http://www.imdb.com/search/title?release_date=2017&ref_=rlm_yr&genres=sport
            #http://www.imdb.com/search/title?release_date=2017&genres=action,romance&page=2&ref_=adv_nxt
            #http://www.imdb.com/search/title?release_date=2017&ref_=rlm_yr&genres=action,romance
        elif int(totaltitles)>=50 and int(totaltitles)<=10000:
            item=ImdbItem()
            item['year']=year
            item['pageurl']=response.url
            item['mainurl']=response.url
            yield item
            urlpart1="http://www.imdb.com/search/title?release_date="
            urlpart2="&page="
            urlpart3="&ref_=adv_nxt"
            noofpages=int(totaltitles)/50
            for i in range(2,noofpages+2):
                pageurl=urlpart1+year+urlpart2+str(i)+urlpart3
                item=ImdbItem()
                item['year']=year
                item['pageurl']=pageurl
                item['mainurl']=response.url
                yield item
        elif int(totaltitles)>10000:
            item=ImdbItem()
            item['year']=year
            item['pageurl']=response.url
            item['mainurl']=response.url
            yield item
            urlpart1="http://www.imdb.com/search/title?release_date="
            urlpart2="&page="
            urlpart3="&ref_=adv_nxt"
            noofpages=201
            for i in range(2,noofpages):
                pageurl=urlpart1+year+urlpart2+str(i)+urlpart3
                item=ImdbItem()
                item['year']=year
                item['pageurl']=pageurl
                item['mainurl']=response.url
                yield item