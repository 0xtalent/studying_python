# Section06-2
# Selenium
# Selenium 사용 실습(2) - 실습 프로젝트(1)

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# Selenium 임포트하기
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")

# webdriver 설정(Chrome, Firefox 등) - Headless 모드로 작동(브라우저 안뜸)
# browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe', options=chrome_options)

# 일반 모드
browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe')


# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# 브라우저 사이즈 조절해주기
browser.set_window_size(1920, 1280) # maximize_window(), minimize_window()

# 페이지 이동
browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

# 1차 페이지 내용
# print('Before Page Contents : {}'.format(browser.page_source))

# 제조사별 더보기 페이지 클릭1
# Explicity wait

WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()

# # 제조사별 더보기 페이지 클릭2
# # implicitly wait
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()
