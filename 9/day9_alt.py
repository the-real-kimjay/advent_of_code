import sys

def main():
    lines = getInput()
    invalid_num = findInvalidNum(lines)
    print(invalid_num)


def findInvalidNum(lines):
    for i,num in enumerate(lines):
        if i > 24:
            check_range = lines[i-25:i]
            if not any([(num - num2) in check_range[i2+1:] for i2,num2 in enumerate(check_range)]):
                return num  



def getInput(input_file='input.txt'):
    with open (input_file, 'r') as f:
        return [int(line.rstrip('\n')) for line in f]


if __name__ == '__main__':
    main()