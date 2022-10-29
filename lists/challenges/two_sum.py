# Write a program to find all pairs of integers whose sum is equal to a given number.
# [2,6,3,9,11]       9 ----> [6,3]

def find_pairs(array:'array of values', num: 'target value')->'index of values':
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                continue
            elif array[i] + array[j] == num:
                print(i, j)

def main():
    if __name__ == '__main__':
        find_pairs([2,6,3,9,11], 9)
        
        find_pairs([2,7,11,15], 9)

        find_pairs([3,2,4], 6)

        find_pairs([3,3], 6)

main()
