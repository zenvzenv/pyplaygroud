import requests
import re
import csv

url = 'https://movie.douban.com/top250'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}
resp = requests.get(url, headers=headers)
# print(resp.text)
page_content = resp.text

# re.S 表示 '.' 能过匹配所有字符
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<title>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?</p>'
                 r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*?<span>(?P<people>.*?)人评价</span>',
                 re.S)
result = obj.finditer(page_content)
for i in result:
    print(i.group('title'))
    print(i.group('year').strip())
    print(i.group('score'))
    print(i.group('people'))
resp.close()
