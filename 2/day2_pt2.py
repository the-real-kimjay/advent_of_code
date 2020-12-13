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

        pos_count = 0
        for limit in len_limits:
            if password[limit - 1] == valid_char:
                pos_count += 1

        if pos_count == 1: 
            valid_passwords.append(password)

print(valid_passwords)
print('')
print(len(valid_passwords))
        

