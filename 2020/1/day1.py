import sys
import itertools
from math import prod

input = sys.argv[1]
combo_count = int(sys.argv[2])
#Let's not assume that there's only one correct answer, though the problem implies it.
answers = []

with open (input, 'r') as f:
    expenses = [int(line) for line in f]
    

for combo in itertools.combinations(expenses,combo_count):
    if sum(combo) == 2020:
        answers.append(prod(combo))

# only for 2 combos
# for index,expense1 in enumerate(expenses):
#     for expense2 in expenses[index+1:]:
#         if expense1 + expense2 == 2020:
#             answers.append(expense1 * expense2)


for answer in answers:
    print(answer)

