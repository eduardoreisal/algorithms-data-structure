
def check_uniqueness(array):
    new_array = []
    for value in array:
        if value not in new_array:
            new_array.append(value)
        else:
            print(f'[-] The value {value} is already present in the list')
            break
    if len(new_array) == len(array):
        print('[+] array of unique elements')
    else:
        print(sorted(array))
        print('[-] not all elements are unique')

array = [1,20,30,44,5,56,57,8,19,10,31,12,13,14,35,16,27,58,19,21]
check_uniqueness(array)
