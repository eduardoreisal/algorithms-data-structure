my_list = [1,2,3,4,5,6,7,8,9]

print(my_list)

my_list[0] = 100

print(my_list)

# Insert, first parameter position. Second parameter value
my_list.insert(0, 101)
print(my_list)

# Append. Adds value to the end of the list 
my_list.append(99)
print(my_list)

# Extend
new_list = [11,12,13,14,15,16,17,18,19]
my_list.extend(new_list)
print(my_list)
