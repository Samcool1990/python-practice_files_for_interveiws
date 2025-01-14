####Fibonnaci series###
# by using while loop
def fibonacci(n):
    a, b = 0, 1
    print(a)
    while b < n:
        print(b)
        a, b = b, a + b


fibonacci(5)


# By using for loop
def fibonacci2(n):
    a, b = 0, 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)


fibonacci2(5)



######################################
# fibonacci_series using a Generator #
######################################
def fibonacci_series(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

f1 = fibonacci_series(5)
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))

##RECURSSION##
def fibonacci3(n):
    if n <= 1:
        return n
    else:
        return fibonacci3(n - 1) + fibonacci3(n - 2)


n = 5
if n <= 0:
    print("Put valid number")
else:
    for i in range(n):
        print(fibonacci3(i))




def fibonacci_series2(n):
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

f2 = fibonacci_series(5)
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))



def fibonacci_range(start, end):
    fib_sequence = []
    a, b = 0, 1
    while b <= end:
        if b >= start:
            fib_sequence.append(b)
        a, b = b, a + b
    return fib_sequence


start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))
fib_range = fibonacci_range(start, end)
print("Fibonacci numbers in the range:", fib_range)
