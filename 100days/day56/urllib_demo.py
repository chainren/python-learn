
from urllib import request

from urllib import error

from urllib import parse

from urllib import robotparser

# resp = request.urlopen('http://www.baidu.com')

# 创建一个post请求
data = {'kw':'python'}
data = bytes(parse.urlencode(data), encoding='utf-8')
response = request.urlopen('https://fanyi.baidu.com/sug',data)
print(response.read().decode('unicode_escape'))


# Request应用实例
url = 'http://www.python.org'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
req = request.Request(url, headers = headers, method='GET')
response = request.urlopen(req)
# print(response.read())


## URLError实例
try:
    resp = request.urlopen('https://www,baidu.com')
except error.URLError as e:
    print(e.reason)


## urlparse实例，解析url各个部分
url = 'http://www.baidu.com/urllib.parse.html;python?kw=urllib.parse#module-urllib'
result = parse.urlparse(url)
print(result)


## urlunparse实例，用于合并多个部分组成url
dataList = ['http', 'www.baidu.com', '/urllib.parse.html', 'python', 'kw=urllib.parse', 'modul-urllib'] # 六个字符串都必须填写，否则会出现 ValueError 错误，如果某一字符串不存在则填入空字符
dataTuple = ('http', 'www.baidu.com', '/urllib.parse.html', '', 'kw=urllib.parse', 'modul-urllib') # 六个字符串都必须填写，否则会出现 ValueError 错误，如果某一字符串不存在则填入空字符
url_list = parse.urlunparse(dataList)
print('url_list unparse : %s' % url_list)
url_tuple = parse.urlunparse(dataTuple)
print('url_tuple unparse : %s' % url_tuple)


## urlencode实例
params = {'username':'xxx', 'password':'123'}
base_url = 'http://www.baidu.com'
url = base_url + '?' + parse.urlencode(params)
print(url)


## robotparser实例

rp = robotparser.RobotFileParser()
rp.set_url('http://www.baidu.com/robots.txt')
rp.read()
print(rp.can_fetch('Baiduspider', 'http://www.baidu.com')) 
print(rp.can_fetch('*', 'http://www.baidu.com'))
