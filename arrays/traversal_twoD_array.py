import numpy as np

two_dimensional = np.array([
    [11,15,10,6], 
    [10,14,11,5], 
    [12,17,12,8], 
    [15,18,14,9]])

def traverse_array(array):
    for i in array:
        for j in i:
            print(j)


traverse_array(two_dimensional)
