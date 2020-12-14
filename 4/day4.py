import sys


def main():
    input_lines = get_input()
    get_valid_count(input_lines)
    # print(get_valid_count(input_lines))


def get_valid_count(lines):
    valid_count = 0
    passport = []
    passports = []
    skip = before = after = 0

    for line in lines:
    	print(line)
    	if len(line) == 0:
    		passports.append(passport)
    		passports = []
    	else:
    		print('else')
    		passport.append(line)
		print(passport)

	print(len(lines))
    # print(skip)
    # print(before)
    # print(after)
    print(passports)
    

    return valid_count


def get_input(input_file='day4_input.txt'):
    with open (input_file, 'r') as f:
        return [line.rstrip('\n') for line in f]
        # f.read()

if __name__ == '__main__':
    main()