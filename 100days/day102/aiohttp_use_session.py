import aiohttp
import asyncio
from datetime import datetime


async def fetch(client):
    print('client: %s' % client)
    async with client.get('http://httpbin.org/get') as resp:
        assert resp.status == 200
        # text()
        # json() 可以直接处理json返回结果
        # read() 处理字节流，比如图片
        html = await resp.json()
        print('fetch result : %s' % html)


async def main():
    async with aiohttp.ClientSession() as client:
        tasks = []
        for i in range(30):
            tasks.append(asyncio.create_task(fetch(client)))
        await asyncio.wait(tasks)


loop = asyncio.get_event_loop()

start = datetime.now()

loop.run_until_complete(main())

end = datetime.now()

print("aiohttp(same session)版爬虫花费时间为：")
print(end - start)
