name = "sameer"
# used to find the length of the string
names=len(name)
print(names)
print(name[0:5]) 
# this will go from 0 to (5-1)=4 i.e.samee
print(name[:5])
#   # python will take it as to start from 0 automatically
print(name[5:])
# 5 se end tk
print(name[2:4])
print(name[:])
#  # this gives the full length
# last me (n-1) tk jayega yaha n=5 hai mtlb (5-1)=4 tk jayega i.e. 0=s,1=a,2=m,3=e,4=e

print(name[0:-3]) 
# above is same as print(name[0:len(name)-3]) and then (n-1) rule therefire [0:2]
# output=sam

print(name[-1:-3]) 
# this will be 6 and 6-3 i.e. 5:3 and this does not make sense 
  
print(name[-3:]) 
# above will give output-"eer"
print(name[-3:-1]) 
# this is 3:5







