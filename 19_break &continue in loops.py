# BREAK-The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.(BREAKING OUT OF THE LOOP-loop se bahar aajate hai)

for i in range(12):
    print("5 x",i+1,"=",5*(i+1))
    if(i==10):
        break

# print("break mtlb:loop ko chor kr nikal ja")

# in above break statement loop 11 tak jayegi kyuki 10 tk jane k baad (+1) hua aur 11 se multiply hua and then check ho kr break hhua but in below statement break pehle check hoga isliye 10 pr in end hua(2nd code me 10 isliye gye kyuki 9 check hua procced hua (+1) krke 10 bna aur execute hua and then 10 pr break leliya)

for i in range(12):
    if(i==10):
        break
    print("5 x",i+1,"=",5*(i+1))


# ------break jo hota hai wo for aur while dono k liye use hota hai


# CONTINUE-The continue statement skips the rest of the loop statements and causes the next iteration to occur.(shirf whi part skip hota hai "shirf whi iteration" and fhir next iteration start ho jata hai)

for i in range(12):
    if(i==10):
        print("isme 11 se multiply hone wali value skip ho jayegi")
        continue
    print("5 x",i+1,"=",5*(i+1))


# do.while loop
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break

for i in range(1,101,1):
    print(i ,end=" ")
# (end=" ") krne se i k baad "Mississippi" same line me aaja rha hai otherwise next line me ayega
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")