import scrapy
from scrapy1.items import QiuShiBaiKe
# 爬取糗事百科


class QiushibaikeSpider(scrapy.Spider):
    name = 'qiushibaike'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/text']

    def parse(self, response, **kwargs):
        # 解析作者的名称和段子
        # 拿到所有段子的 div 标签
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        for div in div_list:
            # 得到的结果是 selector。
            # extract 可以将 selector 中的字符串提取出来
            # author = div.xpath('./div[@class="author clearfix"]/a[2]/h2/text()')[0].extract()
            # 提取列表中的第一个元素
            author = div.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract_first()
            # 忽略每段中间的 span 标签
            content = div.xpath('./a[@class="contentHerf"]/div[@class="content"]/span//text()').extract()
            content = ''.join(content)
            # print(author.strip(), content.strip())
            item = QiuShiBaiKe()
            item['author'] = author.strip()
            item['content'] = content.strip()
            # 将 item 对象提交到管道
            yield item

    # 基于终端指令的持久化
    # def parse(self, response, **kwargs):
    #     # 解析作者的名称和段子
    #     # 拿到所有段子的 div 标签
    #     all_data  = []
    #     div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
    #     for div in div_list:
    #         # 得到的结果是 selector。
    #         # extract 可以将 selector 中的字符串提取出来
    #         # author = div.xpath('./div[@class="author clearfix"]/a[2]/h2/text()')[0].extract()
    #         # 提取列表中的第一个元素
    #         author = div.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract_first()
    #         # 忽略每段中间的 span 标签
    #         content = div.xpath('./a[@class="contentHerf"]/div[@class="content"]/span//text()').extract()
    #         content = ''.join(content)
    #         print(author.strip(), content.strip())
    #         dic = {
    #             'author': author.strip(),
    #             'content': content.strip()
    #         }
    #         all_data.append(dic)
    #     # 终端命令持久化需要在运行爬虫时指定 -o ${file_name} 来定制保存的文件
    #     return all_data
