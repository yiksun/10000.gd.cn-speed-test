#!/usr/bin/env python
# coding: utf-8

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = uc.Chrome(headless=False, use_subprocess=False)
driver.implicitly_wait(15)
wait = WebDriverWait(driver, 60)
driver.get('http://speed.neu.edu.cn/')
print(driver.title)

driver.find_element(By.ID, 'startStopBtn').click()
print('测速开始')

wait.until_not(ec.element_to_be_clickable((By.CLASS_NAME, "running")))  # 等待测速结束
print('测速结束')

download_desc = driver.find_element(By.XPATH, '//div[@class="testGroup"][1]/div[@class="testArea"][1]/div[1]').text
download_speed = driver.find_element(By.XPATH, '//div[@class="testGroup"][1]/div[@class="testArea"][1]/div[2]').text
download_unit = driver.find_element(By.XPATH, '//div[@class="testGroup"][1]/div[@class="testArea"][1]/div[3]').text
print('{}: {} {}'.format(download_desc, download_speed, download_unit))

upload_desc = driver.find_element(By.XPATH, '//div[@class="testGroup"][1]/div[@class="testArea"][2]/div[1]').text
upload_speed = driver.find_element(By.XPATH, '//div[@class="testGroup"][1]/div[@class="testArea"][2]/div[2]').text
upload_unit = driver.find_element(By.XPATH, '//div[@class="testGroup"][1]/div[@class="testArea"][2]/div[3]').text
print('{}: {} {}'.format(upload_desc, upload_speed, upload_unit))

driver.quit()
