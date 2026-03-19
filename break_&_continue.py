""" break in python is use to stop while loop """

while True:
    num = input("Enter a number (0 to quit): ")
    num = int(num)

    if num == 0:
        break
    
    else:
        print(f"Your number is {num}!")



""" continue in python is use to run while loop from starting without exequting bottom code """

while True:
    num = input("Enter a number (0 to quit): ")
    num = int(num)

    if num < 0:
        print("Pls enter a prositive number")
        continue

    if num == 0:
        break
    
    else:
        print(f"Your number is {num}!")
















