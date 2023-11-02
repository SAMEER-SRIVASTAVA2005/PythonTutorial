# PYTHON LISTS----
# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets [].
# Lists are changeable meaning we can alter them after creation.


list1=[1,2,3,4,5,6,7]
print(len(list1))
print(list)
print(type(list))
print(list[7])

list2=[4,5,"sam",True,89,102,"sachin","engineering",False]
print(list2)
print(list2[2])
print(list2[3])

# INDEXING     (negative indexing)
print(list2[-2])
# if we count from backside(starting from "-1") we will get the answer
# other way to understand (steps hai ek hi way ke)
print(list2[len(list2)-2])
print(list2[9-2])
print(list2[7])       # now count from starting from 0 
  
#   to check an element is in list or not
if "yuppppp" in list2:
# agr "6" (6 ko as a string) aise check krenge to nhi milega kyuki 6 as an integer hai hmari list2 me
    print("haan hai")
else:
    print("nhi hai")

# below done thing (same can be applied fo strins) 
if "sm" in "sam":
# if "sa" in "sam":      this will give "yuppppppppppp"
    print("yuppppppppppp")
else:
    print("nhi hai ")


# SLICING- taking elements from one given index to another given index. 

# Range of Index:  You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range.
# Syntax:    listName[start : end : jumpIndex]


print(list2[:])
print(list2[1:-1])  #this will give till "sam" as per rules (n-1) in last term ,therefore (-1-1)=-2 hence, will get "sam"
print(list2[0:10:2])
# Above after slicing jump part:"2" start counting and print the     0th(the very first term from which list starts) then      2nd 4th 6th position and so on values which we get while we start counting from the very first term 

# jump index-slicing k baad sbse pehle term print hojata hai aur fhir jo bhi jump indexing di gyi h uske according (nth),where n is the jump index print hoti rehti hai

# LIST COMPREHENTION-- are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

lst=[i*i for i in range(10)]
print(lst)
lst=[i*i for i in range(10) if i%2==0]
print(lst)          # only square of even numbers by if statement

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [i for i in names if "o" in i]
print(namesWith_O)


names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
name= [item for item in names if (len(item) > 4)]
print(name)











