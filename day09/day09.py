import copy
from itertools import combinations

with open('input.txt') as f:
    real_input = [int(line.strip()) for line in f.readlines()]

test_input = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''.splitlines()
test_input = [int(num) for num in test_input]

look_back = 25
used_input = real_input
bad_num = -1
for i, num in enumerate(used_input):
    if i >= look_back:
        combs = combinations(used_input[i-look_back:i], 2)
        sums = [sum(comb) for comb in combs]
        if used_input[i] not in sums:
            bad_num = used_input[i]
            print(used_input[i])

def find_weakness(real_input: list):
    total = 0
    for i, num in enumerate(real_input):
        total += real_input[i]
        if total == bad_num:
            return min(real_input[0:i+1]) + max(real_input[0:i+1])
        if total > bad_num:
            real_input.pop(0)
            return None


copied_input = copy.deepcopy(used_input)
not_found = True

while not_found:
    result = find_weakness(copied_input)
    if result:
        print(result)
        break




