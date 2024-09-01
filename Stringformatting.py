# using List
def string_format(s):
    l = []
    temp = s.split(" ")
    for i in temp:
        l.append(i[0].lower() + i[1:].upper())
    s = " ".join(l)
    print(s)


s = "This is a string"
print(s)
string_format(s)


# using string
def string_format2(s):
    new_str = ""
    temp = s.split("_")
    for i in temp:
        new_str = new_str + i[0].lower() + i[1:].upper() + "."
    new_str = new_str[:-1]
    print(new_str)


s = "This_is_a_string"
print(s)
string_format2(s)
