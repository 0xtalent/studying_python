# Selenium 예제

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# Selenium 임포트하기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time

# Selenium 예제: python.org 사이트 오픈, input 필드를 검색하여 Key 이벤트 전달
chrome_driver = './webdriver/chrome/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver)

driver.get('https://www.python.org')

search = driver.find_element_by_id('id-search-field')

search.clear()
time.sleep(3)

search.send_keys('lambda')

time.sleep(3)
search.send_keys(Keys.RETURN)

time.sleep(3)

driver.close()
