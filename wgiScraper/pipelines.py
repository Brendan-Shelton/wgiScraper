# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import pymysql
from wgiScraper.items import WgiscraperItem
from wgiScraper.items import GuardItem
from wgiScraper.items import WindsItem
from numbers import Number
from datetime import datetime

#TODO: Only try to insert 3-4 weeks of data, or check if a competition has already been inserted before selecting to put less stress on server

class WgiscraperPipeline(object):
    def __init__(self):
            self.conn = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='wgiscores')
            self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if(item['MusEffOvr'][0]):
            prelims = False
            if("Prelims" in item['compType'][0]):
                prelims = True
            #Process date for item
            if(item['date'][0]):
                date = item['date'][0].split('-')
                print(item['date'][0])
                print(str(date[0]))
                dateFormatted = datetime.strptime(date[0], '%A, %B %d, %Y ')
                print("Formatted date: " + str(dateFormatted))
                print(item['name'][0])
            if(isinstance(item, WgiscraperItem)):
                #Split up select into two selects to get the ensemble and then if the ensemble is in the database, check for duplicates and then insert
                #SELECT * FROM scores, ensembles_perc WHERE scores.date = date AND ensembles_perc.name LIKE name AND scores.prelims = prelims
                sql = """INSERT INTO scores (name, MusEffOvr, 
                MusEffMus, MusEffTot, VisEffOvr, VisEffVis, VisEffTot, MusComp,
                MusPerf, MusTot, VisComp, VisPerf, VisTot, SubTot, PenTot, score)
                VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (item['name'][0],
                item['MusEffOvr'][0],
                item['MusEffMus'][0],
                item['MusEffTot'][0],
                item['VisEffOvr'][0],
                item['VisEffVis'][0],
                item['VisEffTot'][0],
                item['MusComp'][0],
                item['MusPerf'][0],
                item['MusTot'][0],
                item['VisComp'][0],
                item['VisPerf'][0],
                item['VisTot'][0],
                item['SubTot'][0],
                item['PenTot'][0],
                item['score'][0])
                print(str(sql))
                self.cursor.execute(sql) 

                self.conn.commit()

                return item
            elif(isinstance(item, GuardItem)):
                sql = """INSERT INTO scores_guard (name, EAVoc, EAExc, EATot, MAVoc,
                MAExc, MATot, DAComp, DAExc, DATot, GERep1, GEPerf1, GESub1, GERep1,
                GEPerf2, GESub2, SubTot, PenTot, score) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', 
                '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (item['name'][0],
                item['EAVoc'][0],
                item['EAExc'][0],
                item['EATot'][0],
                item['MAVoc'][0],
                item['MATot'][0],
                item['DAComp'][0],
                item['DAExc'][0],
                item['DATot'][0],
                item['GERep1'][0],
                item['GEPerf1'][0],
                item['GESub1'][0],
                item['GERep2'][0],
                item['GEPerf2'][0],
                item['GESub2'][0],
                item['SubTot'][0],
                item['PenTot'][0],
                item['score'][0])
                self.cursor.execute(sql)

                self.conn.commit()

                return item
            elif(isinstance(item, WindsItem)):
                sql = """INSERT INTO scores_winds (name, OERep, OEComm, OETot,
                MAComp, MAAch, MATot, VAComp, VAAch, VATot, SubTot, PenTot, score)
                VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (item['name'][0],
                item['OERep'][0],
                item['OEComm'][0],
                item['OETot'][0],
                item['MAComp'][0],
                item['MAAch'][0],
                item['MATot'][0],
                item['VAComp'][0],
                item['VAAch'][0],
                item['VATot'][0],
                item['SubTot'][0],
                item['PenTot'][0],
                item['score'][0])
                self.cursor.execute(sql)
                self.conn.commit()

                return item
            else:
                return item
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()