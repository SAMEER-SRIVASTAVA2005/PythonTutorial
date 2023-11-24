# 'is' vs '==' in Python
# In Python, is and == are both comparison operators that can be used to check if two values are equal. However, there are some important differences between the two that you should be aware of.

# The is operator compares the identity of two objects, while the == operator compares the values of the objects. This means that is will only return True if the objects being compared are the exact same object in memory, while == will return True if the objects have the same value.

# inshort
# 'is' compare the exact location of object in memory
#  and
# '==' compares the value of objects
# (dono comparision operators hote hai)


# example-
a=[12,34,56,78,90]
b=[12,34,56,78,90]

print(a is b)     #(gives False)       #compares the location
print(a==b)      #(gives True)      #compares the value
 
#  In this case, a and b are two separate lists that have the same values, so == returns True. However, a and b are not the same object in memory, so is returns False.


x=3
y=3
print(x is y)        #jb python me constant bnate hai to ye memory location me ek baar bnta hai aur python ko pta h ye change nhi hoga as bcoz ye constant/value/(immutable) hai to jb value dusre variable to assign kroge to python ek aur memory location nhi bnata same value ka and leverage kr lega so now the situation is that x and y are pointing toward same memory location where 3 is located

# note:- (strings can be overwritten)

j="sam"
k="sam"
print("yes this statement is also",j is k,"for strings")

# One important thing to note is that, in Python, strings and integers are immutable, which means that once they are created, their value cannot be changed. This means that, for strings and integers, is and == will always return the same result:


# it also true for "tuple"
# same goes for "none"

i=None
print(i is None)            #true


# For mutable objects such as lists and dictionaries, is and == can behave differently. In general, you should use == when you want to compare the values of two objects, and use is when you want to check if two objects are the same object in memory.





















































