###################################
def sum_of_digit(n):
    sum = 0
    temp=n
    if n>9:
        while temp>0:
            digit= temp%10
            sum= sum + digit
            temp= temp//10
    else:
        sum = n
    return sum

print(sum_of_digit(123456789))
