"""
python 正则表达式使用
re 模块
"""

import re

# 如果匹配，返回re.Match对象
m = re.match(r'1\d', '13')
print(m)
# 不匹配，返回None
m = re.match(r'1\d', '23')
print(m)

# 用 ( ) 分组就可以提取出子字符串比如上面的邮件正则表达式，在Python中使用 Match 对象的 group() 函数提取出子字符串，groups() 函数返回所有子字符串的元组
email = re.match(r'([A-Za-z0-9_\-\.]+)\@([A-Za-z0-9_\-\.]+)\.([A-Za-z]{2,4})', 'abc@gmai.com')
print(email.group(0))

print(email.group(1))

print(email.group(2))

print(email.group(3))

## 2. 替换 re提供的sub()函数替换子字符串的内容
test = '021- 1101101 10' # 替换字符串中的空格
s = re.sub(r'\s', '', test)
print(s)


## 编译
'''
在使用 re 模块的时候，Python 帮我们做了两件事：
   1. 编译正则表达式，如果正则表示不合法会报错
   2. 用编译后的正则表示匹配字符串
使用re.compile()编译正则表达式。 返回的是一个Pattern对象
'''

test = re.compile(r'test(.{1,6})')
# groups 表达式中的分组数量
r = test.match('testPy').groups()
print(r)

# 编译时的匹配模式
print(test.flags)