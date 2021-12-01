import sys
import itertools

input_lines = sys.argv[1]
valid_passwords = []

with open (input_lines, 'r') as f:
    for line in f:
        input_parts = line.split(':')
        password = input_parts[1][1:]
        rule_parts = input_parts[0].split(' ')
        len_limits = [int(x) for x in rule_parts[0].split('-')]
        valid_char = rule_parts[1]

        char_count = 0

        for char in password:
            print(char)
            if char == valid_char:
                char_count += 1
        print('')

        if len_limits[0] <= char_count <= len_limits[1]:
            valid_passwords.append(password)

print(valid_passwords)
print('')
print(len(valid_passwords))
        
# for answer in answers:
#     print(answer)

# for combo in combos:
#     print(combo)

