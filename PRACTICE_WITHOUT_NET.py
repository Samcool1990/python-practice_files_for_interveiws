donutStoreDataSet = [
    {
        "id": "0001",
        "type": "donut",
        "name": "Cake",
        "ppu": 0.55,
        "batters": {
            "batter": [
                {"id": "1001", "type": "Regular"},
                {"id": "1002", "type": "Chocolate"},
                {"id": "1003", "type": "Blueberry"},
                {"id": "1004", "type": "Devil's Food"},
            ]
        },
        "topping": [
            {"id": "5001", "type": "None"},
            {"id": "5002", "type": "Glazed"},
            {"id": "5005", "type": "Sugar"},
            {"id": "5007", "type": "Powdered Sugar"},
            {"id": "5006", "type": "Chocolate with Sprinkles"},
            {"id": "5003", "type": "Chocolate"},
            {"id": "5004", "type": "Maple"},
        ],
    },
    {
        "id": "0002",
        "type": "donut",
        "name": "Raised",
        "ppu": 0.55,
        "batters": {"batter": [{"id": "1001", "type": "Regular"}]},
        "topping": [
            {"id": "5001", "type": "None"},
            {"id": "5002", "type": "Glazed"},
            {"id": "5005", "type": "Sugar"},
            {"id": "5003", "type": "Chocolate"},
            {"id": "5004", "type": "Maple"},
        ],
    },
    {
        "id": "0003",
        "type": "donut",
        "name": "Old Fashioned",
        "ppu": 0.55,
        "batters": {
            "batter": [
                {"id": "1001", "type": "Regular"},
                {"id": "1002", "type": "Chocolate"},
            ]
        },
        "topping": [
            {"id": "5001", "type": "None"},
            {"id": "5002", "type": "Glazed"},
            {"id": "5003", "type": "Chocolate"},
            {"id": "5004", "type": "Maple"},
        ],
    },
]


def compare_topping(donut):
    return len(donut["topping"])


sorted_dict = sorted(donutStoreDataSet, key=compare_topping, reverse=True)

print(sorted_dict)


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


print(are_parentheses_balanced("{{{{))))((()))}}}}"))


def armstrong(n):
    return n == sum(int(digit) ** len(str(n)) for digit in str(n))


print(armstrong(50))

d1 = {"1": {"2": "some", "3": {"4": "the"}}}


def recursive_search(d, key):
    if key in d:
        return d[key]
    for value in d.values():
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


def flatten_dict(d, parent_key="", separator="_"):
    items = {}
    for key, value in d.items():
        new_key = parent_key + separator + key if parent_key else key
        if isinstance(value, dict):
            items.update(flatten_dict(value, new_key, separator))
        else:
            items[new_key] = value
    return items


# Example nested dictionary
nested_dict = {"a": 1, "b": {"c": 2, "d": {"e": 3}}, "f": 4}

# Flatten the dictionary
flattened_dict = flatten_dict(nested_dict)

print(flattened_dict)


def number_to_words2(n):
    if n == 0:
        return "Zero"

    def one_to_ninteen(n):
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

    def helper_function(n):
        if n < 20:
            return one_to_ninteen(n)
        elif n < 100:
            return tens(n // 10) + (" " + one_to_ninteen(n % 10) if n % 10 != 0 else "")
        elif n < 1000:
            return one_to_ninteen(n // 100) + (
                " Hundred " + helper_function(n % 100) if n % 100 != 0 else ""
            )

        elif n < 1000000:
            return helper_function(n // 1000) + (
                " Thousand " + helper_function(n % 1000) if n % 1000 != 0 else ""
            )

        elif n < 1000000000:
            return helper_function(n // 1000000) + (
                " Million " + helper_function(n % 1000000) if n % 1000000 != 0 else ""
            )

    return helper_function(n) + " Only"


numbers = 987654321
# Example usage:
print(number_to_words2(numbers))


def prime_number(number):
    for i in range(2, number // 2 + 1):
        if i % number == 0:
            return True
            break
        else:
            return False
    else:
        return False


l1 = ["a", "b", "c"]
l2 = [1, 2, 3]

output = {k: v for k, v in zip(l1, sorted(l2, reverse=True))}
print(output)


def generatorfunc(number):
    for i in range(1, number + 1):
        yield i * i


obj = generatorfunc(3)
print(next(obj))
print(next(obj))
print(next(obj))

iter_list = iter([1, 2, 3])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))


# from django.db import models


# class User(models.Model):
#     name = models.CharField()
#     is_active = models.BooleanField(default=True)


# active_user = User.objects.filter(is_active=True)
# users_decending_order = User.objects.order_by("-name")
# user_start_with_a = User.objects.filter(name__istartswith="a").delete()
# count_active_user = User.objects.filter(is_active=True).count()
# count_inactive_user = User.objects.filter(is_active=False).count()


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fibonnaci(n):
    if n <= 0:
        return n
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)


def sum_of_digits(n):
    temp = n
    summ = 0
    if n > 9:
        while temp > 0:
            digit = temp % 10
            summ += digit
            temp = temp // 10
    else:
        summ = n
    return summ


print(sum_of_digits(123456789))

str = "This_is_a_string"

new_str = ""
str = str.split("_")
print(str)
for i in str:
    new_str += i[0].lower() + i[1:].upper() + " "
print(new_str)


class CorpRatio:
    def __init__(self) -> None:
        self.corps = {}
        self.total_harvest = 0

    def add(self, corp_name, quantity):
        if corp_name in self.corps:
            self.corps[corp_name] += quantity
        else:
            self.corps[corp_name] = quantity
        self.total_harvest += quantity

    def proportion(self, corp_name):
        if corp_name in self.corps:
            return self.corps[corp_name] / self.total_harvest
        else:
            return 0


crop_ratio = CorpRatio()
print(crop_ratio.add("Wheat", 4))
print(crop_ratio.add("Wheat", 5))
print(crop_ratio.add("Rice", 1))

print(crop_ratio.proportion("Wheat"))  # should return 0.9
print(crop_ratio.proportion("Rice"))  # should return 0.1
print(crop_ratio.proportion("Corn"))  # should return 0.


def longest_palindrome(s):
    n = len(s)
    start = 0
    max_length = 1

    dp = [[False for _ in range(n)] for _ in range(n)]

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


def min_removals_to_make_palindrome(str):
    n = len(str)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for k in range(2, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if s[i] == s[j] and k == 2:
                dp[i][j] == 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    lps_length = dp[0][n - 1]
    removal_count = n - lps_length
    return removal_count


# Example usage
s = "abcda"
result = min_removals_to_make_palindrome(s)
print(result)


def worker_function(start, end):
    total = sum(i * i for i in range(start, end))
    return total


import multiprocessing
import time


def multiprocessing_func(num_process=4, range_end=1000000):
    range_per_process = range_end // num_process
    pool = multiprocessing.Pool(processes=num_process)

    task = [
        (i * range_per_process, (i + 1) * range_per_process) for i in range(num_process)
    ]

    start = time.time()

    results = pool.starmap(worker_function, task)
    total_sum = sum(results)

    end = time.time()

    pool.close()
    pool.join()
    total_time = end - start


if __name__ == "__main__":
    multiprocessing_func(4, 1000000)
