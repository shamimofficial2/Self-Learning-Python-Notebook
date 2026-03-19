my_list = ["samir", "sami", "shohan", "arbit", "ridwan", 1, 2, 3.50, False] # List is mutable which means we can change or modify them
print(my_list) #['samir', 'sami', 'shohan', 'arbit', 'ridwan', 1, 2, 3.5, False]


# LIST INDEXING

print(my_list[0]) #samir
print(my_list[0:9]) #['samir', 'sami', 'shohan', 'arbit', 'ridwan', 1, 2, 3.5, False]


# LIST METHODS

my_list.append("shamim") # append() - Adds a single element to the end of the list.
print(my_list) #['samir', 'sami', 'shohan', 'arbit', 'ridwan', 1, 2, 3.5, False, 'shamim']


my_list.extend(["Hello World", 2025]) # extend() - Adds all elements from another iterable to the end of the list.
print(my_list) #['samir', 'sami', 'shohan', 'arbit', 'ridwan', 1, 2, 3.5, False, 'shamim', 'Hello World', 2025]


my_list.insert(0,"HI") # insert() - Inserts an element at a specific position.
print(my_list) #['HI', 'samir', 'sami', 'shohan', 'arbit', 'ridwan', 1, 2, 3.5, False, 'shamim', 'Hello World', 2025]


my_list.remove("HI") # remove() - Removes the first occurrence of a specific value.
print(my_list) #['samir', 'sami', 'shohan', 'arbit', 'ridwan', 1, 2, 3.5, False, 'shamim', 'Hello World', 2025]


my_list.pop(0) # pop() - Removes and returns an element at a given index.
print(my_list) #['sami', 'shohan', 'arbit', 'ridwan', 1, 2, 3.5, False, 'shamim', 'Hello World', 2025]

#or

my_list.pop() # pop() - Removes the last element if no index is specified).
print(my_list) #['samir', 'sami', 'shohan', 'arbit', 'ridwan', 1, 2, 3.5, False, 'shamim', 'Hello World']


my_list.clear() # clear() - Removes all elements from the list.
print(my_list) #[]


idx = my_list.index("arbit") # index() - Returns the index of the first occurrence of a value.
print(idx) #3


count = my_list.count("samir") # count() - Returns the number of times a value appears in the list.
print(count) #1


new_list = my_list.copy() #copy() - Returns a shallow copy of the list.
print(new_list) #['samir', 'sami', 'shohan', 'arbit', 'ridwan', 1, 2, 3.5, False]


num_list = [1,2,3,7,6,5,4,8,9,0]

num_list.sort() # sort() - Sorts the list in place
print(num_list) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


num_list.reverse() # reverse() - Reverses the order of elements in place.
print(num_list) #[0, 9, 8, 4, 5, 6, 7, 3, 2, 1]


str_list = ["arbit","shamim","arup","ridwan"]

str_list.sort() # sort() - Sorts the list in place
print(str_list) #['arbit', 'arup', 'ridwan', 'shamim']


str_list.reverse() # reverse() - Reverses the order of elements in place.
print(str_list) #['ridwan', 'arup', 'shamim', 'arbit']


# List enumerate() function

list_ = ["Shamim","Ahmed","Nahid"]

for index, value in enumerate(list_):
    print(index,value) 
    # 0 Shamim
    # 1 Ahmed
    # 2 Nahid


# List Comprehensions

even_numbers = [i for i in range(1,11) if i % 2 == 0]
print(even_numbers) # [2, 4, 6, 8, 10]