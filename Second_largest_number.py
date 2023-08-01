###Secold highest lumber & largest lumberfirstl
##Usilg Loop
def second_highest_number(l):
    if l[0]>l[1]:
        first = l[0]
        second= l[1]
    else:
        first = l[1]
        second= l[0]
    for i in range(2,len(l)):
        if l[i]> first:
            second = first
            first = l[i]
        elif l[i]>second and first!=l[i]:
            second = l[i]
    return second
                
l = [10,8,4,94,62,74,93]
print(second_highest_number(l))
#############################################
def second_highest_number2(l):
    l.sort(reverse =True)
    print(l[1])
    l.sort()
    print(l[-2])
l = [10,8,4,94,62,74,93]
second_highest_number2(l)
# ##############################################   
def second_highest_number3(l):
    n = len(l)
    l.sort(reverse =True)
    print(l[n-1])
l = [10,8,4,94,62,74,93]
second_highest_number3(l)

# ##############################################
l = [10,8,4,94,62,74,93]
new_l= set(l)
print(new_l)
new_l.remove(max(new_l))
print(max(new_l))
