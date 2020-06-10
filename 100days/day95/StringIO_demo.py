
from io import StringIO

# 定义一个 StringIO 对象，写入并读取其在内存中的内容
f = StringIO()

f.write('Python-100')
str = f.getvalue() # 读取写入的内容
print('写入内存中的字符串为:%s' %str)

f.write('\n') # 追加内容

f.write('坚持100天')

f.close() # 关闭


f1 = StringIO('Python-100' + '\n' + '坚持100天')
# 读取内容
print(f1.read())

f1.close()



# 假设的爬虫数据输出函数 outputData()
def outputData():
    dataOne   = '我是 1 号爬虫数据\n'
    dataTwo   = '我是 2 号爬虫数据\n'
    dataThree = '我是 3 号爬虫数据'
    data = dataOne + dataTwo + dataThree
    return data

# dataStr 为爬虫数据字符串
dataStr = outputData()

# 1. 将 outputData() 函数返回的内容写入内存中
dataIO = StringIO(dataStr)

# 假设的爬虫数据输出函数 outputData()
def outputData():
    dataOne   = '我是 1 号爬虫数据\n'
    dataTwo   = '我是 2 号爬虫数据\n'
    dataThree = '我是 3 号爬虫数据'
    data = dataOne + dataTwo + dataThree
    return data

# dataStr 为爬虫数据字符串
dataStr = outputData()

# 1. 将 outputData() 函数返回的内容写入内存中
dataIO = StringIO(dataStr)

# 1.1 输出 StringIO 在内存中写入的数据
print('1.1内存中写入的数据为:\n%s' %dataIO.getvalue())

# 1.2 按行输出写入的数据方式一
print('1.2按行输出写入的数据方式一:')
for data in dataIO.readlines():
    print(data.strip('\n')) # 去掉每行数据末尾的换行符


# 1.2 按行输出写入的数据方式一
print('1.2按行输出写入的数据方式一:')
for data in dataIO.readlines():
    print(data.strip('\n')) # 去掉每行数据末尾的换行符


# 1.3 按行输出写入的数据方式二
# 由于上一步的操作，此时文件指针指向数据末尾(32)，我们需要将指针指向起始位置
print('由于上一步操作的输出，此时文件指针位置为:%d' %dataIO.tell())

# 将文件指针指向起始位置，方便下面的演示
dataIO.seek(0)
print('1.3按行输出写入的数据方式二:')
for data in dataIO:
    print(data.strip('\n'))