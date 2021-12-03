import sys


def get_input():
    with open(sys.argv[1], 'r') as f:
        return [line.strip() for line in f]


def get_bit(i, list):
    return sum([int(_[i]) for _ in list])


def get_gamma_epsilon(bit, threshold, gamma, epsilon):
    gamma += '1' if bit >= threshold / 2 else '0'
    epsilon += '0' if bit >= threshold / 2 else '1'
    return gamma, epsilon


def get_ls_sub_rating(diag, rating_type):
    gamma = ''
    epsilon = ''

    for i in range(len(diag[0])):
        bit = get_bit(i, diag)
        gamma, epsilon = get_gamma_epsilon(bit, len(diag), gamma, epsilon)

        if len(diag) > 1:
            power_type = gamma if rating_type == 'o2' else epsilon
            diag = [x for x in diag if x[i] == power_type[i]]

    return diag


def get_power_consumption():
    diag = get_input()
    gamma = ''
    epsilon = ''

    for i in range(len(diag[0])):
        bit = get_bit(i, diag)
        gamma, epsilon = get_gamma_epsilon(bit, len(diag), gamma, epsilon)

    return int(gamma, 2) * int(epsilon, 2)


def get_life_support_rating():
    o2_rating = get_ls_sub_rating(get_input(), 'o2')
    co2_rating = get_ls_sub_rating(get_input(), 'co2')
    return int(o2_rating[0], 2) * int(co2_rating[0], 2)


print(f'Part 1 answer: {get_power_consumption()}')
print(f'Part 2 answer: {get_life_support_rating()}')
