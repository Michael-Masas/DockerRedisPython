import time
import selenium
from selenium import webdriver                          ##Import Web Driver Module for Web Automation
from selenium.webdriver.common.keys import Keys         ##Import Send Keys Module from selenium library

driver = webdriver.Chrome(executable_path='C:\ci_pipeline\chromedriver.exe')                                       #Define Web Driver Path
driver.get("http://127.0.0.1:5000")
time.sleep(30)

driver.quit()
