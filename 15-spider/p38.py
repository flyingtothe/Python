from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# 可能需要手动添加路径
driver = webdriver.Chrome()

url = 'http://www.baidu.com'

driver.get(url)

text = driver.find_element_by_id('wrapper').text
print(text)
print(driver.title)
# 得到页面的快照
driver.save_screenshot('index.png')

# id = 'kw' 是百度的输入框，得到输入框的 ui 元素后直接输入大熊猫
driver.find_element_by_id('kw').send_keys(u'大熊猫')

# id='su' 是百度的搜索按钮，click 模拟点击
driver.find_element_by_id('su').click()

time.sleep(5)
driver.save_screenshot('daxiongmao.png')

# 获取当前页面的 cookie
print(driver.get_cookies())

# 模拟输入两个按键 ctrl+a
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
# 模拟输入 ctr+x
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, "x")

driver.find_element_by_id('kw').send_keys(u'航空母舰')
driver.save_screenshot('hangmu.png')

driver.find_element_by_id('su').send_keys(Keys.CONTROL)

time.sleep(5)
driver.save_screenshot('hangmu2.png')

# 清空输入框
driver.find_element_by_id('kw').clear()
driver.save_screenshot('clear.png')

# 关闭浏览器
driver.quit()