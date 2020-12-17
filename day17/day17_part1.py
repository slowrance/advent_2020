import copy

with open('input.txt') as f:
    real_input = [line.strip() for line in f.readlines()]

test_input = '''.#.
..#
###'''.splitlines()

used_input = real_input

# for i in used_input:
#     for j in i:

initial = [[[j for j in i] for i in used_input]]

def empty_field(size: int):
    return [['.' for j in range(size)] for i in range(size)]

def grow_matrix(old_matrix, size):
    new_matrix = copy.deepcopy(old_matrix)
    current_size = len(new_matrix[0])
    for z in new_matrix:
        if size > current_size:
            for y in z:
                y.insert(0, '.')
                y.append('.')
            z.insert(0, list('.' * size))
            z.append(list('.' * size))
    if size >= current_size:
        new_matrix.insert(0, empty_field(size))
        new_matrix.append(empty_field(size))
    return new_matrix

def count_active_neighbors(matrix, position):
    active = 0
    planes = len(matrix)
    rows = len(matrix[0])
    cols = len(matrix[0][0])
    for z in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for x in [-1, 0, 1]:
                if x == y == z == 0:
                    continue
                # is_seat = False
                if position[0] + z >= planes or position[1] + y >= rows or position[2] + x >= cols:
                    break
                # if layout[seat[0] + r * depth][seat[1] + c * depth] in ['L', '#']:
                #     is_seat = True
                #     break

                if 0 <= position[0] + z < planes and 0 <= position[1] + y < rows and 0 <= position[2] + x < cols:
                    if matrix[position[0] + z][position[1] + y][position[2] + x] == '#':
                        active += 1
    return active

def update_matrix(matrix):
    new_matrix = copy.deepcopy(matrix)
    for z, plane in enumerate(matrix):
        for y, row in enumerate(plane):
            for x, col in enumerate(row):
                if col == '#' and count_active_neighbors(matrix, [z, y, x]) not in [2, 3]:
                    new_matrix[z][y][x] = '.'
                elif col == '.' and count_active_neighbors(matrix, [z, y, x]) == 3:
                    new_matrix[z][y][x] = '#'
    return new_matrix

# for z in initial:
#     for y in z:
#         print(y)
# for z, plane in enumerate(initial):
#     for y, row in enumerate(plane):
#         for x, col in enumerate(row):
#             print(count_active_neighbors(initial, [z,y,x]), col)

size = len(used_input)
matrix = copy.deepcopy(initial)
for _ in range(6):
    matrix = grow_matrix(matrix, size)
    # for z in matrix:
    #     print('\n')
    #     for y in z:
    #         print(y)
    matrix = update_matrix(matrix)
    # for z in matrix:
    #     print('\n')
    #     for y in z:
    #         print(y)
    size += 2
# for z in matrix:
#     print('\n')
#     for y in z:
#         print(y)

count = 0
for z, plane in enumerate(matrix):
    for y, row in enumerate(plane):
        for x, col in enumerate(row):
            if col == '#':
                count += 1
print(count)