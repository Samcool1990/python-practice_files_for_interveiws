def find_contiguous_ranges(nums):
    # Convert the input to a sorted list (if not already sorted)
    nums = sorted(nums)
    result = []  # Initialize the result list
    start = nums[0]  # Start of the current range

    for i in range(1, len(nums)):
        # Check if the current number is not contiguous with the previous one
        if nums[i] != nums[i - 1] + 1:
            # If the start equals the previous number, it's a single value
            if start == nums[i - 1]:
                result.append(f"{start}")
            else:
                # Otherwise, it's a range
                result.append(f"{start}-{nums[i - 1]}")
            # Update the start to the current number
            start = nums[i]

    # Add the last range or single value
    if start == nums[-1]:
        result.append(f"{start}")
    else:
        result.append(f"{start}-{nums[-1]}")

    return result


# Example usage
input_set = {1, 2, 3, 5, 8, 9, 10, 11, 13}
output = find_contiguous_ranges(input_set)
print(output)  # Output: ['1-3', '5', '8-11', '13']
