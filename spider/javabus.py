import requests
import csv
import time
from lxml import etree


# 爬取内容
def start():
    total = 0
    html = etree.HTML(resp.text)
    # 找到所有电影卡片
    divs = html.xpath('//*[@id="waterfall"]/div')
    for div in divs:
        # 获取每个电影卡片中的超链接，准备请求该链接以获取磁力链接
        href_arr = div.xpath("./a[@class='movie-box']/@href")
        if not len(href_arr) == 0:
            total += 1
            # 因为每个 a 标签中只有一个所以直接去除第一个值
            child_url = href_arr[0]
            # 子页面链接的结尾是番号，需要获取到之后加入到请求头中，因为页面有反扒机制
            number = child_url.split('/')[-1]
            # print(number)
            referer = domain + number
            # 组件请求头
            child_headers = {
                "referer": referer,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
            }
            child_resp = requests.get(url=child_url, headers=child_headers)
            child_resp.encoding = 'utf-8'
            child_html = etree.HTML(child_resp.text)
            # 获取番号和标题
            number_title = child_html.xpath('/html/body/div[5]/h3/text()')[0]
            # 获取到请求磁力链接的参数字符串
            magnet_arr = child_html.xpath('/html/body/script[3]/text()')[0].split(';')
            gid = magnet_arr[0].strip().split(' ')[-1]
            uc = magnet_arr[1].strip().split(' ')[-1]
            # 截取字符串前后的单引号
            img = (magnet_arr[2].strip().split(' ')[-1])[1: -1]
            # print(gid, uc, img)
            # 准备请求磁力链接
            params = {
                'gid': gid,
                'uc': uc,
                'img': img
            }
            print(f'获取{number_title}磁力链接...')
            magnet_resp = requests.get(url=magnet, params=params, headers=headers)
            magnet_str = parser_magnet(magnet_resp.text)
            csv_writer.writerow([number_title, magnet_str])
    print(f'爬取结束，本次共爬取{total}条数据.')


# 获取到磁力链接
# 后续可以优化成优先获取高清和中文字幕，目前只获取第一个磁力链接即可
def parser_magnet(html_text):
    # 去除第一个 \n 符号
    html = etree.HTML(html_text[1: -1])
    return html.xpath('//tr[1]/td[1]/a/@href')[0]


if __name__ == '__main__':
    pages = input('请输入爬取的页数:')
    pages = int(pages)
    domain = 'https://www.dmmsee.fun/'
    magnet = domain + 'ajax/uncledatoolsbyajax.php'
    f = open(f'magnet{time.strftime("%Y%m%d", time.localtime())}.csv', mode='w', encoding='utf-8')
    csv_writer = csv.writer(f)
    for page in range(pages):
        print(f'正在爬取第{page + 1}页内容...')
        # print("https://www.dmmsee.fun/page/{}".format(page + 1))
        headers = {
            "referer": "https://www.dmmsee.fun/page/{}".format(page + 1),  # 防盗链，用于反爬虫
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
        }
        resp = requests.get(url=domain, headers=headers)
        resp.encoding = 'utf-8'
        start()
        resp.close()
    f.close()
