import requests
from urllib import parse
import re
from lxml import etree

# 下载91美剧网瑞克和莫迪的视频内容
# 获取进行转发的连接
obj = re.compile(r'var v="(?P<url>.*?)"', re.S)
mjw_domain = 'https://91mjw.com'
mjw_play_domain = 'https://91mjw.com/vplay'
player_domain = 'https://91mjw.com/player/'
headers = {
    "Referer": mjw_play_domain,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}
rick_morty_url = mjw_play_domain + '/NTMxOC0xLTA=.html'
rick_morty_resp = requests.get(rick_morty_url, headers=headers)
rick_morty_html = etree.HTML(rick_morty_resp.text)
rick_morty_resp.close()
# 获取一些网页上的信息，用于后续的请求
script_content = rick_morty_html.xpath('//script[@type="text/javascript"]/text()')[0].strip()
page_params = script_content.split('\n  ')
play_type = page_params[1].split('=')[-1][1: -2]
vid = page_params[2].split('=')[-1][1: -2]
video_id = page_params[3].split('=')[-1][1: -2]
s_time = page_params[5].split('=')[-1]
user_id = page_params[7].split('=')[-1][1: -2]
next_url = page_params[8].split('"')[1]
params = {
    'v': vid,
    'type': play_type,
    'uid': user_id,
    'id': video_id,
    'sTime': s_time,
    'next_url': next_url
}
# 此处请求是为了获取第一个 m3u8 文件，后续还有两个 m3u8 文件
player_resp = requests.get(player_domain, params=params, headers=headers)
url1 = obj.search(player_resp.text).group('url')
player_resp.close()
# 获取第二个 m3u8 文件
url1_resp = requests.get(mjw_domain + url1, headers)
url2 = url1_resp.text.split('\n')[-1]
url1_resp.close()
url2 = parse.unquote(url2)
print(url2)
# 服务器会重定向
url2_resp = requests.get(url2)
redirect_list = url2_resp.history
url2_resp.close()
# 拿到服务器的转发地址
redirect_url = redirect_list[len(redirect_list) - 1].headers["location"]
print(redirect_url)
# 需要去请求重定向的连接拿到最终 m3u8
redirect_resp = requests.get(redirect_url)
final_url = redirect_resp.text.strip().split('\n')[-1]
print(final_url)
# 获取域名
redirect_domain = redirect_url.split('com')[0] + 'com'
print(redirect_domain)

# m3u8_url = 'https://e1.monidai.com/ppvod/493794552290F30507E5F99D8A4E8BFE.m3u8'
m3u8_url = redirect_domain + final_url

resp = requests.get(m3u8_url, headers=headers)
with open('rackandmody.m3u8', mode='wb') as f:
    f.write(resp.content)
resp.close()
n = 1
with open('rackandmody.m3u8', mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line.startswith('#'):
            # 下载 ts 视频片段文件
            ts_resp = requests.get(line, headers=headers)
            with open(f'video/{n}.ts', mode='wb') as tsf:
                tsf.write(ts_resp.content)
            print(f'完成了第{n + 1}个文件')
