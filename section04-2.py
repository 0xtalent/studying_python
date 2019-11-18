# Section04-1
# Requests
# Requests 사용 스크랩핑(2) - JSON 형식

import sys
import io
import requests
import json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 세션 열기
s = requests.Session()

# 100개 JSON 데이터 요청하기
r = s.get('http://httpbin.org/stream/100', stream=True) # True로 주면 직렬화해서 가져옴

# 수신 확인
print(r.text)

# Encoding 확인
print('Before Encoding : {}'.format(r.encoding))

if r.encoding is None:
    r.encoding = 'UTF-8'

print('After Encoding : {}'.format(r.encoding))

for line in r.iter_lines(decode_unicode=True):
    # 라인 출력 후 타입 확인
    # print(line)
    # print(type(line))

    # JSON을 딕셔너리 형식으로 변환 후 확인하기
    b = json.loads(line) # str -> dict
    print(b)
    print(type(b))

    # 정보 내용 출력
    for k, v in b.items():
        print("key : {}, Value : {}".format(k, v))

    print()
    print()

s.close()

# 한번 더!
r = s.get('https://jsonplaceholder.typicode.com/todos/1')

# Header 정보
print(r.headers)

# 본문 정보
print(r.text)

# JSON 변환
print(r.json())

# key 반환
print(r.json().keys())
print(r.json().values())

# 인코딩 반환
print(r.encoding)

# 바이너리 정보 확인
print(r.content)

s.close()
