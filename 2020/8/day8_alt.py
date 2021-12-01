import sys

def main():
    lines = get_input()
    acc = get_acc(lines)
    print(acc)


def get_acc(lines):
    pos = acc = 0
    # run = list(range(len(instructions)))
    instructions = {i:{inst.split(' ')[0]:int(inst.split(' ')[1])} for i,inst in enumerate(lines)}

    while pos in instructions:
        print(instructions[pos])
        func,num = instructions[pos].items()
        # func = inst[0]
        # num  = inst[1]
        # print(run)
        # print(pos)
        # print(inst_parts)
       
        if func == 'acc':
            acc += num
            # print('popping ' + str(pos))
            run.remove(pos)
            pos +=1
        elif func == 'jmp':
            run.remove(pos)
            pos += num
        else:
            run.remove(pos)
            pos +=1

        # print(acc)
        # print(pos)
        # print(run)
        # print('')
    # print(run)
    return acc


def get_input(input_file='input.txt'):
    with open (input_file, 'r') as f:
        return [line.rstrip('\n') for line in f]


if __name__ == '__main__':
    main()