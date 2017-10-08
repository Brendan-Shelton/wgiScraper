import scrapy

from wgiScraper.items import WgiscraperItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

#Works with all competitionsuite html pages


#  TODO:
#     Add send to database
#     Add specification of which website from
#     Add date of score
#     A separate scrape will need to be done for Winds/Guard/Percussion/Concert/Double Panels for each maybe not tho

class wgiSpider(scrapy.Spider):
    name = "wgi"
    allowed_domains = ["wgi.org", "recaps.competitionsuite.com", "mccga.org" "sc-pa.org"]
    start_urls = [
        "https://www.wgi.org/event-scores/2016-Percussion-Scores.html",
        #"http://mccga.org/2017-schedule/",
        #"http://sc-pa.org/"
    ]
    def parse(self, response):
        xpath_str = ""
        i = 0
        if("wgi" in str(response)):
            xpath_str = "div#content-main > div.content-detail > table > tr > td > a::attr('href')"
        elif("mccga" in str(response)):
            xpath_str = "div#content > div > div > table > tbody > tr > td > a::attr('href')"
        elif("sc-pa" in str(response)):
            xpath_str = "div.scores_box > div > ul.list-group > li > a::attr('href')"
        for href in response.css(xpath_str):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_content)
        i = i+1
    def parse_content(self, response):
        
        #find out what type the sheet is: winds, guard, or perc. Then, a separate check will be done if it is a double panel
        #sheets could be combined, so we need to get the category at the top of each table instead of on a sheet by sheet basis
        #ensClassStr = response.xpath('/html/body/div/table/tr[1]/td/text()').extract()
        #TODO: Ensure no duplicates are added, ensure if prelims/finals, only finals are inserted, 
        compType = response.xpath('/html/body/div[10]/div[2]/table/tr/td[2]/div[2]/text()').extract()
        date = response.xpath('/html/body/div[10]/div[2]/table/tr/td[2]/div[3]/text()').extract()
        for table in response.xpath('/html/body/div'):
            ensClassStr = table.xpath('table/tr/td/text()').extract()
            print(str(ensClassStr))
            print(str(table))
            for sel in table.xpath('table/tr/td/table/tr'):
                
                #item['ensClass'] = ensClassStr
                if("Percussion" in str(ensClassStr)):
                    item = WgiscraperItem()
                    if(sel.xpath('td[last()]/table/tr[1]/td/text()').extract() == sel.xpath('td[17]/table/tr[1]/td/text()').extract()):
                        item['name'] = sel.xpath('td[1]/text()').extract()
                        item['MusEffOvr'] = sel.xpath('td[2]/table/tr[1]/td/text()').extract()
                        item['MusEffMus'] = sel.xpath('td[3]/table/tr[1]/td/text()').extract()
                        item['MusEffTot'] = sel.xpath('td[4]/table/tr[1]/td/text()').extract()
                        item['VisEffOvr'] = sel.xpath('td[5]/table/tr[1]/td/text()').extract()
                        item['VisEffVis'] = sel.xpath('td[6]/table/tr[1]/td/text()').extract()
                        item['VisEffTot'] = sel.xpath('td[7]/table/tr[1]/td/text()').extract()
                        item['MusComp'] = sel.xpath('td[8]/table/tr[1]/td/text()').extract()
                        item['MusPerf'] = sel.xpath('td[9]/table/tr[1]/td/text()').extract()
                        item['MusTot'] = sel.xpath('td[10]/table/tr[1]/td/text()').extract()
                        item['VisComp'] = sel.xpath('td[11]/table/tr[1]/td/text()').extract()
                        item['VisPerf'] = sel.xpath('td[12]/table/tr[1]/td/text()').extract()
                        item['VisTot'] = sel.xpath('td[13]/table/tr[1]/td/text()').extract()
                        item['SubTot'] = sel.xpath('td[14]/table/tr[1]/td/text()').extract()
                        item['PenTot'] = sel.xpath('td[16]/table/tr/td/text()').extract()
                        item['score'] = sel.xpath('td[last()]/table/tr[1]/td/text()').extract()
                        item['compType'] = compType
                        item['date'] = date
                        yield item 

                    else:
                        #double panel
                        print(str(sel.xpath('td[last()]/table/tr[1]/td/text()')) + " != " + str(sel.xpath('td[17]/table/tr[1]/td/text()')))
                        print("Invalid format!")

                elif("Guard" in str(ensClassStr)):
                    item = GuardItem()
                    if(sel.xpath('td[last()]/table/tr[1]/td/text()').extract() == sel.xpath('td[21]/table/tr[1]/td/text()')):
                        item['name'] = sel.xpath('td[1]/text()').extract()
                        item['EAVoc'] = sel.xpath('td[2]/table/tr[1]/td/text()').extract()
                        item['EAExc'] = sel.xpath('td[3]/table/tr[1]/td/text()').extract()
                        item['EATot'] = sel.xpath('td[4]/table/tr[1]/td/text()').extract()
                        item['MAVoc'] = sel.xpath('td[5]/table/tr[1]/td/text()').extract()
                        item['MAExc'] = sel.xpath('td[6]/table/tr[1]/td/text()').extract()
                        item['MATot'] = sel.xpath('td[7]/table/tr[1]/td/text()').extract()
                        item['DAComp'] = sel.xpath('td[8]/table/tr[1]/td/text()').extract()
                        item['DAExc'] = sel.xpath('td[9]/table/tr[1]/td/text()').extract()
                        item['DATot'] = sel.xpath('td[10]/table/tr[1]/td/text()').extract()
                        item['GERep1'] = sel.xpath('td[11]/table/tr[1]/td/text()').extract()
                        item['GEPerf1'] = sel.xpath('td[12]/table/tr[1]/td/text()').extract()
                        item['GESub1'] = sel.xpath('td[13]/table/tr[1]/td/text()').extract()
                        item['GERep2'] = sel.xpath('td[14]/table/tr[1]/td/text()').extract()
                        item['GEPerf2'] = sel.xpath('td[15]/table/tr[1]/td/text()').extract()
                        item['GESub2'] = sel.xpath('td[16]/table/tr[1]/td/text()').extract()
                        item['GETot'] = sel.xpath('td[17]/table/tr[1]/td/text()').extract()
                        item['SubTot'] = sel.xpath('td[18]/table/tr[1]/td/text()').extract()
                        item['PenTot'] = sel.xpath('td[20]/table/tr[1]/td/text()').extract()
                        item['score'] = sel.xpath('td[21]/table/tr[1]/td/text()').extract()
                        item['compType'] = compType
                        item['date'] = date
                        yield item

                    else:
                        #double panel
                        print(str(sel.xpath('td[last()]/table/tr[1]/td/text()')) + " != " + str(sel.xpath('td[17]/table/tr[1]/td/text()')))
                        print("Invalid format!") 

                elif("Winds" in str(ensClassStr)):
                    item = WindsItem()
                    if(sel.xpath('td[last()]/table/tr[1]/td/text()') == sel.xpath('td[14]/table/tr[1]/td/text()')):
                        item['name'] = sel.xpath('td[1]/text()').extract()
                        item['OERep'] = sel.xpath('td[2]/table/tr[1]/td/text()').extract()
                        item['OEComm'] = sel.xpath('td[3]/table/tr[1]/td/text()').extract()
                        item['OETot'] = sel.xpath('td[4]/table/tr[1]/td/text()').extract()
                        item['MAComp'] = sel.xpath('td[5]/table/tr[1]/td/text()').extract()
                        item['MAAch'] = sel.xpath('td[6]/table/tr[1]/td/text()').extract()
                        item['MATot'] = sel.xpath('td[7]/table/tr[1]/td/text()').extract()
                        item['VAComp'] = sel.xpath('td[8]/table/tr[1]/td/text()').extract()
                        item['VAAch'] = sel.xpath('td[9]/table/tr[1]/td/text()').extract()
                        item['VATot'] = sel.xpath('td[10]/table/tr[1]/td/text()').extract()
                        item['SubTot'] = sel.xpath('td[11]/table/tr[1]/td/text()').extract()
                        item['PenTot'] = sel.xpath('td[13]/table/tr[1]/td/text()').extract()
                        item['score'] = sel.xpath('td[14]/table/tr[1]/td/text()').extract()
                        item['compType'] = compType
                        item['date'] = date
                        yield item

                    else:
                        #double panel
                        print(str(sel.xpath('td[last()]/table/tr[1]/td/text()')) + " != " + str(sel.xpath('td[17]/table/tr[1]/td/text()')))
                        print("Invalid format!") 
#XPATH for date & location: /html/body/div[3]/div[2]/table/tbody/tr/td[2]/div[3]