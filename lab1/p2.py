print("Enter the card Number")
email = input()
count = 0
res = ""
for i in email:
    count += 1
    if count%2 == 0:
        res += '*'
    else:
        res += i

print(res)