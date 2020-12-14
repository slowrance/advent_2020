with open('input.txt') as f:
    real_input = [line.strip() for line in f]

test_input = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''.splitlines()

test_input_2 = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''.splitlines()

initialization = real_input

# part 1
memory = {}
and_mask = ''
or_mask = ''
for line in initialization:
    command, value = line.split(' = ')
    if command == 'mask':
        and_mask = ''
        or_mask = ''
        for val in value:
            and_mask += '1' if val != '0' else '0'
            or_mask += '0' if val != '1' else '1'
        and_mask = int(and_mask, 2)
        or_mask = int(or_mask, 2)
    elif command[:3] == 'mem':
        position = command[4:-1]
        value = int(value)
        value = value & and_mask
        value = value | or_mask
        memory[position] = value

print(memory)
print(sum(memory.values()))

# part 2
def make_masks(mask, value):
    results = ['' for _ in range(36)]

    new_mask = list(mask)
    string_value = f'{int(value):b}'.zfill(36)
    new_value = list(string_value)

    for i, char in enumerate(mask):

        if char == 'X':

            for val in ['0', '1']:
                new_value[i] = val
                new_mask[i] = '0'
                make_masks(new_mask, int(''.join(new_value), 2))

        elif char == '0':
            new_value[i] = string_value[i]
        elif char == '1':
            new_value[i] = '1'
        if i == len(mask) - 1:
            possibles.add(''.join(new_value))


memory = {}
current_mask = ''
possibles = set()
for line in initialization:

    command, value = line.split(' = ')
    mem_addresses = []
    if command == 'mask':
        current_mask = value

    elif command[:3] == 'mem':
        memory_values = []
        masks = []
        position = command[4:-1]
        make_masks(current_mask, position)

        for mem in set(possibles):
            value = int(value)
            memory[int(mem, 2)] = value
        possibles = set()


print(memory)
print(sum(memory.values()))

