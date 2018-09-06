# coding=utf8
# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：

file = open('C:/pywrite.txt', 'w', encoding='utf8')

file.writelines('Hello world!')

file.close()


# 使用with来写文件
with open('C:/pywrite1.txt', 'w', encoding='utf8') as file:
    file.writelines('人生苦短，我用python\n')


# 以追加的方式写入, 模式改为'a'
with open('C:/pywrite1.txt','a', encoding='utf8') as file:
    file.writelines('人生苦短，我用python\n')

