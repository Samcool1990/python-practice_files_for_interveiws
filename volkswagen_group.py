#Question: Given a positive integer n. Write a recurssive function to print number from -n to n.
# Answer:
def print_numbers(n, current=None):
    if current is None:
        current = -n  # Initialize starting point

    # Base case: If current exceeds n, stop recursion
    if current > n:
        return

    # Print current number
    print(current)

    # Recursive call with incremented current value
    print_numbers(n, current + 1)

# Example usage
n = 5
print_numbers(n)    

# Question: Which clause gives you the list of query data 
# Answer: SELECT clause.

# Question: Write a sql query to remove all duplicate records without using a temporary table.
# Answer:
# WITH CTE AS (
#     SELECT 
#         ROW_NUMBER() OVER (PARTITION BY column1, column2, column3 ORDER BY id) AS row_num,
#         id
#     FROM table_name
# )
# DELETE FROM table_name
# WHERE id IN (
#     SELECT id
#     FROM CTE
#     WHERE row_num > 1
# );
