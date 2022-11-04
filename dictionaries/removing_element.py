# Removing element from dictionary

myDict = {'name': 'Eduardo', 'age': 26, 'address': 'New Zealand'}

print(myDict)
print(myDict.pop('name'))
print(myDict)
myDict.clear()  # -> Delete everything from dictionary
print(myDict)


myDict = {'name': 'Eduardo', 'age': 26, 'address': 'New Zealand'}
del myDict['age']
print(myDict)
