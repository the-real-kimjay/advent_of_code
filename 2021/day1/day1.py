import sys

increases = 0
avg_increases = 0

with open(sys.argv[1], 'r') as f:
    depths = [int(line) for line in f]

for i, depth in enumerate(depths):
    if i > 0 and depths[i] > depths[i-1]:
        increases += 1
    if i > 2 and sum(depths[i-3:i]) < sum(depths[i-2:i+1]):
        avg_increases += 1

print(f'Part 1 answer: {increases}')
print(f'Part 2 answer: {avg_increases}')
