with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

trees = 0
idx = 0
for i, line in enumerate(lines):
    if i%2 == 1:
        continue
    print(i, idx)
    print(lines[i][idx])
    if lines[i][idx] == '#':
        trees += 1
    idx += 1
    if idx > 30:
        idx = idx - 31

print(trees)