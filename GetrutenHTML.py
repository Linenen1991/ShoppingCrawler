#!/usr/bin/python3
from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.ruten.com.tw/find/?q=%E6%9D%8E%E6%80%A1%E5%9A%B4');
prod_list = driver.find_elements_by_css_selector('.site_loop > dd')
print(prod_list);

for f in prod_list:
    print(f.find_element_by_class_name('price').text)

driver.close()
driver.quit() # close chrome
