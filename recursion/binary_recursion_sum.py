def sum(arr, start, stop):
    if start >= stop:
        return 0
    elif start == stop - 1:
        return arr[start]
    else:
        mid = (start + stop) // 2
        return sum(arr, start, mid) + sum(arr, mid, stop)

arr = [10,10,10,10,10]
print(sum(arr, 0, len(arr)))
