# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapiesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class AuthorItem(scrapy.Item):
    name = scrapy.Field()
    desc = scrapy.Field()
    dynasty = scrapy.Field()
    take_count = scrapy.Field()