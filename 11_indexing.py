# apple= "He said, "I want to eat an apple"
# this will give error double coat k ander ek double coat lga rkha hai

apple= 'He said, "I want to eat an apple'
# to avoid error bahar single coat lga denge
print(apple)

# apple= 'He said,
# he is a good boy
# he like to play football
# "I want to eat an apple'
# print(apple)
#  this will show EOL:end of line error as bcoz python searches the end of string in the same line the string started

apple='''He said,
he is a good boy
he like to play football
"I want to eat an apple'''
print(apple)
# to avoid this will use triple (single coat) or we can also use triple (double coat)

name="SAMEER"
# indexing gives position (in programming index starts from 0)
print(name[0]) 
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
# print(name[6]) # throws an error
print("\n")

for character in apple:
    print(character)
    # above used for indexing large string
 