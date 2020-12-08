import copy

with open('input.txt') as f:
    real_input = [line for line in f.readlines()]

test_input = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.splitlines()


def run_program(instructions):
    acc = 0
    used = {}
    i = 0
    inf_loop = False
    while not inf_loop:
        if used.get(i) :
            print('inf_loop', acc)
            inf_loop = True
            break
        if i > len(instructions) - 1:
            print('end program', acc)
            inf_loop = True
            break
        used[i] = True
        command, value = instructions[i].split()
        if command == 'nop':
            i += 1
            pass
        elif command == 'acc':
            acc += int(value)
            i += 1
        elif command == 'jmp':
            i += int(value)


run_program(test_input)

for i in range(len(real_input)):
    modified = copy.deepcopy(real_input)
    command, value = modified[i].split()
    if command == 'nop':
        modified[i] = ' '.join(['jmp', value])
    elif command == 'jmp':
        modified[i] = ' '.join(['nop', value])
    run_program(modified)

