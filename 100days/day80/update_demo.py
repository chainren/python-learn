import pymysql

conn = pymysql.Connection(
    host = '192.168.160.33',
    port = 3306,
    user = 'develop',
    password='xs_dev',
    database='test',
    charset='utf8'
)

cursor = conn.cursor()

sql = "UPDATE user1 SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')

try:
    # 执行sql
    cursor.execute(sql)
    # 提交
    conn.commit()
except:
    # 异常回滚
    conn.rollback()
finally:
    conn.close()