# -*- coding: utf-8 -*-
import scrapy
import urllib

import os
import time
import re
import json
import re
import datetime
import demjson

class StapleItems(scrapy.Item):
    price = scrapy.Field()
    title= scrapy.Field()
    model_no= scrapy.Field()
    breadcrumb= scrapy.Field()
    item_no= scrapy.Field()
    id= scrapy.Field()
    response_url= scrapy.Field()


class stapleSpider(scrapy.Spider):
    imgcount = 1
    name = "staple_productinfo_18-04-2018"
    allowed_domains = []

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]

    def parse(self, response):
        urls_done=[]
        urls=[
["2","https://www.staples.com/blueline-executive-business-journal-notebook-professional-black-lizard-look-hardbound-cover-150-pgs-75-shts-9-1-4-x-7-1-4/product_384621"],
["3","https://www.staples.com/blueline-executive-business-journal-black-lizard-look-hardbound-cover-150-pages-75-sheets-11-x-8-1-2/product_464190"],
["4","https://www.staples.com/hp-office-quickpack-8-1-2-x-11-half-case/product_391460"],
["5","https://www.staples.com/hp-multipurpose-paper-8-1-2-x-11-case/product_814178"],
["6","https://www.staples.com/c-line-plastic-sorters-general-23-1-2-x-3/product_508950"],
["7","https://www.staples.com/c-line-plastic-sorters-letter-size-all-purpose/product_897696"],
["8","https://www.staples.com/southworth-25-cotton-business-paper-8-5-x-11-32-lb-linen-finish-ivory-250-sheets-pack-j568c/product_619282"],
["9","https://www.staples.com/southworth-25-cotton-business-paper-8-5-x-11-32-lb-linen-finish-white-250-sheets-pack-j558c/product_619352"],
["10","https://www.staples.com/southworth-linen-business-cover-stock-8-1-2-x-11-65-lb-linen-finish-ivory-100-box/product_666125"],
]
        for url in urls:
            #requesturl = scrapy.FormRequest("https://www.amazon.com/dp/"+url+"/",callback=self.parse1,headers={'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}, dont_filter=True)
            #req = scrapy.Request(url[2], headers={'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'} ,callback=self.parse1, meta={"category":url[1], "department":url[3], "position":url[4], "product_id":url[0], "zipcode":url[5]}, dont_filter=True)
            #requesturl.cookies = {'aws-target-static-id':'1452239187641-159842', 'aws-business-metrics-last-visit':'1460349972900', '__utmv':'194891197.%22QDSe8l%404pyTIl%3FpKm5C24aEFXeBtLGw3BhDIGikRUeXlFGLshyp4Dtw4gLRG%3F9cU%22', 'aws-userInfo':'%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A111320495319%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22rahul%2520bhaskar%22%2C%22keybase%22%3A%22%22%2C%22issuer%22%3A%22https%3A%2F%2Fwww.amazon.com%2Fap%2Fsignin%22%7D', 's_pers':'%20s_vnum%3D1880352564702%2526vn%253D3%7C1880352564702%3B%20s_invisit%3Dtrue%7C1470309348410%3B%20s_nr%3D1470307548416-Repeat%7C1478083548416%3B', '__utma':'194891197.372951375.1452236845.1470290622.1470307550.17', 'aws-ubid-main':'182-7331780-4611541', '_mkto_trk':'id:112-TZM-766&token:_mch-aws.amazon.com-1484112318467-15791', 'aws-target-visitor-id':'1452239187643-451048.20_19', 'aws-target-data':'%7B%22support%22%3A%221%22%7D', 's_fid':'70673D38D5DFE123-1B689FC000FE2EFF', 'regStatus':'registered', 'ubid-main':'156-9680828-0484351', 'ca':'ALAAAAAAEAAAAAQGAAEIAUQ=', 's_vnum':'1926421318258%26vn%3D2', 's_nr':'1514281824850-New', 's_dslv':'1514281824851', 'session-id':'144-3935774-8062208', 'session-id-time':'2082787201l', 'x-amz-captcha-1':'1518768468239967', 'x-amz-captcha-2':'8brJzDGjVr0g6SMt7y51KQ==', 'a-ogbcbff':'1', 'x-main':'"fycgicqnXAG9h3NMiDoGTALK8XmKMT8Y7zmG2J0BNpcL1f@?TcYxcPMWWipZhvof"', 'at-main':'Atza|IwEBIJvW6xlsbiH1hRs9vJ2V_w16jlQhSQjg3ehsg3W76LxrQT-VH9tsIRiHoHcaMXn9pyYCgqS8ncyALBot9Lfa-oHQ9B5haHTZ234l1wd5cjS3lIpoebl3XqE8R13u2oHsAscFbcYZ1OArAxJHSYSkJxFwIlml-M4T3b8VcujEZdeoQEzvAipwwJHDzh7P4QQmNxSFyR7173IySmfados6vrpYc0OdSwLDpR42eLBACHhfFxTrY2EdG0O7vgr2UoDUnvd4o5SOTq54TBh4f2fNkV5OObxldSU1DMPF7E4PJnqBYC0n_gjy2Re3AId4a80qUdi0mQGItumFTtvkVmM_Ha5AXBWKaUL2SLS9RWjbeDoBRIQdaftjGACfgp_USVFfOBWwq_-7HQbM7J_EasxZZjfzA9JdgMGy37DAIGWG9abF-A2XLSehJ3qw9yD6Ce0it8E', 'sess-at-main':'"pXRzY7+0cEA6QAXiw7xtqkVPnlTizA/bSV5Ufn8LWUQ="', 'sst-main':'Sst1|PQFckmUHN5sOVumX4CdB104DCaCzuvSHXylkeh4qpfwQHzhV2em2zJkPumi2szBhhz9iPmGUE6CWI7DPT2W-mOFK_1ffiVN_x7DG-d0D6cM-mLVUboxgRg6LPiCypuwOCA2ORnqALrSSjuRTm8JbkhYlSW1hevw1Va5WGMEvvNpNAg4AtoISvv6jyI79Gsl3-drWQ6lRJ9PSdiUTY2SgCdjGnexsZA_-Rnd9BInaqRJzwMYPOlCHY9p-4QpuybnnbX17HPFzOAJhrhSCUiDFSEt9wYOKaMQw3urk_a2zCjOjBwo', 'lc-main':'en_US', 'x-wl-uid':'1qO28TBan5h3oE1QxU2WGyoczvrC0FTgSurawI1g3sgmWQYwqLKN1zESoN3ANbMEfUc3uWSsKr9FyRbNyggYPQ+zMMdgAVJ2WL/Tf3lZHoYsm3zTt0ornhvjL6gVv6qw2U2rxb397ybM7PcAb7MFQVQ==', 'session-token':'"8oBu2yRmYSRcMko83QPjy+BgTzk9Hoeu/IhZqLO6f9E6sk3RoJ5TYUU+uS72FeKUc/090SieEJSZ4zIMwli8u+wD1adpp/yhZA6tz6CgQs96B6clWL1YtQZuyYMlXLRIxynxTrfIXGxY01cAkMTzFq+Dz2tG/5U194x6UTPT684kVRuSYdXgGsTzDoN/af1mq+m4FjMcoS4q/SJJRMHzDiQUmcKll91lr4Eemcp7bfnd7huqHdUFMgC/i0Jl7w5TA9Vgmcih4vGkWck7b5lAaA=="', 'csm-hit':'GJ6HJMM3CFA43W994KHK+b-ZQ6HYQ744MSFND7T1VVB|1519010944543'}
            #requesturl.meta['asin']=url
            #time.sleep(.1)
            req = scrapy.Request(url[1], headers={'accept-encoding': 'gzip, deflate, br' , 'accept-language': 'en-US,en;q=0.9' , 'upgrade-insecure-requests': '1' , 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36' , 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'cache-control': 'max-age=0' , 'authority': 'www.staples.com' , 'referer': 'https://www.staples.com/Ink-Toner-Finder/cat_SC43'} ,callback=self.parse1)
            req.cookies={'SSLB':'1', 'SMIDENTITY':'x23tWGRe/fq4b/yyzRHxUo5Ot4lZOgIWI7twXDzfDMT+lvZrwXGJsXOuNuUYeRApTDIjFaizcbmaoR22k/CXquUTRfE2JmCLmBK9iFQrm9jXNcqPryF9LheHx8x6RZtGcR8o+L1OYiO1qIuT0sugZTNF2sYTiNBrL1/BF7BiF3ScX7a6OM2vwMQ2e+MXxgI1rdSbEA19MHDzwQSdnyXO5W9IxgmrrQ8Wck3AaqGjdd5ry4buWw/XaFo9FKvrw+E4NdBE9kOEk3/3zy8pPjcNLbuksqThY0Smfwq/2+wEr5eEG2PQRrPdYqQui6Tokh+StIV12FSgX0FtzJ5xoLiQE+C24/JgIAVYRHHak5aBp3sR5jGMEV9FFYTIoo7uoPI9l34O4nQECE7QMK7cTEL36XYsCcJ6lqPIes6pwUjKw38I5pOUhy3mkOXQPeTdCzKPg4yAKmzUvKc4xEN1swPHsPZq10gkQcWcpXcJ6iRlYgn5TwKUrWUWlq5+QQx/GI+6TE347rJHauq7eyZXekPYxbQX9WrZqeteQ1nzCOU+8KZoEBbzpOSnsqjkRR+ufOmBpXOqZcJQvpI5T0aq2WBjfiU9teo7TVYcwYnLPLmFzNCsb3Fkopv24yQhwaGnmiZscXAB3g2xAFg+IxD10vtSj7KABal9EM/l+LD0I/Jukik=' ,'SBKT':'nc1', 'zipcode':'01701', 'geocode':'42.298643,-71.465635', 'ats-cid-AM-141111-sid':'83599783', '_ga':'GA1.2.72031363.1523857727', '_gid':'GA1.2.1557866557.1523857727', '_mkto_trk':'id:896-JNU-907&token:_mch-staples.com-1523857727613-52691', 'btpdb.LDcB1lr.dWlkIC0gc2lnbmFsIGZpcnN0IHBhcnR5IGlk':'NDE5MTgxODIyMTIwOTQ2NTIx', 'btpdb.LDcB1lr.dGZjLjM3NDQ5ODI':'U0VTU0lPTg', '_abck':'CE754FC14C7EDDC2B916B4C66D6B70DF17394A502F4E00009139D45A2B76834E~0~0gvBchPdLeNkED1/Axe337Cv9ZEqS/FGbVvo40Xm1hw=~-1~-1', 's_fid':'78F979CEC8462370-20AC298CC7658D0D', 's_cc':'true', 'cvo_sid1':'KZ6PQKBAJKTY', 'searchTracking':'B', 'YourStore':'%7B%22address1%22%3A%22659%20Worcester%20Rd%22%2C%22city%22%3A%22Framingham%22%2C%22state%22%3A%22MA%22%2C%22zipCode%22%3A%2201701%22%2C%22storeNumber%22%3A%220349%22%2C%22persists%22%3Atrue%7D', 's_vi':'[CS]v1|2D6A1CCB852A48CE-4000012140000CA2[CE]', '_cplid':'91b025b5a928f3e11d1835f2a3ceee7162ccffaea8', 'xdeviceid':'2edda8f50e4e72f9afb8307568681547', 'EDDIE_CUSTOMER_TOKEN':'e77c89ee-27ce-45c3-b347-69de785051c7', 'langPref':'-1', 'kyd-fp-v1':'1523857735-6269fb5978bf895b3bee8fb7d03f8f4c', 's_v47_persist':'2D6A1CCB852A48CE-4000012140000CA2', 'kyd-tcr-v2':'1523857735062-ff025bfc1d831387874ef4ba1cbd8e4a3a4908d61721fddebc37dd37b82f37bc', 'ctx-token':'c0ebd67ff924279cc131ca5d56c6dca2eed0248c30bd87c6c8489cb0a58bce4f76a1989850a24c3d031a99b993ce3dce254b49c1db55f70ba8305d7cf15af69d93', '__gads':'ID=afd8368160ec8803:T=1523857954:S=ALNI_MabeO_C1FIUOR_u1DX9l_BFaHxJJg', 'ev1':'non-search', 'productnum':'1', 'EDDIE_COOKIE_DETAILS':'%7B%22EDDIE_DEVICE_TOKEN%22%3A%22dd216769-f0ca-495c-b6ce-17f50e2833b0%22%2C%22UT%22%3A%22e77c89ee-27ce-45c3-b347-69de785051c7%22%2C%22TM%22%3A%7B%22CA%22%3A%22A%22%7D%7D', '_olpmID':'ZTUwYTdmZDItMWRjOS00ODZkLTk1NDctMmE4NWNhNjNkMmRm', 'CSEG':'2_NON_REWARDS', 's_atcLocation':'Error%3A%2FInk-Toner-Finder%2Fcat_SC43', '_br_uid_2':'uid%3D9303160111142%3Av%3D11.8%3Ats%3D1523857731676%3Ahc%3D11', 'SSOD':'AM4PAAAAIACHXREAAQAAABc61FoXOtRail0RAAEAAADUedRa1HnUWhUAEwCg8gkAAQN9m5cCc739GAR8efeV', '__evuid':'bcfc8e2ab434f4bcb7ee58c254ee6c01:134d:fed1b92c4d3ae438200727a89b12f98f', 'cvo_tid1':'BlZei3St3n4|1523857816|1523874325|-84', 'mp_staples_mixpanel':'%7B%22distinct_id%22%3A%20%22162ccffabf168-0d35a3969a7235-3f3c5501-1fa400-162ccffabf2c1%22%7D', 'inside-stp':'344328153-b651bdad4a768b27c17264ed5f9eb609007cc5c486a0ed43ffee7b3619d96b68-0-0', 's_sq':'staplescomprod%3D%2526c.%2526a.%2526activitymap.%2526page%253DError%25253A%25252FInk-Toner-Finder%25252Fcat_SC43%2526link%253DVIEW%252520ALL%2526region%253Dtab-b%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DError%25253A%25252FInk-Toner-Finder%25252Fcat_SC43%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.staples.com%25252FInk-Toner-Finder%25252Fcat_SC43%2526ot%253DA', 'JSESSIONID':'f89d15aa38a4591e845c95ab84518ec4', 'bm_sz':'1EDB316D94F35FA2130FD8A2FBC660EA~QAAQUEo5F4Pho3FiAQAAdHhr0dguhYDjptqfWOOB860WU9Oqpvk1/UudMRE2fQ/51KYD0PsW5GU7czWrgOkWEWaRILlCpcCInC+IqJv/B47FTLj6mPPctG9YfgyX1zEkgC1KKjWhR00Ntyd/HQBVLgUyBFT2w0U/AqSAwyBiR59mFI1UZshJ+uIwqOX9o6oX', 'ak_bmsc':'07F22C71B21F96492E84ADCBE65EC09D17394A502F4E00000D77D55A72656078~plNIr6t2AVVSS8ZYapgyzDpxdeqwUYOnjLm2wMuQN3sQh8kNc1Q/KcpGPuWNnIOMMxpHNRNwnlkBlCEVH7Cv5UfyfhdZeC/gOpLmWAzuKIkOMQdKnuICakAaSjDGluqVsLUziCWBDhlPf9QzqT2NRMu31sU4o4eyYm9GWIb1aCmBKUKtheszxjf6qtgVAtA+ggM7wj94SbWlQuZHFhelYWQOLK2X2pE0n0LhAPxRzjvUo=', 'SSID':'CABXVh0qAAwAAACROdRauJGBHZE51FoWAAAAAAAAAAAA_oDVWgC3vkOKAAHqsg8A_oDVWgEASIcAAUBeDwD-gNVaAQAHiQABPJAPAP6A1VoBAFqIAACQhwAA6ogAAA', 'SSSC':'418.G6544919453904245176.22|34632.1007168:35079.1019964:35395.1028842', 'SSPV':'r3YAAAAAAAYAAAAAAAAAAAAAAAEAAAAAAAAAAAAA', 'SSRT':'HYXVWgADAA', 'akavpau_vp1':'1523943031~id=9505818ce62ea71c48d95e2bbf7e8a70', 'bm_sv':'5DB0A8C3BDC020631AEC64DB3B15C743~f1NEEUB+FxGISXmTxtgnUYAvYyJ1L8XBYuaTksLNcy1rdT0swUs9W+Nabek6WeI5EDNMLeaFM/OfHhrg7jz+6OHezWlR6JB9MyVg6f0GRLroHU4eLq+YPouisKrWEGtkAXjxJPG+cWvz8OaMSfPLeCIBxKiAMxSSwEa2yvaXAHs=', 'RT':'sl=0&ss=1523874213500&tt=0&obo=0&sh=&dm=staples.com&si=4cea9c35-bdde-4017-92d8-40e00b23911e&bcn=%2F%2F36fb6319.akstat.io%2F&r=https%3A%2F%2Fwww.staples.com%2F&ul=1523942825260', 's_ppvl':'Homepage%253A2_NON_REWARDS%2C16%2C16%2C974%2C1329%2C974%2C1920%2C1080%2C1%2CP', 's_ppv':'Error%253A%2FInk-Toner-Finder%2Fcat_SC43%2C45%2C39%2C974%2C1920%2C974%2C1920%2C1080%2C1%2CP'}
            req.meta['id']=url[0]
            yield req

		
		
    def parse1(self, response):
        item=StapleItems()
        title="".join(response.xpath('/html/body/div[4]/div[1]/div/div[2]/div[1]/h1[@class="product-title"]/text()').extract())
        price="".join(response.xpath('/html/body/div[4]/div[1]/div/div[2]/div[1]/div[4]/div[1]/div/div[2]/div/div[@class="stp--price-discounted preferred-price-discounted delivery-price"]/text()').extract())
        model_no="".join(response.xpath('//*[@id="mmx-sku-manufacturerPartNumber"]/text()').extract())
        item_no="".join(response.xpath('//*[@id="mmx-sku-num"]/text()').extract())
        breadcrumb=">".join(response.xpath('/html/body/div[@class="stp--breadcrumbs stp--container mmx-hf-normalize"]/ul/li/a/@title').extract())+">"+title
        item['id']=response.meta['id']
        item['title']=title
        item['price']=price
        item['model_no']=model_no
        item['item_no']=item_no
        item['breadcrumb']=breadcrumb
        item['response_url']=response.url
        yield item