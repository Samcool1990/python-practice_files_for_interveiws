#Using While Loop
def armstrong(n):
    sum = 0
    temp=n
    while temp>0:
        digit= temp%10
        sum= sum + (digit*digit*digit)
        temp= temp//10
    if n == sum :
        return True
    else:
        return False
    
print(armstrong(10))

#Using For Loop
def armstrong2(start,end):
    for n in range(start,end):        
        sum = 0
        temp=n
        while temp>0:
            digit= temp%10
            sum= sum + (digit*digit*digit)
            temp= temp//10
        if n == sum :
            print(n)
        
armstrong2(10,1000)
    