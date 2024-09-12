alten, roy, alten = range(3)
print(alten, roy, alten)


def mk(x):
    def mk1():
        print("DECORATED")
        x()

    return mk1


def mk2():
    print("ORDINARY")


p = mk(mk2)
p()

# ---*---
# --A*A--
# -A*A*A-


def print_pattern():
    n = 3  # Number of rows

    for i in range(n):
        print("-" * (n - i - 1) + "*" + "*" * (2 * i) + "-" * (n - i - 1))

        if i < n - 1:
            print(
                "-" * (n - i - 1)
                + chr(65 + i)
                + "*"
                + "*" * (2 * i)
                + chr(65 + i)
                + "-" * (n - i - 1)
            )


print_pattern()


l = [12, 123, 1234, 12345]
output = [str(item).zfill(5) for item in l]
# output = [int(item) for item in output]
print(output)


l = [("x", 1), ("x", 2), ("x", 3), ("y", 4), ("y", 7)]

output = {}
for item in l:
    key, value = item
    if key in output:
        output[key].append(value)
    else:
        output[key] = [value]

print(output)


emp = [{"id": 199, "name": "suman"}, {"id": 200, "name": "pathak"}]

output = [[d["id"] for d in emp], [d["name"] for d in emp]]

print(output)

data = [
    ("s1", "sub1", "d1", 10),
    ("s2", "sub1", "d1", 25),
    ("s3", "sub1", "d1", 15),
    ("s1", "sub2", "d1", 10),
    ("s2", "sub2", "d1", 20),
    ("s3", "sub2", "d1", 10),
    ("s1", "sub1", "d2", 10),
    ("s2", "sub1", "d2", 20),
    ("s3", "sub1", "d2", 10),
    ("s1", "sub2", "d2", 35),
    ("s2", "sub2", "d2", 20),
    ("s3", "sub2", "d2", 45),
]

# Initialize a dictionary to store scores by department
department_scores = {}

# Process the data
for entry in data:
    student, subject, department, score = entry
    if department not in department_scores:
        department_scores[department] = {}
    if student not in department_scores[department]:
        department_scores[department][student] = 0
    department_scores[department][student] += score

print(department_scores)
# Generate the output
output = {}
for department, scores in department_scores.items():
    students = [student for student, score in scores.items() if score >= 25]
    output[department] = students
print(output)

# Print the output
for department, students in output.items():
    print(f"{department}: {','.join(students)}")
