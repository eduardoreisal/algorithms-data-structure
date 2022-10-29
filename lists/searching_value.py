my_list = [1,2,3,4,5,6,7,8,9]
print(my_list)

if 3 in my_list:
    print(my_list.index(3))
else:
    print('[-] Value not found')

def search_element(list, value):
    for index,num in enumerate(list):
        if num == value:
            return f'[+] Value found. Index: {index}'
    return '[-] Value not found'


search_element(my_list, 9)
