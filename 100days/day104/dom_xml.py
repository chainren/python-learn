from xml.dom.minidom import parse

# 读取xml文件
dom = parse('test.xml')

# 获取文档对象
data = dom.documentElement

# 根据标签名称获取元素列表
stus = data.getElementsByTagName('student')
for stu in stus:
    # 获取标签属性
    st_id = stu.getAttribute('id')
    st_name = stu.getAttribute('name')
    id = stu.getElementsByTagName('id')[0].childNodes[0].nodeValue
    name = stu.getElementsByTagName('name')[0].childNodes[0].nodeValue
    age = stu.getElementsByTagName('age')[0].childNodes[0].nodeValue
    gender = stu.getElementsByTagName('gender')[0].childNodes[0].nodeValue
    print('st_id:', st_id,', st_name:', st_name)
    print('id:', id, ', name:', name, ', age:', age,', gender:', gender)
