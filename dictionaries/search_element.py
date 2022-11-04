myDict = {'name': 'Eduardo', 'age': 26, 'address': 'New Zealand'}

def search_dict(dict, target_value):
    for key,value in dict.items():
        if target_value == value:
            print(key, value)


search_dict(myDict, 26)

