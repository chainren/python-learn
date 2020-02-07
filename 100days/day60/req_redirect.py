"""
重定向
"""
import requests

r = requests.get('http://github.com')

print(r.url)
print(r.status_code)
# 使用响应对象的 history 方法来追踪重定向。
print(r.history)


# 可通过 allow_redirects禁用重定向
# 指定timeout超时时间
r = requests.get('http://github.com', allow_redirects=False, timeout=0.01)
print(r.status_code)
print(r.url)
print(r.history)