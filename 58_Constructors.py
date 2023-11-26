# Constructors
# A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.

# iska kaam h initialization, ye hr baar call hoga jb naya object bnaya jayega (ye method hr baar invoke hoga jb jb object bnaya jayega)

# A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.

# Syntax of Python Constructor
# def __init__(self):
	# initializations

# init is one of the reserved functions in Python. In Object Oriented Programming, it is known as a constructor.


# this is helpful as before we were again assigning new value to the variable defined in the class to creat a new object but here we just pass arguement with __init__ and while calling it 

class Person:
    def __init__(self,name,occ):
        print("Heyy I am a person")
        self.name = name
        self.occ = occ
 
    def info(self):
        print(f"{self.name} is a {self.occ}")
    
a=Person("Sameer","Student")              # yaha jb bhi object bnaunga tb constructor call hoga

b=Person("Sachin","Teacher")              #same here too
#  init teen argument le rha hai i.e. self,n,o and while calling i.e. a=Person we are passing only two argument it is as such bcoz 1 argument is passed by default that is 'a' which is passing at place of self when we run the code     (if we less or more no. of argument then it will through an error)

a.info()
b.info()


# Types of Constructors in Python

# Parameterized Constructor
# Default Constructor

# Parameterized Constructor in Python
# When the constructor accepts arguments along with self, it is known as parameterized constructor.

# These arguments can be used inside the class to assign the values to the data members.


# Default Constructor in Python
# When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.














