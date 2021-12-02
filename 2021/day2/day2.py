import sys

h_pos = 0
v_pos = 0
v_pos2 = 0

with open(sys.argv[1], 'r') as f:
    moves = [line.split() for line in f]

for direc, dist in moves:
    if direc == 'forward':
        h_pos += int(dist)
        v_pos2 += v_pos * int(dist)
    elif direc == 'down':
        v_pos += int(dist)
    elif direc == 'up':
        v_pos -= int(dist)

print(f'Part 1 answer: {h_pos * v_pos}')
print(f'Part 2 answer: {h_pos * v_pos2}')