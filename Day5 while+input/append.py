numbers=[7,12,15,20,23,28,31,40]
result=[]
even_numbers=[]
odd_numbers=[]
for number in numbers:
    number % 2==0
    if number > 20:
        result.append(number)
for number in result:
    if number % 2==0:
        even_numbers.append(number)
    if number % 2 !=0:
        odd_numbers.append(number)
print(f"20 보다 큰 숫자는 {result}")
print(f"짝수{even_numbers}")
print(f"홀수{odd_numbers}")
