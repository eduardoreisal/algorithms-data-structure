import numpy as np

two_dimensional = np.array([
    [11,15,10,6], 
    [10,14,11,5], 
    [12,17,12,8], 
    [15,18,14,9]])

def access_elements(array, row_index, col_index):
    if row_index >= len(array) and col_index >= len(array[0]):
        print('Incorrect index')
    else:
        print(array[row_index][col_index])

access_elements(two_dimensional, 1, 2)
