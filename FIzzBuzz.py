# Using For loop
def fizzbuzz(n):
    for i in range (1,n+1):
        if i%3 == 0 and i%5==0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
print(fizzbuzz(15))

#Using Dictionary 

def fizzbuzz2(n):
    d ={3:'Fizz',5:'Buzz'}
    for i in range(1,n+1):
        result = " "       
        for k,v in d.items():
            if i%k==0:
                result +=v
        if not result:
            result = i
        print(result)
        
        
print(fizzbuzz2(15))                            
            
    