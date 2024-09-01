# 2559. Count Vowel Strings in Ranges
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given a 0-indexed array of strings words and a 2D array of integers queries.

# Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

# Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

# Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.


# Example 1:

# Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
# Output: [2,3,0]
# Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
# The answer to the query [0,2] is 2 (strings "aba" and "ece").
# to query [1,4] is 3 (strings "ece", "aa", "e").
# to query [1,1] is 0.
# We return [2,3,0].
# Example 2:

# Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
# Output: [3,2,1]
# Explanation: Every string satisfies the conditions, so we return [3,2,1].
# from typing import List


def count_vowel_strings_in_ranges(words, queries):
    def is_vowel(letter):
        return letter in "aeiouAEIOU"

    def is_vowel_word(word):
        return is_vowel(word[0]) and is_vowel(word[-1])

    n = len(words)
    prefix_vowel_count = [0] * (n + 1)

    for i in range(n):
        if is_vowel_word(words[i]):
            prefix_vowel_count[i + 1] = prefix_vowel_count[i] + 1
        else:
            prefix_vowel_count[i + 1] = prefix_vowel_count[i]

    results = []
    for l, r in queries:
        result = prefix_vowel_count[r + 1] - prefix_vowel_count[l]
        results.append(result)

    return results


# Example usage:
words = ["apple", "banana", "orange", "umbrella", "grape", "ice"]
queries = [[0, 2], [1, 4], [2, 5]]
print(count_vowel_strings_in_ranges(words, queries))
