l1 = [1, 1, 2, 3, 3, 5]
d = {}
for i in l1:
    d[i] = d.get(i, 0) + 1
print(d)

l2 = [1, 1, 2, 3, 3, 5]
char_count = {char: l2.count(char) for char in l2}
print(char_count)


def fibonacci3(n):
    if n <= 1:
        return n
    else:
        return fibonacci3(n - 1) + fibonacci3(n - 2)


n = 5
if n <= 0:
    print("Put valid number")
else:
    for i in range(n):
        print(fibonacci3(i))
