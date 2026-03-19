my_set = {"samir", "sami", "shohan", "arbit", "ridwan", 1, 2, 3.50, False}

# Sets are unordered
# Sets are unindexed
# There is no way to change items in sets.
# Sets cannot contain duplicate values


# SET METHODS

my_set.add("shamim") # add() - Adds a single element to the set.
print(my_set) #{False, 1, 2, 3.5, 'shamim', 'sami', 'ridwan', 'arbit', 'shohan', 'samir'}

my_set.update({"HI","Hello"}) # update() - Adds multiple elements from another iterable.
print(my_set) #{False, 'shohan', 'arbit', 'ridwan', 1, 2, 3.5, 'samir', 'Hello', 'HI', 'sami', 'shamim'}

my_set.remove("HI") # remove() - Removes a specific element (raises error if not found).
print(my_set) #{False, 1, 2, 'ridwan', 3.5, 'samir', 'shamim', 'shohan', 'sami', 'arbit', 'Hello'}

my_set.discard("Hello") # discard() - Removes a specific element (no error if not found).
print(my_set) #{False, 1, 'samir', 'arbit', 2, 3.5, 'shohan', 'ridwan', 'shamim', 'sami'}

my_set.pop() # pop() - Removes and returns a random element.
print(my_set) #{1, 2, 3.5, False, 'shohan', 'sami', 'samir', 'arbit', 'shamim'}

my_set.clear() # clear() - Removes all elements from the set.
print(my_set) #set()



# OPERATIONS ON SETS

# union() or | - Returns all elements from both sets.

set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2)) #{1, 2, 3, 4, 5}

# or use |

print(set1 | set2) #{1, 2, 3, 4, 5}


# intersection() or & - Returns common elements in both sets.

set1 = {1,2,3}
set2 = {3,4,5}

print(set1.intersection(set2)) #{3}

# or use &

print(set1 & set2) #{3}


# difference() or - - Returns elements in first set but not in second.

set1 = {1,2,3,4}
set2 = {3,4,5}

print(set1.difference(set2)) #{1, 2}

# or use -

print(set1 - set2) #{1, 2}


# symmetric_difference() or ^ - Returns elements in either set, but not in both.

set1 = {1,2,3}
set2 = {3,4,5}

print(set1.symmetric_difference(set2)) #{1, 2, 4, 5}

# or use ^

print(set1 ^ set2) #{1, 2, 4, 5}