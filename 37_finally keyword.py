# Finally Clause------- The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message. 

#    (The finally block is executed irrespective of the outcome of try……except…..else blocks One of the important use cases of finally block is in a function which returns a value.)

#syntax-
def func():
    try:
        l=[2,4,6,8,10,12,14,16]
        i=int(input("Enter the index: "))
        print(l[i])
        return 1
    
    except:
        print("Some error occured")
        return 0
    
    finally:
        print("I am always executed")


    # print("will this be executed")          #this will not be printed
print(func())



# instead of finally clause, directly a statement could also be used with print just to print it always but the problem will be that it would not be printed 

# function try me return kr bhi jayega to bhi finally clause execute hoga















