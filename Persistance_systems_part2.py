list1 = [5, 7, 9, 7, 6, 9, 4]
n = len(list1)
for i in range(n):
    for j in range(i + 1, n):
        if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
print(list1)
list5 = [5, 7, 9, 7, 6, 9, 4]
print(">>>", sorted(list1, reverse=True))
list1.sort(reverse=True)
print(list5)


def odd(x):
    return x % 2 == 1


list2 = [5, 7, 9, 7, 6, 9, 4, 6, 4, 5, 9, 1, 3, 2]
result = filter(odd, list2)
print(list(result))


# # reverse a list without [::-1]
# list3 = [5,7,9,7,6,9,4]
# n = len(list3)
# for i in range(int(n/2)):
#     list3[i],list3[n-i-1] =  list3[n-i-1],list3[i]
# print('>>',list3)
def reverse_list(lst):
    if not lst:
        return []
    return lst[-1] + reverse_list(lst[:-1])


list4 = [
    {"name": "suman", "location": "kolkata"},
    {"name": "pathak", "location": "pune"},
    {"name": "sam", "location": "kolkata"},
]

d = {}
# tem_list = []
for i in list4:
    if i["location"] in d:
        tem_list = []
        tem_list.append(d[i["location"]])
        # tem_list.append(i)
        d[i["location"]] = tem_list
    else:
        d[i["location"]] = [i]
print(d)


def group_by_location(lst):
    grouped = {}  # This will hold the final grouped data

    for item in lst:
        location = item["location"]  # Extract the location
        if location not in grouped:  # If the location is not yet a key in grouped
            grouped[location] = [item]  # Create a new list with the current item
        else:
            grouped[location].append(
                item
            )  # Append the current item to the existing list

    return grouped


# Example usage
output = group_by_location(list4)
print(output)
