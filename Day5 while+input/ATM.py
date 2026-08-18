print("============================")
print("1. 입 금")
print("2. 출 금")
print("3. 잔액 조회")
print("============================")
cash=10000
def balance():
        global cash
        return cash
def deposit(money_in):
        global cash
        cash=cash+money_in
        return cash
def withdraw(money_out):
        global cash
        cash=cash-money_out
        return cash
while True:
    menu_num=int(input("원하시는 서비스를 입력해주세요.:"))
    if menu_num == 1:
        money_in =int(input("입금하실 금액을 입력해주세요.:"))
        deposit(money_in)
        print(f"고객님의 입금 후 잔액은 {cash}원 입니다.")
    elif menu_num == 2:
        money_out=int(input("출금하실 금액을 입력해주세요.:"))
        if cash < money_out:
            print("잔액이 부족합니다")
        else:
            withdraw(money_out)
            print(f"고객님의 출금 후 잔액은 {cash}원 입니다.")
    elif menu_num == 3:
        print(f"고객님의 현재 잔액은 {cash}원 입니다.")




