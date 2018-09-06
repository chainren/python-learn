# 读取文件
try:
    file = open('C:\hello.txt', 'r')
    str = file.read()
    print(str)
finally:
    if file:
        file.close()

# 使用with语句
with open('C:\hello.txt', 'r') as file:
    print(file.read())

# 一次读取所有行并返回list

with open('C:\hello.txt', 'r') as file:
    for line in file.readlines():
        print(line.strip())  # strip把末尾的\n去掉


# file-like Object
# 　像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
#　StringIO就是在内存中创建的file-like Object，常用作临时缓冲。


# 二进制文件
# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
pic = open('C:/timg.jpg','rb')
print(pic.read())
pic.close()


# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件
f = open('C:\hello.txt', 'r', encoding='gbk')
print(f.read())
f.close()

# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
with open('C:/offline_FtnInfo.txt', 'r', errors='ignore') as file:
    for line in file.readlines():
        print(line)


