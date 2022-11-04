new_tuple = ('a', 'b', 'c', 'd', 'e')

def search(tuple, target_value):
    for value in tuple:
        if value == target_value:
            return 'Found'
    return 'Not Found'

print(search(new_tuple,'d'))
print(search(new_tuple,'z'))

