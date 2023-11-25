# Python Class and Objects
# A class is a blueprint or a template(a type of placeholder) for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.

# Creating a Class
class Form:
    Name="Sam"
    Age=20
    Clg="LPU"
    Course="B.tech"
    def details(self):
        print(f"{self.Name} is pursuing {self.Course} from {self.Clg}")


# Creating an Object
a=Form()

# now we can print values
print(a.Name)
print(a.Clg)
print(a.Age)

# here i printed particular property
print(a.Name,a.Course,a.Clg,a.Age)


# here i used the class to create a new object
a.Name="Sachin"
a.Age=22
a.Clg="CU"
a.Course="M.tech"

a.details()      #i printed the method that i defined in the class            (here a is the object on which the method is going to be called)

# self parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It must be provided as the extra parameter inside the method definition.

# self mtlb - wo object jiske liye ye method call kiya ja rha hai
# as I have made "a" an object and when i print methods(using self)as in a.details(), then self mtlb wo object (that is here a) k liye method ko call kro


b=Form()         #created another object using class Form
b.details()



















