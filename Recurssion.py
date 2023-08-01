def reverse_lst(lst):
    if not lst:
        return []
    return [lst[-1]] + reverse_lst(lst[:-1])


print(reverse_lst([1,6,9,4,5]))


def reverse_str(str):
    if not str:
        return ""
    return str[-1] + reverse_str(str[:-1])


print(reverse_str("Suman"))

##RECURSSION##
def fibonacci3(n):
    if n<=1:
        return n
    else:
        return (fibonacci3(n-1)+fibonacci3(n-2))
n=5
if n<=0:
    print("Put valid number")
else:
    for i in range(n):
        print(fibonacci3(i))


