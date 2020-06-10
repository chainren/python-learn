from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')

driver.get('http://www.baidu.com')

time.sleep(2)

# 访问微博
driver.get('http://weibo.com')
time.sleep(2)

# 访问知乎
driver.get('http://www.zhihu.com')
time.sleep(2)

# 返回上个页面
driver.back()
time.sleep(2)

# 前进到下个页面
driver.forward()

# 退出
driver.close()