# tranining01-2
# Selenium 예제2

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

url = 'https://news.v.daum.net/v/20190728165812603'
# chrome driver 로 해당 페이지가 물리적으로 open
driver.get(url)

src = driver.page_source

soup = BeautifulSoup(src, 'html.parser')
comment = soup.select_one('span.alex-count-area')

print(comment.get_text())
