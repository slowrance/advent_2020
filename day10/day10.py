import copy
import math
from itertools import combinations, chain

with open('input.txt') as f:
    real_input = [int(line.strip()) for line in f.readlines()]

test_input = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''.splitlines()
test_input = [int(num) for num in test_input]

used_input = real_input
used_input.insert(0, 0)
used_input.append(max(used_input) + 3)

def calc_diffs(used_input):
    ones = 0
    twos = 0
    threes = 0
    others = 0
    used_input.sort()
    for i, jolt in enumerate(used_input):
        if i == len(used_input) - 1:
            break

        if used_input[i + 1] - jolt > 3:
            others += 1
            break
        elif used_input[i + 1] - jolt == 1:
            ones += 1
        elif used_input[i + 1] - jolt == 2:
            twos += 1
        elif used_input[i + 1] - jolt == 3:
            threes += 1
    return(ones, twos, threes, others)
print(used_input)
output = calc_diffs(used_input)
print(output)
print(output[0] * output[2])

used_input = real_input
possible_adapters = set(used_input)
start = 0
target = used_input[-1]
from functools import lru_cache

@lru_cache(None)
def dfs(pos, target):
    if pos == target:
        return 1
    if pos > target:
        return 0
    valid_count = 0
    for i in range(1,4):
        if pos + i in possible_adapters:
            valid_count += dfs(pos + i, target)
    return valid_count

print(dfs(start, target))
# valid_count = 0
# # combs = []
# def get_combs():
#     for i in range(math.ceil(used_input[-1]/3), len(used_input) - 1):
#         current_combs = combinations(used_input[1:len(used_input)-1], i)
#
#         for comb in current_combs:
#             if used_input[-1] > 3 * (len(comb) - 1):
#                 continue
#             yield comb
#
#
# def make_combs(used_input):
#     return chain.from_iterable(combinations(used_input, i) for i in range(math.ceil(used_input[-1]/3), len(used_input) - 1))
# # print(combs)
#
#
# combs = make_combs(used_input)
#
# for comb in combs:
#     comb = list(comb)
#     comb.insert(0,0)
#     comb.append(used_input[-1])
#
#     output = calc_diffs(comb)
#     if output[3] == 0:
#         print(comb)
#         valid_count += 1
# while i < len(used_input):
#     modified_input = copy.deepcopy(used_input)
#     if i != 0:
#         modified_input.pop(i)
#
#     output = calc_diffs(modified_input)
#     # print(output)
#     print(modified_input)
#     if output[3] == 0:
#         # print(modified_input)
#         valid_count += 1
#     i += 1





# example
# from functools import lru_cache
#
# adapters = list(map(int, adapterstr.split("\n")))
# adapters.sort()
# chk = set(adapters)
# start = 0
# target = max(chk)+3
# chk.add(target)
# global chk
#
# @lru_cache(None)
# def dfs(pos, target):
#     if pos == target:
#         return 1
#     if pos > target:
#         return 0
#     ways = 0
#     for step in range(1,4):
#         if (pos + step) in chk:
#             ways += dfs(pos+step, target)
#     return ways
#
# print(dfs(start, target))

