import sys
import numpy as np


def get_input():
    with open(sys.argv[1], 'r') as f:
        return [[tuple([int(y) for y in x.split(',')]) for x in line.strip().split(' -> ')] for line in f]


def get_grid(coordinate_list):
    max_x = max([point[0] for pair in coordinate_list for point in pair])
    max_y = max([point[1] for pair in coordinate_list for point in pair])
    # print(max_x, max_y)
    return np.zeros((max_x + 1, max_y + 1), int)


def get_line_points(line):
    line_start = line[0]
    line_end = line[1]
    hor_ver_lines = []
    line_points = []
    # if 1 == 2:
    #     print('skip')
    return_lines = []
    if line_start[0] == line_end[0]:
        # hor_ver_lines += 2
        # hor_ver_lines += abs(line_start[1] - line_end[1]) + 1
        return_lines.extend([line_start, line_end])
        for i in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1]) + 1): # use max(key=list)
            hor_ver_lines.append([line[0][0], i])
        line_points = np.linspace(line_start, line_end, abs(line_start[1] - line_end[1]) + 1, dtype=int)
    elif line_start[1] == line_end[1]:
        # hor_ver_lines += 2
        # hor_ver_lines += abs(line_start[0] - line_end[0]) + 1
        return_lines.extend([line_start, line_end])
        for i in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1):
            hor_ver_lines.append([i, line[0][1]])
        line_points = np.linspace(line_start, line_end, abs(line_start[0] - line_end[0]) + 1, dtype=int)
    # elif abs(line_start[0] - line_end[0]) == abs(line_start[1] - line_end[1]):
    #     line_points = np.linspace(line_start, line_end, abs(line_start[1] - line_end[1]) + 1, dtype=np.int32)
    else:
        return None, None
    # return line_points
    return hor_ver_lines, [tuple([xy for xy in point]) for point in line_points]


def get_points(lines=get_input()):
    grid = get_grid(lines)
    list_points = []
    all_points = []
    mark_lines = 0
    print(len(lines))
    print('')
    doubles = 0
    for line in lines:
        # print(line)
        # list_points += [point for point in line]
        hor_ver_lines, line_points = get_line_points(line)
        print(line)
        print(line_points)
        print('')
        if hor_ver_lines is not None:
        # if return_points is not None:
        #     list_points.extend(return_points)
            mark_lines += len(hor_ver_lines)
        # print(line_points)
        # print('')
        if line_points is not None:
            for point in line_points:
                all_points.append(point)
                # print(point))
                # print(point)
                # print(point[0]
                # before = grid[point]
                if grid[point] == 1:
                    doubles += 1
                grid[point] += 1
                # after = grid[point]
                # if after - before != 1:
                #     print(point)
            # print(grid)
        # grid = mark_grid(grid, line_points)
        # print(np.diff(line, axis=0)[0])
        # print(abs(line_start[1] - line_end[1]))
        # print('')
        # for i in range(min(points[0][1], points[1][1]), max(points[0][1], points[1][1]) + 1): # use max(key=list)
        #     grid[i, points[0][0]] += 1
        # elif points[0][1] == points[1][1]:
        #     for i in range(min(points[0][0], points[1][0]), max(points[0][0], points[1][0]) + 1):
        #         grid[points[0][1], i] += 1
    # grid[4, 3] = 33
    # print(grid.T)
    # print(grid[4, 3])
    # print(len(all_points))
    # for point in list_points:
    #     if point not in all_points:
    #         print(point)
    # print(len(lines))
    print(mark_lines)
    # print(len(line_points))
    # print(len(list_points))
    # test = np.split(grid, (0, 10))[1]
    # print(test)
    # for x in test:
    #     print(type(x))
    # print(np.sum(test >= 2))
    # print('test')
    print(len(all_points))
    # print(grid.shape)
    # print(np.sum(grid == 0))
    # print(np.sum(grid == 1))
    print(np.sum(grid))
    print(doubles)
    print(len([x for x in all_points if x not in mark_lines]))
    return np.sum(grid == 2)
    # return None


def main():
    print(f'Part 1 answer: {get_points()}')
    # print(f'Part 2 answer: {get_board_score(last_board)}')


if __name__ == '__main__':
    main()
