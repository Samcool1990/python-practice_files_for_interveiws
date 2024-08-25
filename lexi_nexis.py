s = "Apple is good for health"
s= ''.join(s.split(' '))
print(s)
# s = " ".joins(s)
d= {}
for i in s:
    d[i] = d.get(i,0) + 1
    # else:
    #     d[i] = 1
print(d)


l = ["1","2","3","3","5","6"]
new_lst = []

for i in l:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)


# In Python, all arguments are passed by value. This means that a copy of the argument is passed to the 
# function, and the original argument is not modified. Mutable objects, such as lists, dictionaries, and 
# sets, are passed by reference. This means that the function can modify the mutable object, and the 
# changes will be reflected in the original object.Here is an example of call by value:
# def foo(x):
#   x = 2

# Here, the argument x is passed by value to the function foo. The function then assigns the value 2 to x, 
# but this does not modify the original value of x.
# Here is an example of call by reference:
# def foo(x):
#   x.append(1)

# Here, the argument x is passed by reference to the function foo. The function then appends the value 1 to
#  the list x. This change is reflected in the original value of x. In general, call by value is used when 
# you want to ensure that the original argument is not modified. Call by reference is used when you want 
# to allow the function to modify the original argument.


# AWS questions