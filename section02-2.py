# Section02-2
# 파이썬 크롤링 기초
# urlopen 함수 기초 사용법

import sys
import io
import urllib.request as req
from urllib.error import URLError, HTTPError

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 다운로드 경로 및 파일명

path_list = ["c:/test1.jpg", "c:/index.html"]

# 다운로드 리소스 url
target_url = ["https://pds.joins.com/news/component/htmlphoto_mmdata/201906/07/9c0ff00f-1c93-48bb-a73a-d1e202f5e4cb.jpg", "http://google.com"]

for i, url in enumerate(target_url):
# 이뉴머레이트를 붙여주면 인덱스를 붙여주고 리스트를 받는다.
    # 예외처리
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url)

        # 수신 내용
        contents = response.read()

        print("------------------------------------------")

        # 상태 정보 출력
        print('Header Info-{} : {}'.format(i, response.info()))
        print('HTTP Status Code: {}'.format(response.getcode()))
        print("------------------------------------------")

        with open(path_list[i], 'wb') as c:
            c.write(contents)

    except HTTPError as e:
        print("Download failed.")
        print("HTTPError code : ", e.code)
    except URLError as e:
        print("Download failed.")
        print("URL Error Reason : ". e.reason)

    # 성공
else:
    print()
    print("Download Succeed.")
