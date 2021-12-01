import sys

def main():
    lines = getInput()
    inst = getInstructions(lines)
    acc,exited = getAcc(inst)
    print('Part 1 = ' + str(acc))
    fixed_acc,exited = findFix(lines)
    print('Part 2 exited boot loop = ' + str(exited) + '. Count was ' + str(fixed_acc))


def getAcc(instructions):
    pos = acc = 0
    run = list(range(len(instructions)))

    while pos in run:
        func = instructions[pos]['func']
        num  = instructions[pos]['num']
        run.remove(pos)

        acc += num if func == 'acc' else 0
        pos += num if func == 'jmp' else 1

        if pos == len(instructions):
            return acc,True
  
    return acc,False


def findFix(lines):
    for i in range(len(lines)):
        new_instructions = getInstructions(lines)
        
        if new_instructions[i]['func'] == 'acc':
            continue
        if new_instructions[i]['func'] == 'jmp':
            new_instructions[i]['func'] = 'nop'
        elif new_instructions[i]['func'] == 'nop':
            new_instructions[i]['func'] = 'jmp'

        acc,exited = getAcc(new_instructions)

        if exited:
            return acc,exited

    return 'none found',False


def getInstructions(lines):
    instructions = {i:{'func':parts[0],'num':int(parts[1])} for i,parts in enumerate([line.split(' ') for line in lines])}
    return instructions


def getInput(input_file='input.txt'):
    with open (input_file, 'r') as f:
        return [line.rstrip('\n') for line in f]


if __name__ == '__main__':
    main()