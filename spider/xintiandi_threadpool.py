from concurrent.futures import ThreadPoolExecutor  # 线程池
import requests
import csv


def one_page(url, page):
    params = {
        "limit": '20',
        "current": f"{page}",
        "pubDateStartTime": '',
        "pubDateEndTime": '',
        "prodPcatid": '',
        "prodCatid": '',
        "prodName": ''
    }
    headers = {
        "Referer": "http://www.xinfadi.com.cn/priceDetail.html",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
    }
    resp = requests.get(url, params=params, headers=headers)
    resp.encoding = 'utf-8'
    result_list = resp.json()['list']
    for r in result_list:
        writer.writerow(r.values())
    resp.close()


if __name__ == '__main__':
    url = 'http://www.xinfadi.com.cn/getPriceData.html'
    f = open('aa.csv', mode='w', newline='', encoding='utf-8')
    writer = csv.writer(f)
    with ThreadPoolExecutor(12) as pool:
        for i in range(1, 20000):
            pool.submit(one_page, url, i)
    f.close()
