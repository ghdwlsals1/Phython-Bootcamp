cash = 10000
def balance():
    print(f"고객님의 현재 잔액은 {cash}원 입니다")
def deposit():
    global cash
    money_in=int(input("입금하실 금액을 입력해주세요."))
    cash=cash+money_in
    print(f"고객님의 현재 입금 후에 잔액은 {cash}원 입니다.")
def withdrow():
    print(f"고객님의 현재 출금 후에 잔액은 {cash}원 입니다.")
def menu():
    print("1. 잔액 조회")
    print("2. 입금")
    print("3. 출금")
    print("4. 종료")
while True:
    menu()
    menu_num=int(input("원하시는 서비스의 번호를 입력해주세요."))
    if menu_num==1:
        balance()
    elif menu_num==2:
        deposit()
    elif menu_num==3:
        withdrow()
    elif menu_num==4:
        break

