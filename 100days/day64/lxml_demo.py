"""
lxml解析xml或html文档
"""

from lxml import etree

from io import StringIO

test_html = '''
<html>
    <body>
        <div>
            <!-- 这里是注释 -->
            <h4>手机品牌商<span style="margin-left:10px">4</span></h4>
            <ul>
               <li>小米</li>
               <li>华为</li>
               <li class='blank'> OPPO </li>
               <li>苹果</li>
            </ul>
        </div>
        <div>
            <h4>电脑品牌商<span style="margin-left:10px">3</span></h4>
            <ul class="ul" style="color:red">
                <li>戴尔</li>
                <li>机械革命</li>
                <li>ThinkPad</li>
            </ul>
        </div>
    </body>
</html>
'''

html = etree.parse(StringIO(test_html))

print(html)

## 2. 获取所有li标签数据
li_list = html.xpath('//li')
print('类型：%s' % type(li_list))

print('值：%s' % li_list)

for li in li_list:
    print('li文本：%s ' % li.text)

## 3. 获取带class='blank'属性数据

blank_li_list = html.xpath('//li[@class="blank"]')

print(blank_li_list)

for li in blank_li_list:
    print('blank li 文本为：%s' % li.text)

## 4. 属性操作
ul = html.xpath('//ul')[1] # 取第二个ul

# 遍历属性
for name, value in ul.attrib.items():
    print('{0}={1}'.format(name, value))

# 添加新的属性
ul.set('new_attr', 'true')
# 获取单个属性
new_attr = ul.get('new_attr')
print(new_attr)


## 5. 获取最后一个div标签数据
last_div = html.xpath('//div[last()]')
print(type(last_div))

for div in last_div:
    print('div : %s' % div)

print('TAG: %s' % last_div[0].tag)
print('last_div 值: %s' % last_div[0].text)


## 6. 添加子节点
child = etree.Element('child')
child.text = '新子元素'
div = last_div[0]
div.append(child)
# 查找添加的子元素
child_text = div.find('child').text
print(child_text)

## 7. 删除子元素
# 查找并设置第一个查询到的元素
first_ul = html.find('//ul')
ul_li = first_ul.xpath('li')
for li in ul_li:
    #删除元素
    first_ul.remove(li)

ul_li = first_ul.xpath('li')
if len(ul_li) == 0:
    print('元素被删除了')


print('------------------------------------------------------------')

## 遍历元素后代
body = html.find('body')
for sub in body.iter():
    print(sub.tag)
    print(sub.text)

