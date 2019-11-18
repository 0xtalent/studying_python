# Section05-2
# BeautifulSoup
# BeautifulSoup 사용 스크랩핑(2) - 이미지 다운로드

import sys
import io
import os
import urllib.parse as rep
import urllib.request as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# Header 정보
opener = req.build_opener()
# User-Agent 정보 싣어주기
opener.addheaders = [('User-agent', UserAgent().ie)]
# header 정보 삽입
req.install_opener(opener)

# 네이버 이미지 기본 URL(크롬 개발자 도구 활용)
base = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='

# 검색어
quote = rep.quote_plus('펭수')

# URL 완성
url = base + quote

# 요청 URL 확인
print('Request URL : {}'.format(url))

# Request
res = req.urlopen(url)
# print(res)

# 이미지 저장 경로
savePath = "c:/imagedown/" # \\도 가능

# 폴더 생성 예외 처리(문제 발생 시 프로그램 종료)
try:
    # 기본 폴더가 있는지 체크하기
    if not (os.path.isdir(savePath)):
        # 없으면 폴더 생성
        os.makedirs(os.path.join(savePath))
except OSError as e:
    # 에러가 나면 에러 내용 출력
    print("folder creating failed!!")
    print("forder name : {}".format(e.filename))

    # 런타임 에러
    raise RuntimeError("시스템이 종료됩니다!!!")
else:
    # 폴더 생성이 되었거나, 존재할 경우
    print("Folder가 만들어졌어요~!!!")

# bs4 초기화
soup = BeautifulSoup(res, "html.parser")

# print(soup.prettify())

# select 사용하기
img_list = soup.select('div.img_area > a.thumb._thumb > img')

# finde_all을 사용할 경우
# img_list2 = soup.find_all("a", class_="thumb _thumb")
#
# for v in img_list2:
#     img_t = v.find('img')
#     print(img_t.attrs['data-source'])
#     req.urlretrieve(img_t.attrs['data-source'], fullFileName)

# print(img_list)

for i, img in enumerate(img_list, 1):
    # 속성 확인
    # print(img["data-source"], i)

    # 저장 파일명 및 경로 만들어주기
    fullFileName = os.path.join(savePath, savePath + str(i) + '.png')

    # 파일명 출력
    print(fullFileName)

    # 다운로드 요청(url, 다운로드 경로)
    req.urlretrieve(img['data-source'], fullFileName)
    # 다운로드와 동시에 저장할 수 있는거 urlretrieve

# 다운로드 완료 시 출력
print("다운로드가 완료 되었어요!! 펭펭~")

"""
진짜 어마어마하다
이미지를 이렇게 빨리 다운 받을 수 있다니
머신러닝 딥러닝은 세상을 얼마나 더 효율적으로 빠르게 멋지게 바꿀지 상상이 안간다.
경제, 사회, 문화 전반에 걸쳐 패러다임 체인지를 가져올 것 같다.
정말 열심히 공부하자
딥러닝, 머신러닝, 사이버 전쟁 등등
미친듯이 인강 듣기
의대생처럼 공부하기
정말 열심히 인강 들으며 공부해보자
"""
