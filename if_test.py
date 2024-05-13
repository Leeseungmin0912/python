#제어문 -조건문 if
'''

x = 10

if x:
    print("실행되었습니다.")




x = int(input("정수 하나를 입력하세요"))

if x %2 == 0:
    print("짝수입니다.")

else:
    print("홀수입니다.")


password = int(input("암호르르 문자로 입력하세요"))

if password =="까치":
    print("암호가 맞습니다")

else:
    print("암호가 틀렸습니다")
'''



# age가 15보다 크면 참을 출력하고 15보다 작으면 거짓을 출력하세요
age = 17

if age >= 15:
    print("참")

else:
    print("거짓")