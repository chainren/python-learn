# encoding=utf8

# chardet 可以检测未知字符编码

# 安装： pip install chardet


import chardet
s = chardet.detect(b'Hello world')
print(s)


# 检测中文
data = '十步杀一人，千里不留行'.encode('gbk')
s = chardet.detect(data)
print(s)


# 检测日文
data = '最新の主要ニュース'.encode('euc-jp')
s = chardet.detect(data)
print(s)