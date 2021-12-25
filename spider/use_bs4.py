import requests
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}
domain = 'https://umei.cc'
url = domain + '/bizhitupian/meinvbizhi/xingganmeinv.htm'
resp = requests.get(url, headers)
resp.encoding = 'utf-8'
main_page = BeautifulSoup(resp.text, 'html.parser')
# find，find_all查找标签
# 可以根据标签中的属性来精确定位标签
alist = main_page.find("div", attrs={'class': 'TypeList'}).find_all("a")
for a in alist:
    child_href = domain + a.get('href')
    child_resp = requests.get(child_href, headers)
    child_resp.encoding = 'utf-8'
    child_page = BeautifulSoup(child_resp.text, 'html.parser')
    div = child_page.find('div', class_='ImageBody')
    img_src = div.find('img').get('src')
    print(img_src)
    img_resp = requests.get(img_src, headers)
    img_name = img_src.split('/')[-1]
    with open('d:/img/' + img_name, mode='wb') as f:
        f.write(img_resp.content)
    time.sleep(1)

resp.close()
