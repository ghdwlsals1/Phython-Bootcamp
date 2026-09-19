students=[
    {"name":"철수","score":55},
    {"name":"민수","score":55},
    {"name":"진민","score":90},
    {"name":"정화","score":100},
    {"name":"짱구","score":65},
]
def find_passed(pass1):
    result=[]
    for pass2 in pass1:
        if pass2 ["score"]>=90:
            result.append(pass2)
    return result
result=find_passed(students)
print(result)

    