'''
solution..!
- 대소문자 구분을 안하고 필터링을 걸었음
- mysql에서 대소문자 구분을 안함
- 그냥 쉽게 GUEST를 대문자로 보내면 됨
'''

import requests
from urllib import parse


host = "http://host3.dreamhack.games:13632/"  # target url
data = {"id" : "GUEST", "ps" : "guest"}

r = requests.post(host, data=data) 
print(r.text)