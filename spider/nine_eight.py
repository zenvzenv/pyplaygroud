import requests
import re
import csv


def gen_day_str():
    import time
    return time.strftime('%Y%m%d', time.localtime())


def create_day_dir(path):
    import os
    path = path.strip()
    is_exists = os.path.exists(path)
    if not is_exists:
        print(f'开始创建{path}')
        os.mkdir(path)
        print(f'创建{path}结束')
    else:
        print(f'{path}已经存在')


# 准备一些变量
day_str = gen_day_str()
create_day_dir(day_str)
domain = 'https://www.qwrewr.net/'
page_re = re.compile(r'<em>\[<a href.*?<a href="(?P<url>.*?)".*?class="s xst">(?P<title>.*?)</a>', re.S)
magnet_re = re.compile(r'磁力链接.*?<li>(?P<magnet>.*?)</ol>.*?<br />', re.S)
params = {
    'mod': 'forumdisplay',
    'fid': 36,
    'filter': 'typeid',
    'typeid': 672
}

resp = requests.get(domain + 'forum.php', params=params)
resp.encoding = 'utf-8'
page_content = resp.text
result = page_re.finditer(page_content)
f = open(f'{day_str}/magnet{day_str}.csv', 'w', encoding="utf-8")
writer = csv.writer(f)
for i in result:
    row = []
    child_url = domain + i.group('url').replace('amp;', '')
    child_resp = requests.get(child_url)
    child_resp.encoding = 'utf-8'
    child_res = magnet_re.search(child_resp.text)
    row.append(i.group('title'))
    row.append(child_res.group('magnet'))
    writer.writerow(row)
    child_resp.close()

f.close()
resp.close()
