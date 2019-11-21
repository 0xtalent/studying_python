# tranining01-3
# Selenium 예제3

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

url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=081&aid=0003018031'
# chrome driver 로 해당 페이지가 물리적으로 open
driver.get(url)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.u_cbox_count')))

src = driver.page_source

soup = BeautifulSoup(src, 'html.parser')

driver.close()

comment = soup.select_one('span.u_cbox_count')

print(comment.get_text())
