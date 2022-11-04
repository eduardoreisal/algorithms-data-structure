# Loop trough dictionary

myDict = {'name': 'Eduardo', 'age': 26, 'address': 'New Zealand'}

def loop_dict(dictionary):
    for key,value in dictionary.items():
        print(key, value)

loop_dict(myDict)
