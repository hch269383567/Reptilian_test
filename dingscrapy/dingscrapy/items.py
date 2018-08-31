# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DingscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DingdianItem(scrapy.Item):

    book_name = scrapy.Field()
    zz = scrapy.Field()
    gx = scrapy.Field()
    zs=scrapy.Field()