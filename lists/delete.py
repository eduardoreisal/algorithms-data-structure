my_list = [1,2,3,4,5,6,7,8,9]

# Pop. Deletes last element from list
print(my_list)
print('*'*20)
my_list.pop(1) # 1 refers to index 1. if you don't provide an element, pop will remove last element
print(my_list)

# delete 
print('*'*20)
print(my_list)
del my_list[1]
print(my_list)

# remove. You can remove values
print('*'*20)
print(my_list)
my_list.remove(9)
print(my_list)
