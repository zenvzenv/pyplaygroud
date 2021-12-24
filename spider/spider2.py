import requests

# url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20"
url = "https://movie.douban.com/j/chart/top_list"

params = {
    "type": 24,
    "interval_id": "100%3A90",
    "action": "",
    "start": 0,
    "limit": 20
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}

rep = requests.get(url=url, params=params, headers=headers)
print(rep.request.url)
print('%')

rep.close()
