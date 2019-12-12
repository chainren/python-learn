"""
python datetime模块
"""

from datetime import datetime
import time


# 当前日期和时间
print(datetime.now())

# 获取指定时间
date_test = datetime(2019, 9, 30, 11, 30, 0)
print(date_test)


# 当前时间戳
print(time.time())

# sleep()

time.sleep(1000)
