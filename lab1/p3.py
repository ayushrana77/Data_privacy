import random
import time 
otp =random.random()*1000000
otp = int(otp)

print("OTP was send")
print (otp)

time_end = time.time() + 60

print(time.time())

print("Enter the opt was send on mail")

num = int(input())
if time.time() < time_end:
    if (num == otp):
        print("OTP match")
    else:
        print("OTP not match")
else:
    print("Time out")



