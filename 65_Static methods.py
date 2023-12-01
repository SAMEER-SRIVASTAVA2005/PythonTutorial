# Static methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self). They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data.

class Math:
    def __init__(self,num):
        self.num=num
    
    def addnum(self,n):
        self.num=self.num+n

    @staticmethod                    #we are putting the this static method inside the class as bcoz we want that if we have to share this class incase someone import this class so he/she can use this method
    def add(a,b):
        return a+b
    #do not need to put self in the staticmethod


a=Math(5)
print(a.num)

a.addnum(6)
print(a.num)


# static method is not associated with any instance neither with any class we can call it by using object name or class name too
print(a.add(10,9))           #called by object name


# In this example, the add method is a static method of the Math class. It takes two parameters a and b and returns their sum. The method can be called on the class itself, without the need to create an instance of the class.
print(Math.add(10,9))            #called by class name




# INTERVIEW QUESTION-   If you have to make a method in the class, is it necessary to pass self as an argumetn in that method
# ANSWER-     NO  (like in static method)

















