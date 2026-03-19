string = "Shamim Ahmed" # String is immutable which means that you can't change or modify them.

# length of string

length_string = len(string)
print(length_string) #12


# string index (in pytohn string indexis start from 0 to length - 1)

print(string[0]) #s
print(string[11]) #d

# string negative index (in pytohn string negative index is start from -1 to length)

print(string[-12]) #s
print(string[-1]) #d


# STRING SLICING 

print(string[0:12]) #Shamim Ahmed
print(string[0:6]) #Shamim
print(string[:6]) #Shamim
print(string[0:]) #Shamim Ahmed

# STRING NEGATIVE SLICING 

print(string[-12:-1]) #Shamim Ahme
print(string[-12:]) #Shamim Ahmed
print(string[-5:]) #Ahmed
print(string[-12:-6]) #Shamim or print(string[0:6])


# SLICING WITH SKIP VALUE

print(string[0:12:2]) #Sai he
print(string[0:12:1]) #Shamim Ahmed
print(string[::1]) #Shamim Ahmed
print(string[::-1]) #demhA mimahS


# STRING FUNCTIONS

print(len(string)) #12 (its return the length of the string)
print(string.startswith("S")) #True (yeah the string is start with "S")
print(string.endswith("h")) #False (nope the string isn't end with "h")
print(string.count("a")) #1 (the number of "a" in my string is 1)
print(string.capitalize()) #Shamim ahmed
print(string.upper()) #SHAMIM AHMED
print(string.lower()) #shamim ahmed
print(string.title()) #Shamim Ahmed
print(string.swapcase()) #sHAMIM aHMED
print(string.find("mim")) #3 (find the index number of "mim" in my string if output is -1 it's means there are no "mim" in this string)
print(string.replace("Shamim","Nahid")) #Nahid Ahmed (replace "Shamim" to "Nahid")
print(string.isspace()) #False (it's means the string is not empty by space)


# JOIN METHOD

l = ["Shamim","Ahmed", "Nahid"]
nl = " ".join(l)
print(nl) # Shamim Ahmed Nahid

nl = ", ".join(l)
print(nl) # Shamim, Ahmed, Nahid

nl = "-".join(l)
print(nl) # Shamim-Ahmed-Nahid


# FORMAT METHOD

str_ = "{} {}!".format("Hello","World")
print(str_) # Hello World!

str_ = "{1} {0}!".format("Hello","World")
print(str_) # World Hello!


# ESCAPE SEQUENCE CHARACTERS

print("Hello, \nShamim Ahmed") #\n = Newline
# output: 
# Hello, 
# Shamim Ahmed

print("""Name:\tShamim Ahmed
Age:\t16""") #\t = Tab
# outpur:
# Name:   Shamim Ahmed
# Age:    16

print("C:\\User\\ShamimOfficial") #\\ = Backslash
# output:
# C:\User\ShamimOfficial

print("One day i will be a \"Grade Programer\"") #\" = Double quote
# output:
# One day i will be a "Grade Programer"

print('One day i will be a \'Grade Programer\'') #\' =  Single quote
# output:
# One day i will be a 'Grade Programer'


print("Hello,\b World") #\b = Backspace
# output:
# Hello World


# F-Strings (Formatted String)

name = "Shamim Ahmed"
print(f"My name is {name}")
# output: My name is Shamim Ahmed

# Formatting Numbers

pi = 3.14159265359
print(f"{pi:.2f}") #3.14
print(f"{pi:.4f}") #3.1416

number = 1234567.89
print(f"{number:,}") #1,234,567.89
print(f"{number:,.1f}") #1,234,567.9

# Alignment and padding

name = "Shamim"
print(f"{name:>10}") #Right align
print(f"{name:<10}") #Left align
print(f"{name:^10}") #Center align

number = 2025
print(f"{number:010}") #0000002025


# R-Strings (Raw Strings)

path = r"C:\User\New\Home"
print(path) #C:\User\New\Home


# Combining F-Strings and R-Strings

name = "shamimofficial"
print(fr"C:\User\{name}\Python") #C:\User\shamimofficial\Python
print(rf"C:\User\{name}\Python") #C:\User\shamimofficial\Python