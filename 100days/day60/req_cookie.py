"""
设置cookie
"""

import requests

cookies = dict(cookies_are='working')
r = requests.get('http://httpbin.org/cookies', cookies=cookies)
print(r.text)

jar = requests.cookies.RequestsCookieJar()
# 为路径/cookies设置cookies
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')

url = 'http://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
print(r.text)