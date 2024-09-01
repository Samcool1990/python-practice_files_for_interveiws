########Palindrome#######
# 1#     By Using Split method
s = "malyaylam"


def palindrome(s):
    temp = s[::-1]
    if s == temp:
        print("Yes")
    else:
        print("No")


palindrome(s)


# 2#     By Using indexing / for loop
def palindrome2(s):
    n = len(s)
    for i in range(n):
        if s[i] != s[n - i - 1]:
            return False
    return True


print(palindrome2(s))

# 3#    By using reverse / join


def palindrome3(s):
    temp = "".join(reversed(s))
    if s == temp:
        return True
    return False


print(palindrome3(s))


# 4#  Using While loop
def palindrome4(s):
    n = len(s)
    first = 0
    last = n - 1
    while first < last:
        if s[first] == s[last]:
            first += 1
            last -= 1
        else:
            return False
    return True


print(palindrome4(s))


# 5# while loop number
def palindrome6(n):
    temp = n  # 1456
    rev_n = 0
    while temp > 0:
        d = temp % 10  # 6
        rev_n = rev_n * 10 + d
        temp = temp // 10

    if n == rev_n:
        return True
    return False


print(palindrome6(12345654321))


########Fibonnaci series#######
n = 10


# 1# uSing while loop
def fibonnaci1(n):
    a = 0
    b = 1
    print(a)
    while b < n:
        print(b)
        a, b = b, a + b


fibonnaci1(n)


# 2# using for loop
def fibonacci2(n):
    a = 0
    b = 1
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


fibonacci2(n)


# 3#  using recussion
def fibonacci3(n):
    if n <= 1:
        return n
    else:
        return fibonacci3(n - 1) + fibonacci3(n - 2)


# if n <= 0:
#     print('Invalid')
# else:
#     for i in range(n):
print(fibonacci3(n))


###### Compress String ##########
# for loop
def compress1(s):
    n = len(s)
    count = 1
    new_str = ""
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            new_str += s[i] + str(count)
            count = 1
    new_str += s[n - 1] + str(count)
    return new_str


print(compress1("aaddvffggssrrdd"))


# while loop
def compress2(s):
    n = len(s)
    i = 0
    new_str = ""

    while i < (n - 1):
        count = 1
        while i < (n - 1) and s[i] == s[i + 1]:
            count += 1
            i += 1
        i += 1
        new_str += s[i - 1] + str(count)

    return new_str


print(compress2("aaddvffggssrrdd"))
