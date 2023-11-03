l=[5,1,4,3,2,6]

print(l)
l.append(7)
print(l)
# appends helps us to add the appended element in the list in the end(can contain only 1 element)

l.sort()   # sort- assembled in increasing/ascending order
print(l) 

l.sort(reverse=True)   # decreasing/descending order   
print(l)

l.reverse()
print(l) 
# used to reverse the order of the original list

print(l.index(5))
print(l.index(6))
# used to find the index of an element (in above code index of 5 & 6 are asked)

print(l.count(3))
# used to count the no. of occurance of an element

# m=l
# m[0]=0
# print(l)
# this made a new copy but changed the 0 index element to "0"

# but we use this method to copy
m=l.copy()
m[0]=0
print(l)
 
l.insert(2, 599)
print(l)            # this will insert "599" at 2nd index aur jo 2nd index pr tha wo aage shift ho jayega means 2nd index wala 3rd index pr chala jayega.........

m= [666,777,888]
l.extend(m)
print(l)
# "l" ke baad me "m" list append(add) ho jayega

# uper l me hi append ho gyi thi m list
# if we want a new list in which m is appended in l
k = l+m
print(k)












