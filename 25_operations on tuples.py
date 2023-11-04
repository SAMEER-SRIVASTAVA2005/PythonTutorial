# MANIPULATING TUPLES-
# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.


countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)       #converted tuple into list
print(temp)
temp.append("Russia")       #added item 
print(temp)
temp.pop(3)                 #removed item of index 3
print(temp)
temp[2] = "Finland"         
#change item of 2nd index into Finland 
print(temp)

countries = tuple(temp)     #converted list into tuple
print(countries)



# However, we can directly concatenate two tuples without converting them to list.

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

# SOME METHODS--

tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple1.count(2)
print('Count of 2 in tuple1 is:', res)



#The Index() method returns the first occurrence of the given element from the tuple.(mtlb element pehli baar kis index pr aaya hai)
# syntax-----tuple.index(element, start, end)

# Note: This method raises a ValueError if the element is not found in the tuple.

tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple.index(3)
print('First occurrence of 3 is', res)

res = tuple.index(3, 4, 9)
print("first occurance of 3 between index-4 to 9 is",res)

print(len(tuple))

# CONVENTION- classes ko capital se likha jata hai aur variable ko small letters se likha jata hai