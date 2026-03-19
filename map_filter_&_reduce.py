# map() Function
# Applies a function to every item in an iterable (like list, tuple).
# map(function, iterable)

nums_list = [1,2,3,4,5]
cube = lambda nums_list : nums_list ** 3
print(list(map(cube, nums_list))) # [1, 8, 27, 64, 125]


# filter() Function
# Filters elements based on a condition (True/False function)
# filter(function, iterable)

nums_list = [1,2,3,4,5]
even = lambda nums_list : nums_list % 2 == 0
print(even(2)) # True
print(even(1)) # False
print(list(filter(even, nums_list))) # [2, 4]


# reduce() Function
# Applies a function cumulatively to reduce iterable to a single value
# reduce(function, iterable)
# Import Required

from functools import reduce

nums_list = [1,2,3,4,5]
sum = lambda x, y : x + y
print(reduce(sum, nums_list)) # 15