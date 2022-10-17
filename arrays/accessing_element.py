from array import *

arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d', [1.3,1.4,1.6])

def access_element(array, index):
    if index > len(array) - 1 or index < 0:
        print('[-] You picked an inexistent index')
    else:
        print(array[index])

access_element(arr1, 4)
