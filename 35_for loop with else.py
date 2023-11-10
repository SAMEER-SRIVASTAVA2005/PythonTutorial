# Python - else in Loop
# As you have learned before, the else clause is used along with the if statement.

# Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.



for i in range(5):
    print(i)
else:
    print("nhi ho payega.....")

# using empty list
for i in []:
    print(i)
else:
    print("nhi ho payega .....")


# VERY IMPORTANT --using break in loop (with using else)
for i in range(8):
    print(i)
    if i==5:
        break
else:
    print("nhi ")

    # else statement will not be printed as loop is break before else
 
#else execute tb hota hai jb loop khtm hota hai na ki break hua hai..... (loop break nhi hua, loop successfully khtm hua hai -then else is printed)
        
# using break with while loop (and here too else statement will not be printed as loop khtm nhi hua balki break hua hai)
i=0
while i<7:
    print(i)
    i = i + 1
    if i==5:
        break
else:
    print("nhi")

    
# another example-----
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")












