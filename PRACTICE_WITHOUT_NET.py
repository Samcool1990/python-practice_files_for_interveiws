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
