# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AuthorItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    desc = scrapy.Field()
    dynasty = scrapy.Field()
    take_count = scrapy.Field()


class PoetryItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    category_name = scrapy.Field()
    dynasty = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    shangxi_content = scrapy.Field()
