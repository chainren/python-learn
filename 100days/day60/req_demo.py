import requests


"""
# 安装requests模块
pip install requests
"""

# 发送请求，并获得响应对象
resp = requests.get(url="http://www.baidu.com/s", params={'wd':'python'})

#响应码
print(resp.status_code)

# 相应内容
print(resp.text)