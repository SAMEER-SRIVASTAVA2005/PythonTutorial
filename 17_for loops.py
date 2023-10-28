# two types of loop-for loop and while loop

name="sameer"
for a in name:
    print(a)

colors=["red","green","yellow","blue"]
for color in colors:
    print(color)
    for i in color:
        print(i)

# RANGE- 0 se shuru hota hai (below by dafault is written as range(0,7) so it starts from 0) 
for k in range(7):
    print(k)

# if we want to start from 1(isme 1 add krke dega mtlb 7 tk janaa h to 7 jayega as bcoz in noraml range it stops before the range value given but isme last value me 1 add krke range k equal kr dega)
# we can change "x" in (k+x) as per our convenience
for k in range(7):
    print(k+1)

for l in range(1,20000):
    print(l)

# range k 3 parameter h(click on range and find out)
# -start 
# -stop 
# -step 
# step used below

for k in range(0,20,5):
    print(k+1)
#    just fuckin run n observe!!!