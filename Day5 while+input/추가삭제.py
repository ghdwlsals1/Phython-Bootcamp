users=[
    {"name":"짱구","lv":80,"score":60},
    {"name":"진민","lv":100,"score":95},
    {"name":"정화","lv":120,"score":100},
    {"name":"철수","lv":90,"score":50}
]
result=[]
for user in users:
    if user["score"]>=90:
        result.append(user["score"])
print(result)