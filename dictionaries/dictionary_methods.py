my_dict = {
        'name': 'Eduardo',
        'age': 28,
        'address': 'New Zealand',
        'education': 'Phd'
        }

print(my_dict)

# Copy dictionary
new_dictionary = my_dict.copy()

# Remove all elements from dictionary
my_dict.clear()   

print(new_dictionary)

# Create new dictionary
dictionary3 = {}.fromkeys([1,2,3], 0)
print(dictionary3)

# Returns the False if the value is not found. If the value is found
# return the key value
print(new_dictionary.get('age', False))
print(new_dictionary.get('ages', False))

# Return a view object(Tuple) that display a list of objects
print(new_dictionary.items())

# Return all keys
print(new_dictionary.keys())

# Delete element randomly and return it 
print(dictionary3.popitem())
