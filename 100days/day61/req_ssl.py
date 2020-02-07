"""
ssl证书验证
"""

import requests

r = requests.get('http://httpbin.org', verify=True)
print(r.text)