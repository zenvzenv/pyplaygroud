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