import requests
from urllib import parse

# single quote 사용 불가, admin 키워드 사용 불가

host = "https://los.rubiya.kr/chall/troll_05b5eb65d94daf81c42dd44136cb0063.php?id="
cookies = {"PHPSESSID" : "8s7khiq67rue3qlsffsskni093"}
password_length = 0
s = requests.Session()

param = "ADMIN" # 대소문자 구분
