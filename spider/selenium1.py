from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 事先将 Edge 的驱动包放到和 python 同级目录
web = Edge()
web.get('http://www.baidu.com')
web.find_element(by=By.XPATH, value='//*[@id="kw"]').send_keys('666', Keys.ENTER)
# el = web.find_element(by=By.XPATH, value='//*[@id="su"]')
# el.click()

