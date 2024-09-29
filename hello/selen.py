'''
Author: Bug Router
Date: 2024-09-29 10:00:54
Description: Default
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 初始化 WebDriver（记得替换路径）
driver = webdriver.Chrome()

try:
    # 打开百度首页
    driver.get("https://www.baidu.com")

    # 查找搜索框元素
    search_box = driver.find_element(By.ID, "kw")

    # 输入搜索内容
    search_box.send_keys("稀土掘进")

    # 提交搜索表单
    search_box.send_keys(Keys.RETURN)

    # 等待搜索结果加载
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "content_left"))
    )

    # 打印页面标题
    print("页面标题是:", driver.title)

finally:
    # 关闭浏览器
    driver.quit()