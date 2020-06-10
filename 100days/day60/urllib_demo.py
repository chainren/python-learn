import urllib.parse

import urllib.request

url = 'http://www.baidu.com/s'

params = urllib.parse.urlencode({'wd':'python'})

# 发送请求
resp = urllib.request.urlopen('?'.join([url, params]))

# 处理响应
print(resp.getcode())

print(resp.readlines())