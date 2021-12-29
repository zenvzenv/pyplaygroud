import scrapy


class MjwSpider(scrapy.Spider):
    # 爬虫文件名称，爬虫文件唯一标识
    name = 'mjw'
    # 允许的域名，用来限定 start_urls 列表中
    allowed_domains = ['91mjw.com']
    # 起始的 url 列表，该列表中存放的 url 会被 scrapy 自动的进行请求
    start_urls = ['http://www.baidu.com', 'http://www.sougou.com']

    # 用于数据解析
    def parse(self, response, **kwargs):
        print(response)


