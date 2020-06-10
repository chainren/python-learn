"""
通过Session会话维持
"""

import requests

s = requests.Session()
# 第一次请求设置了一个cookie值
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# 再次通过Session对象请求同一个网站，能够获取上次请求设置的cookie，说明他们在同一个会话中
r = s.get('http://httpbin.org/cookies')
print(r.text)
