# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# Python提供了pickle模块来实现序列化。

import pickle
import logging

logging.basicConfig(level=logging.INFO, format= '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')


logging.info('this is a test')

d = dict(name='chainren', age = 29, score = 100)

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object

stuObj = pickle.dumps(d)

logging.info(stuObj)

file = open('C:/stu_picking.txt','wb')

file.write(stuObj)

file.close()

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
file = open('C:/stu_picking.txt','rb')

obj = pickle.load(file)

logging.info(obj)

file.close()
