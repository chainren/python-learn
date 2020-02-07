import requests

# 获取Json响应数据
resp = requests.get(url='https://api.github.com/events', stream=True)

print(resp.json())