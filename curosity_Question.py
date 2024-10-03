# Find the deuplicate number in a sorted array


def find_duplicate_index(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            return i + 1
    return None


# Example usage
A1 = [2, 3, 4, 5, 5]
A2 = [1, 2, 2, 3, 4, 5]

index_A1 = find_duplicate_index(A1)
index_A2 = find_duplicate_index(A2)

print(index_A1)  # Output: 2
print(index_A2)  # Output: 3


# lexicographically algorithm in python
def lexicographic_sort(input_list):
    return sorted(input_list)


def lexicographical_sort(input_list):
    n = len(input_list)
    # Perform Bubble Sort
    for i in range(n):
        for j in range(i + 1, n):
            # Compare adjacent elements
            if input_list[i] > input_list[j]:
                # Swap if they are in the wrong order
                input_list[i], input_list[j] = input_list[j], input_list[i]
    return input_list


# Example usage
input_list = ["apple", "banana", "cherry", "date", "apricot", "aaple"]
result = lexicographical_sort(input_list)
print(
    ">>>>>>>>>>>>>>>>>>>", result
)  # Output: ['apple', 'apricot', 'banana', 'cherry', 'date']


# input_list = ["apple", "banana", "cherry", "date", "apricot"]
sorted_list = lexicographic_sort(input_list)
print(sorted_list)
print(">>", sorted(input_list))
