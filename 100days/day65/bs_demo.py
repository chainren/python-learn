
# demo1

from bs4 import BeautifulSoup

# 指定解析器
soup = BeautifulSoup('<html><head><title>index</title></head><body>content</body></html>','lxml')
print(soup.head)

with open('example.html', 'r', encoding='utf-8') as f:
    html_doc = f.read()

print(html_doc)

# demo 2 
soup = BeautifulSoup(html_doc, 'lxml')
p_tag = soup.p
print(p_tag.name)
print(p_tag['class'])
print(p_tag.attrs)

# 修改tag名称
# p_tag.name = 'myTag'
# print(p_tag)

## demo3  连续获取属性
print(soup.p.b)

## demo4 通过find_all(tag_name)方法获取所有的某个名字的标签

a_tags = soup.find_all('a')
print(a_tags)


## demo5 通过.contents将tag以列表方式输出
head_tag=soup.head
print(head_tag)

print(head_tag.contents)

# .children 只可以获取 tag 的直接节点
for child in head_tag.children:
    print('child is : ', child)

# 通过.descendants可以获取到子孙节点
head_tag = soup.head
for child in head_tag.descendants:
    print('child is : ' , child)


# 父节点
# 通过 .parent 属性获取标签的父亲节点

# demo7
title_tag = soup.title
print(title_tag.parent)
print(type(soup.html.parent))
print(soup.parent)

# 通过.parents获取指定标签的所有父亲标签
# demo8
a_tag = soup.a

for parent in a_tag.parents:
    print(parent.name)

## 兄弟节点 通过.next_sibling和.previous_sibling来获取下一个标签和上一个标签
# demo9
div_tag = soup.div

print(div_tag.next_sibling)
# div 的第一个 next_sibling 是div 和 p 之间的换行符。这个规则对于 previous_sibling 同样适用
print(div_tag.next_sibling.next_sibling)

# 前进和后退
# 通过.next_element和.previous_element获取指定标签的前一个或有一个备解析的对象

# demo11
head_tag = soup.head
print(head_tag.next_element) # title节点
title_tag = soup.title
print(title_tag.next_element) # 输出index

# 通过.next_elements迭代
div_tag = soup.div
for next_emt in div_tag.next_elements:
    print('next_emt div : ', next_emt)