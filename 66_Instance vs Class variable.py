# Instance vs class variables
# In Python, variables can be defined at the class level or at the instance level. Understanding the difference between these types of variables is crucial for writing efficient and maintainable code.


class Employee:
    companyname="Apple"
    noofemployee=0       #by this you can count the no.of employee e.i. no. of objects made
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02
        Employee.noofemployee +=1

    def showdetails(self):
        print(f"The name of the employee is {self.name} who currently works in {self.companyname} at a raise of {self.raise_amount} and no. of employee are {self.noofemployee}")

emp1=Employee("Sam") 
emp1.raise_amount=0.3
# Employee.companyname="microsoft"    #this will apply at classlevel(it is class variable) and will replace the companyname that is already defined in the class  
emp1.companyname="nestle"        #this will apply at instance level(this is instance variable)
emp1.showdetails()

# above can also be done like below done
emp2=Employee("Sachin")
Employee.showdetails(emp2)
# the error which happens when less arguments are passed like below
# TypeError: Employee.showdetails() takes 0 positional arguments but 1 was given
# this can be understand from this
# Employee.showdetails(emp2)
# here emp2 is passed(inside showdetails) means 1 argument is passed but if we dont use self argument while defining a function then then it will raise error like showdetails() takes 0 positional arguments  THAT IS  the reason why we pass self argument while defining constructor and other methods

# instace variable pehle search hota hai if nhi mila then class variable lg jata hai

print(Employee.companyname)     #gives company name which is apple that is defined already in the class but can be changed like below

Employee.companyname="TCS"
print(Employee.companyname)          #will give company name TCS



# Class Variables
# Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class. For example, a class variable can be used to store the number of instances of a class that have been created.
class MyClass:
    class_variable = 0
    
    def __init__(self):
        MyClass.class_variable += 1
        
    def print_class_variable(self):
        print(MyClass.class_variable)
        

obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()
obj4 = MyClass()

obj1.print_class_variable()
obj2.print_class_variable() 
obj3.print_class_variable()
obj4.print_class_variable()

# In the example above, the class_variable is shared among all instances of the class MyClass. When we create new instances of MyClass, the value of class_variable is incremented. When we call the print_class_variable method on obj1, obj2, obj3 and obj 4 we get the same value of class_variable. i.e. 4 (which is the total no. of object made from that class)


# Instance Variables
# Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method and are usually used to store information that is specific to each instance of the class. For example, an instance variable can be used to store the name of an employee in a class that represents an employee.
class MyClass:
    def __init__(self, name):
        self.name = name
        
    def print_name(self):
        print(self.name)

obj1 = MyClass("John")
obj2 = MyClass("Jane")

obj1.print_name() # Output: John
obj2.print_name() # Output: Jane

# In the example above, each instance of the class MyClass has its own value for the name variable. When we call the print_name method on obj1 and obj2, we get different values for name.


# Summary
# In summary, class variables are shared among all instances of a class and are used to store information that is common to all instances. Instance variables are unique to each instance of a class and are used to store information that is specific to each instance. Understanding the difference between class variables and instance variables is crucial for writing efficient and maintainable code in Python.

# It's also worth noting that, in python, class variables are defined outside of any methods and don't need to be explicitly declared as class variable. They are defined in the class level and can be accessed via classname.varibale_name or self.class.variable_name. But instance variables are defined inside the methods and need to be explicitly declared as instance variable by using self.variable_name.


