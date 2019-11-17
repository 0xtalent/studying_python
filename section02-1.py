# Section02-1
# 파이썬 크롤링 기초
# urllib 사용법 및 기본 스크랩핑

import urllib.request as req

# 파일 URL
img_url = 'https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/2B1N/image/DyrMt3lhvhnF9zBTCc0-un5IOJo.jpg'
html_url = 'http://google.com'

# 다운받을 경로 지정
save_path1 = 'c:/test1.jpg'
save_path2 = 'c:/index.html'

# 예외 처리
try:
    # urlretrieve 함수는 리턴값이 2개
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('Download failed')
    print(e)
else:
    # Header 정보 출력
    print(header1)
    print(header2)

    # 다운로드 파일 정보
    print('Filename1 {}'.format(file1))
    print('Filename2 {}'.format(file2))
    print()

    # 성공
    print('Download succeed')
