
from pyquery import PyQuery as pq

# 将html字符串初始化为对象
html = """
<html>
    <head>
        我爱我的祖国
        <title>China</title>
    </head>
    <body>
        <ul id="container">
            <li class="li1">五星</li>
            <li class="li2">红旗</li>
            <li class="li3">迎风飘扬</li>
        </ul>
    </body>
</html>
"""

# 从字符串中加载
doc = pq(html)
# 从文件中读取
# doc = pq(filename='index.html')

# 从url中读取
# doc = pq(url = 'http://www.baidu.com')

print(type(doc))
print(doc)

## 常用css选择器

# demo1 id选择器
print(type(doc('#container')))
print(doc('#container'))

# demo2 class选择器
print(type(doc('.li2')))
print(doc('.li2'))

# demo3 使用多层选择器
print(doc('html #container'))

## demo4 根据css选择器修改html标签内容
li2 = doc('.li2')
li2.css('font-size', '18px')
print(li2)


## 伪类选择器

# demo5

pseudo_doc = pq(html)
print(pseudo_doc('li:nth-child(2)'))
#打印第一个li标签
print(pseudo_doc('li:first-child'))
#打印最后一个标签
print(pseudo_doc('li:last-child'))


## demo6 通过container方法筛选内容
print(pseudo_doc("li:contains('五星')"))
#找到含有好的li标签
print(pseudo_doc("li:contains('红')"))

#找到含有啊的li标签
print(pseudo_doc("li:contains('啊')"))


# 查找标签
## demo7 通过find查找标签
container = doc.find('#container')
print(container)

## 通过children查找子标签
print(container.children())

## 通过parent查找父标签
print(container.parent())

# 通过slbling查找兄弟标签
li2 = doc.find('.li2')
print(li2.siblings())

# 标签信息的提取。通过.attr()方法提取标签的属性值

# demo8
print(doc('.li2').attr('class'))

## 通过.text()提取标签文本
print(doc('.li2').text())

## 通过.remove(tagname)方法删除某些标签
tag = doc('html')
tag.remove('title')
print(tag.text())


# 处理复杂的网址请求‘
## demo9 附带参数请求
cookies = {'Cookie':'cookie'}
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

resp = pq(url='http://image.baidu.com', headers=headers, cookies=cookies)
#print(resp)
print('====================images=========================')
img = resp('img').items()
print(type(img))
for i in img:
    print(i.attr('src'))