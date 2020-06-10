import pymysql

conn = pymysql.connect(
    host = '192.168.160.33',
    port = 3306,
    user = 'develop',
    password='xs_dev',
    database='test',
    charset='utf8'
)

cursor = conn.cursor()

sql = """
INSERT INTO user1(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Fei', 'Fei', 20, 'M', 1000)
"""

try:
    # 提交sql
    cursor.execute(sql)
    conn.commit()
except:
    # 异常时回滚
    conn.rollback()

conn.close()