import sys

def main():
    lines = getInput()
    acc = getAcc(lines)
    print(acc)


def getAcc(instructions):
    pos = acc = 0
    run = list(range(len(instructions)))

    while pos in run:
        inst = instructions[pos].split(' ')
        func = inst[0]
        num = int(inst[1])
        run.remove(pos)
       
        acc += num if func == 'acc' else 0
        pos += num if func == 'jmp' else 1

    return acc


def getInput(input_file='input.txt'):
    with open (input_file, 'r') as f:
        return [line.rstrip('\n') for line in f]


if __name__ == '__main__':
    main()