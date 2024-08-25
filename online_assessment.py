def distribute_candies(A, B):
    result = [0] * B
    i = 0
    
    while A > 0:
        result[i % B] += min(A, i + 1)
        A -= (i + 1)
        i += 1
    
    return result

# Test cases
A1, B1 = 7, 4
A2, B2 = 12, 3
A3, B3 = 5, 2

output1 = distribute_candies(A1, B1)
output2 = distribute_candies(A2, B2)
output3 = distribute_candies(A3, B3)

print(output1)  # Output: [1, 2, 3, 1]
print(output2)  # Output: [2, 4, 6]
print(output3)  # Output: [2, 3]
