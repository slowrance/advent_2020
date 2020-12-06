import re

with open('input.txt') as f:
    raw_input = f.read()
    groups = raw_input.split('\n\n')


# part 1
clean_groups = []
for group in groups:
    # group = ' '.join(group.splitlines())
    clean_groups.append(re.sub(r'\n', '', group))

total = 0
for group in clean_groups:
    group = set(group)
    total += len(group)

print(total)


# part 2
total = 0
for group in groups:
    people = group.split()
    # if len(people) == 1:
    #     total += len(set(people))
    # elif len(people) > 1:
    people_sets = []
    for person in people:
        people_sets.append(set(person))
    total += len(people_sets[0].intersection(*people_sets))
print(total)
