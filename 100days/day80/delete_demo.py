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

sql = "delete from user1 where id = %s" % 1

try:
    cursor.execute(sql)
    conn.commit()
except pymysql.DatabaseError as e:
    print(e)
    conn.rollback()
finally:
    conn.close()
