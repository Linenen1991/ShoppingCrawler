#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import urllib.parse

class Ruten:
    def __init__(self, keyword):
        self.keyword = keyword
        self.keywordinURL = urllib.parse.quote(self.keyword)
        self.url = 'https://www.ruten.com.tw/find/?cateid=0006&q=' + self.keywordinURL + '&sort=new%2Fdc'

    def Executor(self ,driver):
        wait = WebDriverWait(driver, 50)
        driver.get(self.url)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.site_loop > dd')))
        prod_list = driver.find_elements_by_css_selector('.site_loop > dd')
        for f in prod_list:
            print(f.find_element_by_class_name('price').text)

