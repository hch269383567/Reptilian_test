# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyjuziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    company=scrapy.Field()
    institution = scrapy.Field()
    financing = scrapy.Field()
    lunshu = scrapy.Field()
    money = scrapy.Field()
    time = scrapy.Field()


