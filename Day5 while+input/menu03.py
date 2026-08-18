cash = 10000
def balance():
    return cash
def deposit(money_in):
    global cash
    cash=cash+money_in
    print(f"고객님의 현재 입금 후 잔액은 {cash}원 입니다.")
def withdrow(money_out):
    global cash
    if cash >= money_out:
        cash=cash-money_out
        print(f"고객님의 현재 출금 후 잔액은 {cash}원 입니다.")
    else:
        print("잔액이 부족합니다")
    
def menu():
    print("1. 잔액 조회")
    print("2. 입금")
    print("3. 출금")
    print("4. 종료")
while True:
    menu()
    menu_num=int(input("원하시는 서비스의 번호를 입력해주세요."))
    if menu_num==1:
        current_balance =balance()
        if current_balance >= 100000:
            print("잔액이 충분합니다.")
        else:
            print("잔액이 부족합니다.")
    elif menu_num==2:
        money_in=int(input("입금하실 금액을 입력해주세요."))
        deposit(money_in)
    elif menu_num==3:
        money_out=int(input("출금 하실 금액을 입력해주세요."))
        withdrow(money_out)
    elif menu_num==4:
        break

