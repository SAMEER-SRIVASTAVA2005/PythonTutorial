# /----INSB ME ORDER MATTER NHI KRTA----/

# JOINING METHODS

s1 = {1,3,5,7,9,4,8}
s2 = {2,4,6,8,7,5}

# taking union of two sets (in the procress s1 and s2 are not change)
print(s1.union(s2)) 

# we can update a set by following way
s1.update(s2)
# print(s1.update(s2))              "this prints"
print(s1)

# differeṇce union aur update me ye h ki union does not change the set while update changes the set into the desired set



alpha1={"a","b","c","d","e","f","g"}
alpha2={"d","e","f","g","h","i","j"}
# to find intersection we do so
alpha3=alpha1.intersection(alpha2)
print(alpha3)

# in intersection update the elements which are common in both the lists will appear in the updated list and non common elements will be removed (the list will be updated:CHANGED here)
alpha1.intersection_update(alpha2)
print(alpha1)



# III. symmetric_difference and symmetric_difference_update()-------
# The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets.
#  The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

cities.symmetric_difference_update(cities2)
print(cities)


# IV. difference() and difference_update():----

# The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. 
# The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

cities4 = {"palermo", "professor", "denver", "nyc"}
cities5 = {"professor", "hell-sinki", "nj"}
cities6 = cities4.difference(cities5)
print(cities6)

print(cities4.difference(cities5))
# this works like above used but not like below way
cities4.difference(cities5)
print(cities4)


# SET METHODS

# isdisjoint()------The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True (common honge to false dega and no element common then true dega as it disjoint)

cities8 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities9 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities8.isdisjoint(cities9))




# issuperset()------The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

cities11 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities12 = {"Seoul", "Kabul"}
print(cities11.issuperset(cities12))
cities13 = {"Delhi", "Madrid"}
print(cities11.issuperset(cities13))



# issubset()----The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

cities14 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities15 = {"Delhi", "Madrid"}
print(cities15.issubset(cities14))


# ADD()-if you want to add a single item to set
seher={"bihar","up","punjab","delhi"}
seher.add("gujarat")
print(seher)

# remove()/discard()
seher.discard("up")
print(seher)
# seher.remove("up")
# print(seher)

# The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.



# pop()---- This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.

cities20 = {"Tokyo", "Madrid", "Delhi" ,"Berlin"}
item = cities20.pop()
print(cities20)
print(item)
# print(cities20.pop())

# DEL-it is not a method, it is a keyword which deletes the set entirely and this gives an nameError
# del cities20
# print(cities20)


# What if we don’t want to delete the entire set, we just want to delete all items within that set?

# clear()----This method clears all items in the set and prints an empty set
cities20.clear()
print(cities20)
# result- set()


# to check if an item is exists in set or not 
info={"sam",18,False,8.6}
if False in info:
    print("hn hai bhai")
else:
    print("nhi hai bro")




