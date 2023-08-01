
my_list = [2, 3, 5, 7, 11, 12]
new_list = []
for i in my_list:
    if i%2==1:
        new_list.append(i ** 2)
    else:
        new_list.append(i)
# new_list =[i**2 for i in my_list if i%2==1]
print(new_list)
n = len(new_list)
for i in range(n):
    for j in range(i+1,n):
        if new_list[i] > new_list[j]:
            new_list[j],new_list[i] = new_list[i] , new_list[j]
print(new_list[::-1])



def fibonnaci(n):
    a,b = 0,1
    for i in range(n):
        if i ==1:
            print(a)
        elif i == 2:
            print(b)
        else:
            c=a+b
            a=b
            b=c
        yield c
    return c
print(next(fibonnaci(2)))
print(next(fibonnaci(135)))

str2 = 'persistentsystems'

d= {}

for i in str2:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
result = min(d, key=d.get(2))
print(result)
print(d)
        
        

    

