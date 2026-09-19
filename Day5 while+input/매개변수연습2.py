users=[
    {"name":"철수","lv":80,"score":70},
    {"name":"짱구","lv":120,"score":55},
    {"name":"짱구","lv":150,"score":90},
    {"name":"진민","lv":90,"score":95},
    {"name":"정화","lv":70,"score":100},
]
def find_users(user):
    result=[]
    for user1 in user:
        if (user1 ["lv"]>=100 and user1["score"]>=80)or(user1["score"]>=95):
            result.append(user1)
    return result
result=find_users(users)
print(result)