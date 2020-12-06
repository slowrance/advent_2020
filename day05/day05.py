with open('input.txt') as f:
    real_input = [line for line in f.readlines()]

test_input = ['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
seat_ids = []
for seat in real_input:
    rows = [i for i in range(128)]
    cols = [i for i in range(8)]
    seat_id = 0
    for dir in seat:
        if dir == 'F':
            rows = rows[:int(len(rows)/2)]
        elif dir == 'B':
            rows = rows[int(len(rows)/2):]
        elif dir == 'L':
            cols = cols[:int(len(cols)/2)]
        elif dir == 'R':
            cols = cols[int(len(cols)/2):]
    seat_id = (rows[0] * 8) + cols[0]
    seat_ids.append(seat_id)

print(max(seat_ids))
seat_ids.sort()
for i, seat in enumerate(seat_ids):
    if i == len(seat_ids) - 1:
        break
    if seat_ids[i+1] - seat_ids[i] != 1:
        print(seat)

print(sorted(seat_ids))

