import requests

url = "https://example.com/data"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Assuming the response is in JSON format
    # Process the data here
else:
    print(f"Error: Unable to fetch data from {url}")
import threading


# Define a function that each thread will execute
def print_numbers():
    for i in range(5):
        print(i)


# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Execution complete")


thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict.values())

for k, v in thisdict.items():
    print(v)


import pandas as pd

# Assuming you have a DataFrame called df
df = pd.read_csv(
    "your_data.csv"
)  # You can read your data from a CSV file or create a DataFrame in some other way

# Find duplicate rows based on all columns
duplicate_rows = df[df.duplicated()]

# Find duplicate rows based on specific columns
duplicate_rows_specific = df[df.duplicated(subset=["column1", "column2"])]

# Print or do further processing with the duplicate rows
print("All duplicate rows:")
print(duplicate_rows)

print("\nDuplicate rows based on specific columns:")
print(duplicate_rows_specific)


# INSERT INTO Employee VALUES(1,'Mandy',12000);

# INSERT INTO Employee VALUES(2,'Chris',15000);

# INSERT INTO Employee VALUES(3,'Henry',10000);

# INSERT INTO Employee VALUES(4,'Henry',10000);

# INSERT INTO Employee values(5,'Adams',11000);


# SELECT DISTINCT Salary
# FROM Employee
# ORDER BY Salary DESC
# LIMIT 2, 1;

# DELETE e1
# FROM Employee e1
# JOIN Employee e2
# ON e1.EmployeeID < e2.EmployeeID
#    AND e1.Name = e2.Name
# WHERE e1.Name = 'Henry';
