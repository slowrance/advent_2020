real_input = [19,0,5,1,10,13]

test_input = [1,2 ,3 ]

used_input = real_input
target_turn = 30000000


memo = {}
for i, num in enumerate(used_input, 1):
    memo[num] = i

for i in range(6, target_turn):
    value = used_input[-1]
    if value in memo.keys() and i > 6:
        used_input.append(i - memo[value])
        memo[value] = i
    else:
        used_input.append(0)
        memo[value] = i

print(used_input[-1])