# sets-unordered and dictionary-python 3.7 onwards ordered


ep1 = { 101:46 ,102:49 , 103:53 , 104:74  }
ep2 = { 107:47 ,110:40 }
 
# to update dictionary
ep1.update(ep2)
print(ep1)
# to remove all the items from list
ep1.clear()
print(ep1)

# .another example
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})  # we can change the already exist value too 
info.update({'DOB':2001})
print(info)

# to print an empty dictionary
empt={}
print(empt)


# The pop()---- method removes the key-value pair whose key is passed as a parameter.
info2={"name":"sam","course":"b.tech","branch":"cse", "section":"tq"}
print(info2)
info2.pop("branch")
print(info2)

# popitem()----- is used to remove the last key-value pair from the dict
info2.popitem()
print(info2)


# del used here and particular item is defined to be deleted so the entire dict will not be deleted
del info2["course"]
# del info2[course]  --- this will raise an error as item-course is defined as string in the dict and here it is tried as an integer so it will throw an error

print(info2)


# del----this keyword will remove the dict entirely as  a particular key is not defined to be removed  and  will give nameError not defined
del info2
print(info2)




