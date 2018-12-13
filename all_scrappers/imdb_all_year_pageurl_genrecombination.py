


#Amazon seller list spider
import time
import scrapy
import json
    
	
	
class ImdbItem(scrapy.Item):
    url=scrapy.Field()
    year=scrapy.Field()
    titlecount=scrapy.Field()
    genre=scrapy.Field()

class ImdbSpider(scrapy.Spider):
    
    name = "imdb_all_year_pageurl_genrecombination"
    allowed_domain=[]
    start_urls = ['http://www.imdb.com/year/']
    #start_urls = ["http://www.flipkart.com/search?q=9780005996218"]
    #start_urls = ['https://www.amazon.com/musical-instruments-accessories-sound-recording/b/ref=nav_shopall_mi_ce?ie=UTF8&node=11091801']
    
    
    def parse(self, response):
        genrelist=['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western']
        #yearlist=["1874","1875","1876","1877","1878","1879","1880","1881","1882","1883","1884","1885","1886","1887","1888","1889","1890","1891","1892","1893","1894","1895","1896","1897","1898","1899","1900","1901","1902","1903","1904","1905","1906","1907","1908","1909","1910","1911","1912","1913","1914","1915","1916","1917","1918","1919","1920","1921","1922","1923","1924","1925","1926","1927","1928","1929","1930","1931","1932","1933","1934","1935","1936","1937","1938","1939","1940","1941","1942","1943","1944","1945","1946","1947","1948","1949","1950","1951","1952","1953","1954","1955","1956","1957","1958","1959","1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016"]
        yearlist=["1956","1957","1958","1959","1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016"]
        new_list=[]
        for i in genrelist:
            for j in genrelist:
                if i==j:
                    pass
                elif i+','+j not in new_list:
                    if j+','+i not in new_list:
                        new_list.append(i+","+j)
        for genres in new_list:
            try:
                for years in yearlist:
                    urlpart1="http://www.imdb.com/search/title?release_date="
                    urlpart2="&ref_=rlm_yr&genres="
                    #print urlpart1+genres.lower()
                    req = scrapy.Request( urlpart1+years+urlpart2+genres.lower() , callback=self.parse1, meta={'year':years, 'genre':genres})
                    #req.meta['item_id']=url
                    #req.cookies = { 'lc-main':'en_US', 'x-wl-uid':'1yE71wxptnrPGpU96MVpeAljDAxEwlHAMNmRkGH3kTDbQNlw65AKYm8JBd2Nm33DfONRPH48N1DRE/phePYv7b8VzqI5P36U503gVSzRJSBmwDQKne/e/xfe/X3r9TLt9Mq2dGxVnAVsmo8PkOTlUOw==', 'skin':'noskin', 'x-main':'X2Uw?4D0ZsoVUNTB1ND?IqOhj4jrdt3SQM?nwPoWs2Vra8r9I13YbE1V8fqOmIli', 'at-main':'Atza|IwEBIM6arSMDjanfYsyURnaqmNeb87cZy6ift3_Ewd6ai-VCWQxN1VU8u-feDM43rwF2oZopky98QowPRIgSVmpR_qWGQgSAAMl_YsBf2E0nGom_GkU0Vl5JNLdIaGZ9g-Je-Uld-_qAa3onwe2Q_rUKPCN6j5PAu_78gARA9l5GI48so08VSR_tDyWO8p_WHTqj2dJMXqKZ-6YuhyOYGPbSFgupS_O-PofP6d9lqKlLtruDVDv98__UgkmhRmUXWTt3X3G_2ALthXr4_8tBnT4VpdNEWYqZKsJF0xej6dixrNlFNWoKyK-jojctn-E95wf1GmItDzSmmwM-fzp8LRptCncE_vJEfXTPknNoUcz2qoYx2kBsuYOviBUZSAONWCXII68hZD4SILOFPKAMmAXRBswx', 'sess-at-main':'hTCj4tFy0geBzyuGIGBYRUfOmwxbmm3iJjvmeMi/emE=', 'JSESSIONID':'C70160F1BC7EC0B9D5E1BD946AA543DF', 'csm-hit':'J1CK3EMBJCQHNYC6PB4P+s-CB6DMAQSAGGJC2C8H354|1503728162175', 'session-token':'n2Bkr05TMvQYIlxStLEPDDdd8KmwvXszRPl41nyUA+1+hlViB/+whjJG3jQjbUov8lRYLkN78KFEgYKt3ZQZjLd8PKw5Sp8DO2anI7lIo5iA5ZlBkkhTAAEz6qxH9pejQawVHIgLmQ0WLVWeZup/JQGwjoNITTENdcZ9A+C55Nfj0eEwqpNI661A1pvmaG9Y2hCGn0xf/zWQnGeus1aGeF6u3GdgzUTVEoqoashearQ8cngRhV/i0uxZoqRJly4ivJIy43Khphvj7Z++9vFB3w==', 'ubid-main':'131-1502033-8002851', 'session-id-time':'2082787201l', 'session-id':'130-6537552-1339612'}
                    #req.cookies = {'__csrf_token-1':'xKVo4VZJqkyblSjFlWzEehgUFyHAQg', 'nocache':'detail-1', 'x-ua-device':'tablet', '_ga':'GA1.2.2072088434.1505733636', '_gid':'GA1.2.1081983427.1506316742', 'session-1':'8e46a0f8054191632d15e31849c5862d483ca54447ec216fce4403cd7e3c21de' }
                    yield req
            
            except: raise
		
        for genres in genrelist:
            try:
                for years in yearlist:
                    urlpart1="http://www.imdb.com/search/title?release_date="
                    urlpart2="&ref_=rlm_yr&genres="
                    #print urlpart1+genres.lower()
                    req = scrapy.Request( urlpart1+years+urlpart2+genres.lower() , callback=self.parse1, meta={'year':years, 'genre':genres})
                    #req.meta['item_id']=url
                    #req.cookies = { 'lc-main':'en_US', 'x-wl-uid':'1yE71wxptnrPGpU96MVpeAljDAxEwlHAMNmRkGH3kTDbQNlw65AKYm8JBd2Nm33DfONRPH48N1DRE/phePYv7b8VzqI5P36U503gVSzRJSBmwDQKne/e/xfe/X3r9TLt9Mq2dGxVnAVsmo8PkOTlUOw==', 'skin':'noskin', 'x-main':'X2Uw?4D0ZsoVUNTB1ND?IqOhj4jrdt3SQM?nwPoWs2Vra8r9I13YbE1V8fqOmIli', 'at-main':'Atza|IwEBIM6arSMDjanfYsyURnaqmNeb87cZy6ift3_Ewd6ai-VCWQxN1VU8u-feDM43rwF2oZopky98QowPRIgSVmpR_qWGQgSAAMl_YsBf2E0nGom_GkU0Vl5JNLdIaGZ9g-Je-Uld-_qAa3onwe2Q_rUKPCN6j5PAu_78gARA9l5GI48so08VSR_tDyWO8p_WHTqj2dJMXqKZ-6YuhyOYGPbSFgupS_O-PofP6d9lqKlLtruDVDv98__UgkmhRmUXWTt3X3G_2ALthXr4_8tBnT4VpdNEWYqZKsJF0xej6dixrNlFNWoKyK-jojctn-E95wf1GmItDzSmmwM-fzp8LRptCncE_vJEfXTPknNoUcz2qoYx2kBsuYOviBUZSAONWCXII68hZD4SILOFPKAMmAXRBswx', 'sess-at-main':'hTCj4tFy0geBzyuGIGBYRUfOmwxbmm3iJjvmeMi/emE=', 'JSESSIONID':'C70160F1BC7EC0B9D5E1BD946AA543DF', 'csm-hit':'J1CK3EMBJCQHNYC6PB4P+s-CB6DMAQSAGGJC2C8H354|1503728162175', 'session-token':'n2Bkr05TMvQYIlxStLEPDDdd8KmwvXszRPl41nyUA+1+hlViB/+whjJG3jQjbUov8lRYLkN78KFEgYKt3ZQZjLd8PKw5Sp8DO2anI7lIo5iA5ZlBkkhTAAEz6qxH9pejQawVHIgLmQ0WLVWeZup/JQGwjoNITTENdcZ9A+C55Nfj0eEwqpNI661A1pvmaG9Y2hCGn0xf/zWQnGeus1aGeF6u3GdgzUTVEoqoashearQ8cngRhV/i0uxZoqRJly4ivJIy43Khphvj7Z++9vFB3w==', 'ubid-main':'131-1502033-8002851', 'session-id-time':'2082787201l', 'session-id':'130-6537552-1339612'}
                    #req.cookies = {'__csrf_token-1':'xKVo4VZJqkyblSjFlWzEehgUFyHAQg', 'nocache':'detail-1', 'x-ua-device':'tablet', '_ga':'GA1.2.2072088434.1505733636', '_gid':'GA1.2.1081983427.1506316742', 'session-1':'8e46a0f8054191632d15e31849c5862d483ca54447ec216fce4403cd7e3c21de' }
                    yield req
            
            except: raise
			
    def parse1(self, response):
        year=response.meta['year']
        if response.xpath('//*[@id="main"]/div/div/div[@class="nav"]'):
            try:
                if response.xpath('//*[@id="main"]/div/div/div[1]/div[2]/text()').extract()[2]:
                    titlecount=response.xpath('//*[@id="main"]/div/div/div[1]/div[2]/text()').extract()[2]
            except:
                titlecount=response.xpath('//*[@id="main"]/div/div/div[1]/div[2]/text()').extract()[0]
            #print titlecount
            item=ImdbItem()
            item['url']=response.url
            item['year']=year
            item['genre']=response.meta['genre']
            if titlecount:
                item['titlecount']=titlecount.replace(' ','').replace('of','').replace('titles','').replace('\n','').replace(',','').replace('title','')
            else :
                item['titlecount']="NA"
            yield item
        else:
            item=ImdbItem()
            item['url']=response.url
            item['year']=year
            item['genre']=response.meta['genre']
            item['titlecount']="NA"
            yield item