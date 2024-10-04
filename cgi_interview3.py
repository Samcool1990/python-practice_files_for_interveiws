# DATA ENGINEER ROLE
name = "suman"

new_str = ""
for i in name:
    new_str += i + "_"
new_str = new_str[:-1]

print(new_str)
new_str2 = str("".join([i + "_" for i in name]).strip(""))[:-1]
print(new_str2)

# AWS GLUE
# AWS S3
# AWS APIG
