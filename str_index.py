#문자열 인덱싱
my = "저는 인평자동차고등학교 AI소프트웨어과 1학년 1반 이승민입니다"

school = my[3:12]#인평자동차고등학교
print(school)
print(my[1:15:2])
major = my[13:21]
print(major)


text = 'python programming'
print(text[7:11])
print(text[-7:-3])# -인덱싱
print(text[7:])#7번지부터 끝까지
print(text[:6])#처음부터 5-1번지까지 출력
s = text
print(s[-13:-19:-1])    
print(text[7::2])
print(text[:15:3])


major = "AI소프트웨어과"
print(major[3])
print(major[0:2])#0생략 가능
print(major[-9:-6])
print(major[2:8])
print(major[-9:-1])







#문자열함수
#   len 전체 글자수세기 count (특정 문자를 셀 수 있다.) len(전체 글자를 셀 수 있다.)
#내장함수   메소드     "."명령어()
print(len(major))
major = "AIsoftware!!!"
print(len(major))
print(major.count("!"))
print(major.upper()) #모두 대문자로 변경
print(major.lower()) #모두 소문자로 변경
print(major.replace("AI", "Happy AI")) #문자열 대체
print(major)
