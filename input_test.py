
#기본입출력 input() print()
name = input("이름을 입력하세요>>>") #키보드로부터 값을 입력
age = input("나이를 입력하세요>>>") #input()을 감싸는 형태로 int를 쓰면 str값이나 float값을 적었을 때 오류가 발생한다. ex) int(input("나이를 입력하세요 >>>"))
print(name)
print(age)

print("나의 이름은 "+name+" 이고,내 나이는 "+age+" 입니다")


#숫자 두 개를 입력 받아(변수명 a, b) 두수를 더하여 출력하세요.

a = input("첫번째 수:") #5
b = input("두번째 수:") #7

a = int(a)
b = int(b)
#위에나 아래처럼 하면 input값을 숫자로 바꿀 수 있다

a = int(input("숫자를 입력하세요>>>")) #변수 a에 숫자 하나를 받는다.
b = int(input("숫자를 입력하세요>>>")) #변수 b에 숫자 하나를 더 받는다.

#a에는 숫자 5를 b에는 숫자 7을 넣어주세요

print(a+b) #input을 한 a,b를 서로 더한다.

#input()함수는 모두 문자로 출력되고 인식된다.



#비만도 구하기
#비만도 = 몸무게 / (키의 제곱)*10000


height = int(input("키를 입력하세요. :"))/100
weight = int(input("몸무게를 입력하세요. :"))

BMI = weight / (height * height)
print("사용자의 BMI는",BMI,"입니다")

if BMI >= 30:
    print("고도비만입니다.")

elif BMI >= 25:
    print("비만입니다.")
elif BMI >= 23 and BMI < 25:
    print("과체중입니다.")
elif BMI >= 18.5 and BMI < 23:
    print("정상체중입니다.")
else:
    print("저체중입니다.")