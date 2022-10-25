import numpy as np

two_dimensional = np.array([
    [11,15,10,6], 
    [10,14,11,5], 
    [12,17,12,8], 
    [15,18,14,9]])


def search_value(array, element):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == element:
                return f"[+] Element found. Address: [{i}][{j}]"
    return "[-] Element not found. Try searching another value"

print(search_value(two_dimensional,14))
