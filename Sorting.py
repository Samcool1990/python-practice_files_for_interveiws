#Sorting without SORT method
list1 = [5,7,9,7,6,9,4]
n = len(list1)
for i in range(n):
    for j in range(i+1,n):
        if list1[i]> list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
print(list1)

print(sorted(list1))
list1.sort()
new_lst = []
for i in list1:
    new_lst.append(i)
print(new_lst)

