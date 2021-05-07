#!/usr/bin/python3
from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.ruten.com.tw/find/?q=%e6%9e%97%e7%be%a9%e9%9b%84&sort=new%2Fdc');
driver.get('https://www.google.com');

try:
    cmd=input('Enter your command\n')
    while cmd != 'Q':
        eval(cmd)
        cmd = input('Enter your command\n')
finally:
    driver.close()
