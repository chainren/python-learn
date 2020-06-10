"""
使用Beautiful Soup 搜索文档
"""

html_doc = """
<html><head><title>index</title></head>
<body>
<p class="title"><b>首页</b></p>
<p class="main">我常用的网站
<a href="https://www.google.com" class="website" id="google">Google</a>
<a href="https://www.baidu.com" class="website" id="baidu">Baidu</a>
<a href="https://cn.bing.com" class="website" id="bing">Bing</a>
</p>
<div><!--这是注释内容--></div>
<p class="content1">...</p>
<p class="content2">...</p>
</body>
"""

from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(html_doc, 'lxml')

# 过滤器
# 1. 根据 TAG 的 name 来查找标签，下面的例子会查找文档中的所有 b 标签。同时要注意统一传入 Unicode 编码以避免 Beautiful Soup 解析编码出错。

# demo1 
tags = soup.find_all('b')
print(tags)

# 2. 根据 TAG 的 name 来查找标签，下面的例子会查找文档中的所有 b 标签。同时要注意统一传入 Unicode 编码以避免 Beautiful Soup 解析编码出错。
# demo2
for tag in soup.find_all(re.compile('^b')):
    print(tag.name)

# 3. 如果传入列表参数，那么 Beautiful Soup 会将与列表中任一一个元素匹配的内容返回。
# demo3
for tag in soup.find_all(['a','b']):
    print(tag)

# 4. 如果传入列表参数，那么 Beautiful Soup 会将与列表中任一一个元素匹配的内容返回。
# demo4
for tag in soup.find_all(True):
    print(tag.name, end = ', ')
print('\n')
# 5、方法。我们可以定义一个方法，该方法只接受一个参数，若该方法返回 True 则表示当前元素匹配并且被找到，返回 False 意味着没找到。下面的例子展示了查找所有同时包含 class 属性和 id 属性的节点。
# demo5
def has_id_class(tag):
    return tag.has_attr('id') and tag.has_attr('class')

tags = soup.find_all(has_id_class)
for tag in tags:
    print(tag)

## find_all 函数
# 6. 搜索指定名字的属性时可以使用的参数值包括：字符串，正则表达式，列表，True。也就是我们上文介绍过的过滤器。
# demo6 按属性名和属性值查找
tags = soup.find_all(id='google')
print(tags[0]['href'])

# 查找所有包含id属性的tag
for tag in soup.find_all(id=True):
    print(tag['href'])

# 7. 按照 CSS 类名搜索，但是表示 CSS 的关键字 class 在 Python 中是内置关键字，从 Beautiful Soup 4.1.1 版本开始，可以通过 class_  参数搜索有指定 CSS 类名的 TAG：
# 按照 CSS 类名搜索，但是镖师 CSS 的关键字 class 在 Python 中是内置关键字，从 Beautiful Soup 4.1.1 版本开始，可以通过 class_  参数搜索有指定 CSS 类名的 TAG：
# demo7
tags = soup.find_all('a', class_='website')
for tag in tags:
    print(tag['href'])

# 自定义class过滤器方法
def has_seven_characters(css_class):
    return css_class is not None and len(css_class)==7

for tag in soup.find_all(class_ = has_seven_characters):
    print(tag['id'])

# demo8 指定tag和class属性进行过滤
css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'lxml')
tags = css_soup.find_all('p', class_='strikeout')
print(tags)

# demo9 通过text内容搜索，同时text还可以配合其他属性一起完成搜索任务
soup = BeautifulSoup(html_doc, 'lxml')
tags = soup.find_all(text='Google')
print('google : ', tags)

# 查找多个text
tags = soup.find_all(text=['Baidu','Bing'])
print('baidu & bing : ',tags)

# 查找标签a且包含text=‘Google’
tags = soup.find_all('a', text='Google')
print(tags)

print('\n')
# 限制返回数量
# demo10 
tag = soup.find_all('a', limit=1)
print(tag)

tags = soup.find_all('p', recursive=False)
print(tags)

# demo11
tag = soup.find('div')
print(tag)

## css选择器。通过.select()方法中传染字符串参数即可使用css选择器的语法找到tag

# demo11 通过某个标签逐层查找。
tags = soup.select('body a')
for tag in tags:
    print(tag['href'])

# demo12 查找某个标签下的直接子标签
tags = soup.select('p > a')
print(tags)

# 通过id选择
tags = soup.select('p > #google')
print(tags)

# demo13 通过css类名直接查找
tags = soup.select('.website')
for tag in tags:
    print(tag.string)


# demo14 通过标签的id属性查找
tags = soup.select('#google')
print(tags)

# demo15 通过属性的值来查找
tags = soup.select('a[href="https://cn.bing.com"]')
print(tags)