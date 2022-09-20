def calc_fibonacci(num):
    if num in [0, 1]:
        return num 
    else:
        return calc_fibonacci(num-1) + calc_fibonacci(num-2)

def check_num(num):
    try:
        fibo = int(num)
        print(calc_fibonacci(fibo))
    except RecursionError:
        print('[-] Recursion Error. You need to enter a positive Integer.')
    except ValueError:
        print('[-] Value Error. Make Sure to Enter an Integer.')


def main():
    while True:
        fibo = input("[+] Enter the nth fibonacci number you want to find: ")
        check_num(fibo)

if __name__ == '__main__':
    main()
