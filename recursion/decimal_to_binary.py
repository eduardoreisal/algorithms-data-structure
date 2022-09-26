#!/bin/python

# Convert a Decimal to Binary

def decimal_to_binary(num):
    if num == 0:
        return 0
    else:
        return num%2 + 10 * decimal_to_binary(int(num/2))

print(decimal_to_binary(13))
