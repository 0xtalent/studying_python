# tranining01-4
# Selenium - 실전 웹 크롤링 연습문제 풀이

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# import
import requests
from bs4 import BeautifulSoup

# 뉴스 제목 크롤링
def get_daum_news_title(news_id):
    url = 'https://news.v.daum.net/v/{}'.format(news_id)
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text, 'html.parser')

    title_tag = soup.select_one('h3.tit_view')
    if title_tag:
        return title_tag.get_text()
    return ""

print(get_daum_news_title('20190728165812603'))
print(get_daum_news_title('20191121135937528'))

# 본문 내용 크롤링
def get_daum_news_content(news_id):
    url = 'https://news.v.daum.net/v/{}'.format(news_id)
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text, 'html.parser')

    content =''
    for p in soup.select('div#harmonyContainer p'):
        content += p.get_text()

    return content

print(get_daum_news_content('20190728165812603'))
print(get_daum_news_content('20191121135937528'))
