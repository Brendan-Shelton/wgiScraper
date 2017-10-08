# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#TODO: Items for double panels or integrate double panels, item for concert

class WgiscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name = scrapy.Field()
    MusEffOvr = scrapy.Field()
    MusEffMus = scrapy.Field()
    MusEffTot = scrapy.Field()
    VisEffOvr = scrapy.Field()
    VisEffVis = scrapy.Field()
    VisEffTot = scrapy.Field()
    MusComp = scrapy.Field()
    MusPerf = scrapy.Field()
    MusTot = scrapy.Field()
    VisComp = scrapy.Field()
    VisPerf = scrapy.Field()
    VisTot = scrapy.Field()
    SubTot = scrapy.Field()
    PenTot = scrapy.Field()
    score = scrapy.Field()
    compType = scrapy.Field()
    date = scrapy.Field()
    pass
#item for concert percussion
class ConcertItem(scrapy.Item):
    name = scrapy.Field()
    compType = scrapy.Field()
    date = scrapy.Field()
    pass

#item for guard
class GuardItem(scrapy.Item):

    name = scrapy.Field()
    EAVoc = scrapy.Field()
    EAExc = scrapy.Field()
    EATot = scrapy.Field()
    MAVoc = scrapy.Field()
    MAExc = scrapy.Field()
    MATot = scrapy.Field()
    DAComp = scrapy.Field()
    DAExc = scrapy.Field()
    DATot = scrapy.Field()
    GERep1 = scrapy.Field()
    GEPerf1 = scrapy.Field()
    GESub1 = scrapy.Field()
    GERep2 = scrapy.Field()
    GEPerf2 = scrapy.Field()
    GESub2 = scrapy.Field()
    GETot = scrapy.Field()
    SubTot = scrapy.Field()
    PenTot = scrapy.Field()
    score = scrapy.Field()
    compType = scrapy.Field()
    date = scrapy.Field()
    pass

class WindsItem(scrapy.Item):
    name = scrapy.Field()
    OERep = scrapy.Field()
    OEComm = scrapy.Field()
    OETot = scrapy.Field()
    MAComp = scrapy.Field()
    MAAch = scrapy.Field()
    MATot = scrapy.Field()
    VAComp = scrapy.Field()
    VAAch = scrapy.Field()
    VATot = scrapy.Field()
    SubTot = scrapy.Field()
    PenTot = scrapy.Field()
    score = scrapy.Field()
    compType = scrapy.Field()
    date = scrapy.Field()
    pass