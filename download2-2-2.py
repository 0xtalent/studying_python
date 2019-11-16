import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = 'https://dimg.donga.com/wps/NEWS/IMAGE/2018/11/28/93062428.6.jpg'
htmlURL = 'http://google.com'

savePath1 = 'c:/test1.jpg'
savePath2 = "c:/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1, 'wb') # w : write, r : read, a : add
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료!")

"""
urlretrieve:
저장 -> open('r') -> 변수에 할당 -> 파싱 -> 저장

urlopen:
변수 할당 -> 파싱 -> 저장(db...)
"""
