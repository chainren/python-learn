"""
复杂post请求
"""

import requests

# 设置data参数
payload = {'key1':'value1','key2':'value2'}

r = requests.post('http://httpbin.org/post', data = payload)

print(r.text)

# 设置json参数。 Requests 允许你使用 json 直接传递参数，然后它就会被自动编码。
payload= {'some':'data'}
r = requests.post('http://httpbin.org/post', json=payload)

print(r.text)

# 设置文件参数

files = {'file': open('req_post.py', 'rb')}

r = requests.post('http://httpbin.org/post', files=files)

print(r.text)
