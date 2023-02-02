num= input().split(',')
def new_list(list):
    lst = []
    for i in range(len(list)):
        if len(list[i])<=3:
            lst.append(list[i])
    return lst
print(new_list(num))