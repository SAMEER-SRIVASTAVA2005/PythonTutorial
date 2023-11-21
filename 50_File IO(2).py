# readlines() method
# The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.

f = open('myfile3.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

# The readlines() method reads all the lines of the file and returns them as a list of strings.
# made for the purpose to read a file line by line

# if marks of 3 subjects 3 students are given so we can parse it like this 

f=open("myfile3.txt","r")
i=0
while True:
    i+=1
    line=f.readline()
    if not line:
        break
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])
    print(f"marks of student {i} in mathematics is: {m1}")
    print(f"marks of student {i} in english is: {m2}")
    print(f"marks of student {i} in science is: {m3}")

    print(line)


# writelines() method
# The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.

f=open("myfile3.txt","w")
lines=['line1\n','line2\n','line3\n']
f.writelines(lines)

# as this is "w-write" it will overwrite and to add this to existing content we use append command

# Keep in mind that the writelines() method does not add newline characters between the strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each string separately:

f=open("myfile3.txt","w")
lines=['line1\n','line2\n','line3\n']
for line in lines:
    f.write(line+'\n')
f.close()

# It is also a good practice to close the file after you are done with it.

# myfile3.txt is a file used from within this file












































