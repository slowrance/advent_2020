import copy

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

# lines = '''L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL'''.splitlines()

layout = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        layout[i][j] = char

for line in layout:
    print(line)

def count_full_seats(layout, seat):
    full_seats = 0
    rows = len(layout)
    cols = len(layout[0])
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            depth = 1
            if r == c == 0:
                continue
            is_seat = False
            while not is_seat:
                if seat[0] + (r * depth) >= rows or seat[1] + (c * depth) >= cols:
                    is_seat = True
                    break
                if layout[seat[0] + r * depth][seat[1] + c * depth] in ['L', '#']:
                    is_seat = True
                    break
                depth += 1
            if 0 <= seat[0] + (r * depth) < rows and 0 <= seat[1] + (c * depth) < cols:
                if layout[seat[0] + (r * depth)][seat[1] + (c * depth)] == '#':
                    full_seats += 1
    return full_seats

def run_round(layout):
    new_layout = copy.deepcopy(layout)
    for i, row in enumerate(layout):
        for j, col in enumerate(row):
            if layout[i][j] == 'L' and count_full_seats(layout, [i, j]) == 0:
                new_layout[i][j] = '#'
            if layout[i][j] == '#' and count_full_seats(layout, [i, j]) >= 5:
                new_layout[i][j] = 'L'
    return new_layout

stable = False
while not stable:
    new_layout = run_round(layout)
    if new_layout == layout:
        stable = True
        break
    layout = new_layout
    for line in new_layout:
        print(''.join(line))
    print('\n\n\n')

occupied = 0
for line in new_layout:
    occupied += line.count('#')
print(f'there are {occupied} occupied seats')



