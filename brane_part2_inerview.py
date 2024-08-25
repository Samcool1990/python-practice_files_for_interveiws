# def number_to_words(number):
#     ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
#     tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
#     thousands = ['', 'thousand', 'million', 'billion']

#     def convert_chunk(number):
#         if number == '0':
#             return ''
#         elif number[0] == '0':
#             return convert_chunk(number[1:])
#         elif len(number) == 1:
#             return ones[int(number) - 1]
#         elif len(number) == 2:
#             return teens[int(number) - 11] if number[0] == '1' else tens[int(number[0]) - 1] + ('' if number[1] == '0' else ' ' + ones[int(number[1]) - 1])
#         elif len(number) == 3:
#             return ones[int(number[0]) - 1] + ' hundred' + ('' if number[1:] == '00' else ' and ' + convert_chunk(number[1:]))

#     if number == 0:
#         return 'zero'

#     number_str = str(number)
#     chunks = [number_str[max(i - 3, 0):i] for i in range(len(number_str), 0, -3)]

#     words = [convert_chunk(chunk) + ' ' + thousands[i] for i, chunk in enumerate(chunks) if chunk != '']

#     return ' '.join(reversed(words))

numbers = 987654321
# words = number_to_words(numbers)
# print(words + ' only')


def number_to_words2(n: int) -> str:
    if n == 0:
        return "zero"
    
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
            return tens(n // 10) + (" " + one_to_nineteen(n % 10) if n % 10 != 0 else "")
        elif n < 1000:
            return one_to_nineteen(n // 100) + " hundred" + (" and " + num_to_words_helper(n % 100) if n % 100 != 0 else "")
        elif n < 1_000_000:
            return num_to_words_helper(n // 1_000) + " thousand" + (", " + num_to_words_helper(n % 1_000) if n % 1_000 != 0 else "")
        elif n < 1_000_000_000:
            return num_to_words_helper(n // 1_000_000) + " million" + (", " + num_to_words_helper(n % 1_000_000) if n % 1_000_000 != 0 else "")
        elif n < 1_000_000_000_000:
            return num_to_words_helper(n // 1_000_000_000) + " billion" + (", " + num_to_words_helper(n % 1_000_000_000) if n % 1_000_000_000 != 0 else "")
        elif n < 1_000_000_000_000_000:
            return num_to_words_helper(n // 1_000_000_000_000) + " trillion" + (", " + num_to_words_helper(n % 1_000_000_000_000) if n % 1_000_000_000_000 != 0 else "")
        else:
            return num_to_words_helper(n // 1_000_000_000_000_000) + " quadrillion" + (", " + num_to_words_helper(n % 1_000_000_000_000_000) if n % 1_000_000_000_000_000 != 0 else "")

    return num_to_words_helper(n) + " only."

# Example usage:
print(number_to_words2(numbers))
