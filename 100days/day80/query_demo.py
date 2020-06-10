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

sql = """
select * from user1
"""

try:
    cursor.execute(sql)
    res = cursor.fetchall()
    for row in res:
        id = row[0]
        fname=row[1]
        lname=row[2]
        age =row[3]
        sex=row[4]
        income=row[5]
        print("id=%s,fname=%s,lname=%s,age=%s,sex=%s,income=%s" % (id, fname, lname, age, sex, income))
except Exception as e:
    print(e)

# 关闭连接
conn.close()