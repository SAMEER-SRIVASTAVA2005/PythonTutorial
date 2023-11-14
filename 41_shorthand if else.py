# If ... Else in One Line
# There is also a shorthand syntax for the if-else statement that can be used when the condition being tested is simple and the code blocks to be executed are short. Here's an example:

a = int(input("enter a number"))
b = 330
print(a) if a>b else print("=") if a==b else print("b is greater")

# else ko warna smjh kr padho
# "print(a) if a>b"                this is one thing
# "else print("=") if a==b"        this is one thing
# "else print("b is greater")"     this is one thing

# You can also have multiple else statements on the same line:


# Another Example
# result = value_if_true       if condition        else value_if_false

# This syntax is equivalent to the following if-else statement:

# if condition:
#     result = value_if_true
# else:
#     result = value_if_false

# below given example is of above statement
print("yup") if a>b else 0



# Conclusion
# The shorthand syntax can be a convenient way to write simple if-else statements, especially when you want to assign a value to a variable based on a condition.
# However, it's not suitable for more complex situations where you need to execute multiple statements or perform more complex logic. In those cases, it's best to use the full if-else syntax.

