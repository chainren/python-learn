# Python内置的os模块也可以直接调用操作系统提供的接口函数。

# 操作文件和目录

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中

import os

# 查看当前目录的绝对路径
print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('C:/', 'pytest')

path = 'C:/pytest'
# 然后创建一个目录
if(not os.path.exists(path)):
    print('file not exist')
    os.mkdir(path)
else:
    print('file existed')

# 删除一个目录
os.rmdir(path)


# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符

# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

files = os.path.split('C:/pywrite.txt')
print(files)


# 得到文件后缀
files = os.path.splitext('C:/pywrite.txt')
print(files)

# 重命名
# os.rename('test.txt','test.py')

# 移除
# os.remove('test.txt')


# shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充
import shutil
f1 = open('C:/pywrite.txt', 'r')
f2 = open('Q:/pywrite.txt', 'w')

shutil.copyfileobj(f1,f2)

f1.close()
f2.close()

# 如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录
list = [x for x in os.listdir('c:/') if os.path.isdir(x)]
print(list)
for dir in list:
    print(dir)
