# Best solution to calculate powers using recursion
# Algorithms anda data structures page 173
def power(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x,n // 2)
        result = partial * partial
        # TODO: Research the reason this funcion is much better
        if n % 2 == 1:
            result *= x 
        print(partial, result)
        return result

print(power(5, 5))
