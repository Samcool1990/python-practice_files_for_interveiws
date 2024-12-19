

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
