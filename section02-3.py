# Section02-3
# 파이썬 크롤링 기초
# lmxl 사용 기초 스크랩(1)

import sys
import io
import requests
import lxml.html

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인함수
    """

    # 스크랩핑 대상 URL
    response = requests.get("https://www.naver.com") # Get방식, Post방식이 있다.

    # 신문사 링크 리스트 획득
    urls = scrape_news_list_page(response)

    # 결과 출력
    for url in urls:
        # url 출력
        print(url)
        # 파일 쓰기
        # 생략

def scrape_news_list_page(response):
    # URL 리스트 선언
    urls = []

    # 태크 정보 문자열 저장
    root = lxml.html.fromstring(response.content)

    for a in root.cssselect(""):
        pass

# 스크랩핑 시작
if __name__ == "__main__":
    main()
