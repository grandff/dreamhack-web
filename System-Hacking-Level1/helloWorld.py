quiz = [116, 66, 85, 81, 93, 120, 81, 83, 91]
for i in range(len(quiz)):
    quiz[i] ^= 0x30 # 연산자의 왼쪽 값에서 오른쪽 값을 비트 배타적 논리곱 한 값을 왼쪽에 할당한다. ? 
    print(quiz[i])
quiz = ''.join([chr(_) for _ in quiz])
print(quiz)
answer = input()
if answer == quiz:
    print("Welcome Hackers :)")
else:
    print("No No :/")