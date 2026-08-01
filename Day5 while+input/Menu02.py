menu=5
while True:
    menu=int(input("번호를 입력해주세요."))
    if menu ==1:
        print("게임 시작")
    elif menu ==2:
        print("설정")
    elif menu ==3:
        print("종료")
        break
    else:
        print("1~3번중에서 입력해주세요")