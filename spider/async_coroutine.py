import asyncio
import aiohttp

urls = [
    'http://kr.shanghai-jiuxin.com/file/bizhi/20211216/etaqlwmikpj.jpg',
    'http://kr.shanghai-jiuxin.com/file/bizhi/20211216/4xaod5oo3ny.jpg',
    'http://kr.shanghai-jiuxin.com/file/bizhi/20211216/cg21aj02mt5.jpg'
]


async def aio_download(url):
    # 从右往左切分
    name = url.rsplit('/', 1)[1]
    # 异步发起请求，得到 session 对象
    async with aiohttp.ClientSession() as session:
        #
        async with session.get(url) as resp:
            with open(name, mode='wb') as f:
                # 获取响应内容，异步写入文件
                # 异步文件模块 aiofiles
                f.write(await resp.content.read())
    print(f'{name} over!')


async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(aio_download(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    # Windows 上需要修改成如下代码否则会报 RuntimeError: Event loop is closed 错
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
