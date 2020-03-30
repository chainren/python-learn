import aiohttp

import asyncio

from datetime import datetime

async def fetch(client):
    async with client.get('http://httpbin.org/get') as resp:
        assert resp.status == 200
        return await resp.text()


async def main():
    async with aiohttp.ClientSession() as client:
        html = await fetch(client)
        print(html)


loop = asyncio.get_event_loop()


tasks = []

for i in range(30):
    task = loop.create_task(main())
    tasks.append(task)

start = datetime.now()

loop.run_until_complete(main())

end = datetime.now()

print("aiohttp版爬虫花费时间为：")
print(end - start)