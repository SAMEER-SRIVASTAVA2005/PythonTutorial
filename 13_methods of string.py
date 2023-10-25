a="!!!!sam!!!!!!!!!!!"
# strings are immutable(do not change) when we apply any methode (it works on existing string and generate a new string)
# but variable can be overwritten
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
# rstrip only remove trailing part (strip-remove all covering from) and this do not remove leading part
print(a.replace("sam","aman") )
# and this replace remove all the occurence as if in a there were sam written two three times then it would replace all of them

b="sam sachin aman"
print(b.split(" "))

blogheading="intoduction to cSS"
print(blogheading.capitalize())
# introduction ka i capital hojayeaga and if further koi letter shi format me nhi h to kr dega like "cSS" ko "css" me

# str1="Welcome to the Consol!!!"
# print(str1.center())
# ye center krne k liye hota haai but smjh nhi aaya

print(a.count("sam"))   # used to count

# startswith(): The endswith() method checks if the string starts with a given value. If yes then return True, else return False.
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1="Welcome to the Consol!!!"
print(str1.endswith("!!!"))
# this check if the string ends with the given value.if yes then it returns true(it answers in boleans)

# We can even also check for a value in-between the string by providing start and end index positions.........4,10 me "ome to" aur isme to aarha h thats the logic
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

# find(): The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
str1="He's name is Dan.He is an honest man."
print(str1.find("is"))
# he's me is h but python isse nhi detect krega .....python will detect literal word as ask to search

# index(): The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent then raise an exception(error).
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))
#agr hm chahte hai hmara program error dekr exit hojaye if asked value is absent then we use index

# isalnum(): The isalnum() method returns True only if the entire string only consists of "A-Z, a-z, 0-9". If any other characters or punctuations are present, then it returns False.
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1="Welcome/"
print(str1.isalnum())

# isalpha(): The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
str1 = "Welcome"
print(str1.isalpha())

# islower(): The islower() method returns True if all the characters in the string are lower case, else it returns False.
# isupper():The isupper() method returns True if all the characters in the string are upper case, else it returns False
str1 = "hello world"
print(str1.islower())

# isprintable(): The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())
str1 = "We wish you a Merry Christmas\n"
# "/n" new line dedega but literally print nhi hoga
print(str1.isprintable())

# isspace(): The isspace() method returns True only and only if the string contains white spaces, else returns False.
str1 = "         "       #using Spacebar(even one space is considered)
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())

# istitle(): returns True only if the first letter of each word of the string is capitalized, else it returns False.
str1 = "World Health Organization" 
print(str1.istitle())

# swapcase() :The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

# title() :The title() method capitalizes each letter of the word within the string.
str1 = "His name is Dan. Dan is an honest man."
print(str1.title())