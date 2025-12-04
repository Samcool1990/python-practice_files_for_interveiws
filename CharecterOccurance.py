# Least occuring charecter
def least_charecter_occurance(s):
    ch = {}
    for i in s:
        if i in ch:
            ch[i] = ch[i] + 1
        else:
            ch[i] = 1
    print("result1", ch)
    result = min(ch, key=ch.get)
    print("result2", result)
    return result


print("result3", least_charecter_occurance("asdasfsdgfhfghfghgddd"))

# Using Counter
from collections import Counter

s = "asdasfsdgfhfghfghgddd"
ch = Counter(s)
ch = min(ch, key=ch.get)
print(ch)


# Count of any particular element usin dictionary
def count_charecter_occurance2(s, search_char):
    ch = {}
    for i in s:
        if i in ch:
            ch[i] = ch[i] + 1
        else:
            ch[i] = 1
    print(ch)
    try:
        print(ch[search_char])
    except:
        print(0)


count_charecter_occurance2("asdasfsdgfhfghfghgddd", "a")


# Count all the elements


def least_charecter_occurance4(s):
    ch = {}
    for i in s:
        if i in ch:
            ch[i] = ch[i] + 1
        else:
            ch[i] = 1
    print(ch)


least_charecter_occurance4("aakkbjjgasdlkjjjlfof")



# Python
s = "asdasfsdgfhfghfghgddd"
d = {c: s.count(c) for c in set(s)}
print(d)



s = "asdasfsdgfhfghfghgddd"
d = {}
for i in s:
    d[i] = d.get(i,0) +1
print(d)