

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
output = []
index = 0
group_size = 1

while index < len(s):
    group = ''.join(s[index:index + group_size])
    output.append(group)
    index += group_size
    group_size += 1

# Print the result
for group in output:
    print(group)


# Question: What is the difference between Where & Having Clause
# Answer:
# The main difference between the WHERE and HAVING clauses in SQL is that the WHERE clause filters individual 
# rows, while the HAVING clause filters groups of rows: 
# WHERE clause
# Filters individual rows in a table or table-valued object before grouping. It's used with row-level 
# conditions and comes before GROUP BY.
# HAVING clause
# Filters groups of rows in the result set after grouping. It's used with aggregate functions and comes after 
# GROUP BY.

