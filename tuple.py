my_tuple = ("samir", "sami", "shohan", "arbit", "ridwan", 1, 2, 3.50, False) # A tuple is an immutable data type in python.
print(my_tuple) #('samir', 'sami', 'shohan', 'arbit', 'ridwan', 1, 2, 3.5, False)


# TUPLE INDEXING

print(my_tuple[0]) #samir
print(my_tuple[0:9]) #['samir', 'sami', 'shohan', 'arbit', 'ridwan', 1, 2, 3.5, False]


# TUPLE METHODS

print(my_tuple.count(2)) #1

print(my_tuple.index(2)) #6

print(len(my_tuple)) #9


num_tuple = (1,2,3)

print(num_tuple + my_tuple) #(1, 2, 3, 'samir', 'sami', 'shohan', 'arbit', 'ridwan', 1, 2, 3.5, False)

print(num_tuple * 2) #(1, 2, 3, 1, 2, 3)

a, b, c = num_tuple

print(a) #1
print(b) #2
print(c) #3

print(2 in num_tuple) #True