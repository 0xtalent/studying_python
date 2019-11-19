# Section06-1
# Selenium
# Selenium 사용 실습(1) - 설정 및 기본 테스트

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# selenium 임포트하기
from selenium import webdriver

# webdriver 성정(Chrome, Firefox 등 다 됨)
browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# 속성 확인하기
print(dir(browser))

# 브라우저 사이즈 지정하기
browser.set_window_size(1920, 1280) # maximize_window(), minimize_window()

# 페이지 이동
browser.get('https://www.daum.net')

# 페이지 내용 가져오기
print('Page Contencts : {}'.format(browser.page_source))

print()

# 세션 값 출력해보기
print('Session ID : {}'.format(browser.session_id))

# 타이틀 출력
print('Title : {}'.format(browser.title))

# 현재 URL 출력
print('URL : {}'.format(browser.current_url))

# 현재 쿠키 정보 출력
print('Cookies : {}'.format(browser.get_cookies()))

# 검색창 input 선택
element = browser.find_element_by_css_selector('div.inner_search > input.tf_keyword')

# 검색어 입력
element.send_keys('펭수')

# 검색: 엔터 쳐주는 작업(Form Submit)
element.submit()
