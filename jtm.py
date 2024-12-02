#회원가입 사이트

print("사이트에 오신 것을 환영합니다",end="")
print("회원가입을 진행하시겠습니까?",end="")

print("1. 회원가입")
print("2. 로그인")
print("3. 회원 정보 찾기")
print("4. 회원 탈퇴")

q = 1 #회원가입
w = 2 #로그인
e = 3 #회원 정보 찾기
r = 4 #회원 탈퇴
gaeip = int(input())  #가입 함수

if gaeip == 1:
    print("회원가입을 시작합니다")

    print("개인정보 이용 동의를 하십니까?")

    yes = 1
    no = 2

    dong = int(input()) #동의 함수

    if dong == 1:
        print("동의하셨습니다. 회원가입을 진행합니다")

        print("사용자의 이름을 입력해주세요")
        name = input()

        print("사용자의 나이를 입력해주세요")
        age = input()

        print("사용자의 전화번호를 '-' 빼고 입력해주세요")
        phone_number = input()

        print("사용자가 이용하는 통신사를 적어주세요")
        togsin = input()

        print("사용자가 입력한 정보가 맞는지 확인하겠습니다")

        print(name, age,"살",phone_number,togsin,"이 맞으십니까?")

        yes1 = 1
        no1 = 2

        right1 = int(input)

        if right1 == 1:
            print("확인되었습니다")
            print("사용자가 사용할 아이디를 입력해주세요")

            id = input()

            print("사용자가 사용할 비밀번호를 적어주세요")

            pw = input()

            print("방금 입력한 비밀번호를 다시 입력해주세요")

            pw1 = input

            if pw == pw1:
                print("확인되었습니다.")

            print("사용자가 실사용하고있는 이메일을 입력하세요")

            email = input()

            print("회원가입이 완료되었습니다.")

        if right1 == 2:
            print("틀린 부분을 다시 입력해주세요")

            print("사용자의 이름을 입력해주세요")
        name1 = input()

        print("사용자의 나이를 입력해주세요")
        age1 = input()

        print("사용자의 전화번호를 '-' 빼고 입력해주세요")
        phone_number1 = input()

        print("사용자가 이용하는 통신사를 적어주세요")
        togsin1 = input()

        print("사용자가 입력한 정보가 맞는지 확인하겠습니다")

        print(name1, age1,"살",phone_number1,togsin1,"이 맞으십니까?")


    if dong == 2:
        print("동의하지 않으셨습니다. 회원가입 진행을 하실 수 없습니다") 

        print("개인정보이용을 동의하시겠습니까?")

        yes3 = 1
        no3 = 2

        dong3 = int(input)

        if dong3 == 1:
            print("동의해주셔서 감사합니다. 회원가입을 시작합니다.")

            print("사용자의 이름을 입력해주세요")
        name = input()

        print("사용자의 나이를 입력해주세요")
        age = input()

        print("사용자의 전화번호를 '-' 빼고 입력해주세요")
        phone_number = input()

        print("사용자가 이용하는 통신사를 적어주세요")
        togsin = input()

        print("사용자가 입력한 정보가 맞는지 확인하겠습니다")

        print(name, age,"살",phone_number,togsin,"이 맞으십니까?")

        yes1 = 1
        no1 = 2

        right1 = int(input)

        if right1 == 1:
            print("확인되었습니다")
            print("사용자가 사용할 아이디를 입력해주세요")

            id = input()

            print("사용자가 사용할 비밀번호를 적어주세요")

            pw = input()

            print("방금 입력한 비밀번호를 다시 입력해주세요")

            pw1 = input

            if pw == pw1:
                print("확인되었습니다.")

            print("사용자가 실사용하고있는 이메일을 입력하세요")

            email = input()

            print("회원가입이 완료되었습니다.")

        if right1 == 2:
            print("틀린 부분을 다시 입력해주세요")

            print("사용자의 이름을 입력해주세요")
        name1 = input()

        print("사용자의 나이를 입력해주세요")
        age1 = input()

        print("사용자의 전화번호를 '-' 빼고 입력해주세요")
        phone_number1 = input()

        print("사용자가 이용하는 통신사를 적어주세요")
        togsin1 = input()

        print("사용자가 입력한 정보가 맞는지 확인하겠습니다")

        print(name1, age1,"살",phone_number1,togsin1,"이 맞으십니까?")

        if dong3 == 2:
            print("동의를 안하시면 회원가입이 불가능 합니다")

            print("회원가입을 종료합니다.")

if gaeip == 2:
    print("로그인 합니다.")

    print("id를 입력해주세요")

    id = input()

    print("비밀번호를 입력해주세요")

    pw = input()

    print("로그인 완료")


if gaeip == 3:
    print("회원 정보를 찾습니다.")


    print("회원 정보를 찾으시겠습니까?")


    yes = 1
    no = 2

    gug = int(input())

    if gug == 1:
        print("사용자의 이름을 알려주세요")

        name = input()

        print("이름이 똑같은 사용자를 찾는중입니다.")

        print("사용자의 나이를 입력하세요")

        age = int(input())

        print("사용자와 나이가 같은 사용자를 찾는중입니다..")

        print("사용자와 일치한 사용자를 찾았습니다 확인차 전화번호를 입력해주세요")

        phone_number  = input()

        if phone_number == "010-0000-0000":
            print("사용자의 아이디는 ~~~~입니다")

            print("사용자의 비밀번호도 찾으시겠습니까?")

            

            yes = 1
            no = 2

            find_pw = int(input())

            if find_pw == 1:
                print("사용자의 비밀번호를 찾겠습니다.")

                print("사용자의 이름을 알려주세요")

        name = input()

        print("이름이 똑같은 사용자를 찾는중입니다.")

        print("사용자의 나이를 입력하세요")

        age = int(input())

        print("사용자와 나이가 같은 사용자를 찾는중입니다..")

        print("사용자와 일치한 사용자를 찾았습니다 확인차 전화번호를 입력해주세요")


if gaeip == 4:
    print("회원 탈퇴를 진행합니다.")
