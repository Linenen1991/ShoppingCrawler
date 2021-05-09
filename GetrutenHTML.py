#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options,desired_capabilities=capa)
wait = WebDriverWait(driver, 50)


driver.get('https://www.ruten.com.tw/find/?q=%E6%9D%8E%E6%80%A1%E5%9A%B4');

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.site_loop > dd')))

prod_list = driver.find_elements_by_css_selector('.site_loop > dd')
print(prod_list);

for f in prod_list:
    print(f.find_element_by_class_name('price').text)


print(driver.page_source)
driver.close()
driver.quit() # close chrome
