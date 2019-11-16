import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = 'http://www.encar.com'

mem = req.urlopen(url)

# print(type(mem))
print(type({}))
print(type([]))
print(type(()))
