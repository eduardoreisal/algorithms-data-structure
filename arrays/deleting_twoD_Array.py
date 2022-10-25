import numpy as np

two_dimensional = np.array([
    [11,15,10,6], 
    [10,14,11,5], 
    [12,17,12,8], 
    [15,18,14,9]])


print(two_dimensional)

# axis = 0 == rol
# axis = 1 == col
# 0 here represents col or row
new_array = np.delete(two_dimensional, 0, axis = 0)
print('*'*20)
print(new_array)
