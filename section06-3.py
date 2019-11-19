# Section06-3
# Selenium
# Selenium 사용 실습(3) - 실습 프로젝트(2)

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

WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="selectMaker_simple_priceCompare_A"]/li[14]/label'))).click()

# 2초간 대기
time.sleep(2)

# 현재 페이지
cur_page = 1

# 크롤링 페이지 수
target_crawl_num = 5

while cur_page <= target_crawl_num:

    # bs4 초기화
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    # # 소스코드 정리
    # print(soup.prettify())

    # 메인 상품 리스트 선택
    pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')

    # 상품 리스트 확인

    # print(pro_list)

    # 페이지 번호 출력
    print('****** Current Page : {}'.format(cur_page), '******')
    print()

    # 필요 정보 추출하기
    for v in pro_list:
        # 임시 출력
        # print(v)

        if not v.find('div', class_="ad_header"):

            # 없는거 상품명, 이미지, 가격 출력해주자
            print(v.select('p.prod_name > a')[0].text.strip())
            print(v.select('a.thumb_link > img')[0]['data-original'])
            print(v.select('p.price_sect > a')[0].text.strip())

            # 이 부분에서 엑셀 저장(파일, DB 등)
            # CODE
            # CODE

        print()
    print()

    # 페이지 별 스크린 샷 저장하기
    browser.save_screenshot('c:/target_page{}.png'.format(cur_page))

    # 페이지 증가
    cur_page += 1

    if cur_page > target_crawl_num:
        print('Crawling Succeed!!')
        break

    # 페이지 이동 클릭 소스 추가
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.number_wrap > a:nth-child({})'.format(cur_page)))).click()

    # BeautifulSoup 인스턴스 삭제
    del soup

    # 3초간 대기
    time.sleep(3)


# 브라우저 종료해주기
browser.close()
