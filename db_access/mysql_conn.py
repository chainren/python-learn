# -*- encoding -*-

# 连接mysql数据库

# 安装mysql驱动:pip install mysql-connector


import mysql.connector

conn = mysql.connector.connect(host='127.0.0.1', port = 3306,user='root', password='root', database='test')

cursor = conn.cursor()

# 查询数据，注：mysql的占位符是%s
cursor.execute('select * from `user` where id = %s', (1,))

# 获取结果集
rows = cursor.fetchone()

print(rows)

cursor.close()

conn.close()