import sys

def main():
    bag = sys.argv[1]
    lines = get_input()
    rules = get_rules(lines)
    print(rules)
    print('')    
    # outer_parents = get_parents(bag,rules)
    total_count,count_list = get_counts(rules,bag)
    print('')
    print(total_count)
    print(count_list)
    print(sum(count_list))
    # print(len(outer_parents),total_count)


def get_rules(lines):
    rules = {}
    for line in lines:
        rule_parts = line.split(' contain')
        parent = rule_parts[0].rstrip('s')
        children = {child[3:].rstrip('s'):int(child[1:2]) for child in rule_parts[1].rstrip('.').split(',') if child[1:2] != 'n'}
        rules[parent] = children

    return rules


def get_parents(bag,rules,parents=[]):
    for parent,children in rules.items():
        if bag in children and parent not in parents:
            parents.append(parent)
            get_parents(parent,rules,parents)

    return parents


def get_counts(rules,bag,parent_count=1,total_count=0,count_list=[]):
    for child,count in rules[bag].items():
        child_count = parent_count * (count)
        # total_count +=  child_count
        count_list.append(child_count)
        get_counts(rules,child,child_count,total_count,count_list)

    return total_count,count_list


def get_counts_bak(bag,rules,total_count=0,count_list=[]):
    print('new loop')
    print(bag)
    print(rules[bag])
    print(total_count)
    for child,count in rules[bag].items():
        # if count == 'n':
        #     count = 0
        # print(total_count)
        print(child)
        print(rules[child])
        print(count)
        print('child count sum = ' + str(sum([count for child,count in rules[child].items()])))
        # total_count += count
        # count_list.append(count)
        child_count = count * (sum([count for child,count in rules[child].items()]))
        total_count +=  child_count
        count_list.append(child_count)
        print(total_count)
        print('')
        get_counts(child,rules,total_count,count_list)

    return total_count,count_list


def get_counts_2(bag,rules,child_count=0,count_list=[]):
    # print('new loop')
    # print(bag)
    # # print(rules[bag])
    # print(child_count)
        # rule_count = 0
        # if count == 'n':
        #     count = 0
    print(child_count)
    print(rules[bag])
    # print(int(count))
    rule_count = sum([count for child,count in rules[bag].items()])  
    print('rule count is ' + str(rule_count))
    child_count += (child_count * rule_count)
    count_list.append(child_count * rule_count)
    print(child_count)
    print('')
    get_counts(child,rules,child_count,count_list)
        

    return child_count,count_list


def get_input(input_file='test_input.txt'):
    with open (input_file, 'r') as f:
        return [line.rstrip('\n') for line in f]


if __name__ == '__main__':
    main()