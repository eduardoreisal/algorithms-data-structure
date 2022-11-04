# Check if array contains a number in python

my_list  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def find_num(array, number):
    for index, element in enumerate(array):
        if element == number:
            print(f'[+] Element found in index {index}')


find_num(my_list, 1)
