# There are four types of arguments that we can provide in a function:
# Default Arguments                           # Keyword Arguments
# Variable length Arguments                   # Required Arguments

#    DEFAULT ARGUMENTS:
# We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument-

def average(a=3,b=6):
    average=(a+b)/2
    print("The average of given values are" ,average)
average(8,6)
# a b value dene se default value ko ingore krke in value ko priority dega
average(4)     # here 4 will be considered as value of a and b will be taken from default value
average(b=9)   # a will be taken from default value

def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)
name("Amy","pink")



#      KEYWORD ARGUMENTS:
# We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

average(b=20 ,a=5)
# b pehle likha hai but this doesnot matter if u use keyword

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name(mname = "Peter", lname = "Wesker", fname = "Jade")


#          REQUIRED ARGUMENTS:
# In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

# Example 1: when number of arguments passed does not match to the actual function definition.

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("Peter", "Quill")
# This throws error as -TypeError: name() missing 1 required positional argument: 'lname'
# concentrate on DEFINITION


# below we have taken argument as a tuple and defined the average for many numbers
def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  print("Average is: ", sum / len(numbers))

average(5, 6, 7, 1)
   

#           return Statement
# The return statement is used to return the value of the expression back to the calling function.

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname
print(name("James", "Buchanan", "Barnes"))


# instead of printing the function we want that it to returns a vlaue (niche average hme c ki value k roop ne return ho rha hai)
def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
#   return 7
  return sum / len(numbers)
# if return na kre to (comment out return n see) hme "none" milega run krne pr
 
#  return mtlb wapas chale jao iss value ko leke(agr hm if else k ander return lga rhe hai to jo bhi return isse pehle mil jayega wo value final krke wapas chala jayega funtion)  agr return 7 pehle mil gya to whi final krke 7 value dedega
# agr hm do return statement lga dete hai to pehla wala mana jata hai uske baad k saare ignore kr diye jate hai

c = average(5, 6, 7, 1)     #  this is the calling function
print(c)
  


#                    YE SMJH ME NHI AAYA HAI...................

# Variable-length arguments:
# Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.  --------There are two ways to achieve this:

#               Arbitrary Arguments:
# While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.

def name(*name):
    print("Hello,", name[0], name[1], name[2])
name("James", "Buchanan", "Barnes")



#              Keyword Arbitrary Arguments:
# While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname = "Buchanan", lname = "Barnes", fname = "James")
