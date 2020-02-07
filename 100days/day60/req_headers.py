"""
通过设置请求头header，模拟复杂请求。比如模拟正常浏览器，避过爬虫拦截
"""

import requests

url = "http://www.baidu.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36"}

resp  = requests.get(url=url, headers=headers)

print(resp.request.headers)