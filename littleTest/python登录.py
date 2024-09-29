from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 创建 WebDriver 实例
driver = webdriver.Chrome()

# 打开目标网站
driver.get('url')

# 等待表单加载完成，可以根据实际情况调整等待条件
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'form')))

# 通过 name 属性定位输入框和提交按钮等元素
username_input = driver.find_element(By.CSS_SELECTOR, '.form input[placeholder="请输入用户名/手机号"]')
password_input = driver.find_element(By.CSS_SELECTOR, '.form input[placeholder="请输入密码"]')
submit_button = driver.find_element(By.CSS_SELECTOR, 'div[class="btn"]')

# 输入用户名和密码并点击提交按钮
username_input.send_keys('***')
password_input.send_keys('***')
submit_button.click()

# 等待登录后的页面加载完成或进行其他验证操作
# 可以添加一些延迟，以便观察页面加载情况
time.sleep(500)

# 关闭浏览器
driver.quit()