#ROMAN NAME
def roman(n):
    i = ["","I","II","III", "IV","V","VI","VII","VIII","IX"]
    j = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]

    ones = i[n%10]
    tens = j[(n%100)//10]

    roman_Word = tens + ones
    return roman_Word

print(roman(90))


def prime_number4(start,end):

    
    
    for i in range(start, end):
        for j in range(2,i//2+1):
            if i%j ==0:
                break
        else:
            print(i)

print(prime_number4(1,100))

