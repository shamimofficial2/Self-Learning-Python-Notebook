my_dict = {
    "Name" : "Shamim Ahmed Nahid",
    "Age" : 16,
    "Hobby" : {
        "Coding" : "Python",
        "Study" : "Math"

    } # Nested Dictionary

} # Dictionary is a collection of keys-value pairs, dictionary is mutable and it's Cannot contain duplicate keys.

print(my_dict) #{'Name': ' Shamim Ahmed Nahid', 'Age': 16, 'Hobby': {'Coding': 'Python', 'Study': 'Math'}}


# DICTIONARY INDEXING

print(my_dict["Name"]) #Shamim Ahmed Nahid
print(my_dict["Age"]) #16
print(my_dict["Hobby"]) #{'Coding': 'Python', 'Study': 'Math'}
print(my_dict["Hobby"]["Coding"]) #Python
print(my_dict["Hobby"]["Study"]) #Math


# CHECKING KEYS

if "Name" in my_dict: # Check if key exists
    print("Name exists") #Name exists

if "Shamim Ahmed Nahid" in my_dict.values(): # Check if value exists
    print("Name exists") # Name exists

if "City" not in my_dict: # Check if key doesn't exist
    print("City doesn't exist") #City doesn't exist

if "Bangladesh" not in my_dict.values(): # Check if value doesn't exist
    print("City doesn't exist")


# GETTING DICTIONARY SIZE

print(len(my_dict)) #3


# ITERATING OVER DICTIONARIES

for key in my_dict: # Iterate over keys (default)
    print(key)
            #Name
            #Age
            #Hobby

for key in my_dict.keys(): # Iterate over keys explicitly
    print(key)
            #Name
            #Age
            #Hobby

for value in my_dict.values(): # Iterate over values
    print(value)
            #Shamim Ahmed Nahid
            #16
            #{'Coding': 'Python', 'Study': 'Math'}

for key, value in my_dict.items(): # Iterate over key-value pairs
    print(f"{key}: {value}")
            # Name: Shamim Ahmed Nahid
            # Age: 16
            # Hobby: {'Coding': 'Python', 'Study': 'Math'}


# GETTING ALL KEYS OR VALUES AS A LIST

keys_list = list(my_dict.keys())
print(keys_list) #['Name', 'Age', 'Hobby']

values_list = list(my_dict.values())
print(values_list) #['Shamim Ahmed Nahid', 16, {'Coding': 'Python', 'Study': 'Math'}]

items_list = list(my_dict.items())
print(items_list) #[('Name', 'Shamim Ahmed Nahid'), ('Age', 16), ('Hobby', {'Coding': 'Python', 'Study': 'Math'})]


# DICTIONARY MERGE

dict1 = {"a":1,"b":2}
dict2 = {"c":3,"d":4}

print(dict1 | dict2) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# DICTIONARY METHODS

my_dict = my_dict.get("Name") # get() - Returns the value for a key, or a default value if the key doesn't exist 
print(my_dict) #Shamim Ahmed Nahid

my_dict = my_dict.get("Country") # get() - Returns the value for a key, or a default value if the key doesn't exist 
print(my_dict) #None (default)

my_dict = my_dict.get("Country","Not Found") # get() - Returns the value for a key, or a default value if the key doesn't exist 
print(my_dict) #Not Found 


my_dict = my_dict.keys() # keys() - Returns a view of all keys in the dictionary.
print(my_dict) #dict_keys(['Name', 'Age', 'Hobby'])

my_dict = my_dict["Hobby"].keys() # keys() - Returns a view of all keys in the dictionary.
print(my_dict) #dict_keys(['Coding', 'Study'])


my_dict = my_dict.values() # values() - Returns a view of all values in the dictionary.
print(my_dict) #dict_values(['Shamim Ahmed Nahid', 16, {'Coding': 'Python', 'Study': 'Math'}])

my_dict = my_dict["Hobby"].values() # values() - Returns a view of all values in the dictionary.
print(my_dict) #dict_values(['Python', 'Math'])


my_dict = my_dict.items() # items() - Returns a view of all key-value pairs as tuples.
print(my_dict) #dict_items([('Name', 'Shamim Ahmed Nahid'), ('Age', 16), ('Hobby', {'Coding': 'Python', 'Study': 'Math'})])

for key, value in my_dict.items(): # items() - Returns a view of all key-value pairs as tuples.
    print(f"{key} : {value}") # loop dict
    #Name : Shamim Ahmed Nahid
    #Age : 16
    #Hobby : {'Coding': 'Python', 'Study': 'Math'}

for key, value in my_dict["Hobby"].items(): # items() - Returns a view of all key-value pairs as tuples.
    print(f"{key} : {value}") # loop dict
    # Coding : Python
    # Study : Math


my_dict.update({"Age" : 17}) # update() - Updates the dictionary with key-value pairs from another dictionary or iterable.
print(my_dict) #{'Name': 'Shamim Ahmed Nahid', 'Age': 17, 'Hobby': {'Coding': 'Python', 'Study': 'Math'}}


my_dict.pop("Hobby") # pop() - Removes a key and returns its value. Raises KeyError if key doesn't exist (unless default is provided).
print(my_dict) #{'Name': 'Shamim Ahmed Nahid', 'Age': 16}

my_dict = my_dict.pop("City", "Not Found") # pop() - Removes a key and returns its value. Raises KeyError if key doesn't exist (unless default is provided).
print(my_dict) #Not Found


my_dict = my_dict.popitem() # popitem() - Removes and returns the last inserted key-value pair as a tuple.
print(my_dict) #('Hobby', {'Coding': 'Python', 'Study': 'Math'})


my_dict.clear() # clear() - Removes all items from the dictionary.
print(my_dict) #{}


Age = my_dict.setdefault("Age", 17) # setdefault() - Returns the value of a key if it exists, otherwise inserts the key with a default value and returns it.
print(Age) #16
print(my_dict) #{'Name': 'Shamim Ahmed Nahid', 'Age': 16, 'Hobby': {'Coding': 'Python', 'Study': 'Math'}}

City = my_dict.setdefault("City", "Bangladesh") # setdefault() - Returns the value of a key if it exists, otherwise inserts the key with a default value and returns it.
print(City) #1Bangladesh
print(my_dict) #{'Name': 'Shamim Ahmed Nahid', 'Age': 16, 'Hobby': {'Coding': 'Python', 'Study': 'Math'}, 'City': 'Bangladesh'}


new_dict = my_dict.copy() # copy() - Returns a shallow copy of the dictionary.
print(new_dict) #{'Name': 'Shamim Ahmed Nahid', 'Age': 16, 'Hobby': {'Coding': 'Python', 'Study': 'Math'}}


my_dict = my_dict.fromkeys(my_dict, "Unknown") # fromkeys() - Creates a new dictionary from a sequence of keys with a specified value (class method).
print(my_dict) #{'Name': 'Unknown', 'Age': 'Unknown', 'Hobby': 'Unknown'}
