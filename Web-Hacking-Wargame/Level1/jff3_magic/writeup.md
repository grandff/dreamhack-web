# Solution..!
- form submit을 할 경우 하단에 hash값이 나오는데, haval 128,5 해시임...?
- get 방식에 no를 0으로 주면 admin 계정 화면으로 들어감
    - no를 이용한 injection 문제
- 어지간한 인젝션은 다 막혀있는데 or은 열려 있음
- no=5 || length(pw) = 32 를 통해 true일 경우 admin을 리턴, false일 경우 빈값이 리턴되는걸 확인할 수 있음
    - password 길이는 32인걸 확인

- like와 char를 사용해서 pw 를 찾아내는 인젝션 수행

- 비밀번호를 보면 0e로 시작하는데, magic hash로 되어있어서 그대로 입력하면 안됨..
- magic hash가 모여있는 사이트에서 32글자 짜리 암호화 해시를 모두 찾아내 하나씩 넣는 방식으로 진행..
- 115528287