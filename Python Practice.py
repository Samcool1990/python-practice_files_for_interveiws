def sum1(a,b,c):
    if a == "sum":
        return (int(b)+int(c))
    
   
    
print(sum1("sum","4","7")) 



rows = int(input("Enter Pyramid Pattern Rows = "))

print("Pyramid Star Pattern") 

for i in range(0, rows):
    for j in range(0, rows - i - 1):
        print(end = ' ')
    for k in range(0, i + 1):
        if i%2==0:
            
            print('*', end = ' ')
    print()


n=5
for i in range(n):
    for j in range(i,n,2):
        print(' ',end='')
    for j in range(i+1):
        if i%2==0:
            print("#",end='')
    
    print()