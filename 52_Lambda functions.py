# Lambda Functions in Python
# In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:

# lambda arguments: expression

# Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

# for example-
# "name of func " = "lambda" variable you want to take: operation u want to execute 
# then call it when desired

multiply = lambda y: y*5

print(multiply(6))


# in terms of multiple variables
add = lambda a,b,c,d: ((a+b)*c)/d

print(add(5,15,2,10))        

# lambda function is used when one-liner function are into scene

 #here i called sam funtion and callling multiply funtion inside it 
def sam(i,o):
    return 6* i(o)

print(sam(multiply,8))         

# actual use of lambda function- used when we want to pass a function as an argument (we can also function to a function)

print(sam(lambda j:j*3 ,8))         


# anonymous function is the funtion which is not defined but is used in such a way that it functions in the desired manner
















