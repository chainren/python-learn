from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')

driver.get('http://www.baidu.com')
time.sleep(2)

# 新增一个标签页
driver.execute_script('window.open()')

time.sleep(2)

# 打印标签页
print(driver.window_handles)

# 切换至标签页1
driver.switch_to_window(driver.window_handles[1])

time.sleep(2)

# 在当前标签页访问知乎
driver.get('http://www.zhihu.com')
time.sleep(2)

# 切换至标签页0
driver.switch_to_window(driver.window_handles[0])

time.sleep(2)

# 在标签页0访问微博
driver.get('http://www.weibo.com')

time.sleep(2)

# 关闭
driver.close()

# 退出
driver.quit()