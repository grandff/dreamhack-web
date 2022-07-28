'''
solution..!
- 입력값에 대한 어떠한 검증도 하지 않으므로 참과 거짓을 확인할 수 있는 구문으로 테스트
    - ' or 1=1 limit 0,1 -- - 과 ' or 1=2 limit 0,1 -- - 
    - limit 0,1은 row가 1인 조건이 있으므로 만족시키기 위해서임
- 참인지 거짓인지 확인할 수 있으면 아래의 순서대로 익스플로잇을 설계
    1. admin 패스워드 길이 찾기
    2. 각 문자별 비트열 길이 찾기
    3. 각 문자별 비트열 추출
    4. 비트열을 문자로 변환(각 문자의 인코딩은 utf-8)
        - 비트열을 정수로 변환 -> 정수를 Big Endian 형태의 문자로 변환 -> 변환된 문자를 인코딩에 맞게 변환
- python의 request 사용
- 거의 write up 보고 했기 때문에 연관 문제 한번 풀어보기
'''
import os
from flask import Flask, request, render_template_string
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'user')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'pass')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'user_db')
mysql = MySQL(app)

template ='''
<pre style="font-size:200%">SELECT * FROM users WHERE uid='{{uid}}';</pre><hr/>
<form>
    <input tyupe='text' name='uid' placeholder='uid'>
    <input type='submit' value='submit'>
</form>
{% if nrows == 1%}
    <pre style="font-size:150%">user "{{uid}}" exists.</pre>
{% endif %}
'''

@app.route('/', methods=['GET'])
def index():
    uid = request.args.get('uid', '')
    nrows = 0

    if uid:
        cur = mysql.connection.cursor()
        nrows = cur.execute(f"SELECT * FROM users WHERE uid='{uid}';")

    return render_template_string(template, uid=uid, nrows=nrows)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
