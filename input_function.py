""" input function in python is used to take input from the user. input function returns a string value. """

# Input function

input_text = input("Enter your name: ") # takes name as a input from the user
print("Welcome to python", input_text) # prints the input text


input_num1 = input("Enter your 1st number: ") # takes number as a input from the user
input_num2 = input("Enter your 2nd number: ") # takes another number as a input from the user

print(f"1st number is {type(input_num1)} and 2nd number is {type(input_num2)}") # both numbers are return string values

""" if we want to convert the input text to integer or float, we can use int() or float() function """

input_num1 = input("Enter your 1st number: ") # takes number as a input from the user
input_num2 = input("Enter your 2nd number: ") # takes another number as a input from the user

print(int(input_num1) + int(input_num2)) # converts input text to integer and adds them
print(int(input_num1) - int(input_num2)) # converts input text to integer and subtracts them
print(int(input_num1) * int(input_num2)) # converts input text to integer and multiplies them
print(int(input_num1) / int(input_num2)) # converts input text to integer and divides them


