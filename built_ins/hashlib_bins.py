# 摘要算法简介
# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
import hashlib

md5 = hashlib.md5()

md5.update('hello world'.encode('utf-8'))
print(md5.hexdigest())

# hsa1摘要算法
sha1 = hashlib.sha1()
sha1.update('hello world'.encode('utf-8'))
s = sha1.hexdigest()
print(s)

