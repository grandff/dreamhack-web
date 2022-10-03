# 개요
escapeshellcmd 함수와 curl에 대해서 잘 알고 있어야함.

# 코드분석
escapeshellcmd 함수에서는 ‘-' 문자에 '\’ 문자를 추가하지 않으므로 curl 명령어의 “-o” 옵션을 사용해 임의 디렉터리에 파일을 생성할 수 있는 취약점이 있음

# 참고
[dream hack Command Injection Advanced](https://learn.dreamhack.io/310#9)
