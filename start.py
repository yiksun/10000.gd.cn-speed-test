#!/usr/bin/env python
# coding: utf-8

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

try:
    driver = uc.Chrome(headless=False, use_subprocess=False)
    driver.implicitly_wait(15)
    driver.get('http://10000.gd.cn')
    print(driver.title)

    start = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH, "//div[contains(text(),' 测速 ')]")))  # 等待 测速 按钮出现
    start.click()
    driver.find_element(By.XPATH, "//*[@class='youxian']").click()  # 请选择网络环境: 有线
    driver.find_element(By.XPATH, "//*[@class='comfirmNet']").click()
    print('测速开始...')

    WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH, "//div[contains(text(),' 重测 ')]")))  # 等待 重测 按钮出现
    print('测速结束...')

    download_speed = driver.find_element(By.XPATH, "//p[contains(text(),' 下载/Mbps')]/following-sibling::p").text
    upload_speed = driver.find_element(By.XPATH, "//p[contains(text(),' 上传/Mbps')]/following-sibling::p").text
    print('下载/Mbps', download_speed)
    print('上传/Mbps', upload_speed)
except Exception as e:
    print(e)
finally:
    driver.quit()
    print('Driver closed...')
