####Fibonnaci series###
#by using while loop
def fibonacci(n):
    a,b = 0,1
    print(a)
    while (b<n):
        print(b)
        a,b = b, a+b

fibonacci(5)

#By using for loop
def fibonacci2(n):
    a,b=0,1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fibonacci2(5)
        
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