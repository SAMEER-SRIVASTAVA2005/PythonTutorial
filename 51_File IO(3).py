# seek() and tell() functions
# In Python, the seek() and tell() functions are used to work with file objects and their positions within a file. These functions are part of the built-in io module, which provides a consistent interface for reading and writing to various file-like objects, such as files, pipes, and in-memory buffers.

# seek() function
# The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position

# tell() function
# The tell() function returns the current position within the file, in bytes. This can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position. For example:


# for example-
with open("myfile4.txt","r") as f:
    print(type(f))        #this means all these process are happening from inside of built-in io module

    f.seek(16)     # move(get onto) to 16th byte in the file

    print(f.tell())           #this will give seek position(the current position in the file)

    print(f.read(7))         #read the next 7 bytes after getting to 16th byte


# truncate() function
# When you open a file in Python using the open function, you can specify the mode in which you want to open the file. If you specify the mode as 'w' or 'a', the file is opened in write mode and you can write to the file. However, if you want to truncate the file to a specific size, you can use the truncate function.

with open("myfile5.txt","w") as f:
    f.write("hello samayara")
    f.truncate(9)       #truncate means jitna part chahiye utna part utha rhe bs
    
    #it count simple (counts spaces too, not start from 0 (start from 1))

with open("myfile5.txt","r") as f:
    print(f.read())


# myfile4.txt and myfile5.txt are other files related to this file

















