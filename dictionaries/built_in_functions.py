my_dict = {
        'name': 'Eduardo',
        'age': 28,
        'address': 'New Zealand',
        'education': 'Phd',
        }


# in operator only checks the value of keys
print('name' in my_dict)

# You need to use values() to check the value for values
print(28 in my_dict.values())

for key in my_dict:
    print(key)

# Checks if all values are True or all values are False
dictionary2 = {0: False, 1: False}
print(all(my_dict))
print(all(dictionary2))

# Sorted function. Sort using key values
dictionary3 = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(dictionary3))
print(sorted(dictionary3, reverse=True))
