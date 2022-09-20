def power_of_two(n):
    if n == 0:
        return 1
    else:
        power = power_of_two(n - 1)
        return power * 2

def power_of_two_it(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power

if __name__ == '__main__':
    print(power_of_two(5))
    print(power_of_two_it(5))
