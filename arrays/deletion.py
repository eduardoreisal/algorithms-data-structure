from array import *

arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d', [1.3,1.4,1.6])

def remove_function(array, value):
    array.remove(value)
    print(array)

def remove(array, value):
    my_array = []
    for element in array:
        if element != value:
            my_array.append(element)
    return(my_array)


print(remove(arr1, 5))
remove_function(arr1, 4)
