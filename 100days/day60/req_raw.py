"""
获取原始相应数据
"""

import requests

resp = requests.get(url = "https://api.github.com/events", stream=True)

print(resp.raw)

print(resp.raw.read(10))