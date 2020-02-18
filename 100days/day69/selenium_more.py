from selenium import webdriver

from selenium.webdriver.common.by import By

# 设置无窗口
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')


# 申明浏览器对象
driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')

# 访问页面
driver.get('http://www.baidu.com')

# 通过id查找
element = driver.find_element_by_id('kw')
print(element)

# 通过name查找
element = driver.find_element_by_name('wd')
print(element.tag_name)

# 通xpath查找
element = driver.find_element_by_xpath('//*[@id="kw"]')
print(element.tag_name)


from selenium import webdriver
from selenium.webdriver.common.by import By

# 声明浏览器对象
driver = webdriver.Chrome()
# 访问页面
driver.get("http://www.baidu.com")

# 通过id查找
element = driver.find_element_by_id("kw")
print(element.tag_name)
# 通过name查找
element = driver.find_element_by_name("wd")
print(element.tag_name)
# 通过xpath查找
element = driver.find_element_by_xpath('//*[@id="kw"]')
print(element.tag_name)

# 通过另一种方式查找
element = driver.find_element(By.ID, "kw")
print(element.tag_name)

# 查找多个元素
elements = driver.find_elements(By.CLASS_NAME, 'mnav')
for e in elements:
    print(e.text)