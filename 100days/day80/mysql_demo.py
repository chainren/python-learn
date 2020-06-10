"""
python pymysql模块

## 安装
```
pip install PyMySQL
```

"""

import pymysql

# 连接数据库
conn = pymysql.connect(
    host = '192.168.160.33',
    port = 3306,
    user = 'develop',
    password='xs_dev',
    database='test',
    charset='utf8'
)

# print(conn)
# print(type(conn))

## conn.cursor()获取游标 
# develop

cursor_test = conn.cursor()
# print(cursor_test)


# execute(query,args=None): 执行单条的sql语句，执行成功后返回受影响的行数
# query：要执行的sql语句，字符串类型
# args：可选的序列或映射，用于query的参数值。如果args为序列，query中必须使用%s做占位符；如果args为映射，query中必须使用%(key)s做占位符

# executemany(query,args=None)：
# 函数作用：批量执行sql语句，比如批量插入数据，执行成功后返回受影响的行数
# 参数说明：
#   query：要执行的sql语句，字符串类型
#   args：嵌套的序列或映射，用于query的参数值

## demo 
# 使用execute()方法执行sql查询
cursor_test.execute('select version()')
print(cursor_test.fetchone())
conn.commit()

# 创建表
sql = """
CREATE TABLE IF NOT EXISTS user1 (
        ID INT(11) PRIMARY KEY AUTO_INCREMENT,
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT ) 
"""
cursor_test = conn.cursor()
cursor_test.execute(sql)
conn.close()
