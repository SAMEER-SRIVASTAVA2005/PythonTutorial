# Python Decorators
# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.

# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function.

# Decorators are often used to add functionality to functions and methods, such as logging, memoization, and access control.

def greet(fx):
    def mfx():
        print("GOOD MORNING")
        fx()
        print("THANKS FOR VISITING")
    return mfx

# two syntax of adding greet func. are
            # 1st is 
# @greet
# def func():
#     print("sam")
# func()
            # 2nd 
# print(func)()

@greet
def hello():
    print("Hello World")
hello()

# greet(hello)()       this can also be used to do the same that is done above

# another example when arguments are passed in the function
def greet(fx):
    def mfx(*args,**kwargs):
        print("GOOD MORNING")
        fx(*args,**kwargs)
        print("THANKS FOR VISITING")
    return mfx

# @greet
def add(a,b):
    print(a+b)
# add(6,7)

greet(add)(4,5)   

# Practical use case
# One common use of decorators is to add logging to a function. For example, you could use a decorator to log the arguments and return value of a function each time it is called:

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

print(my_function)

# In this example, the log_function_call decorator takes a function as an argument and returns a new function that logs the function call before and after the original function is called.

# logs ko console ya kahi pr dekhne k kaam aata hai, ya fhir log ko transmit krna chahte ho overnetwork then you can use logging
# we can also define logging level like debug an level, info an level, error an level 


# Conclusion
# Decorators are a powerful and flexible feature in Python that can be used to add functionality to functions and methods without modifying their source code. They are a great tool for separating concerns, reducing code duplication, and making your code more readable and maintainable.

# In conclusion, python decorators are a way to extend the functionality of functions and methods, by modifying its behavior without modifying the source code. They are used for a variety of purposes, such as logging, memoization, access control, and more. They are a powerful tool that can be used to make your code more readable, maintainable, and extendable.








