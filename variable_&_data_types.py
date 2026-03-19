""" Variable in python is used to store data values. """

# Variable 

text = "Hello World!"
print(text) # "text" is a variable of Hello World! 

num = 10 
print(num) # "num" is a variable of 10

name,age = "Shamim Ahmed Nahid", 16
print(name,age) # "name" is a variable of "Shamim Ahmed Nahid" and "age" is a variable of 16



""" Data types in python are used to define the type of data a variable can hold. """

# Numeric data types

num1 = 5 # integer
print(type(num1)) # <class 'int'>

num2 = 3.1416 #float
print(type(num2)) # <class 'float'>


# Sequence data types

text1 = "Hello Shamim!" # string
print(type(text1)) # <class 'str'>

my_list = [1,2,3,4,5] # list
print(type(my_list)) # <class 'list'>

my_tuple = (1,2,3,4,5) # tuple
print(type(my_tuple)) # <class 'tuple'>


# Dictionary data type

my_dict = {
    "Name" : "Shamim Ahmed Nahid",
    "Age" : 16,
} # dictionary
print(type(my_dict)) # <class 'dict'>


# Boolean data type

is_true = True # boolean
print(type(is_true)) # <class 'bool'>

is_false = False # boolean
print(type(is_false)) # <class 'bool'> 


# Set data type

my_set = {1,2,3,4,5} # set
print(type(my_set)) # <class 'set'>


# None data type

my_none = None # NoneType
print(type(my_none)) # <class 'NoneType'>