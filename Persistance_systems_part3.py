def longest_palindrome(s):
    n = len(s)
    # Create a table to store results of subproblems
    dp = [[False for _ in range(n)] for _ in range(n)]

    # All substrings of length 1 are palindromes
    max_length = 1
    start = 0

    # Mark all substrings of length 1 as palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for substring of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            max_length = 2
            start = i

    # Check for lengths greater than 2
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            # Check if the first and last characters are the same and if the
            # substring in between is a palindrome
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                if k > max_length:
                    max_length = k
                    start = i

    return s[start : start + max_length]


# Example usage
s = "babad"
result = longest_palindrome(s)
print(result)  # Output: "bab"


# sort a list without sort function
lst = [4, 6, 9, 8]
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print(lst)
# Tech stack
