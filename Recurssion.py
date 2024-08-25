def recursive_search(dictionary, target_key):
    if target_key in dictionary:
        return dictionary[target_key]
    for value in dictionary.values():
        if isinstance(value, dict):
            result = recursive_search(value, target_key)
            if result is not None:
                return result

                
d1 = {"1": {"2": "some", "3": {"4": "the"}}}
# Example usages
result_3 = recursive_search(d1, "3")
result_4 = recursive_search(d1, "4")
result_2 = recursive_search(d1, "2")

print(result_3)  # Output: {'4': 'the'}
print(result_4)  # Output: the
print(result_2)  # Output: some

#list1= [1,2,[3,[4,[5]]]]
#flatten the list
def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def reverse_lst(lst):
    if not lst:
        return []
    return [lst[-1]] + reverse_lst(lst[:-1])


print(reverse_lst([1,6,9,4,5]))


def reverse_str(str):
    if not str:
        return ""
    return str[-1] + reverse_str(str[:-1])


print(reverse_str("Suman"))

##RECURSSION##
def fibonacci3(n):
    if n<=1:
        return n
    else:
        return (fibonacci3(n-1)+fibonacci3(n-2))
n=5
if n<=0:
    print("Put valid number")
else:
    for i in range(n):
        print(fibonacci3(i))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)