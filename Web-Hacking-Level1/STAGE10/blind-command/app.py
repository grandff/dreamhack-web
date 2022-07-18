'''
solution..!
- GET은 안되지만 HEAD는 GET과 동일하게 동작함
- HEAD를 통해서 풀어나가야할거 같은 느낌이 듬....
- 문제는 HEAD는 그게 안됨 출력이
- 그래서 HEAD를 통해 다른 쪽으로 요청하거나 하는 방식으로..?
1안) curl를 이용해서 데이터를 준다?? -> 근데 이게 어디 있는줄ㅇ ㅏㄹ고
2안) vi를 통해 파일을 생성한다?? -> 풀 명령어를 모름..
'''
#!/usr/bin/env python3
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/' , methods=['GET'])
def index():
    cmd = request.args.get('cmd', '')
    result = request.args.get('result', '')
    print(result)
    if not cmd:
        return "?cmd=[cmd]"

    if request.method == 'GET':
        ''
    else:
        print(cmd)
        os.system(cmd)
        print(os.system(cmd))        
    return cmd

app.run(host='0.0.0.0', port=8000)