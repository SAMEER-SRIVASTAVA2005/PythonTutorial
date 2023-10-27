# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
# click on link while pressing ctrl

import time
timestamp=time.strftime("%H:%M:%S")
print(timestamp)
hours=int(time.strftime('%H'))

# hours=int(input())                # isme time daal kr check kr skte ki kya output dega
# print(hours)

if(hours>=0 and hours<12):
    print("Good Morning Sir!")
elif(hours>=12 and hours<18):
    print("Good After Noon Sir!")
elif(hours>=18 and hours<21):
    print("Good Evening Sir!")
elif(hours>=21 and hours==24):
    print("Good Night Sir!") 


# try running this program on terminal
# 1-python
# 2-import time
# timestamp=time.strftime("%H:%M:%S")
# 3-timestamp
# then local time will be shown












