from array import *

arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d', [1.3,1.4,1.6])

def search_in_array(array, value):
    for index,num in enumerate(array):
        if num == value:
            return index
    return "The element does not exist in this array"

print(search_in_array(arr1, 3))
