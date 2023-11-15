# Enumerate function in python
# The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works:

marks=[12,34,64,89,1,57,7,41,77]

# below is normal way of doing it
index=0
for mark in marks:
    print(mark)
    if(index==3):
        print("sam, this is the index we want! ")
    index +=1

# now using enumerate

for index,mark in enumerate(marks):
    print(index,mark)
    if(index==3):
        print("sam, this is the index we want! ")

# Changing the start index: one can use "start" to start iterating the loop from where we want
for index,mark in enumerate(marks,start=1):
    print(index,mark)
    if(index==3):
        print("sam, this is the index we want! ")

# we can use it for other sequence type also like tuple,strings




# abc=[12,34,64,89,1,34,57,07,41,77]
# 7 is displaying in red booz leading zero in decimal integral literal are not permitted: use an 0o  prefix for octal integers
abc=[12,34,64,89,1,34,57,0o7,41,77]