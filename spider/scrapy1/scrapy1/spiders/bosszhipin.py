import scrapy
from scrapy1.items import BossZhiPin


class BosszhipinSpider(scrapy.Spider):
    name = 'bosszhipin'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/c101190100/?query=Python&industry=&position=&ka=hot-position-6']
    boss_domain = 'https://www.zhipin.com/'

    def start_requests(self):
        cookie = 'lastCity=101190100; sid=sem; __zp_seo_uuid__=bb361996-b32b-4881-8e83-1fe9d401ce1d; __g=sem; __l=r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fwww.zhipin.com%2Fnanjing%2F%3Fkeyword%3D589007744%26qhclickid%3D187a82078543bf3c%26sid%3Dsem%26_ts%3D1640763787483&g=%2Fwww.zhipin.com%2Fnanjing%2F%3Fkeyword%3D589007744%26qhclickid%3D187a82078543bf3c%26sid%3Dsem%26_ts%3D1640763787483&s=3&friend_source=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1640763792; __c=1640763787; __a=75057693.1640763787..1640763787.3.1.3.3; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1640763830; __zp_stoken__=5b76dJFBmPTl4eG1SXHxVOThkNysNOFIcCGpIGB10YiBxLlU4EnpmGBsEPSsWZl00AiBfN206ShQXYTxnCSBRYwg0GndJfwFdezcZKDJuURI6RxtNIFg9MmZ%2BSXozQzp%2FQBltQxxbSD9aXTk%3D; acw_tc=0bdd34b616407686740541828e019e68dfe0b1a0fcf9fad5d10a8b9cfbd66f; __zp_sseed__=66BUCf7F3RW7wZx/9T2Q2O9vSc5yZPWDA8HhAtiIGFI=; __zp_sname__=b959db78; __zp_sts__=1640768674067'
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'Referer': 'https://www.zhipin.com',
            'Cookie': cookie
        }
        cookies = {i.split('=')[0]: i.split('=')[1] for i in cookie.split('; ')}
        yield scrapy.Request(
            url=self.start_urls[0],
            callback=self.parse,
            cookies=cookies,
            headers=headers
        )

    def parse_detail(self, response):
        item = response.meta['item']
        job_desc = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[@class="job-sec"]//text()').extract()
        job_desc = ''.join(job_desc)
        item['job_desc'] = job_desc.strip()
        print(job_desc)
        # 提交到管道
        yield item

    def parse(self, response, **kwargs):
        li_list = response.xpath('//*[@id="main"]/div/div[2]/ul/li')
        for li in li_list:
            item = BossZhiPin()
            job_title = li.xpath('//span[@class="job-name"]/a/text()').extract_first()
            job_desc_url = li.xpath('//span[@class="job-name"]/a/@href').extract_first()
            item['job_title'] = job_title
            print(job_title)
            # 手动发送请求时通过 meta 字典进行参数传递
            yield scrapy.Request(url=self.boss_domain + job_desc_url, callback=self.parse_detail, meta={'item': item})
