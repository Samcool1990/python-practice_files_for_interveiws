str = "Suman"

s = str[-1:-3:-2]
print(s)

str = "Suman"

s = str[-1:-3:-1]
print(s)

##Use SET without set function
list1 = [1, 3, 3, 9, 66]
new_lst = []
n = len(list1)
for i in list1:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)


def generate_output(employee_name, hire_date):
    parts = hire_date.split(".")

    if len(parts) != 3:
        raise ValueError("hire_date should be in the format 'dd.mm.yyyy'")

    # day, month, year = parts[0], parts[1], parts[2]
    formatted_date = parts[1].zfill(2)

    return employee_name[:3] + formatted_date


# Example usage
employee_name = "Suman"
hire_date = "14.07.2023"
output = generate_output(employee_name, hire_date)
print(output)


# select emp_name, hire_date from emp_table
# where date like "01-%" and "7%"
# SELECT emp_name, hiredate
# FROM employees
# WHERE DATEPART(wk, hiredate) <= 1;


# # select emp_name, max(salary) from emp_table
# # where salary < (select emp_name, max(salary) from emp_table
# # where )

# # select emp_name, distinct(salary) from emp_table
# # group by salary
# # order by desc
# # limit 6,1;


# SELECT e.emp_name, e.salary
# FROM employees e
# WHERE e.salary = (
#   SELECT DISTINCT salary
#   FROM employees
#   ORDER BY salary DESC
#   OFFSET 6 ROWS FETCH NEXT 1 ROW ONLY
# );
