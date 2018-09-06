# 如果要操作二进制数据，就需要使用BytesIO。
# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：

from io import BytesIO

f = BytesIO()

f.write('中文'.encode('utf-8'))

print(f.getvalue())