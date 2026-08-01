print("========================")
print("1. 잔액 조회")
print("2. 입 금")
print("3. 출 금")
print("4. 종 료 ")
print("========================")
cash=10000
while True:
    menu=int(input("원하시는 작업을 입력 해주세요."))
    if menu == 1:
        print("잔액 조회 입니다.")
        print(f"고객님의 현재 잔액은 {cash} 입니다")
    elif menu ==2:
        print("입금 하시겠습니까.?")
        money_in=int(input("입금하실 금액을 입금 해주세요"))
        cash=cash+money_in
        print(f"고객님의 현재 잔액은 {cash}원 입니다.")
    elif menu ==3:
        print("출금 하시겠습니까.?" )
        money_out=int(input("출금하실 금액을 입력 해주세요."))
        if cash >= money_out:
            cash=cash-money_out
        else:
            print("잔액이 부족합니다.")
        print(f"고객님의 현재 잔액은 {cash}원 입니다.")
    elif menu ==4:
        print("종 료")
        break

