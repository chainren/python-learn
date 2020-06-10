import aiohttp
import asyncio


# 抓取字节流数据并处理
async def fetch(client):
    async with client.get('http://httpbin.org/image/png') as resp:
        return await resp.read()


async def main():
    async with aiohttp.ClientSession() as client:
        img = await fetch(client)
        with open('httpbin_img.png', 'wb') as f:
            f.write(img)
            print('download image success.')


# 传递参数
async def fetch_with_params(client):
    params = [('a', 1), ('b', 2)]
    async with client.get('http://httpbin.org/get', params=params, timeout=60) as resp:
        return await resp.text()


# 请求时添加headers
async def fetch_with_headers(client):
    headers = {'content-type': 'application/json',
               'User-Agent': 'Python/3.7 aiohttp/3.7.2'}
    async with client.get('http://httpbin.org/get', headers=headers) as resp:
        return await resp.text()


async def fetch_with_post(client):
    data = {'a':'a','b':'b'}
    async with  client.post('http://httpbin.org/post', data=data) as resp:
        return await resp.text()


async def handle_text_resp():
    async with aiohttp.ClientSession() as client:
        # text = await fetch_with_params(client)
        text = await fetch_with_post(client)
        print("response : %s" % text)


# 请求会话中添加cookies信息，将其放在创建会话session时，可以与整个会话共享
async def session_with_cookies():
    cookies = {'cookies': 'this is cookie'}
    async with aiohttp.ClientSession(cookies=cookies) as client:
        html = await fetch_with_params(client)
        print("response : %s" % html)


loop = asyncio.get_event_loop()

loop.run_until_complete(handle_text_resp())
