from selenium.webdriver import Edge
from selenium.webdriver.common.by import By

# edge 无头请求
EDGE = {
    "browserName": "MicrosoftEdge",
    "version": "96.0.1054.62",
    "platform": "WINDOWS",
    "ms:edgeOptions": {
        'extensions': [],
        'args': [
            '--headless',
            '--disable-gpu'
        ]}
}

web = Edge('./msedgedriver.exe', capabilities=EDGE)
web.get('https://ys.endata.cn/BoxOffice/Ranking')
table = web.find_element(by=By.XPATH, value='//*[@id="app"]/section/main/div/div[1]/div/section/section/section/section/div[1]/div[3]/table')
# 获取表格票房数据
print(table.text)
# 拿到页面真正的源代码
print(web.page_source)
web.close()
