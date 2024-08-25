def replace_second_occurrence(input_string, char):
    count = 0
    output_string = ''

    for i in input_string:
        if i == char:
            count += 1
            if count == 2:
                output_string += '2'
            else:
                output_string += i
        else:
            output_string += i

    return output_string

# Example usage
A = 'SUMAN PAATHAK'
output = replace_second_occurrence(A, 'A')
print(output)




"""SELECT department_id, SUM(salary) AS total_salary
FROM employees
GROUP BY department_id
ORDER BY total_salary DESC
LIMIT 1;
"""