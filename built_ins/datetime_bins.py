# -- coding: utf-8 --

from datetime import datetime, timedelta, timezone

# 获取当前日期和时间
now = datetime.now()
print(now)
print(type(now))


# 获取指定日期和时间
# 要指定某个日期和时间，我们直接用参数构造一个datetime：
dt = datetime(2018, 8, 29, 20, 56)
print(dt)


# datetime转换为timestamp 把一个datetime类型转换为timestamp只需要简单调用timestamp()方法：
dt = datetime(2018, 8, 29, 20, 57)
ts = dt.timestamp()
print(ts)


# timestamp转换为datetime
ts =  1535547420.0
dt = datetime.fromtimestamp(ts)
print(dt)


# str转换成datetime
cday = datetime.strptime('2018-08-30 09:40:00', '%Y-%m-%d %H:%M:%S')
print(cday)


# datetime转换成str
now = datetime.now()
str = datetime.strftime(now,'%Y-%m-%d %H:%M:%S')
print(str)


# date加减, 需要导入timedelta

now = datetime.now()
print(now + timedelta(hours=12))
print(now + timedelta(days=10))
print(now + timedelta(days=20, hours=12))


# 本地时间转换为UTC时间
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。

# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区

tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
print(now)

dt = now.replace(tzinfo=tz_utc_8)
print(dt)

# 时区转换 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc) # 拿到UTC时间，并强制设置时区为UTC+0:00
print(utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。


# 练习： 接受用户输入的时间和时区字符串，转换成timestamp
def totimestemp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    print('input date : %s' % dt)
    tz_offset = int(tz_str[3:-3], base=10)
    print(tz_offset)
    tz = timezone(timedelta(hours=tz_offset))
    dt = dt.replace(tzinfo=tz)
    print('use timezone trans : %s' % dt)
    return dt.timestamp()

t1 = totimestemp('2018-08-30 02:15:00','UTC+7:00')
print(t1)
t2 = totimestemp('2018-08-29 10:15:00','UTC-9:00')
print(t2)

assert t1==t2
