#출력 포멧팅

name = "이승민"
age = 17
print("나의 이름은",name,"이고 나이는",age,"입니다.")
#1
print("나의 이름은 %s이고 나이는 %d입니다."%(name,age))
#2
print("나의 이름은 {}이고 나이는{} 입니다.".format(name,age))
#3
print(f"나의 이름은 {name}이고 나이는{age} 입니다.")
print(f"{3.141592:0.4f}")


pi = 3.141592
print(format(pi,".3f"))