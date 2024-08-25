s1 = 'inteview'
s2 = 'interview'

def is_anagram(s1,s2):
    d1 ={}
    d2 = {}
    for i in s1:
        d1[i] = d1.get(i,0) + 1

    for j in s2:
        d2[j] = d2.get(j,0) + 1

    if d1 == d2:
        print("TRUE")
    else:
        print("FALSE")

print(is_anagram(s1,s2))

#DJANGO ORM difference between get() & filter() with example