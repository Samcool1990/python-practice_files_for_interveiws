def roman(number):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"]
    roman_name = ""
    i = 0
    while number > 0:
        for j in range(number // val[i]):
            roman_name += syb[i]
            number -= val[i]
        i += 1
    return roman_name


print(roman(90))


def number_to_words2(n: int) -> str:
    if n == 0:
        return "zero"

    def one_to_nineteen(n):
        words = [
            "",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "eleven",
            "twelve",
            "thirteen",
            "fourteen",
            "fifteen",
            "sixteen",
            "seventeen",
            "eighteen",
            "nineteen",
        ]
        return words[n]

    def tens(n):
        words = [
            "",
            "",
            "twenty",
            "thirty",
            "forty",
            "fifty",
            "sixty",
            "seventy",
            "eighty",
            "ninety",
        ]
        return words[n]

    def num_to_words_helper(n):
        if n < 20:
            return one_to_nineteen(n)
        elif n < 100:
            return tens(n // 10) + (
                " " + one_to_nineteen(n % 10) if n % 10 != 0 else ""
            )
        elif n < 1000:
            return (
                one_to_nineteen(n // 100)
                + " hundred"
                + (" and " + num_to_words_helper(n % 100) if n % 100 != 0 else "")
            )
        elif n < 1_000_000:
            return (
                num_to_words_helper(n // 1_000)
                + " thousand"
                + (", " + num_to_words_helper(n % 1_000) if n % 1_000 != 0 else "")
            )
        elif n < 1_000_000_000:
            return (
                num_to_words_helper(n // 1_000_000)
                + " million"
                + (
                    ", " + num_to_words_helper(n % 1_000_000)
                    if n % 1_000_000 != 0
                    else ""
                )
            )
        elif n < 1_000_000_000_000:
            return (
                num_to_words_helper(n // 1_000_000_000)
                + " billion"
                + (
                    ", " + num_to_words_helper(n % 1_000_000_000)
                    if n % 1_000_000_000 != 0
                    else ""
                )
            )
        elif n < 1_000_000_000_000_000:
            return (
                num_to_words_helper(n // 1_000_000_000_000)
                + " trillion"
                + (
                    ", " + num_to_words_helper(n % 1_000_000_000_000)
                    if n % 1_000_000_000_000 != 0
                    else ""
                )
            )
        else:
            return (
                num_to_words_helper(n // 1_000_000_000_000_000)
                + " quadrillion"
                + (
                    ", " + num_to_words_helper(n % 1_000_000_000_000_000)
                    if n % 1_000_000_000_000_000 != 0
                    else ""
                )
            )

    return num_to_words_helper(n) + " only."


numbers = 999
# Example usage:
print(number_to_words2(numbers))


# Given a string find out by which elements can be remove to make it the string palindrome
def min_removals_to_make_palindrome(s):
    n = len(s)
    # Initialize a table to store LPS lengths
    dp = [[0] * n for _ in range(n)]
    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = 1
    # Build the table in bottom-up manner
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # Length of longest palindromic subsequence
    lps_length = dp[0][n - 1]

    # Number of characters to be removed
    min_removals = n - lps_length

    return min_removals


# Example usage
s = "abcda"
result = min_removals_to_make_palindrome(s)
print(result)  # Output: 2


def longest_palindrome(s):
    n = len(s)

    dp = [[False for _ in range(n)] for _ in range(n)]

    max_length = 1
    start = 0

    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            max_length = 2
            start = i

    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
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
print(
    "count_vowel_strings_in_ranges", count_vowel_strings_in_ranges(words, queries)
)  # Output: [2, 2, 2]


import multiprocessing
import time


def worker_sum_squares(start, end):
    results = sum(i * i for i in range(start, end))
    return results


def multiprocess_func(num_process=4, range_end=1000000):
    range_per_process = range_end // num_process
    pool = multiprocessing.Pool(processes=num_process)

    tasks = [
        (i * range_per_process, (i + 1) * range_per_process) for i in range(num_process)
    ]

    start_time = time.time()

    result = pool.starmap(worker_sum_squares, tasks)

    total_sum = sum(result)

    end_time = time.time()

    pool.close()
    pool.join()

    print(total_sum)
    print(end_time - start_time)


if __name__ == "__main__":
    multiprocess_func(num_process=4, range_end=1000000)


# Example nested dictionary
nested_dict = {"a": 1, "b": {"c": 2, "d": {"e": 3}}, "f": 4}


def flatten_dict(dictionary, parent_key=" ", separator="_"):
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


def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


d1 = {"1": {"2": "some", "3": {"4": "the"}}}


def recursive_search(dictionary, key):
    if key in dictionary.keys():
        return dictionary[key]
    for key, value in dictionary.items():
        if isinstance(value, dict):
            result = recursive_search(value, key)
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
    opening = "({["
    closing = ")}]"

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

list4 = [
    {"name": "suman", "location": "kolkata"},
    {"name": "pathak", "location": "pune"},
    {"name": "sam", "location": "kolkata"},
]


def group_by_location(lst):
    grouped = {}  # This will hold the final grouped data

    for item in lst:
        location = item["location"]  # Extract the location
        if location not in grouped:  # If the location is not yet a key in grouped
            grouped[location] = [item]  # Create a new list with the current item
        else:
            grouped[location].append(
                item
            )  # Append the current item to the existing list

    return grouped


# Example usage
output = group_by_location(list4)
print(output)


import logging
import sys
from logging.handlers import RotatingFileHandler


class CustomLogger:
    def __init__(
        self,
        name,
        log_file="app.log",
        level=logging.DEBUG,
        max_bytes=1048576,
        backup_count=5,
    ):
        """Initialize the custom logger with console and rotating file handlers."""
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Console handler for outputting to the console
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # Rotating file handler for logging to a file with rotation
        file_handler = RotatingFileHandler(
            log_file, maxBytes=max_bytes, backupCount=backup_count
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger

    def add_context(self, **context):
        """Add context information to the logs."""
        return ContextFilter(context)


class ContextFilter(logging.Filter):
    def __init__(self, context):
        super().__init__()
        self.context = context

    def filter(self, record):
        for key, value in self.context.items():
            setattr(record, key, value)
        return True


# Example usage
if __name__ == "__main__":
    # Create a logger with a specific name
    logger_util = CustomLogger("MyAppLogger")
    logger = logger_util.get_logger()

    # Add custom context (e.g., user ID, session ID)
    context_filter = logger_util.add_context(user_id="12345", session_id="abcde")
    logger.addFilter(context_filter)

    # Log messages at various levels
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

    # Additional log message with context
    logger.info("User performed an action")


class InvalidTransactionError(Exception):
    """Exception raised for errors in the transaction process.

    Attributes:
        transaction_id -- ID of the transaction which caused the error
        amount -- amount involved in the transaction
        message -- explanation of the error
    """

    def __init__(self, transaction_id, amount, message="Invalid transaction"):
        self.transaction_id = transaction_id
        self.amount = amount
        self.message = (
            f"{message}: Transaction ID {transaction_id} with amount ${amount:.2f}"
        )
        super().__init__(self.message)

    def log_error(self):
        """Log the error details to a file or external system."""
        with open("transaction_errors.log", "a") as log_file:
            log_file.write(f"ERROR: {self.message}\n")
        print(f"Logged error: {self.message}")

    def __str__(self):
        return self.message


# Example usage
try:
    # Simulate an invalid transaction scenario
    transaction_id = 12345
    amount = -100.50  # Negative amount is invalid
    if amount < 0:
        raise InvalidTransactionError(
            transaction_id, amount, "Negative amount not allowed"
        )
except InvalidTransactionError as e:
    e.log_error()
    print(e)
