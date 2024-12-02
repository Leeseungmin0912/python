#예외처리
#파일처리
#클래스

balance = 8000 #통장잔고

def deposit(money):
    global balance
    balance += money
    print(str(money) + '원 입금 완료되었습니다')

def inquire():
    print('잔액은 %d원입니다.' %balance)

deposit(2000)
inquire()

#클래스 변환
class Account: #클래스정의
    def __init__(self, balance): #생성자
        self.balance = balance

    def deposit(self, money): #입금매서드
        self.balance += money
        print(money,'입금 완료되었습니다.',money)
    def inquire(self): #잔액조회
        print('잔액은 %d원입니다'%self.balance)


kakao = Account(8000) #객체생성
kakao.deposit(3000)#입금 3000원
kakao.inquire()

toss = Account(100000)#계좌개설 잔액 10만원
toss.deposit(50000)#5만원입금
toss.inquire() 












#예외처리
'''
arr = [1,2,3]
print(arr[3]) #indexError

try:
    print(arr[2])
    print(arr[3]) #오류발생 이유 : 리스트변수 arr 에 3번지 값이 없어서 오류가 발생함
except:
    print('리스트 요소에 접근하지 못했습니다.')
    '''



i = 9
try:
    div = i/0
    print(div)#zeroDivision Error발생 예외처리하시오
except:
    print('오류발생!!! 윤후윤후버프!!!!!! 윤후윤후버프로 인해 컴퓨터가 종료됩니다')
