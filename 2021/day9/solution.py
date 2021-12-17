import sys
import math


def get_input():
    with open(sys.argv[1], 'r') as f:
        return [[int(height) for height in line.strip()] for line in f]


def get_basin_points(points, lines):
    basins = []

    for point in points:
        points_to_check = [point]
        basin_points = []

        while len(points_to_check) > 0:
            point = points_to_check[0]
            basin_points.append(point)
            x = point[0]
            y = point[1]
            row = lines[y]

            if x < len(lines[y]) - 1 and row[x + 1] != 9 and (x + 1, y) not in points_to_check and (x + 1, y) not in basin_points:
                points_to_check.append((x + 1, y))
            if x > 0 and row[x - 1] != 9 and (x - 1, y) not in points_to_check and (x - 1, y) not in basin_points:
                points_to_check.append((x - 1, y))
            if y < len(lines) - 1 and lines[y + 1][x] != 9 and (x, y + 1) not in points_to_check and (x, y + 1) not in basin_points:
                points_to_check.append((x, y + 1))
            if y > 0 and lines[y - 1][x] != 9 and (x, y - 1) not in points_to_check and (x, y - 1) not in basin_points:
                points_to_check.append((x, y - 1))

            points_to_check.remove(point)
        basins.append(len(basin_points))

    return basins


def get_local_mins(lines=get_input()):
    total_risk = 0
    x_low_points = []
    y_low_points = []
    low_points = []

    for y, line in enumerate(lines):
        for x, num in enumerate(line):
            # x_low_points.append()
            if x == len(line) - 1 or num < line[x + 1]:
                if x == 0 or num < line[x - 1]:
                    if y == len(lines) - 1 or num < lines[y + 1][x]:
                        if y == 0 or num < lines[y - 1][x]:
                            total_risk += (num + 1)
                            low_points.append((x, y))

    basin_lengths = get_basin_points(low_points, lines)
    basin_lengths.sort()

    return total_risk, math.prod(basin_lengths[-3:])


def main():
    part1, part2 = get_local_mins()
    print(f'Part 1 answer: {part1}')
    print(f'Part 2 answer: {part2}')


if __name__ == '__main__':
    main()
