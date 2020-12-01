with open('input.txt') as f:
    values = [int(line.strip()) for line in f.readlines()]

# print(sorted(values))

#part 1
for val in values:
    if (2020 - val) in values:
        print(val * (2020 - val))


# part 2
for val1 in values:
    for val2 in values:
        if (2020 - val1 - val2) in values:
            print(val1 * val2 * (2020 - val1 - val2))
