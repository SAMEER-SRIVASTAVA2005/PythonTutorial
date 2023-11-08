s = {8, 90, 4, 6, 9, 12, 12, 12, 90, 6,6,6 ,6}
print(s)

# Python Sets------Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

info = {"Carla", 19, False, 5.9, 19, False}
print(info)
# You can access items of set using a for loop
for i in info:
    print(i)

sam={}
# above results as empty dict not an empty set as curly bracket is used in dict too
# to make an empty set we do so
sam=set()
print(type(sam))












