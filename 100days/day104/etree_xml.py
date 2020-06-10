import xml.etree.ElementTree as et

# 解析xml文件
tree = et.parse('test.xml')

# 根节点
root = tree.getroot()

# 标签名
print('root_tag:', root.tag,'\n\n')

for stu in root:
    # 属性值
    print('stu_id:', stu.attrib['id'], ', stu_name:', stu.attrib['name'])
    # 标签中的内容
    print('id:', stu[0].text)
    print('name:', stu[1].text)
    print('age:', stu[2].text)
    print('gender:', stu[3].text)

    print('--------------------------------------------------------')