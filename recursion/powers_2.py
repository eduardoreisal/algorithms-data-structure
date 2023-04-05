def powers(num1, num2):
    if num2 == 0:
        return 1
    else:
        return num1 * powers(num1, num2-1)

print(powers(5, 5))
