# Section04-3
# Requests
# Requests 사용 스크랩핑(3) - Rest API
# Rest API : GET, POST, DELETE, PUT: UPDATE, REPLACE(FETCH: UPDATE, MODIFY)
# 중요: 왜 쓰냐? url을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미
# /movies : 영화를 전부 조회
#

import sys
import io
import requests
import json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 세션 활성화

s = requests.Session()

# 예제1
r = s.get('https://api.github.com/events')

# 수신상태 체크
r.raise_for_status()

# 출력
print(r.text)

# 예제2
# 쿠키설정
jar = requests.cookies.RequestsCookieJar()
# 쿠키 삽입
jar.set('name', 'niceman', domain='httpbin.org', path='/cookies')

# 요청
r = s.get('http://httpbin.org/cookies', cookies=jar)

# 출력
print(r.text)

# 예제3
r = s.get('https://github.com', timeout=5)

# 출력
print(r.text)

# 예제4
r = s.post('http://httpbin.org/post', data={'id':'test77', 'pw': '111'}, cookies=jar)

# 출력
print(r.text)
print(r.headers)

# 예제5
# 요청(POST)
payload1 = {'id':'test77', 'pw': '111'}
payload2 = (('id', 'test77'), ('pw', '111'))

r = s.post('http://httpbin.org/post', data=payload1)

# 출력
print(r.text)

# 예제6(PUT)

r= s.put('http://httpbin.org/put', data=payload1)

print(r.text)

# 예제7(DELETE)
r = s.delete('http://httpbin.org/delete', data={'id' : 1})

print(r.text)

r = s.delete('http://jsonplaceholder.typicode.com/posts/1')

print(r.text)

s.close()
