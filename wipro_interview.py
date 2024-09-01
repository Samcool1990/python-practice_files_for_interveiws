# ROMAN NAME
def roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"]

    roman_name = ""
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_name += syb[i]
            num -= val[i]
        i += 1
    return roman_name


print(roman(90))


def prime_number4(start, end):
    for i in range(start, end):
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                break
        else:
            print(i)


print(prime_number4(1, 100))
