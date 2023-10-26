a=int(input("Enter your age:", ))
print("Your age is:", a )

    # conditional operators
    # <,>,<=,>=,==(compare two values to be equal or not),!=(not equal to)
print(a<18)
print(a>18)
print(a<=18)
print(a>=18)
print(a==18)
print(a!=18)

if(a>18):
    print("You can drive") #indentation:print k aage jo space hai means starting of a block(here space indicates that we are inside "if" block )
else:
    print("You can not drive")
    print("ye else block k ander h")
print("ye else k ander nhi hai")  

applePrice =int(input("enter the price:", ))
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")

# below is example of elif

num=int(input("Enter the num:"))
if (num<0):
    print("num is negative")
elif (num == 0):
    print("num is 0")
elif (num==99):
    print("num special hai bhai")
else:
    print("num chutiya hai behnchod")

# below are 2 example of nested if statements

num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

num=int(input("Enter the num:"))
if(num==0):
    print("0 hai")
elif(num>0):
    print("bhai positive hai ye")
    if(num<=10):
        print("10 k ander hai")
    elif(num<20):
        print("20 k ander hai")
    else:
        print("20 se jyada hai vro")    
else:
    print("negative")
