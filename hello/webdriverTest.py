'''
Author: Bug Router
Date: 2024-09-27 10:30:22
Description: Default
'''
from selenium import webdriver

# 创建 Chrome 浏览器驱动对象
driver = webdriver.Chrome()

# 打开百度页面
driver.get('https://www.baidu.com')

# 可以添加一些延迟，以便观察页面加载情况
import time
time.sleep(5)

# 关闭浏览器
driver.quit()