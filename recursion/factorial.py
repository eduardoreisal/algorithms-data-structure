import sys
sys.setrecursionlimit(10000) # You can increase stack memory this way

def factorial(num):
    if num in [0, 1]:
        return 1
    else:
        return num * factorial(num-1)

def check_num_requirements(num):
    assert num >= 0 and int(num) == num, '[-] You need to enter a positive Integer'

def main():
    if __name__ == '__main__':
        num = int(input("Enter a number: "))
        check_num_requirements(num)
        print(f"Factorial of {num}: {factorial(num)}")

main()

