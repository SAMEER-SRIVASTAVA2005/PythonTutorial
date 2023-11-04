# the difference between list and tuple is that-tuple can not be changed(unchangble)

# thistuple=(11,22,44,33,66)
# thistuple[0]=50
# print(thistuple)
# above code will show error as it can not be changed
# ------(agr hm aisa program chahte hai jo change naho to isse use krte hai)------

tup=(1,5,7,True,"samienem")
print(type(tup),tup)

# idexing in tuple(same as in list in respect of +ve and -ve indexing is same as well)
print(tup[0])
print(tup[4])

# check for an item
if True in tup:
    print("hn present hai ")


# here after slicing a new tuple is returned (original tuple is not changed )
tup2=tup[0:4]
print(tup2)

# if tuple me shirf 1 element rkhenge to type int  ho jayega(check below)
tup=(1)
print(type(tup),tup)

# if we want to make tuple of one element we need to put comma in the end .........like given below
tup=(1,)
print(type(tup),tup)


# STRINGS / TUPLES are immutable
# LISTS are mutable













