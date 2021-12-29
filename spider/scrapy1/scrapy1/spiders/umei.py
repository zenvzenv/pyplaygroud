import scrapy


class UmeiSpider(scrapy.Spider):
    name = 'umei'
    # allowed_domains = ['umei.cc']
    start_urls = ['https://umei.cc/bizhitupian/huyanbizhi/']
    #      https://umei.cc/bizhitupian/huyanbizhi/index_2.htm
    url = 'https://umei.cc/bizhitupian/huyanbizhi/index_%d.htm'
    page_num = 2

    def parse(self, response, **kwargs):
        li_list = response.xpath('/html/body/div[2]/div[8]/ul/li')
        for li in li_list:
            # 提取列表第一个
            img_name = li.xpath('./a/span/text()').extract_first()
            print(img_name)
        if self.page_num <= 11:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            # 手动请求发送
            yield scrapy.Request(url=new_url, callback=self.parse)
