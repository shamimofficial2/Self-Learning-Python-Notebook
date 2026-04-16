""" def (definition) function in pytohn """

def function(num): # 'num' is a paramrter
    return num # return 123 as a output

print(function(123)) # '123' is a argument 



""" default argument in def function  """

def function(num1, num2 = 100, num3 = 200 ): # num2 = 100 & num3 = 200 is a default argument
    print(num1, num2, num3)

function(50) # return 50 100 200 as a output


def function(num1, num2 = 100, num3 = 200 ): # num2 = 100 & num3 = 200 is a default argument
    print(num1, num2, num3)

function(50,150,250) # return 50 150 250 as a output



""" scope in fynction """

num = 456 # it's a global scope you can print it inside/outside of a function

def function(num):
    global name # golbal in a kyeword which is manke local scope to global scope
    name = "shamim ahmed" # now it's a global scope you can print it inside/outside of a function
    print(num,name) # it's a local scope yon can only print it inside of a function

function(123) # it's retunr 123 as a output which is a local scope 
print(num,name) # it's retunr 456 as a output which is a global scope


""" Ternary Operator """

def fun(x):
    return "True" if x == 1 else "False"
    # value_if_true if condition else value_if_false

print(fun(1)) # True



""" *args & **kwargs """

# *args allows a function to accept multiple positional arguments.

def function(*args): # args is just a name; * is what matters
    print(args) # args return a tuple

print(function(1,2,3)) # (1, 2, 3)


# **kwargs allows a function to accept multiple keyword arguments.

def function(**kwargs): # kwargs is just a name; ** is what matters
    print(kwargs) # kwargs return a dictionary

print(function(Name = "Nahid", Age = 17)) # {'Name': 'Nahid', 'Age': 17}
