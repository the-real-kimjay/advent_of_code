import sys
import re

def main():
    input_lines = get_input()
    print(get_valid_count(input_lines))


def get_valid_count(lines):
    # part1
    # required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    requirements = get_requirements()
    passport = {}
    valid_part1 = valid_part2 = 0

    for i,line in enumerate(lines):
        if len(line) > 0:
            # part1
            # passport_fields = [value.split(':')[0] for value in line.split(' ')]
            passport_fields = {value.split(':')[0]:value.split(':')[1] for value in line.split(' ')}
            passport.update(passport_fields)
        if len(line) == 0 or i+1 == len(lines):
            is_valid_part1 = all(field in passport.keys() for field in requirements)
            if is_valid_part1: valid_part1 += 1
            if is_valid_part1 and all(eval(requirements[k].format(v)) for k,v in passport.items() if k in requirements): valid_part2 += 1
            for k,v in passport.items():
                if k in requirements:
                    print(k + ':' + v)
                    print(eval(requirements[k].format(v)))
                    print('')
            passport = {}

    return valid_part1,valid_part2


def get_requirements():
    return {
    'byr':'1920 <= {0} <= 2002',
    'iyr':'2010 <= {0} <= 2020',
    'eyr':'2020 <= {0} <= 2030',
    'hgt':'hgt_check("{0}")',
    'hcl':'hcl_check("{0}")',
    'ecl':'"{0}" in ["amb","blu","brn","gry","grn","hzl","oth"]',
    'pid':'len("{0}".lstrip("0")) == 9'
    }

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.


def hcl_check(hcl_string):
    if re.match("#([0-9]|[a-f]){6}",hcl_string):
        return True
    else:
        return False


def hgt_check(hgt_string):
    if hgt_string[-2:] == 'cm':
        return 150 <= int(hgt_string[:-2]) <= 193
    elif hgt_string[-2:] == 'in':
        return 59 <= int(hgt_string[:-2]) <= 76
    return False


def get_input(input_file='day4_input.txt'):
    with open (input_file, 'r') as f:
        return [line.rstrip('\n') for line in f]

if __name__ == '__main__':
    main()
