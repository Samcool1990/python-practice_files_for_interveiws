def roman(number):
    val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syb = [ 'm','cm','d','cd','c','xc','l','xl','x','ix','v', 'iv','i'] 
    roman_name = ""
    i = 0
    while number > 0:
        for j in range(number // val[i]):
            roman_name += syb[i]
            number -= val[i]
        
        
        i+= 1
    
    
    return roman_name
    

print(roman(90))



def longest_palindrome(string):
    n = len(s)
    
    dp = [[False for _ in range(n)] for _ in range(n)]
    
    max_length = 1
    start = 0
    
    for i in range(n):
        dp[i][i] = True
        
    for i in range(n - 1 ):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            max_length = 2
            start = i
    
    for k in range(3, n+1):
        for i in range(n-k+1):
            j = i + k -1
            if dp[i+1][j-1] and s[i] == s[j]:
                dp[i][j] = True
                if k >  max_length:
                    max_length = k
                    start = i
    return string[start: start+max_length]
# Example usage
s = "babad"
result = longest_palindrome(s)
print(result)  # Output: "bab"




def count_vowel_strings_in_ranges(words, queries):
    def is_vowel(letter):
        return letter in 'aeiouAEIOU'
    
    def is_vowel_word(word):
        return is_vowel(word[0]) and is_vowel(word[-1])
    
    n = len(words)
    prefix_vowel_count = [0] * (n+1)
    
    for i in range(n):
        if is_vowel_word(words[i]):
            prefix_vowel_count[i + 1] = prefix_vowel_count[i] +1
        else:
            prefix_vowel_count[i+1] = prefix_vowel_count[i]
            
    results = []
    for l,r in queries:
        result = prefix_vowel_count[r+1] - prefix_vowel_count[l]
        results.append(result)
    
    
    
    return results

# Example usage:
words = ["apple", "banana", "orange", "umbrella", "grape", "ice"]
queries = [[0, 2], [1, 4], [2, 5]]
print(count_vowel_strings_in_ranges(words, queries))  # Output: [2, 2, 2]



import multiprocess
import time

def worker_sum_squares(start, end):
    results = sum(i * i for i in range(start, end))
    return results
    
def multiprocess_func(num_process = 4, range_end = 1000000):
    range_per_process = range_end // num_process
    pool = multiprocess.Pool(process = num_process)
    
    tasks = [(i * range_per_process, (i+1) * range_per_process) for i in range(num_process)]
    
    start_time = time.time()
    
    result = pool.startmap(worker_sum_squares, tasks)
    
    total_sum = sum(result)
    
    end_time = time.time()
    
    pool.close()
    pool.join()
    
    print(total_sum)
    print(end_time - start_time)
    
if __name__ == "__main__":
    multiprocess_func(num_process = 4, range_end = 1000000)
    


def number_to_words2(n):
    if n == 0:
        return 'Zero'
        
    def one_to_nineteen(n):
        words = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                 "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        return words[n]
    def tens(n):
        words = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        return words[n]
    
    def num_to_words_helper(n):
        if n < 20:
            return one_to_nineteen(n) 
        elif n < 100:
            return tens(n//10) + (one_to_nineteen(n%10) if n % 10 != 0 else "")
        elif n < 1000:
            return one_to_nineteen(n // 100) + ( num_to_words_helper(n % 100) if n % 100 != 0 else "")
    
    return num_to_words_helper(n) + " only."
numbers = 999
# Example usage:
print(number_to_words2(numbers))



# Example nested dictionary
nested_dict = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    },
    'f': 4
}


def flatten_dict(dictionary, parent_key = " ", separator = "_"):
    items = {}
    for key, value in dictionary.items():
        new_key = parent_key + separator + key if parent_key else key
        if isinstance(value, dict):
            items.update(flatten_dict(value, new_key, separator))
        else:
            items[new_key] = value
    
    return items
# Flatten the dictionary
print(flatten_dict(nested_dict))



d1 = {"1": {"2": "some", "3": {"4": "the"}}}
def recursive_search(dictionary, key):
    if key in dictionary.keys():
        return dictionary[key]
    for key, value in dictionary.items():
        if isinstance(value, dict):
            result = recursive_search(value,key)
            if result is not None:
                return result



# Example usages
result_3 = recursive_search(d1, "3")
result_4 = recursive_search(d1, "4")
result_2 = recursive_search(d1, "2")
        
print(result_3)  # Output: {'4': 'the'}
print(result_4)  # Output: the
print(result_2)  # Output: some
    
def are_parentheses_balanced(str):
    stack = []
    opening= '({['
    closing = ')}]'
    
    for char in str:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            if opening.index(stack.pop()) != closing.index(char):
                return False
    return not stack
    
 # Example usage
print(are_parentheses_balanced("()"))
print(are_parentheses_balanced("()[]{}"))
print(are_parentheses_balanced("([{}])"))
print(are_parentheses_balanced("([)]"))
print(are_parentheses_balanced("{{{{))))((()))}}}}"))  
    
