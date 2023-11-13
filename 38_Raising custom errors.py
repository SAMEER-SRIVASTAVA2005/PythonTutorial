# Raising Custom errors
# In python, we can raise custom errors by using the raise keyword.

# In the previous tutorial, we learned about different built-in exceptions in Python and why it is important to handle exceptions-it is imp to handle error(exception) taki baki ka code run kre. However, sometimes we may need to create our own custom exceptions that serve our purpose.

    # example
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")


    #another example
a=int(input("enter a value: "))
if a<5 or a>9:
    raise ValueError("value is not defined")
else:
    print("input value is ", a)

# there are many errors (on google-built-in exception in python)



# Defining Custom Exceptions'
# In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

# syntax

# class CustomError(Exception):
#   # code ...
#   pass
  
# try:
#   # code ...

# except CustomError:
#   # code...

# try using custom exception


# quick quiz by harry
x=input()
if x=="quit":
    print("please enter an integer between 5 and 9")
elif int(x)<5 or int(x)>9:
    raise ValueError
else:
    print(x)



# This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an api, etc.