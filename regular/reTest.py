# -- coding: utf-8 --


# 正则表达式

# Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用\转义，所以要特别注意：
""
s = 'ABC\\-001' # Python的字符串
# 对应的正则表达式字符串变成：
# 'ABC\-001'

""
# 因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：

"""
s = r'ABC\-001' ，对应的正则表达式不变：ABC\-001
"""


import re

res = re.match(r'\d{3}\-\d{3,8}','010-12345')
print('match result %s' % res)

res = re.match(r'\d{3}-\d{3,8}', '010, 12345')
print(res)

# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None


# 使用正则切分字符串
l = re.split(r'\s+', 'a b  c')
print('result : %s' % l)

l = re.split(r'[\s\,]+', 'a,b c ,d')
print('result : %s' % l)


# 分组
# 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。如：^(\d{3}-(\d{3,8}))$定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)

print('group 0 : %s' % m.group(0))
print('group 1 : %s' % m.group(1))
print('group 2 : %s' % m.group(2))

# 如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。

# 贪婪匹配 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符,
gs = re.match(r'^(\d+)(0*)$', '102932000').groups()
print(gs)

# 加个?就可以让\d+采用非贪婪匹配
gs = re.match(r'^(\d+?)(0*)$', '102932000').groups()
print(gs)


# 编译
# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：
# 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# 用编译后的正则表达式去匹配字符串。
# 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：


re_tel = re.compile(r'^(\d{3})-(\d{3,8})$')

gs = re_tel.match('010-12345').groups()
print(gs)
gs = re_tel.match('010-10086').groups()
print(gs)


# 练习，验证email的正则
re_email = re.compile(r'^(\w+)\@(\w+)\.(\w+)$')

res = re_email.match('chenrengui@xiangshang360.com')
print(res)
res = re_email.match('736061765@qq.com')
print(res)


def validate_mail(mail_addr):
    if re_email.match(mail_addr):
        return True
    else:
        return False

print(validate_mail('hello@gmail.com'))