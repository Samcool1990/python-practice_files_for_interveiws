def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for consistent comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if both strings have the same length
    if len(str1) != len(str2):
        return False

    # Create a dictionary to count the frequency of characters in str1
    count_dict = {}    
    # Count characters in str1
    for char in str1:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    # Subtract the count of characters in str2
    for char in str2:
        if char in count_dict:
            count_dict[char] -= 1
        else:
            return False

    # Check if all counts are zero
    for count in count_dict.values():
        if count != 0:
            return False

    return True

# Example usage
str1 = "listen"
str2 = "silent"
if are_anagrams(str1, str2):
    print(f"'{str1}' and '{str2}' are anagrams.")
else:
    print(f"'{str1}' and '{str2}' are not anagrams.")



def two_sum(nums, target):
    # Create a dictionary to store the numbers we have seen so far
    seen = {}
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement (the number that, when added to num, gives the target)
        complement = target - num        
        # If the complement is in the dictionary, we have found a solution
        if complement in seen:
            return [seen[complement], i]        
        # Otherwise, store the current number and its index in the dictionary
        seen[num] = i    
    # Return None if no solution is found
    return None

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)

if result:
    print(f"Indices of the numbers that add up to {target}: {result}")
else:
    print(f"No solution found for the target {target}.")

# Questions:
# How would you handle rate limiting in application level
# Circuit breaker pattern
# you have one lambda with 4GB ram then you increase the RAM to 8GB & then add another lambda to it. 
# What type of scaling is it horizontal or Vertical.
# Raw SQL queries
