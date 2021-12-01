import sys

def main():
    bag = sys.argv[1]
    lines = get_input()
    rules = get_rules(lines)
    outer_bag_count = get_parents(rules,bag)
    total_count,count_list = get_counts(rules,bag)
    print('Part 1 = ' + str(outer_bag_count))
    print('Part 2 = ' + str(count_list))
    print('Total should match part two above: ' + str(total_count))


def get_rules(lines):
    rules = {}
    for line in lines:
        rule_parts = line.split(' contain')
        parent = rule_parts[0].rstrip('s')
        children = {child[3:].rstrip('s'):int(child[1:2]) for child in rule_parts[1].rstrip('.').split(',') if child[1:2] != 'n'}
        rules[parent] = children

    return rules


def get_parents(rules,bag,parents=[]):
    for parent,children in rules.items():
        if bag in children and parent not in parents:
            parents.append(parent)
            get_parents(rules,parent,parents)

    return len(parents)


def get_counts(rules,bag,parent_count=1,total_count=0,count_list=[]):
    for child,count in rules[bag].items():
        child_count = parent_count * (count)
        total_count +=  child_count
        count_list.append(child_count)
        get_counts(rules,child,child_count,total_count,count_list)

    return total_count,sum(count_list)


def get_input(input_file='input.txt'):
    with open (input_file, 'r') as f:
        return [line.rstrip('\n') for line in f]


if __name__ == '__main__':
    main()