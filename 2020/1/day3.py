import sys
from math import prod

def main():
    input_lines = get_input(sys.argv[1])
    cases_1 = [(1,3)]
    cases_2 = [(1,1),(1,3),(1,5),(1,7),(2,1)]
    
    print(prod(get_tree_count(input_lines,case[0],case[1]) for case in cases_1))
    print(prod(get_tree_count(input_lines,case[0],case[1]) for case in cases_2))



def get_tree_count(input_lines,rise,run):
    trees = 0
    for i,line in enumerate(input_lines):
        pos = (int(i/rise) * run) % len(line)
        if i % rise == 0 and line[pos] == '#':
            trees += 1
    return trees

    # trees = i = 0 
    # while i < len(input_lines):
    #     line = input_lines[i]
    #     pos = (i * run) % len(line)
    #     if line[pos] == '#':
    #         trees += 1
    #     i += rise


def get_input(input_file):
    with open (input_file, 'r') as f:
        return [line.rstrip('\n') for line in f]


if __name__ == '__main__':
    main()
