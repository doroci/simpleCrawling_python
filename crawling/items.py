# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()  # 제목
    contents = scrapy.Field()  # 기사 내용
    source = scrapy.Field()  # 출처
    date = scrapy.Field()  # 날짜

pass
