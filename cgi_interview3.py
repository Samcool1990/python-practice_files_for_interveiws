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


# Advance technique
def transform_string(input_string):
    # Split the string by space to handle the parts separately
    words = input_string.split()
    
    # Apply the transformation on each word
    transformed_words = []
    for word in words:
        transformed_word = "_".join(list(word))  # Join the characters of the word with underscores
        transformed_words.append(transformed_word)
    
    # Join the transformed words with space
    return " ".join(transformed_words)

# Test the function
input_string = "suman pathak"
output_string = transform_string(input_string)
print(output_string)
