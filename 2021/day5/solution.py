import sys
import numpy as np


def get_input():
    with open(sys.argv[1], 'r') as f:
        return [[tuple([int(y) for y in x.split(',')]) for x in line.strip().split(' -> ')] for line in f]


def get_grid(coordinate_list):
    max_x = max([point[0] for pair in coordinate_list for point in pair])
    max_y = max([point[1] for pair in coordinate_list for point in pair])
    return np.zeros((max_x + 1, max_y + 1), int)


def complete_line(line_start, line_end, pos):
    points = np.linspace(line_start, line_end, abs(line_start[pos] - line_end[pos]) + 1)
    return [tuple([int(xy) for xy in point]) for point in np.around(points, decimals=0)]

def get_line_points(line):
    line_start = line[0]
    line_end = line[1]
    #Calculate slope here and then reduce code below. vertical slope below is wrong.
    if line_start[0] == line_end[0]:
        slope = 0
        line_points = complete_line(line_start, line_end, 1)
    elif line_start[1] == line_end[1]:
        slope = 0
        line_points = complete_line(line_start, line_end, 0)
    elif abs(line_start[0] - line_end[0]) == abs(line_start[1] - line_end[1]):
        slope = 45
        line_points = complete_line(line_start, line_end, 1)
    else:
        return None, None

    return line_points, slope


def get_intersection_count(lines=get_input()):
    grid = get_grid(lines)

    diag_points = []
    for line in lines:
        line_points, slope = get_line_points(line)
        if slope == 0:
            for point in line_points:
                grid[point] += 1
        elif slope == 45:
            diag_points.extend(line_points)

    hor_ver_point_count = np.sum(grid >= 2)
    for point in diag_points:
        grid[point] += 1

    return hor_ver_point_count, np.sum(grid >= 2)


def main():
    part1, part2 = get_intersection_count()
    print(f'Part 1 answer: {part1}')
    print(f'Part 2 answer: {part2}')


if __name__ == '__main__':
    main()
