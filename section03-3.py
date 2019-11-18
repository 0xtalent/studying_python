# Section03-3
# 기본 스크랩핑 실습
# 다음 주식 정보 가져오기

import sys
import io
import json
import urllib.request as req
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# Fake Header 정보(가상으로 User-agent 생성)
ua = UserAgent()
# print(ua.ie)
# print(ua.msie)
# print(ua.chrome)
# print(ua.safari)
# print(ua.random)

# 헤더 정보
headers = {
    'User-agent': ua.ie,
    'referer' : "https://finance.daum.net"
}

# 다음 주식 요청 URL

url = "https://finance.daum.net/api/search/ranks?limit=10"

# 요청
res = req.urlopen(req.Request(url, headers=headers)).read().decode('UTF-8')

# 응답 데이터 확인(Json Data)
# print('res', res)

# 응답 데이터 str 문자열 -> json 변환 및 data 값 출력
rank_json = json.loads(res)['data']

# 중간 확인
print('중간 확인 : ', rank_json, '\n')

# 리스트로 넘어왔으니까 for문으로 반복가능
for elm in rank_json:
    print('순위 : {}, 금액 : {}, 회사명 : {}'.format(elm['rank'], elm['tradePrice'], elm['name']))

"""
와 내가!! 크롤링을 해오다니!!!
여러 get 방식 개념 등
urllib 선택자 등
공부 좀 더 하면
반복하면 개발자 될 수 있을 듯!!!
"""
