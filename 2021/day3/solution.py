import sys


def get_input():
    with open(sys.argv[1], 'r') as f:
        return [line.strip() for line in f]


def get_gamma_epsilon(i, input_list, gamma, epsilon):
    threshold = len(input_list) / 2
    bit = sum([int(x[i]) for x in input_list])
    gamma += '1' if bit >= threshold else '0'
    epsilon += '0' if bit >= threshold else '1'
    return gamma, epsilon


def get_components(diag, rating_type):
    gamma = ''
    epsilon = ''

    for i in range(len(diag[0])):
        gamma, epsilon = get_gamma_epsilon(i, diag, gamma, epsilon)

        if rating_type is not None and len(diag) > 1:
            power_type = gamma if rating_type == 'o2' else epsilon
            diag = [x for x in diag if x[i] == power_type[i]]

    return gamma, epsilon, diag[0]


def get_power_consumption():
    gamma, epsilon, _ = get_components(get_input(), None)
    return int(gamma, 2) * int(epsilon, 2)


def get_life_support_rating():
    _, _, o2_rating = get_components(get_input(), 'o2')
    _, _, co2_rating = get_components(get_input(), 'co2')
    return int(o2_rating, 2) * int(co2_rating, 2)


print(f'Part 1 answer: {get_power_consumption()}')
print(f'Part 2 answer: {get_life_support_rating()}')
