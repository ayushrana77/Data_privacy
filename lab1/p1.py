print("Enter the email address")
email = input()
flag = True
count = 0
res = ""
for i in email:
    if(i == '@'):
        flag = False
        res += i
    else:
        count += 1
        if count > 2 and flag:
            res += '*'
        else:
            res += i

print(res)