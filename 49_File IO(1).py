# Python provides several ways to manipulate files. Today, we will discuss how to handle files in Python.

# Opening a File
# Before we can perform any operations on a file, we must first open it. Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.
f=open("myfile.txt","r")
# print(f)       does not have much work (nothing in output)


# Modes in file
# There are various modes in which we can open files.

# read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

# write (w): This mode opens the file for writing only and creates a new file if the file does not exist.
# f=open("myfile2.txt","w")
# f.write('hello, world!')           
# above code will create file name "myfile2.txt" if it does not exists

# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

# create (x): This mode creates a file and gives an error if the file already exists.
# f=open("myfile2.txt","x")   #syntax

# text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).
f=open("myfile.txt","rt")


# binary (b): used to handle binary files (images, pdfs, etc).
f=open("myfile.txt","rb")
# output- b'hello, world!'       b represents binary

# READING FROM A FILE
print(f.read())     #reads the entire content of file and return it as a string

# Writing to a File
# to write to a file, we first need to open it in write mode
f=open("myfile2.txt","w")
f.write('hello, world!')           #this way we can write

# Keep in mind that writing to a file will overwrite its contents. If you want to append to a file instead of overwriting it, you can open it in append mode.

f=open("myfile.txt","a")
f.write("\nthis is the appended part")

# CLOSING a File
# It is important to close a file after you are done with it. This releases the resources used by the file and allows other programs to access it.

# To close a file, you can use the close() method.
f=open("myfile.txt","r")
# done something with this file then close
f.close()

# according to harry close krna chahiye but uske bina bhi execute ho jarha hai may be it has been updated in way that it works without using close()


# The 'with' statement
# Alternatively, you can use the with statement to automatically close the file after you are done with it. (you do not need to use close() at the end of your code)

with open("myfile2.txt","w") as f:
    f.write("""hey there! Sam this side
            Currently I am pursuing my B.tech from LPU""")


# here 
# myfile.txt and myfile2.txt are other files


# after knowing about the file handling we can store any data of our program in the file



