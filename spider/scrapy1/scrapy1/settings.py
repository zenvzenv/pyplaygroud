# Scrapy settings for scrapy1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy1'

SPIDER_MODULES = ['scrapy1.spiders']
NEWSPIDER_MODULE = 'scrapy1.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 日志级别
LOG_LEVEL = 'ERROR'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'en',
#     'Referer': 'https://www.zhipin.com',
#     'Cookie': 'acw_tc=0bdd34b616407637874693296e019ec2ef193b4e063a7e4d431f97621f6584; lastCity=101190100; sid=sem; __zp_seo_uuid__=bb361996-b32b-4881-8e83-1fe9d401ce1d; __g=sem; __l=r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fwww.zhipin.com%2Fnanjing%2F%3Fkeyword%3D589007744%26qhclickid%3D187a82078543bf3c%26sid%3Dsem%26_ts%3D1640763787483&g=%2Fwww.zhipin.com%2Fnanjing%2F%3Fkeyword%3D589007744%26qhclickid%3D187a82078543bf3c%26sid%3Dsem%26_ts%3D1640763787483&s=3&friend_source=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1640763792; __c=1640763787; __a=75057693.1640763787..1640763787.2.1.2.2; __zp_stoken__=5b76dJFBmPTl4eHpdUHtzOThkNytsVS5JRwxIGB10YiJ%2FKGRHTHpmGBsEQD13PFM0AiBfN206ShQXbUlnCSNUOhdDZGdMfBZvJxQtKDJuURI6RxtDejkrT2Z%2BSXozHTp%2FQBltQxxbSD9aXTk%3D; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1640763801; __zp_sseed__=66BUCf7F3RW7wZx/9T2Q2LM3MQyKqaM8U4mCDRf4nNs=; __zp_sname__=b959db78; __zp_sts__=1640763829085'
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'scrapy1.middlewares.Scrapy1SpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'scrapy1.middlewares.Scrapy1DownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 定义的管道会按优先级依次执行，糗事百科管道
    # 'scrapy1.pipelines.QiuShiBaiKePipeline': 300,
    'scrapy1.pipelines.BossZhiPinPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
