# scrapy 基本使用
1. pip install pywin32
2. pip install Scrapy
3. scrapy startproject ${project_name} // 创建爬虫工程
4. cd ${project_name}
5. scrapy genspider ${spider_name} ${domain} // 创建爬虫文件
6. scrapy crawl ${spider_name} // 执行爬虫
# 持久化
## 基于终端命令
1. 要求：只可以将 parse 方法的返回值进行持久化到本地文件系统
2. 命令：scrapy crawl ${spider_name} -o ${file_name}
## 基于管道
### 编码流程
1. 数据解析
2. 封装数据到 item 对象，items.py 文件中定义
3. 将 item 对象提交给管道进行持久化操作，pipelines.py文件
4. pipelines.py 接收 item 对象并进行持久化
5. 在配置文件中开启管道,setting.py 中的 ITEM_PIPELINES 选项
# 五大核心组件
## Spider
1. 产生 url
2. 数据清晰
## 
# 中间件
## 下载中间件
1. 位置：引擎和下载器之间
2. 作用：批量拦截到整个工程的请求和响应
3. 拦截请求：
    1. UA 伪装：process_request
    2. 代理 IP：process_exception:return request
4. 拦截响应：
    1. 篡改响应数据和响应对象
# CrawlScrapy
一个 Spider 的子类，进行全站数据爬取
## 全站数据爬取方式
1. 基于 Spider 手动请求
2. 基于 CrawlSpider
## 使用
1. 创建工程：scrapy startproject ${scrapy_name}
2. 创建爬虫文件：scrapy genspider -t crawl ${spider_name} ${domain}
3. 连接提取器，根据指定的规则(allow)进行指定连接的爬取
4. 规则解析器：将连接提取器提取到的连接进行解析(call_back)
