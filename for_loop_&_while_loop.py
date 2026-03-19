""" for loop in python helps to do the same thing at multipul times """

for i in range(10):
    print(i) # it's print 0 to 9 numbers 


for i in range(1,11):
    print(i) # it's print 1 to 10 numbers


result = 0
for i in range(51):
    result += i

print(result) # it's print the sum of 0 + 1 + 2 + 3 + ... + ... + ... + 50 which is 1275"


for i in range(5,51,5):
    print(i) # it's print 5 to 50 numbers and their difference between 5 numbers


result = 0
for i in range(1,101):
    if i % 5 == 0:
        print(i) # it's print 1 to 100 num which is perfectly divisible by 5
        result += i

print(result) # it's print the sum of 1 to 100 num which is perfectly divisible by 5


my_list = [10,20,30,50,40]
n = my_list[0]
for i in my_list:
    if i > n:
        n = i 
        
print(n) # it's print the max munber from the list 


saarc = ["Bangladesh", "Afghanistan", "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka"]

for i in saarc:
    print(f"{i} is the member of SAARC") # it's print all item on list

print(f"There are total {len(saarc)} countries") # it's print the number of the item on list 

country = input("Enter your country name: ")

if country in saarc:
    print(f"{country} is the member of SAARC") 

else:
    print(f"{country} isn't the member of SAARC")



""" while loop in python helps to do the same thing at multipul times """

i = 0
while i < 10:
    print(i) # it's print 0 to 9 numbers
    i += 1


i = 0
while i < 11:
    print(i) # it's print 1 to 10 numbers
    i += 1 


i = 0
result = 0
while i < 51:
    result += i
    i += 1

print(result) # it's print the sum of 0 + 1 + 2 + 3 + ... + ... + ... + 50 which is 1275"


i = 0
result = 0
while i < 101:
    if i % 5 == 0:
        print(i) # it's print 1 to 100 num which is perfectly divisible by 5
        result += i
    i += 1

print(result) # it's print the sum of 1 to 100 num which is perfectly divisible by 5 