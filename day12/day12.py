import math
with open('input.txt') as f:
    instructions = [line.strip() for line in f]


# instructions = '''F10
# N3
# F7
# R90
# F11'''.splitlines()


direction = 'E'
x_pos = 0
y_pos = 0
dirs = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

# part 1
for step in instructions:
    command = step[0]
    amount = int(step[1:])
    if command == 'F':
        command = direction
    if command == 'N':
        y_pos += amount
    if command == 'S':
        y_pos -= amount
    if command == 'E':
        x_pos += amount
    if command == 'W':
        x_pos -= amount
    if command == 'L':
        amount = amount / 90
        amount = dirs[direction] - amount
        if amount < 0:
            amount += 4
        for k, v in dirs.items():
            if amount == v:
                direction = k
    if command == 'R':
        amount = amount / 90
        amount = dirs[direction] + amount
        if amount > 3:
            amount -= 4
        for k, v in dirs.items():
            if amount == v:
                direction = k
print(x_pos, y_pos)
print(abs(x_pos) + abs(y_pos))


# part 2

direction = 'E'
x_pos = 0
y_pos = 0
way_x = 10
way_y = 1
dirs = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point
    angle = math.radians(angle)
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return int(round(qx)), int(round(qy))

for step in instructions:
    command = step[0]
    amount = int(step[1:])
    multiplier = 1
    if command == 'F':
        multiplier = amount
        x_pos += way_x * multiplier
        y_pos += way_y * multiplier
    if command == 'N':
        way_y += amount
    if command == 'S':
        way_y -= amount
    if command == 'E':
        way_x += amount
    if command == 'W':
        way_x -= amount
    if command == 'L':
        origin = [0,0]
        point = [way_x, way_y]
        way_x, way_y = rotate(origin, point, amount)
    if command == 'R':
        origin = [0, 0]
        point = [way_x, way_y]
        way_x, way_y = rotate(origin, point, -amount)
print(x_pos, y_pos)
print(abs(x_pos) + abs(y_pos))