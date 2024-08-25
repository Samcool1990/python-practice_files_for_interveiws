#Prime number using FLAG
def prime_number(n):
    flag = False
    if n>1:
        for i in range(2,(n//2+1)):
            if n%i==0:
                flag = True
                break
    if flag:
        return "No! Its not a prime number"
    else:
        return "Yes! Its a prime number"     
    
print(prime_number(4))   

#Using for else
def prime_number2(n):
    if n>1:
        for i in range(2,(n//2+1)):
            if n%i==0:
                print("No")
                break
        else:
            print('Yes')
    else:
        print("No")
print(prime_number2(4))   

#Using start & end
def prime_number3(start, end):
    for n in range(start, end):
        if n>1:
            for i in range(2,(n//2+1)):
                if n%i==0:
                    break
                else:
                    print(n)
prime_number3(10,100)


def prime_number4(start,end):
    res = []
    for i in range(start, end):
        for j in range(2,i//2):
            if i%j ==0:
                break
        else:
            res.append(i)


print(prime_number4(100,200))