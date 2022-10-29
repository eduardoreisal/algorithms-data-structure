# Find the missing number in an integer array of 1 to 100

import random

def create_list_with_missing_number():
    full_list = list(range(1,101))
    list_with_missing_num = full_list
    list_with_missing_num.pop(random.randrange(len(full_list)))
    return list_with_missing_num

# def get_missing_num(array_missing_num):
#     full_list = list(range(1,101))
#     for i in range(len(full_list)):
#         if full_list[i] != array_missing_num[i]:
#             return full_list[i]

def get_missing_num(array_missing_num, n):
    if array_missing_num[n] != n + 1:
        return n + 1 
    else:
        return get_missing_num(array_missing_num, n + 1)

def main():
    if __name__ == '__main__':
        my_list = create_list_with_missing_number()
        missing_num = get_missing_num(my_list, 0)
        print(my_list)
        print(f"Missing num: {missing_num}")

main()
