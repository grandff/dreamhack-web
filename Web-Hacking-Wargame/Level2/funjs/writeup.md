# 개요
자바스크립트 난독화가 되어있는 소스에서 플래그 획득

# exploit
flag는 난독화가 안되어있고, debugger 삭제, move function 삭제 등을 통해 소스 확인을 할 수 있음.

종합해보자면..
1. input에는 총 36글자가 들어감
```javascript
if (flag[_0x374fd6(0x17c)] != 0x24) {   
    text2img(_0x374fd6(0x185));            
    return;
}
```
> 해당 소스 로그를 찍어보면 input값이 36글자인지 확인하고 아니면 return을 함

2. flag 입력값이 실제 flag값인지 비교함
```javascript
for (var i = 0x0; i < flag[_0x374fd6(0x17c)]; i++) {    
    if (flag[_0x374fd6(0x176)](i) == operator[i % operator[_0x374fd6(0x17c)]](_0x4949[i], _0x42931[i])) {

    } else {
        text2img(_0x374fd6(0x185));
        return;
    }
}
text2img(flag);
```
> _0x374fd6(0x176)은 charCodeAt
> flag[_0x374fd6(0x176)](i)는 i번째 인덱스에 들어간 문자의 아스키코드임
> operator[i % operator[_0x374fd6(0x17c)]](_0x4949[i], _0x42931[i])는 flag의 i번째 아스키코드값임
> 따라서 0~35 반복문을 돌면서 입력한 flag값이 flag와 일치하는지 아스키코드로 비교함

3. 아래의 코드로 flag를 구한 후 dreamhack tools로 (From Decimal) flag 획득
```javascript
let fullCode = "";
for (var i = 0x0; i < flag[_0x374fd6(0x17c)]; i++) {
    fullCode += operator[i % operator[_0x374fd6(0x17c)]](_0x4949[i], _0x42931[i]) + ",";
}
console.log(fullCode)
```