# Walrus Operator (:=) allows assignment inside an expression it also known as "assignment expression."

print(x := "Hello World!") # assign value to x AND return the value
print(x) # Hello World!


if (list_ := len([1,2,3,4,5,6,7,8,9])) > 8:
    print(list_) # 9
        
else:
    pass



while str_ := input("") != "quit":
    print(str_) # True

else:
    exit() # break the code



try:
    with open("filename.txt","r") as file:
        for i in (content := file.readlines()):
            print(i, end="") 

except Exception as e:
    print(e)