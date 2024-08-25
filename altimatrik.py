# WITH RankedSalaries AS (
#   SELECT
#     EmpName,
#     Salary,
#     Department,
#     ROW_NUMBER() OVER (PARTITION BY Department ORDER BY Salary DESC) AS Rank
#   FROM Employee
# )
# SELECT
#   EmpName,
#   Salary,
#   Department
# FROM RankedSalaries
# WHERE Rank <= 3;




def are_parentheses_balanced(s):
    stack = []
    opening = '([{'
    closing = ')]}'
    for char in s:
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




def solve(A):
    stack = []
    for i in A:
        if i in "{[(":
            stack.append(i)
        else:
            if not stack:
                return 0
            top = stack.pop()
            if (i == "}" and top != "{") or (i == ")" and top != "(") or (i == "]" and top != "["):
                return 0

    if not stack:
        return 1
    return 0


print(solve("()"))
print(solve("()[]{}"))
print(solve("([{}])"))
print(solve("([)]"))
print(solve("{{{{))))((()))}}}}"))