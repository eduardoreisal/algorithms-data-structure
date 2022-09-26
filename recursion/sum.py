#!/bin/python

# How to find the sum of digits of a positive number using recursion?

# TODO: Check if num is a positive Integer
def check_num(num):
    num = int(num)
    if num > 0 and int(num) == num:
        return num
    else:
        return None

# TODO: Find Sum of digits
def find_sum(num):
    if num == 0:
        return num
    else:
        return int(num%10) + find_sum(int(num/10))

def main():
    while True:
        num = input("Enter number: ")
        num = check_num(num)
        print(find_sum(num))

if __name__ == '__main__':
    main()
