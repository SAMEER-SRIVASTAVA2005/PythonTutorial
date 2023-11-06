# example of string formating-
details="hey buddy my name is {} and i am pursuing my b.tech from {}"
name="sam"
clg="LPU"
print(details.format(name, clg))

# ex2-
details="hey buddy my name is {1} and i am pursuing my b.tech from {0}"
name="sam"
clg="LPU"
print(details.format(clg, name))

# ex3-
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# but this was not so good for large number of data so f-string is used to plug variables in large strings
# F-STRING is newly introduced - python-3.6 onwards  
print(f"hy myself {name} and {clg} is my clg")

val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  


print(f"{2 * 30}")
print(type(f"{2 * 30}"))


# if we want to print exact same thing in the output too we can do so by this method
print(f"hy myself {{name}} and {{clg}} is my clg")


















