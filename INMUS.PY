# django specific
# WHAT IS DJANGO FOR, drf, orm vs sql, ADVANTAGE & disadvantage of ORM, 

# leetcode question on an array of strings & calculate in a given query how many vowelsadded string is there..
# Problem Statement
# # You're given an array of strings words and an array of queries. Each query is a pair [l, r], and your task is to return the 
# number of strings in the range [l, r] (inclusive) that start and end with a vowel.
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
print(count_vowel_strings_in_ranges(words, queries))  # Output: [2, 2, 2]
