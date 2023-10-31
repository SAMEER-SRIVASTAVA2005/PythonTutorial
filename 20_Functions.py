# PYTHON.FUNCTIONS
# A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.

# TYPES OF FUNCTIONS: Built-in functions AND User-defined functions
# Built-in functions-These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:
# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

# User-defined functions-We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.(def krke jo bnate hai hm)



def calculategmean(a, b):
    mean=(a*b)/(a+b)
    print(mean)

def isgreater(a,b):
    if(a>b):
        print("1st no. is greater than 2nd no.")
    else:
        print("2nd no. is greater than 1st no.")

def islesser(a,b):
    pass
# above we have started making of a function but not completed it as I wish to complete it later(so I wrote "pass" below so that the code run without any intereption)

a=8
b=9
calculategmean(a,b)
calculategmean(7,9)  #aise direct likh kr bhi kr skte hai  
isgreater(a,b)



c=5
d=3
calculategmean(c,d)

isgreater(c,d)




