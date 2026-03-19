# Opening Files

# file = open('filename.txt', 'mode') # Use the open() function to open a file


# Reading Files

# 'r' Read (default) - opens file for reading, error if file doesn't exist

file = open("filename.txt","r") # or, file = open("filename.txt") 
content = file.read() # read() - Read entire file
print(content)
file.close()

file = open("filename.txt","r")
content = file.read(100) # read(size) - Read specific number of characters
print(content)
file.close()

file  = open("filename.txt","r")
line1 = file.readline() # readline() - Read one line at a time
line2 = file.readline() # readline() - Read one line at a time
print(line1)
print(line2)
file.close()

file = open("filename.txt","r")
lines = file.readlines() # readlines() - Read all lines into a list
print(lines)
file.close()

file = open("filename.txt","r")
for line in file: # Loop through file (Most efficient)
    print(line.strip()) # removes newline characters
file.close()


# Writing to Files

# 'w' Write - creates new file or overwrites existing file if the file already have writen write() will remove the text then rewrite it.

file = open("filename.txt","w")
content = file.write("I'm coding in Python\n") # write() - Write string to file
print(content)
content = file.write('This is a new line.') # write() - Write string to file
print(content)
file.close()
  
file = open("filename.txt","w")
lines = ["HAY!!!\n", "IT'S MEH!!!\n"]
content = file.writelines(lines) # writelines() - Write a list of strings
print(content)
file.close()


# Appending to Files

# 'a' Append - adds to the end of file, creates if doesn't exist

file = open("filename.txt","a")
content = file.write("SENPAI!!!") # Appending to Files
print(content)
file.close()


# Using with Statement  

# The with statement automatically closes the file, even if an error occurs.

with open("filename.txt","r") as file:
    content = file.read()
    print(content)



# Binary Files

with open("image.jpg","rb") as file:
    data = file.read() # Reading binary file
    print(data)

with open("copy.jpg","wb") as file:
    data = file.write(data) # Writing binary file
    print(data)


# File Position

with open("filename.txt") as file:
    content = file.tell() # tell() - Get current position
    print(content) #0 (at start)

    file.read(5)
    content = file.tell() # tell() - Get current position
    print(content) #5 (after reading 5 characters)

with open("filename.txt") as file:
    file.seek(0) # seek() - Move to specific position
    print(file.read()) #Move to beginning

    file.seek(5) # seek() - Move to specific position
    print(file.read()) #Move to position 10


# Checking if File Exists

import os
print(os.path.exists("filename.txt")) #True


# Read and Write

# "r+" Read and Write - file must exist

with open("filename.txt","r+") as file:
    content = file.read()
    print(content)

    content = file.write("\nHi!!!") # Write at current position (end of file after reading)
    print(content)



# Write and Read

# "w+" Write and Read - creates new file or overwrites

with open("filename.txt","w+") as file: # File is now EMPTY
    content = file.read()
    print(content)

    content = file.write("HELLO!!!") 
    print(content)


# Append and Read

# "a+" Append and Read - creates if doesn't exist

with open("filename.txt","a+") as file:
    content = file.write("\nHI!!!")
    print(content)


# Using Multiple Context Managers in a Single with Statement

with (

    open("filename.txt","r") as f1,
    open("image.jpg","rb") as f2
):

    print(f1.read())
    print(f2.read())