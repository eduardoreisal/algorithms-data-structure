import numpy as np

two_dimensional = np.array([
    [11,15,10,6], 
    [10,14,11,5], 
    [12,17,12,8], 
    [15,18,14,9]])

print(two_dimensional)

# axis=1 will insert colum, axis=0 will insert row
new_TwoD_array = np.insert(two_dimensional, 0, [[1,2,3,4]], axis=1)
print("="*20)
print(new_TwoD_array)
print("="*20)
# To just append a new row to array
new_array = np.append(two_dimensional, [[10,20,30,40]], axis=0)
print(new_array)
