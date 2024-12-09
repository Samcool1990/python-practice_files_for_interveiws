# Write function which will find the second lowest element without using indexing, sort, set method. Use min 
# & max to find the element

lst = [3,9,3,6,3,4]

min_val = min(lst)
max_val = max(lst)
print(min_val, max_val)
second_element = 0
for i in lst:
    if i > min_val and i < max_val:
        second_element = i
print(second_element)