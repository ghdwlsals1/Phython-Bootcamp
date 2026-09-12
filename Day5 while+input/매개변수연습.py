items=['방패','갑옷','옷','창','칼','사랑']
def check_item(items):
    result=[]
    for item in items:
        if len(item)==2:
            result.append(item)
    return result
result =check_item(items)
print(result)