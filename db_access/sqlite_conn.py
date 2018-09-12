# -*- coding:utf-8 -*-

# Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。

import sqlite3

# 创建连接，如果数据库文件不存在，则自动在当前目录创建
conn = sqlite3.connect('test.db')

# 创建cursor
cursor = conn.cursor()

# 创建表
cursor.execute('create table user(id varchar(20) primary key, `name` varchar(20))')

# 插入数据
cursor.execute('insert into user(id, name) values(1, \'Michael\')')

# 通过rowcount获得插入的行数:
print('insert row count : %s' % cursor.rowcount)

# 关闭cursor
cursor.close()

# 提交事务
conn.commit()

# 半闭连接
conn.close()