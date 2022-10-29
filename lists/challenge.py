'''
Create a program to receive n inputs from the user, the program may quit when the user
enter 'done'. The program will return the average between the numbers received.
Use lists
'''

def check_valid_value(num):
    if isinstance(num, int):
        if num > 0:
            return True
    return False

def calc_avg(array):
    return sum(array) / len(array)

def main():
    if __name__ == '__main__':
        nums_list = []
        while True:
            value = int(input('[+] Enter value or type 0 to exit: '))
            if check_valid_value(value):
                nums_list.append(value)
            else:
                print('[-] Exiting program')
                break
        print(f'Avg: {calc_avg(nums_list)}')

main()

