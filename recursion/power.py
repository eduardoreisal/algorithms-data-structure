def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

def convert_to_positive(num):
    if num < 0:
        num = num * -1
    return num

base = int(input('Enter base: '))
exponent = int(input('Enter exponent: '))
exponent = convert_to_positive(exponent)
print(power(base, exponent))
