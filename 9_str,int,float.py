a=2
b=4
print(a+b)
# this will result in 6 as it will not be considered as string
a="2"
b="4"
print(a+b)
# this will result in 24 as python string ko one after one likhta jatta hai
# typecasting can be used here to one convert one data type to another data type
# a="1sam" ye convert nhi hoga invalid hai
a="2"
b="4"
print(int(a)+int(b))
# int converted string a and b into integer and then added

c=1.9
d=7
# c float hai aur d int hai to as an example of implicit yaha ye hoga ki python d ko float me convert krke add kr dega aur result float me ayega
print(type(c))
print(type(d))
print(c + d)
print(type(c+d))