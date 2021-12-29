# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# 提交的 item 会被哪个管道类进行处理？
# 优先级高的管道类先执行
class QiuShiBaiKe(scrapy.Item):
    author = scrapy.Field()
    content = scrapy.Field()


class BossZhiPin(scrapy.Item):
    job_title = scrapy.Field()
    job_desc = scrapy.Field()
