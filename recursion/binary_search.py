def binary_search(data, target, low, high):
    """ 
    Return True if target is found in indicated portion of a Python list.
    The search only considers the portion from data[low] to data[high] inclusive
    """
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 14
low = 0
high = 15
print(binary_search(data, target, low, high))
