# The major difference between tuples and list is: Tuples are imutable, and lists are mutable

list1 = [0,1,2,3,4,5,6,7,8,9]
print(list1)

for index,value in enumerate(list1):
    list1[index] = value * 2

print(list1)
list1.pop(0)
print(list1)

tuple1 = (0,1,2,3,4,5,6,7,8,9)
print(tuple1)
# It's not possible to reassign a single value 
# But it's possible to reassign the entire tuples
tuple1 = (9,8,7,6,5,4,3,2,1,0)
print(tuple1)
# It is possible to delete the entire tuple, but you can't delete single elements
