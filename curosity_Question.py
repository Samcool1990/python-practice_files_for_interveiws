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


input_list = ["apple", "banana", "cherry", "date", "apricot"]
sorted_list = lexicographic_sort(input_list)
print(sorted_list)
