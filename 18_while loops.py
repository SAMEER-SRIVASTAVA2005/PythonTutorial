# while loop 
i=0
while(i<3):
    print(i)
    i=i+1
# agr isme last line i=i+1 nhi likhenge to continuosly "0" print krta rhega..............


i=int(1)
while(i<=20):
    i=int(input("enter:"))         # jaise hi input value 20 se uper jayegi interpreter will come out of loop
    print(i)
print("bssssss...ho gya abhi")


# decreamenting while loop
count=5
while(count>0):
    print(count)
    count=count-1

# meaning of iteration:jitni baar loop me ghusa utni baar iteration hui
# ek baar loop me gya,condition check hui mtlb "1 iteration"

# else can be used with while loop (condition false hone k baad else statement print ho jata hai)
count=5
while(count>0):
    print(count)
    count=count-1
else:
    print("ho gya bhai abhi")



# do.while loop (do not work in python,work in C++)
# do.while loop - do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition:true or false) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.
# Explanation
# This loop uses True as its formal condition. This trick turns the loop into an infinite loop. Before the conditional statement, the loop runs all the required processing and updates the breaking condition. If this condition evaluates to true, then the break statement breaks out of the loop, and the program execution continues its normal path.

# below code runs in C language
# do {
#     # loop body;
# }while(condition);

# below code is similar to do.while 
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
