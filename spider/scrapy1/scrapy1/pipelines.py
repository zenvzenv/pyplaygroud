# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Scrapy1Pipeline(object):
    def process_item(self, item, spider):
        return item


# 将爬虫内容存储到 txt 中
class QiuShiBaiKePipeline(object):
    fp = None

    # 处理 item 对象
    # 该方法可以接收爬虫文件提交过来的 item 对象
    # 每接受到一个 item 会执行一次该方法
    def open_spider(self, spider):
        print('开始爬虫')
        self.fp = open('./qiubai.txt', mode='w', encoding='utf-8')

    # 处理 item 对象
    # 该方法可以接收爬虫文件提交过来的 item 对象
    # 每接受到一个 item 会执行一次该方法
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + ':' + content + '\n')
        # 如果此处 return 出去了，那么参数会被传递到下一个即将被执行的管道类
        return item

    def close_spider(self, spider):
        print('关闭爬虫')
        self.fp.close()


class BossZhiPinPipeline(object):
    def process_item(self, item, spider):
        print(item)
        return item
