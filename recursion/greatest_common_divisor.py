#!/bin/python

# Find the greatest common divisor of two numbers without a remainder

def gcd(num1, num2):
    assert int(num1) == num1 and int(num2) == num2, 'The numbers must be integer only!'
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1%num2)

print(gcd(48, 18))
