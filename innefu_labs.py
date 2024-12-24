dict1 = {'a': 1, 'b': 2, 'c': 3, 'd':4}
dict2 = {'a': 5, 'b': 6, 'c': 7, 'e':4}
# output = {'a': 6, 'b': 8, 'c': 10, 'd':4, 'e': 4}

combined_dict = {k:(dict1.get(k, 0)) +(dict2.get(k, 0))    for k in dict1.keys() | dict2.keys() }

print(combined_dict)
nested_list = [1, 2, 3, 4, [5, 6, 7], 8]

# Flattening a list using list comprehension
flattened_list = [
    item 
    for sublist in nested_list 
    for item in (sublist if isinstance(sublist, list) else [sublist])
]

print(flattened_list)
