#!/usr/bin/python3
from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.ruten.com.tw/find/?q=%e6%9e%97%e7%be%a9%e9%9b%84&sort=new%2Fdc');
driver.get('https://www.ruten.com.tw/find/?q=%E6%9D%8E%E6%80%A1%E5%9A%B4');
prod_list = driver.find_elements_by_css_selector('.site_loop > .isImpressTs')
print(prod_list);

for f in prod_list:
    print(f.find_element_by_class_name('price').text)
driver.close()
driver.quit() # close chrome
