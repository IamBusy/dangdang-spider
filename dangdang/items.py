# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Product(scrapy.Item):
    pid = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()
    subtitle = scrapy.Field()
    photo  = scrapy.Field()
    category_1 = scrapy.Field()
    category_2 = scrapy.Field()
    category_3 = scrapy.Field()
    description = scrapy.Field()
    publisher		= scrapy.Field()
    author			= scrapy.Field()
    publish_time	= scrapy.Field()
    price 	= scrapy.Field()
    sell_price		= scrapy.Field()
    isbn			= scrapy.Field()
