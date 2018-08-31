# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    name = scrapy.Field()
    biaoti = scrapy.Field()
    fangjianhao = scrapy.Field()
    game = scrapy.Field()
    hot = scrapy.Field()
    fans=scrapy.Field()
