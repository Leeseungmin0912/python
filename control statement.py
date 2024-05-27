#제어문  - 조건문

#홀짝 판별

print('정수를 입력하세요 >>>')
number = int(input())

if number %2 == 0: #짝수
    print(f'{number}은/는 짝수입니다')

else: #홀수
    print(f'{number}은/는 홀수입니다')


#키보드로부터 점수를 입력받아 60점 넘으면 합격 60점 미만이면 불합격 출력
print('점수를 입력하세요 >>>')
score = int(input())


if score >= 60:
    print('합격입니다')
else:
    print('불합격입니다.')



#열날때 행동 요령

temp = float(input('체온을 입력하세요 >>>'))

if temp >= 40:
    print(f'{temp}는 고열입니다 당장 병원가세요')

elif temp >= 38:
    print(f'{temp}는 미열입니다 해열제 먹고 병원으로 가세요')

elif 37 >= temp > 36:
    print(f'{temp}는 미열입니다. 학교에가서 보건선생님은 만나주세요')

else:
    print(f'{temp}는 정상체온입니다 학교로 가세요')



#학점 판별

print('점수를 입력해주세요')

score = int(input())

if score >= 90:
    print(f'{score}의 점수를 받으셨기에 A입니다.')

elif score >= 80:
    print(f'{score}의 점수를 받으셨기에 B입니다.')

elif score >= 70:
    print(f'{score}의 점수를 받으셨기에 C입니다.')

if score >= 60:
    print(f'{score}의 점수를 받으셨기에 D입니다.')

else:
    print(f'{score}의 점수를 받으셨기에 E입니다.')
