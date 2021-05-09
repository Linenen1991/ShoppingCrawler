#!/usr/bin/python3
from selenium import webdriver
from WebSiteTemp import Ruten
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options,desired_capabilities=capa)

yisyong = Ruten('林義雄')
Ruten.Executor(yisyong,driver)


# print(driver.page_source)
driver.close()
driver.quit() # close chrome
