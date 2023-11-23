# jb ek function ko dusra funtion as an argument leleta hai then it is called as an higher order function


# Map, Filter and Reduce are niether only used in python or nor only for lists
# Map, Filter and Reduce
# In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. These functions are known as higher-order functions, as they take other functions as arguments.


def cube(x):
    return x*x*x

l=[1,2,3,4,5,6,7]
# newl=[]
# for item in l:
#     newl.append(cube(item))       #instead of above three lines you can use below map function to do the same

# map
# The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. The map function has the following syntax:
# map(function, iterable)

# The function argument is a function that is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.
# using map func- give function name to map and then give the list in which u want to apply this function to every element
newl=list(map(cube,l))
print(newl)

newl=list(map(lambda s:s*s*s,l))
print(newl)             #like this you can apply lambda function in map function



# filter
# The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate. The filter function has the following syntax:

# filter(predicate, iterable)

# The predicate argument is a funmction that returns a boolean value and is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

def funx(k):
    return k%2==0
l = [2,5,8,15,66,19,98,27]

print(list(filter(funx,l))) 

# lambda in filter
print(list(filter(lambda j:j%3==0,l)))



# reduce     (we need to import reduce func before using it)
# The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python and has the following syntax:

# reduce(function, iterable)

# The function argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements, such as a list or tuple.

# The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element, and so on. The reduce function returns the final result.

from functools import reduce
 
t=[1,2,3,4,5,6,7,8,9]

def sum (o,p):
    return o+p

print(reduce(sum,t))

# by using lambda funtion
print(reduce(lambda o,p:o+p,t))

# In the above example, the reduce function applies the lambda function lambda x, y: x + y to the elements in the numbers list. The lambda function adds the two arguments x and y and returns the result. The reduce function applies the lambda function to the first two elements in the list (1 and 2), then applies the function to the result (3) and the next element (3), and so on. The final result is the sum of all the elements in the list, which is 45.

# It is important to note that the reduce function requires the functools module to be imported in order to use it.






