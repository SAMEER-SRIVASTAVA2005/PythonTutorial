# a=input()
# print("My name is" , a)
# run krne k baas terminal me sam likhunga tb My name is sam krke ayega
# a=input("Enter your name ")
# print("My name is" , a)
# this  will show Enter your name and then terminal me name dalne k baad my name is sam krke show krega

# x= input("Enter first number: ")
# y= input("Enter second number: ")
# print(x + y)
# if we procced with 1st no.=55
# and 2nd no.=67
# then heere result will be 5567 bcoz it will be considered as string by python and will be concatenated
# print(int(x)+int(y))    # this will give  122

# checking for all operations
t=input("1st no: ")
q=input("2nd no: ")

#without typecasting
print(t + q)
print(t - q)
print(t * q)
print(t / q)
print(t // q)
print(t % q)
# in above situation except in case of addition ......others are giving errors

# with typecasting
print(int(t) + int(q))
print(int(t) - int(q))
print(int(t) * int(q))
print(int(t) / int(q))
print(int(t) // int(q))
print(int(t) % int(q))
# all r working
