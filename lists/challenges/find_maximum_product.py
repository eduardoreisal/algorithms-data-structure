# Find maximum product of two integers in the array where all elements are positive

my_array = [1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21]


def find_maximum_product(array):
    value1 = 0
    value2 = 0
    for index,value in enumerate(array):
        if value1 < value2 or value1 == value2:
            if value > value1:
                value1 = value
        else:
            if value > value2:
                value2 = value
    print(value1 + value2)


find_maximum_product(my_array)

print(sorted(my_array))


