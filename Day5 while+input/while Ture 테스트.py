even_numbers=[]
odd_numbers=[]
while True:
    answer=int(input("숫자를 입력해주세요."))
    if answer==0:
        break
    if answer % 2==0:
        print("짝수입니다:",answer)
        even_numbers.append(answer)
    else:
        print("홀수입니다:",answer)
        odd_numbers.append(answer)
print(f"짝수",even_numbers)
print(f"홀수",odd_numbers)
