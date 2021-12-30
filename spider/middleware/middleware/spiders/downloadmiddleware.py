import scrapy


class DownloadmiddlewareSpider(scrapy.Spider):
    name = 'downloadmiddleware'
    # allowed_domains = ['xxx']
    start_urls = ['http://www.baidu.com/s?wd=ip']

    def parse(self, response, **kwargs):
        html = response.text
        with open('ip.html', mode='w', encoding='utf-8') as f:
            f.write(html)

