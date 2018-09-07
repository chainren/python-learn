# encoding=utf8

# requests模块
# 安装： pip install requests

import requests
import logging

logging.basicConfig(level=logging.INFO, format= '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

req = requests.get('https://www.douban.com/')
print(req.encoding)
print(req.status_code)
# logging.info(req.text) # 输出获取的网页内容


# 对于带参数的URL，传入一个dict作为params参数：
# req = requests.get('https://www.douban.com/search', params={'q':'python','cat':'1001'})
# print(req.url)


# 用content属性获得bytes对象
bytes = req.content
# logging.info(bytes) # 输出二进制


# 可直接获取响应的json数据
req = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# logging.info(req.json())


# 需要传入HTTP Header时，我们传入一个dict作为headers参数：
req = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}, cookies={'foo':'bar'})
# logging.info(req.text) # 输出手机版网页内容


# 要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
req = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
# print(req.status_code)
# print(req.text)


# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
req = requests.post('https://accounts.douban.com/login', json={'username':'xxxx', 'password':'xxxx'})
print(req.status_code)


# 上传文件
upload_file = {'file':open('./xxx', 'rb')}
req = requests.post('', files=upload_file)


# 把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。

