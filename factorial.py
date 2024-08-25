# #########
# from unicodedata import digit

def factorial_recurssion(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recurssion(n-1)
print(factorial_recurssion(5))
def factorial(n):
    facto = 1
    for i in range(1,n+1):
        facto = facto * i
    return facto
print("Result>>>>>>",factorial(5))

#######Wheather number follows tha case
def sum_of_facto(n):
    temp = n
    sum =0
    while temp >0:
        digit = temp%10
        temp = temp //10
        facto = factorial(digit)
        sum = sum + facto
    if sum == n:
        print("Yes",sum)
    else:
        print('No')

sum_of_facto(135)
#######Print list of numbers that follows the case within interval
def sum_of_facto2(start,end):
    for n in range(start,end):
        temp = n
        sum = 0
        while (temp >0):
            digit = temp % 10
            temp = temp //10
            facto = factorial(digit)
            sum = sum + facto

    
        if sum == n:
            print(n)
       
sum_of_facto2(1,200000)